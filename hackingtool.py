#!/usr/bin/env python3
"""
HackingTool - A collection of hacking tools for security researchers and penetration testers.
Fork of Z4nzu/hackingtool

This is the main entry point for the hackingtool application.
"""

import os
import sys
import subprocess

# Ensure the script is run with Python 3
if sys.version_info[0] < 3:
    print("[!] HackingTool requires Python 3. Please use 'python3' to run this script.")
    sys.exit(1)


def banner():
    """Display the ASCII art banner for HackingTool."""
    print(r"""
    ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗
    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝
    ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
    ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
    ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
         ████████╗ ██████╗  ██████╗ ██╗
            ██╔══╝██╔═══██╗██╔═══██╗██║
            ██║   ██║   ██║██║   ██║██║
            ██║   ██║   ██║██║   ██║██║
            ██║   ╚██████╔╝╚██████╔╝███████╗
            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
    """)
    print("    [*] HackingTool - All in One Hacking Tool")
    print("    [*] For Educational Purposes Only")
    print("    [*] Use Responsibly and Legally\n")


def check_root():
    """Check if the script is running with root privileges."""
    if os.geteuid() != 0:
        print("[!] Warning: Some tools may require root privileges.")
        print("[!] Consider running with 'sudo' if you encounter permission errors.\n")
        return False
    return True


def check_dependencies():
    """Check if required system dependencies are installed."""
    dependencies = ["git", "python3", "pip3"]
    missing = []

    for dep in dependencies:
        try:
            subprocess.run(
                [dep, "--version"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            missing.append(dep)

    if missing:
        print(f"[!] Missing dependencies: {', '.join(missing)}")
        print("[!] Please install them before proceeding.")
        return False

    return True


def show_main_menu():
    """Display the main menu and return the user's choice."""
    print("\n" + "=" * 60)
    print(" " * 20 + "MAIN MENU")
    print("=" * 60)

    categories = [
        ("1",  "Anonymous Surfing Tools"),
        ("2",  "Information Gathering Tools"),
        ("3",  "Wordlist Generator"),
        ("4",  "Wireless Attack Tools"),
        ("5",  "SQL Injection Tools"),
        ("6",  "Phishing Attack Tools"),
        ("7",  "Web Attack Tools"),
        ("8",  "Post Exploitation Tools"),
        ("9",  "Forensic Tools"),
        ("10", "Payload Creation Tools"),
        ("11", "Exploit Framework Tools"),
        ("12", "Reverse Engineering Tools"),
        ("13", "DDOS Attack Tools"),
        ("14", "Remote Administrator Tools (RAT)"),
        ("15", "XSS Attack Tools"),
        ("16", "Steganography Tools"),
        ("17", "SocialMedia Brute Force"),
        ("18", "Android Hacking Tools"),
        ("19", "IDN Homograph Attack Tools"),
        ("20", "Email Verify Tools"),
        ("21", "Hash Cracking Tools"),
        ("22", "Wifi Deauthenticate Tools"),
        ("23", "SocialMedia Finder"),
        ("24", "Payload Injector Tools"),
        ("25", "Server/Web Hacking Tools"),
        ("99", "Exit"),
    ]

    for num, name in categories:
        print(f"  [{num:>2}] {name}")

    print("=" * 60)
    return input("\n[?] Select a category: ").strip()


def main():
    """Main function to run the HackingTool application."""
    try:
        banner()
        check_root()

        if not check_dependencies():
            sys.exit(1)

        while True:
            choice = show_main_menu()

            if choice == "99":
                print("\n[*] Exiting HackingTool. Stay ethical!\n")
                sys.exit(0)
            else:
                print(f"\n[!] Category '{choice}' is not yet implemented in this version.")
                input("[*] Press Enter to return to the main menu...")

    except KeyboardInterrupt:
        print("\n\n[*] Interrupted by user. Exiting...\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
