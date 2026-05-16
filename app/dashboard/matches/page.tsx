export default function MatchesPage() {
  return (
    <div className="p-6 bg-slate-900 min-h-screen text-white">
      {/* Page Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold tracking-tight">Match Dashboard</h1>
        <p className="text-slate-400">Manage, view, and input current league scores.</p>
      </div>

      {/* 3-Column Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 items-start">
        
        {/* COLUMN 1: PAST MATCHES */}
        <div className="bg-slate-800/80 backdrop-blur-md p-6 rounded-2xl border border-slate-700/50 shadow-[0_20px_50px_rgba(0,0,0,0.3)] min-h-[500px]">
          <h2 className="text-xl font-bold mb-4 text-slate-400 border-b border-slate-700 pb-2">Past Matches</h2>
          <div className="space-y-4">
            {/* We will drop past cards here */}
            <div className="bg-slate-900/60 p-4 rounded-xl border border-slate-700 shadow-inner">
  <div className="text-center text-xs font-semibold text-cyan-400 uppercase tracking-wider mb-2">Rocket League Varsity</div>
  <div className="flex items-center justify-between px-2 mb-4">
    <div className="text-center flex-1">
      <div className="w-12 h-12 bg-orange-600 rounded-full mx-auto flex items-center justify-center font-bold text-lg shadow-md">B</div>
      <div className="text-sm font-bold mt-1">Beatrice</div>
      <div className="text-sm font-bold mt-1">2</div>
    </div>
    <div className="text-slate-500 font-extrabold tracking-widest text-sm">VS</div>
    <div className="text-center flex-1">
      <div className="w-12 h-12 bg-red-600 rounded-full mx-auto flex items-center justify-center font-bold text-lg shadow-md">C</div>
      <div className="text-sm font-bold mt-1">Crete</div>
      <div className="text-sm font-bold mt-1">1</div>
    </div>
  </div>
  </div>
            <p className="text-xs text-slate-500 text-center py-4">History locked</p>
          </div>
        </div>

        {/* COLUMN 2: CURRENT WEEK (THE WOW FACTOR) */}
        <div className="bg-slate-800 p-6 rounded-2xl border-2 border-indigo-500/50 shadow-[0_20px_50px_rgba(99,102,241,0.15)] min-h-[500px] relative">
          <span className="absolute -top-3 right-6 bg-indigo-500 text-xs uppercase tracking-widest font-extrabold px-3 py-1 rounded-full shadow-lg">Live Week</span>
          <h2 className="text-xl font-bold mb-4 text-indigo-400 border-b border-indigo-900 pb-2">Active Matches</h2>
          <div className="space-y-4">
            {/* Form cards go here */}
            <div className="bg-slate-900/60 p-4 rounded-xl border border-slate-700 shadow-inner">
  <div className="text-center text-xs font-semibold text-cyan-400 uppercase tracking-wider mb-2">Rocket League Varsity</div>
  
  <div className="flex items-center justify-between px-2 mb-4">
    <div className="text-center flex-1">
      <div className="w-12 h-12 bg-orange-600 rounded-full mx-auto flex items-center justify-center font-bold text-lg shadow-md">B</div>
      <div className="text-sm font-bold mt-1">Beatrice</div>
      
    </div>
    <div className="text-slate-500 font-extrabold tracking-widest text-sm">VS</div>
    <div className="text-center flex-1">
      <div className="w-12 h-12 bg-red-600 rounded-full mx-auto flex items-center justify-center font-bold text-lg shadow-md">C</div>
      <div className="text-sm font-bold mt-1">Crete</div>
    </div>
  </div>

  {/* Rocket League Specific Inputs */}
  <div className="bg-slate-800 p-2 rounded-lg grid grid-cols-2 gap-2 text-center">
    <div>
      <label className="text-[10px] text-slate-400 block mb-1">Beatrice Wins</label>
      <input type="number" max="3" placeholder="0" className="w-full bg-slate-950 border border-slate-700 rounded p-1 text-center font-bold text-indigo-400 focus:outline-none focus:border-indigo-500" />
    </div>
    <div>
      <label className="text-[10px] text-slate-400 block mb-1">Crete Wins</label>
      <input type="number" max="3" placeholder="0" className="w-full bg-slate-950 border border-slate-700 rounded p-1 text-center font-bold text-indigo-400 focus:outline-none focus:border-indigo-500" />
    </div>
  </div>
  <button className="w-full mt-3 bg-indigo-600 hover:bg-indigo-500 text-xs font-bold py-2 rounded-lg shadow-md transition-all">Submit Series Score</button>
</div>
<div className="bg-slate-900/60 p-4 rounded-xl border border-slate-700 shadow-inner mt-4">
  <div className="text-center text-xs font-semibold text-emerald-400 uppercase tracking-wider mb-2">Super Smash Bros Crew Battle</div>
  
  <div className="flex items-center justify-between px-2 mb-4">
    <div className="text-center flex-1">
      <div className="w-12 h-12 bg-orange-600 rounded-full mx-auto flex items-center justify-center font-bold text-lg shadow-md">B</div>
      <div className="text-sm font-bold mt-1">Beatrice</div>
    </div>
    <div className="text-slate-500 font-extrabold tracking-widest text-sm">VS</div>
    <div className="text-center flex-1">
      <div className="w-12 h-12 bg-green-600 rounded-full mx-auto flex items-center justify-center font-bold text-lg shadow-md">N</div>
      <div className="text-sm font-bold mt-1">Norris</div>
    </div>
  </div>

  {/* Fighter/Stock Ruleset Inputs */}
  <div className="space-y-2">
    <div className="flex justify-between items-center bg-slate-800 px-3 py-1.5 rounded-lg text-xs">
      <span className="text-slate-300">Winner Selection:</span>
      <select className="bg-slate-950 border border-slate-700 rounded px-2 py-1 text-emerald-400 font-bold focus:outline-none">
        <option>Select Winner...</option>
        <option>Beatrice</option>
        <option>Norris</option>
      </select>
    </div>
    <div>
      <input type="number" placeholder="Remaining Stocks (Tie-Breaker)" className="w-full bg-slate-950 border border-slate-700 rounded p-1.5 text-center text-xs text-slate-300 focus:outline-none" />
    </div>
  </div>
  <button className="w-full mt-3 bg-indigo-600 hover:bg-indigo-500 text-xs font-bold py-2 rounded-lg shadow-md transition-all">Submit Crew Score</button>
</div>
          </div>
        </div>

        {/* COLUMN 3: UPCOMING MATCHES */}
        <div className="bg-slate-800/80 backdrop-blur-md p-6 rounded-2xl border border-slate-700/50 shadow-[0_20px_50px_rgba(0,0,0,0.3)] min-h-[500px]">
          <h2 className="text-xl font-bold mb-4 text-slate-400 border-b border-slate-700 pb-2">Upcoming Schedule</h2>
          <div className="space-y-4">
            {/* Upcoming cards go here */}

          </div>
        </div>

      
    </div>
  </div>);
}