export default function RostersPage() {
  return (
    <div className="p-6 bg-slate-900 min-h-screen text-white">
      {/* Page Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold tracking-tight">Roster Dashboard</h1>
        <p className="text-slate-400">Manage, view, and lock current game rosters.</p>
      </div>

      {/* 3-Column Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 items-start">
        
        {/* COLUMN 1: PAST MATCHES */}
        <div className="bg-slate-800/80 backdrop-blur-md p-6 rounded-2xl border border-slate-700/50 shadow-[0_20px_50px_rgba(0,0,0,0.3)] min-h-[500px]">
          <h2 className="text-xl font-bold mb-4 text-slate-400 border-b border-slate-700 pb-2">Rocket League Varsity</h2>
          <div className="space-y-4">
            {/* We will drop past cards here */}
            <div className="bg-slate-900/60 p-4 rounded-xl border border-slate-700 shadow-inner">
  <div className="text-center text-xs font-semibold text-cyan-400 uppercase tracking-wider mb-2">Player Tags</div>
  <div className="flex items-center justify-between px-2 mb-4">
    <div className="text-center flex-1">
      Rocket_Mann
      Johnny_Five_Alive
      Crusher67
    </div>
  </div>
  </div>
            <p className="text-xs text-slate-500 text-center py-4">Roster Locked</p>
          </div>
        </div>

        {/* COLUMN 2: CURRENT WEEK (THE WOW FACTOR) */}
        <div className="bg-slate-800 p-6 rounded-2xl border-2 border-indigo-500/50 shadow-[0_20px_50px_rgba(99,102,241,0.15)] min-h-[500px] relative">
          
          <h2 className="text-xl font-bold mb-4 text-slate-400 border-b border-slate-700 pb-2">Super Smash Bros</h2>
          <div className="space-y-4">
            {/* Form cards go here */}
     
          </div>
        </div>

        {/* COLUMN 3: UPCOMING MATCHES */}
        <div className="bg-slate-800/80 backdrop-blur-md p-6 rounded-2xl border border-slate-700/50 shadow-[0_20px_50px_rgba(0,0,0,0.3)] min-h-[500px]">
          <h2 className="text-xl font-bold mb-4 text-slate-400 border-b border-slate-700 pb-2">Valorant</h2>
          <div className="space-y-4">
            {/* Upcoming cards go here */}

          </div>
        </div>

      
    </div>
  </div>);
}