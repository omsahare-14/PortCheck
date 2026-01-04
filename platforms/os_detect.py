import platform

def get_os():
    os_name = platform.system().lower()

    if os_name == "windows":
        return "windows"
    elif os_name == "linux":
        return "linux"
    else:
        return "unsupported"