import React, { useState } from 'react'
import { Menu, X, Terminal } from 'lucide-react'
import NavLinks from './NavLinks'


const Navbar: React.FC = () => {
    const [mobileMenuOpen, setMobileMenuOpen] = useState<boolean>(false)
    const toggleMobileMenu = () => setMobileMenuOpen(prev => !prev)


    return (
        <header className="sticky top-0 z-50 w-full border-b border-neutral-800 bg-black/80 backdrop-blur-md">
            <div className="mx-auto flex h-14 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        
                {/* Left Section: Brand & Navlinks */}
                <div className="flex items-center gap-8">
                    {/* Brand Logo */}
                    <a
                        href="/"
                        className="flex items-center gap-2 font-mono text-sm font-semibold tracking-tight text-white hover:opacity-90 transition-opacity"
                    >
                        <div className="flex h-6 w-6 items-center justify-center rounded bg-white text-black">
                            <Terminal className="h-3.5 w-3.5 stroke-[2.5]" />
                        </div>
                        <span>micro blog</span>
                    </a>

                    {/* Desktop Navigation Links */}
                    <nav className="hidden md:flex md:items-center md:gap-6">
                        {NavLinks.map(link => {
                            const label = link.label
                            return (
                                <a
                                    key={label}
                                    href={link.href}
                                    className="text-xs font-medium text-neutral-400 transition-colors hover:text-white"
                                >
                                    {label}
                                </a>
                            )                            
                        })}
                    </nav>
                </div>

                {/* Right Section: Auth Actions */}
                <div className="hidden items-center gap-3 md:flex">
                    <a
                        href="/login"
                        className="rounded-md px-3 py-1.5 text-xs font-medium text-neutral-300 transition-colors hover:text-white"
                    >
                        Log in
                    </a>
                    <a
                        href="/register"
                        className="rounded-md bg-white px-3 py-1.5 text-xs font-medium text-black transition-all hover:bg-neutral-200 active:scale-95"
                    >
                        Sign up
                    </a>
                </div>

                {/* Mobile Menu Button */}
                <div className="flex md:hidden">
                    <button
                        type="button"
                        onClick={toggleMobileMenu}
                        aria-label="Toggle Navigation Menu"
                        className="inline-flex items-center justify-center rounded-md p-2 text-neutral-400 hover:bg-neutral-900 hover:text-white focus:outline-none"
                    >
                        {mobileMenuOpen ? (
                            <X className="h-5 w-5" />
                        ) : (
                            <Menu className="h-5 w-5" />
                        )}
                    </button>
                </div>
            </div>

            {/* Mobile Drawer Navigation */}
            {mobileMenuOpen && (
                <div className="border-b border-neutral-800 bg-black px-4 pt-2 pb-6 md:hidden">
                    <div className="flex flex-col space-y-3 pt-2">
                        {NavLinks.map(link => {
                            const label = link.label
                            return (
                                <a
                                    key={label}
                                    href={link.href}
                                    onClick={() => setMobileMenuOpen(false)}
                                    className="rounded-md px-3 py-2 text-sm font-medium text-neutral-300 hover:bg-neutral-900 hover:text-white"
                                >
                                    {label}
                                </a>
                            )                            
                        })}
                        <div className="mt-4 border-t border-neutral-800 pt-4 flex flex-col gap-2">
                            <a
                                href="/login"
                                onClick={() => setMobileMenuOpen(false)}
                                className="w-full rounded-md border border-neutral-800 bg-neutral-950 py-2 text-center text-xs font-medium text-neutral-300 hover:bg-neutral-900 hover:text-white"
                            >
                                Log in
                            </a>
                            <a
                                href="/register"
                                onClick={() => setMobileMenuOpen(false)}
                                className="w-full rounded-md bg-white py-2 text-center text-xs font-medium text-black hover:bg-neutral-200"
                            >
                                Sign up
                            </a>
                        </div>
                    </div>
                </div>
            )}
    </header>
  )
}


export default Navbar
