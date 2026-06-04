# Port-EX — Full-Range TCP Port Scanner

> A fast TCP port scanner written in Python that scans all 65,535 ports on a target host and identifies open services. Built as a learning tool to understand how tools like Nmap perform service discovery at the socket level.

---

## What It Does

- Scans all 65,535 TCP ports on a given IP address
- Identifies open ports and resolves service names (HTTP, SSH, FTP, etc.)
- Displays a clean terminal banner via `pyfiglet`
- Configurable timeout to balance speed vs. accuracy

---

## Demo

```
 ____            _     _____  __
|  _ \ ___  _ __| |_  | ____|/ _|
| |_) / _ \| '__| __|  |  _|  |_
|  __/ (_) | |  | |_   | |___|  _|
|_|   \___/|_|   \__|  |_____|_|

Scanning 192.168.1.1 for open ports...

[+] Port 22 is open (ssh)
[+] Port 80 is open (http)
[+] Port 443 is open (https)
[+] Port 3306 is open (mysql)
```

---

## Installation

```bash
git clone https://github.com/parth0xu/Port-Scanner
cd Port-Scanner
pip install pyfiglet
```

---

## Usage

```bash
python3 port.py
# Enter target IP when prompted: 192.168.1.1
```

> **Legal notice:** Only scan hosts you own or have explicit permission to test. Unauthorized port scanning may be illegal.

---

## How It Works

The scanner uses Python's `socket` library to attempt a TCP connection (`connect_ex`) on each port. A return value of `0` means the port accepted the connection — it's open. The `socket.getservbyport()` call maps port numbers to known service names from the system's `/etc/services` database.

```python
result = s.connect_ex((target, port))
if result == 0:
    service = socket.getservbyport(port)
    print(f"[+] Port {port} is open ({service})")
```

**Why `connect_ex` instead of `connect`?** `connect()` raises an exception on failure. `connect_ex()` returns an error code — cleaner for looping over thousands of ports without try/except overhead on every closed port.

---

## Limitations & Planned Improvements

- Currently single-threaded — scanning all 65,535 ports is slow (~30+ min). Next version will use `concurrent.futures.ThreadPoolExecutor` for parallel scanning.
- Only TCP connect scan — no SYN (half-open) scan, which requires raw sockets and root privileges
- No banner grabbing yet — future version will attempt to read service banners for version detection

---

## Skills Demonstrated

`Python` `Socket Programming` `Network Scanning` `TCP/IP` `Service Enumeration`
