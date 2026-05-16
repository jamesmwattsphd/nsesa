import Image from "next/image";

export default function Home() {
  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="p-6 bg-slate-900 min-h-screen text-white">
        <Image
              className="dark:invert"
              src="/title.png"
              alt="Vercel logomark"
              width={900}
              height={500}
            />

        
          <h1 className=" text-3xl font-semibold leading-10 tracking-tight text-white dark:text-zinc-50">
            Welcome to the Nebraska Schools eSports Association's Gaming Hub
          </h1>
          <p className="max-w-md text-lg leading-8 text-zinc-600 dark:text-zinc-400">
            
            
          </p>
        
        <div className="flex flex-col gap-4 text-base font-medium sm:flex-row">
          <a
            className="flex h-12 w-full items-center justify-center gap-2 rounded-full bg-foreground px-5 text-background transition-colors hover:bg-[#383838] dark:hover:bg-[#ccc] md:w-[158px]"
            href="/login"
            target="_blank"
            rel="noopener noreferrer"
          >
            
            Log In
          </a></div>
        <div className="flex flex-col gap-4 text-base font-medium sm:flex-row">
          <a
            className="flex h-12 w-full items-center justify-center gap-2 rounded-full bg-foreground px-5 text-background transition-colors hover:bg-[#383838] dark:hover:bg-[#ccc] md:w-[158px]"
            href="/join"
            target="_blank"
            rel="noopener noreferrer"
          >
            
            Join Us
          </a>
        </div>
      </main>
    </div>
  );
}
