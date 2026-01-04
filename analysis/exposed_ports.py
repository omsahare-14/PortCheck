PORT_EXPLANATIONS = {
    22:  "SSH – Remote shell access. If exposed broadly, enables brute force and credential abuse.",
    21:  "FTP – Plaintext file transfer. Credentials can be intercepted or brute forced.",
    23:  "Telnet – Unencrypted remote access. Deprecated and unsafe.",
    25:  "SMTP – Mail transfer service. Can be abused for spam or spoofing if misconfigured.",
    53:  "DNS – Name resolution service. Can be abused for amplification or poisoning attacks.",
    80:  "HTTP – Web service. Vulnerable to common web attacks if misconfigured.",
    443: "HTTPS – Web service. Misconfigurations or vulnerable apps can be exploited.",
    135: "Windows RPC – Core Windows service. Common lateral movement vector.",
    139: "NetBIOS – Windows networking service. Information leakage and lateral movement risk.",
    445: "SMB – Windows file sharing. Widely abused in ransomware and lateral movement.",
    3389: "RDP – Remote Desktop. Frequent brute force and takeover target.",
    3306: "MySQL – Database service. Databases should not be internet facing.",
    5432: "PostgreSQL – Database service. Should be restricted to private networks.",
    1433: "MSSQL – Database service. High risk if exposed publicly.",
    27017: "MongoDB – Database service. Historically exposed without authentication.",
    6379: "Redis – Database/cache. No auth by default in many setups.",
    5900: "VNC – Remote desktop service. Weak auth and brute force risk.",
    8080: "HTTP Alt – Often admin or dev interfaces. Frequently misconfigured.",
    8443: "HTTPS Alt – Admin or internal web interface.",
    8000: "HTTP Alt – Common dev or admin service.",
    8888: "HTTP Alt – Often used for dashboards or notebooks.",
    9000: "Hadoop – Internal cluster service. Not meant to be public.",
    9200: "Elasticsearch – Database/search engine. Massive data exposure risk.",
    11211: "Memcached – Cache service. Abuse and data leakage risk.",
    4444: "Metasploit – Common malware or backdoor port.",
    5555: "ADB – Android debug bridge. Should never be exposed."
}

def get_finding(entry):
    if entry["exposure"] != "exposed":
        return None

    port = entry["port"]

    if port not in PORT_EXPLANATIONS:
        return None

    return {
        "service": PORT_EXPLANATIONS[port]
    }
