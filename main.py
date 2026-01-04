from platforms.os_detect import get_os
from platforms.windows_ports import scan_windows_ports
from analysis.exposure_check import classify_exposure
from analysis.exposed_ports import get_finding
from output.console import print_results

def deduplicate(entries):
    grouped = {}

    for e in entries:
        key = (e["port"], e["process"])

        if key not in grouped:
            grouped[key] = {
                "protocol": e["protocol"],
                "port": e["port"],
                "process": e["process"],
                "pid": e["pid"],
                "service": e["service"],
                "addresses": {e["address"]}
            }
        else:
            grouped[key]["addresses"].add(e["address"])

    for v in grouped.values():
        v["addresses"] = list(v["addresses"])

    return list(grouped.values())


def main():
    if get_os() != "windows":
        print("Windows only for now.")
        return

    entries = scan_windows_ports()
    results = []

    for entry in entries:
        entry["exposure"] = classify_exposure(entry["address"])
        finding = get_finding(entry)

        if finding:
            entry.update(finding)
            results.append(entry)

    if not results:
        print("No exposed services of interest found.")
        return

    final = deduplicate(results)
    print_results(final)


if __name__ == "__main__":
    main()
