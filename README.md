# PortCheck

PortCheck is a **Windows-only local attack surface awareness tool**.

It identifies **specific exposed network ports** that are commonly abused in real-world attacks and explains **why security professionals care about them**.

This tool does **not** attempt to exploit anything.  
It does **not** guess intent.  
It does **not** label services as malicious.

It answers one simple question:

> If this port is exposed on my system, why should I pay attention to it?

---

## Why PortCheck exists

Most built-in utilities and scanners show **raw networking data**:

- `netstat`
- `tasklist`
- generic port scanners

They tell you *what* is listening, but not *why it matters*.

PortCheck bridges that gap by adding **security context** to a **curated list of high-impact ports** that are frequently involved in breaches, lateral movement, ransomware, and misconfiguration incidents.

---

## What PortCheck does

- Enumerates listening TCP and UDP ports on Windows
- Detects which ports are **network exposed**
- Flags only **explicitly defined ports of interest**
- Explains, in plain language:
  - what the service is
  - why exposure matters
- Deduplicates services bound to multiple interfaces
- Presents clean, readable console output

---

## What PortCheck does NOT do

- It does not exploit vulnerabilities
- It does not scan remote hosts
- It does not guess whether a service is “safe”
- It does not analyze firewall rules
- It does not generate CVE lists
- It does not auto-remediate anything

This tool is about **visibility and understanding**, not automation.

---

## Supported platform

- Windows only
- Tested on Windows 10 and Windows 11
- Administrator privileges recommended for full visibility

Linux support is intentionally **not included yet**.

---

## How it works internally

1. Runs native Windows networking commands to enumerate listening ports
2. Filters ports that are externally reachable
3. Matches exposed ports against a **static, curated list**
4. Attaches a short security explanation per port
5. Deduplicates repeated bindings across interfaces
6. Prints a human-readable report

No machine learning.  
No heuristics.  
No hidden logic.

---

## Example output

[EXPOSED] TCP multiple interfaces:135 svchost.exe PID 2076
Info: Windows RPC – Core Windows service. Common lateral movement vector.

[EXPOSED] TCP multiple interfaces:445 System PID 4
Info: SMB – Windows file sharing. Widely abused in ransomware and lateral movement.

[EXPOSED] TCP 0.0.0.0:3389 svchost.exe PID 1020
Info: RDP – Remote Desktop. Frequent brute force and takeover target.


If a port is **not** in the predefined list, it is intentionally ignored.

---

## Why some ports are flagged and others are not

PortCheck does **not** try to flag everything.

It only flags ports that meet **all three** conditions:

- The port is exposed to the network
- The port is known to be a high-impact service
- The port has a clear, explainable security history

This keeps the signal high and avoids misleading output.

---

## Included port coverage

Examples of ports currently explained by PortCheck (Only a few ports are listed below; the tool scans more ports):

### Remote access services
- SSH (22)
- RDP (3389)
- VNC (5900)
- Telnet (23)
- FTP (21)

### Windows lateral movement services
- RPC (135)
- NetBIOS (139)
- SMB (445)

### Databases and data stores
- MySQL (3306)
- PostgreSQL (5432)
- MSSQL (1433)
- MongoDB (27017)
- Redis (6379)
- Elasticsearch (9200)
- Memcached (11211)

### Web and administrative interfaces
- HTTP (80)
- HTTPS (443)
- Alternative web ports (8000, 8080, 8443, 8888)

### Explicitly abuse-prone ports
- Metasploit (4444)
- Android Debug Bridge (5555)

The list is **explicit and static by design**.

---