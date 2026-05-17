import streamlit as st
import time
import os
import pandas as pd
from pathlib import Path

from pygments.lexer import default
from supabase import Client, create_client
# Accessing the secrets
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

# Initialize the Supabase client
supabase: Client = create_client(url, key)
# Find the absolute path to the directory this app.py file is sitting in
THIS_DIR = Path(__file__).parent
# --- 1. SET PAGE CONFIG (Must be the very first Streamlit command) ---
st.set_page_config(page_title="NSeSA League Manager", layout="wide", initial_sidebar_state="expanded")
@st.cache_data(ttl=600)
def load_schools_directory():
    try:
        response = supabase.table("teams").select("*").execute()
        if response.data:
            return pd.DataFrame(response.data)
    except Exception as e:
        st.error(f"Error loading school profiles: {e}")
    return pd.DataFrame()
def load_games_directory():
    try:
        response = supabase.table("games").select("""
    match_id,
    game,
    week,
    home ( school, logo_file),
    away ( school, logo_file),
    home_score,
    away_score
""").execute()
        if response.data:
            return pd.DataFrame(response.data)
    except Exception as e:
        st.error(f"Error loading school profiles: {e}")
    return pd.DataFrame()
# --- 2. Load DB!
schools_df = load_schools_directory()
games_df = load_games_directory()

# --- 3. INITIALIZE MEMORY (Session State) ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "school_profile" not in st.session_state:
    st.session_state.school_profile = {}

# --- 4. NAVIGATION CONTROLLER ---
# SCREEN 1: LOGIN PAGE
if not st.session_state.logged_in:
    title_pic = THIS_DIR/"title.png"
    st.image(title_pic)
    st.title("NSeSA League Management Portal", text_alignment="center")
    tab_login, tab_interest = st.tabs(["🔑 Coach Login", "📝 School Interest Form"])
    with tab_login:
        st.subheader("Welcome, Coach! Please sign in.")
        with st.container(border=True):
            with st.form(key="coach_login_form"):
                pin = st.text_input("Enter Coach PIN", type="password", key="login_pin")
                login_button = st.form_submit_button("Log In", width='content', type="primary")
            if login_button:
                if not schools_df.empty:
                    matched_row = schools_df[schools_df["login"] == int(pin)]
                    if not matched_row.empty:
                        school_dict = matched_row.iloc[0].to_dict()
                        st.session_state.logged_in = True
                        st.session_state.school_profile = school_dict
                        st.success(f"Welcome back, coach from {school_dict['school']}!")
                        st.rerun()
                    else:
                        st.error("Invalid PIN.")
                else:
                    st.error("Database Offline")
    with tab_interest:
        st.subheader("Bring Esports to Your School")
        st.caption("Fill out this form to submit your interest directly to the NSeSA database.")

        # 2. CREATE THE NATIVE STREAMLIT FORM
        with st.form(key="new_interest_form", clear_on_submit=True):
            # Form Input Fields
            applicant_name = st.text_input("Your Name")
            applicant_email = st.text_input("Contact Email Address")
            school_name = st.text_input("School / District Name")
            submit_button = st.form_submit_button(label="Submit Application", type="primary", width='content')
            if submit_button:
                # Quick check to make sure they didn't submit empty fields
                if applicant_name and applicant_email and school_name:

                    # Bundle the data into a clean dictionary matching your SQL columns
                    form_data = {
                        "name": applicant_name,
                        "email": applicant_email,
                        "school_name": school_name,
                    }

                    try:
                        # Inject data straight into your Supabase table!
                        response = supabase.table("league_interest").insert(form_data).execute()

                        # Celebrate success!
                        st.success("🎉 Application Submitted Successfully! Welcome to NSeSA.")
                        st.balloons()  # Fun alternate shortcut animation to celebrate!

                    except Exception as e:
                        st.error(f"Database Error: {e}")
                else:
                    st.warning("Please fill out all required fields before submitting.")
