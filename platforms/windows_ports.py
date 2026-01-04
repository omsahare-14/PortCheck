import subprocess
import re

# This funtions runs `netstat -ano` in cmd and returns the output
def run_netstat():
    try:
        output = subprocess.check_output(
            ["netstat", "-ano"],
            text=True,
            stderr=subprocess.DEVNULL
        )
        return output
    except Exception:
        return None

# Filter the ports that are in LISTENING mode only
def filter_listening_ports(netstat_output):
    listening_lines = [] # stores the lines which has LISTENING state

    for line in netstat_output.splitlines():
        line = line.strip() # Split the lines

        if not line: # Skip empty lines
            continue

        # If lines starts with TCP and is LISTENING then append to listening_lines
        if line.startswith("TCP") and "LISTENING" in line:
            listening_lines.append(line)

        # If lines starts with UDP (because UDP is always listening) then append to listening_lines
        elif line.startswith("UDP"):
            listening_lines.append(line)

    return listening_lines

# Parse the lines and convert them into json
def parse_listening_lines(lines):
    parsed = []

    for line in lines:
        parts = re.split(r"\s+", line)

        try:
            protocol = parts[0].lower()
            local_addr = parts[1]
            pid = parts[-1]

            address, port = local_addr.rsplit(":", 1)

            parsed.append({
                "protocol": protocol,
                "address": address,
                "port": int(port),
                "pid": int(pid)
            })

        except Exception:
            continue

    return parsed

# Get the process assigned with the particular pid.
def get_process_name(pid):
    try:
        output = subprocess.check_output(
            ["tasklist", "/FI", f"PID eq {pid}"],
            text=True,
            stderr=subprocess.DEVNULL
        )
    except Exception:
        return "unknown"

    lines = output.splitlines()

    if len(lines) < 4:
        return "unknown"

    return lines[3].split()[0]

def scan_windows_ports():
    raw = run_netstat()
    if not raw:
        return []

    listening = filter_listening_ports(raw)
    parsed = parse_listening_lines(listening)

    for entry in parsed:
        entry["process"] = get_process_name(entry["pid"])

    return parsed