# HackingTool 🔧

> A fork of [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) — All-in-One Hacking Tool for Linux.

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Linux-lightgrey.svg)

## ⚠️ Disclaimer

This tool is intended for **educational and ethical security research purposes only**. The author is not responsible for any misuse or damage caused by this program. Use it only on systems you own or have explicit permission to test.

## 📋 Features

- Anonymous Surfing Tools
- Information Gathering Tools
- Wordlist Generator
- Wireless Attack Tools
- SQL Injection Tools
- Phishing Attack Tools
- Web Attack Tools
- Post Exploitation Tools
- Forensic Tools
- Payload Creation Tools
- Exploit Framework
- Reverse Engineering Tools
- DDOS Attack Tools
- Steganography Tools
- And more...

## 🔧 Requirements

- Python 3.x
- Linux (Kali Linux, Parrot OS, Ubuntu, Debian recommended)
- Root privileges (for some tools)

## 📦 Installation

### Standard Installation

```bash
git clone https://github.com/your-username/hackingtool.git
cd hackingtool
pip3 install -r requirements.txt
python3 install.py
```

### Docker Installation

```bash
docker build -t hackingtool .
docker run -it hackingtool
```

## 🚀 Usage

```bash
python3 hackingtool.py
```

Or if installed system-wide:

```bash
hackingtool
```

## 🗒️ Personal Notes

> I'm using this fork primarily to learn about network reconnaissance and information gathering tools. The SQL injection and web attack sections have been most useful for my CTF practice on platforms like HackTheBox and TryHackMe.
>
> **Tools I've found most useful so far:**
> - `nmap` (Information Gathering) — bread and butter for recon
> - `sqlmap` (SQL Injection) — great for SQLi challenges on HTB
> - `gobuster` (Web Attack) — fast directory brute-forcing
> - `nikto` (Web Attack) — handy for quick web server scans before diving deeper
> - `ffuf` (Web Attack) — started preferring this over gobuster for vhost fuzzing
>
> **CTF tips I keep forgetting:**
> - Always run `nmap -sV -sC` first for a solid baseline scan
> - Pair `gobuster` with `-x php,html,txt` on PHP-heavy boxes
> - Use `nmap -p-` for a full port scan when the default scan misses something — caught a box on a non-standard port (8080, 8443) this way more than once
> - `sqlmap --level=3 --risk=2` is worth trying if the default run comes up empty
> - `ffuf -w wordlist.txt -u http://target/ -H "Host: FUZZ.target.htb"` for vhost discovery
> - `feroxbuster` is worth trying as an alternative to `ffuf`/`gobuster` — recursive scanning by default saves a lot of manual follow-up
> - `wfuzz` is another fuzzer worth having in the toolkit — useful when `ffuf` chokes on certain response filtering edge cases
> - For OSCP-style boxes, `enum4linux-ng` is a solid upgrade over the original `enum4linux` for SMB enumeration

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](.github/PULL_REQUEST_TEMPLATE.md) before submitting a pull request.

### Reporting Bugs

Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template when opening an issue.

### Requesting Feat