# SCREEN 2: AUTHENTICATED DASHBOARD
else:
    # Fetch logged in school details
    school_data = st.session_state.school_profile
    school_name = school_data['school']
    school_color = school_data['color']
    school_mascot = school_data['mascot']
    school_pic = school_data["logo_file"]
    def match_card_creator(match_info_row, entry=False):
        #read match info_row
        title = match_info_row["game"]
        week = match_info_row["week"]
        hdata = match_info_row["home"]
        adata = match_info_row["away"]
        hname = hdata["school"]
        aname = adata["school"]
        hlogo = hdata["logo_file"]
        alogo = adata["logo_file"]
        hscore = match_info_row["home_score"]
        ascore = match_info_row["away_score"]
        # top of card
        with st.container(border=True):
            st.header(title, text_alignment='center')
            st.caption(f"Week: {week}", text_alignment='center')
            home,away = st.columns(2)
            with home:
                st.write("Home")
                st.write(hname)

                st.header(hscore, text_alignment="center")
                st.image(str(THIS_DIR / hlogo), width=100)
            with away:
                st.write("Away")
                st.write (aname)

                st.header(ascore, text_alignment="center")
                st.image(str(THIS_DIR / alogo), width=100)

    # --- SIDEBAR NAVIGATION ---
    with st.sidebar:
        if (THIS_DIR / school_pic).exists():
            st.image(str(THIS_DIR / school_pic), width = 120)
        else:
            st.title("🎮")
        st.markdown(f"**{school_name}**")
        st.markdown(f"**Mascot:** {school_mascot}")
        st.write("---")

        # Simple navigation radio buttons
        page_selection = st.radio("Navigate", ["Dashboard", "Score Entry", "Roster Management", "Standings"])

        st.write("---")
        if st.button("Log Out", type="secondary"):
            st.session_state.logged_in = False
            st.session_state.school_profile = {}
            st.rerun()

    # --- DYNAMIC HEADER CONTENT ---
    # Here is where we inject the school's unique color dynamically!
    st.markdown(
        f"""
        <div style="background-color: {school_color}; padding: 20px; border-radius: 15px; margin-bottom: 25px; text-align: center; color: white;">
            <h1 style="margin: 0;">{school_name} Esports</h1>
            <p style="margin: 5px 0 0 0; font-size: 18px; opacity: 0.9;">Home of the {school_mascot}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- ROUTING THE PAGES ---
    if page_selection == "Score Entry":
        st.header("⚡ Active Matches")
        st.caption("*Score Entry Enabled*")
        #3-Columns, 1 for each game that is available.
        col1, col2, col3 = st.columns(3)
        with col1:
            match_row = games_df[games_df["match_id"]=="d1rl1"]
            game_dict = match_row.iloc[0].to_dict()
            match_card_creator(game_dict)
            with st.form(key="RL1"):
                homec, awayc = st.columns(2)
                with homec:
                    hr1 = st.number_input("Game 1 Score")
                    hr2 = st.number_input("Game 2 Score")
                    hr3 = st.number_input("Game 3 Score")
                with awayc:
                    ar1 = st.number_input("")
                    ar2 = st.number_input(" ")
                    ar3 = st.number_input("  ")
                submit_button = st.form_submit_button(label="Submit Scores", type="primary", width='stretch')
    if page_selection == "Dashboard":
        st.header("Dashboard", text_alignment="center")


        # 3-COLUMN 3D ELEVATED LOOK USING STREAMLIT BORDER CONTAINERS
        col1, col2, col3 = st.columns(3)

        with col2:
            # Container with border simulates that floating card look
            with st.container(border=True):
                st.markdown("### 📁 Past Matches")
                st.caption("History Locked")
                st.write("---")
                st.markdown("**Beatrice (3)** vs Crete (1)")
                st.text("Rocket League Varsity • Tue")

        with col3:
            with st.container(border=True):
                st.markdown("### 📅 Upcoming Schedule")
                st.write("---")
                st.markdown(f"**{school_name}** vs Norris")
                st.text("Valorant Varsity • Thursday")


    elif page_selection == "Roster Management":

        st.header("📋 State League Roster Management")

        # 1. ROSTER RULES & METADATA (Your Game Datasheet Rules)

        ROSTER_LIMITS = {

            "Rocket League": {"min": 3, "max": 5, "desc": "3 Active, up to 2 Substitutes"},

            "Super Smash Bros Crew": {"min": 4, "max": 7, "desc": "4 Active, up to 3 Substitutes"},

            "Valorant": {"min": 5, "max": 8, "desc": "5 Active, up to 3 Substitutes"}

        }

        ROSTER_LOCK_DATE = "October 15, 2026"

        # Display League Rules Alert Banner

        st.info(
            f"🔒 **Roster Lock Deadline:** {ROSTER_LOCK_DATE}. All rosters must meet minimum player limits by midnight.")

        # 2. PULL FRESH ROSTER DATA FROM SUPABASE

        try:

            response = supabase.table("league_rosters").select("*").execute()

            # Turn it into a dataframe or make a blank one if database is completely empty

            if response.data:

                all_rosters_df = pd.DataFrame(response.data)

            else:

                all_rosters_df = pd.DataFrame(columns=["id", "school_id", "game_title", "gamer_tag"])

        except Exception as e:

            st.error(f"Error fetching rosters: {e}")

            all_rosters_df = pd.DataFrame(columns=["id", "school_id", "game_title", "gamer_tag"])

        # 3. SPLIT WORKSPACE INTO TWO TABS: EDIT MY ROSTER VS SCOUT OTHERS

        tab_manage, tab_scout = st.tabs(["⚙️ Manage Your Roster", "👁️ League Scouting Portal"])

        # --- TAB 1: MANAGE YOUR ROSTER (EDIT MODE) ---

        with tab_manage:

            st.subheader(f"Edit Roster for {school_name}")

            st.caption("Add or modify your team's anonymous gamer tags below. Changes commit instantly to Supabase.")

            # Filter master dataframe down to JUST the logged-in coach's school

            my_school_df = all_rosters_df[all_rosters_df["school_id"] == school_name][["id", "game_title", "gamer_tag"]]

            # STREAMLIT MAGIC: st.data_editor turns a dataframe into an editable Excel spreadsheet interface

            edited_df = st.data_editor(

                my_school_df,

                column_config={

                    "id": None,  # Hides the database internal ID column from the coach

                    "game_title": st.column_config.SelectboxColumn(

                        "Game Title",

                        options=list(ROSTER_LIMITS.keys()),

                        required=True

                    ),

                    "gamer_tag": st.column_config.TextColumn(

                        "Student Gamer Tag",

                        default="Enter anonymized tag...",

                        required=True

                    )

                },

                num_rows="dynamic",  # Enables the "+ Add Row" and check-box delete controls natively!

                width='content',

                key="roster_editor"

            )

            # Save changes button to sync edits back up to Supabase

            if st.button("Save Roster Changes", type="primary"):

                # ⚠️ BACKEND SYNCLOGIC: Deep under the hood, it's safer to clear old rows and re-insert the clean matrix

                try:

                    # 1. Clear out old entries for this school

                    supabase.table("league_rosters").delete().eq("school_id", school_name).execute()

                    # 2. Build the payload block from the spreadsheet state

                    new_rows = []

                    for _, row in edited_df.iterrows():

                        if pd.notna(row["game_title"]) and pd.notna(row["gamer_tag"]) and row[
                            "gamer_tag"].strip() != "":
                            new_rows.append({

                                "school_id": school_name,

                                "game_title": row["game_title"],

                                "gamer_tag": row["gamer_tag"].strip()

                            })

                    # 3. Push new rows back to Supabase if any exist

                    if new_rows:
                        supabase.table("league_rosters").insert(new_rows).execute()

                    st.success("💾 Roster synced securely with Supabase cloud server!")

                    st.snow()

                    time.sleep(1)

                    st.rerun()

                except Exception as e:

                    st.error(f"Failed to update database: {e}")

            # ROSTER LIMIT CHECKER: Let's read the current roster and print validation badges!

            st.markdown("### 📊 Active Roster Validation")

            val_cols = st.columns(3)

            for idx, (game, limits) in enumerate(ROSTER_LIMITS.items()):

                # Count how many players this school has registered for this specific game

                current_count = len(edited_df[edited_df["game_title"] == game])

                with val_cols[idx % 3]:

                    with st.container(border=True):

                        st.markdown(f"**{game}**")

                        st.write(f"Current Count: `{current_count}` players")

                        st.caption(f"Allowed: {limits['min']} to {limits['max']} ({limits['desc']})")

                        if current_count < limits["min"]:

                            st.error(f"⚠️ Action Required: Needs {limits['min'] - current_count} more!")

                        elif current_count > limits["max"]:

                            st.danger(f"🚨 Illegal Roster: Remove {current_count - limits['max']} players!")

                        else:

                            st.success("✅ Roster Legal")

        # --- TAB 2: SCOUTING PORTAL (VIEW-ONLY MODE) ---

        with tab_scout:

            st.subheader("State-Wide Scouting Database")

            st.write("Review student rosters across all verified districts to prepare pick/ban strategies.")

            # Dropdown filter to select WHICH school you want to scout

    elif page_selection == "Standings":
        st.header("League Standings")
        st.write("Regional Standings with Strength of Schedule modifiers.")
        # Your pandas dataframe display can easily go here later!
