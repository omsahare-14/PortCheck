from colorama import Fore, Style, init
init(autoreset=True)

def print_results(entries):
    for e in entries:
        if len(e["addresses"]) > 1:
            addr_text = f"{Fore.RED}multiple interfaces{Style.RESET_ALL}"
        else:
            addr_text = e["addresses"][0]

        port_text = f"{Fore.CYAN}{e['port']}{Style.RESET_ALL}"

        print(
            f"{Fore.YELLOW}[EXPOSED]{Style.RESET_ALL} "
            f"{e['protocol'].upper()} "
            f"{addr_text}:{port_text} "
            f"{e['process']} "
            f"PID {e['pid']}"
        )
        print(f"  Info: {e['service']}\n")
