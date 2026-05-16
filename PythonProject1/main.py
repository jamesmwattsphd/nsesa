import streamlit as st
import time
import os
import pandas as pd
from pathlib import Path

# Find the absolute path to the directory this app.py file is sitting in
THIS_DIR = Path(__file__).parent
# --- 1. SET PAGE CONFIG (Must be the very first Streamlit command) ---
st.set_page_config(page_title="NSeSA League Manager", layout="wide", initial_sidebar_state="expanded")

# --- 2. MOCK DATABASE (Your Pandas/Dictionary comfort zone!) ---
SCHOOL_DB = {
    "beatrice": {
        "name": "Beatrice High School",
        "mascot": "Orangemen",
        "color": "#FF6B00",  # Orange
        "logo_file": THIS_DIR/"orange.png"
    },
    "crete": {
        "name": "Crete High School",
        "mascot": "Cardinals",
        "color": "#DD0000",  # Red
        "logo_file": THIS_DIR/"card.png"
    },
    "norris": {
        "name": "Norris High School",
        "mascot": "Titans",
        "color": "#004488",  # Blue
        "logo": "⚔️"
    }
}

# --- 3. INITIALIZE MEMORY (Session State) ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "school_id" not in st.session_state:
    st.session_state.school_id = None

# --- 4. NAVIGATION CONTROLLER ---
# SCREEN 1: LOGIN PAGE
if not st.session_state.logged_in:
    title_pic = THIS_DIR/"title.png"
    st.image(title_pic)
    st.title("🎮 NSeSA League Management Portal")
    st.subheader("Welcome, Coach! Please sign in.")

    # Simple form container that mimics a floating card
    with st.container(border=True):
        selected_school = st.selectbox("Select Your School", options=list(SCHOOL_DB.keys()),
                                       format_func=lambda x: SCHOOL_DB[x]['name'])
        password = st.text_input("Enter Coach PIN", type="password", help="Demo PIN is 1234")

        login_button = st.button("Log In", use_container_width=True, type="primary")

        if login_button:
            if password == "1234":
                st.session_state.logged_in = True
                st.session_state.school_id = selected_school
                st.success("Authentication Successful!")
                st.balloons()  # <--- The shortcut animation you wanted!
                time.sleep(1.5)  # Let them enjoy the balloons before rerunning
                st.rerun()
            else:
                st.error("Invalid PIN. Please try again.")

# SCREEN 2: AUTHENTICATED DASHBOARD
else:
    # Fetch logged in school details
    school_key = st.session_state.school_id
    school_data = SCHOOL_DB[school_key]

    # --- SIDEBAR NAVIGATION ---
    with st.sidebar:
        if os.path.exists(school_data['logo_file']):
            st.image(school_data['logo_file'], width=120)
        else:
            st.title("🎮")
        st.markdown(f" {school_data['name']}")
        st.markdown(f"**Role:** Verified Coach")
        st.write("---")

        # Simple navigation radio buttons
        page_selection = st.radio("Navigate", ["Match Dashboard", "Roster Management", "Standings"])

        st.write("---")
        if st.button("Log Out", type="secondary"):
            st.session_state.logged_in = False
            st.session_state.school_id = None
            st.rerun()

    # --- DYNAMIC HEADER CONTENT ---
    # Here is where we inject the school's unique color dynamically!
    st.markdown(
        f"""
        <div style="background-color: {school_data['color']}; padding: 20px; border-radius: 15px; margin-bottom: 25px; text-align: center; color: white;">
            <h1 style="margin: 0;">{school_data['name']} Esports</h1>
            <p style="margin: 5px 0 0 0; font-size: 18px; opacity: 0.9;">Home of the {school_data['mascot']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- ROUTING THE PAGES ---
    if page_selection == "Match Dashboard":
        st.header("Match Dashboard")
        st.caption("Manage and input current league scores.")

        # 3-COLUMN 3D ELEVATED LOOK USING STREAMLIT BORDER CONTAINERS
        col1, col2, col3 = st.columns(3)

        with col1:
            # Container with border simulates that floating card look
            with st.container(border=True):
                st.markdown("### 📁 Past Matches")
                st.caption("History Locked")
                st.write("---")
                st.markdown("**Beatrice (3)** vs Crete (1)")
                st.text("Rocket League Varsity • Tue")

        with col2:
            with st.container(border=True):
                st.markdown("### ⚡ Active Matches")
                st.markdown("*(Score Entry Enabled)*")
                st.write("---")

                # Custom Game Input Rule 1: Rocket League Best of 5
                st.markdown("**🚀 Rocket League Varsity**")
                r_col1, r_col2 = st.columns(2)
                with r_col1:
                    st.number_input(f"{school_data['name']} Games", min_value=0, max_value=3, value=0, key="rl_home")
                with r_col2:
                    st.number_input("Opponent Games", min_value=0, max_value=3, value=0, key="rl_away")
                st.button("Submit Rocket League Score", use_container_width=True, type="primary")

                st.write("---")

                # Custom Game Input Rule 2: Smash Crew Battle Stocks
                st.markdown("**💥 Super Smash Bros Crew**")
                smash_winner = st.selectbox("Select Winner", ["Select...", school_data['name'], "Opponent School"])
                st.number_input("Remaining Stocks (Tie-Breaker)", min_value=0, max_value=12, value=0)
                st.button("Submit Smash Score", use_container_width=True)

        with col3:
            with st.container(border=True):
                st.markdown("### 📅 Upcoming Schedule")
                st.write("---")
                st.markdown(f"**{school_data['name']}** vs Norris")
                st.text("Valorant Varsity • Thursday")

    elif page_selection == "Roster Management":
        st.header("Roster Management")
        st.write("Manage student players per game title.")
        # Your roster code can easily go here later!

    elif page_selection == "Standings":
        st.header("League Standings")
        st.write("Regional Standings with Strength of Schedule modifiers.")
        # Your pandas dataframe display can easily go here later!
