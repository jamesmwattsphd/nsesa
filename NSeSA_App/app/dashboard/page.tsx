import Image from "next/image";
export default function DashPage() {
  return (
    
    <div className="p-6 bg-slate-900 min-h-screen text-white">
      {/* Page Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold tracking-tight">Beatrice</h1>
        <p className="text-slate-400">Home of the Orange Gamers</p>
      </div>
        <Image
                      className="dark:invert"
                      src="/beatrice_ban.jpg"
                      alt="Vercel logomark"
                      width={900}
                      height={500}
                    />
      {/* 3-Column Grid */}
      </div>)}