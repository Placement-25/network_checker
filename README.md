# 📡 Network Connectivity Checker

A lightweight, cross-platform Python tool to **ping multiple servers and log their availability status**, ideal for network diagnostics, monitoring, and IT automation tasks.

---

## 🚀 Features

- ✅ Pings a list of hostnames/IPs and returns `Online` / `Offline` status
- 📝 Logs each attempt with timestamp and status
- 🌐 Cross-platform support (Linux, macOS, Windows)
- ⚙️ CLI tool ready for automation and cron integration
- 🛠️ Robust error handling for unreachable or malformed hosts

---

## 🔧 Requirements

- Python 3.7+
- No external dependencies

---

## ▶️ Usage

### ✅ Basic command:

```bash
python network_checker.py --hosts google.com 8.8.8.8 github.com
