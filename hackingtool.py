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
        # Changed from a warning to a harder exit -- too many tools silently fail without root
        print("[!] Error: HackingTool must be run with root privileges.")
        print("[!] Please re-run using 'sudo python3 hackingtool.py'.")
        sys.exit(1)
    return True


def check_dependencies():
    """Check if required system dependencies are installed."""
    # Added curl to dependencies -- several tools in the framework rely on it for downloads
    dependencies = ["git", "python3", "pip3", "curl"]
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
        ("12", "Reverse En
