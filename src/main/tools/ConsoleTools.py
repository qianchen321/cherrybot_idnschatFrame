from colorama import *


def console_colour(config: str):
    init(autoreset=True, convert=True)
    RESET_ALL = Fore.RESET + Back.RESET + Style.RESET_ALL
    if config == "ERROR":
        r = Fore.RED + Style.BRIGHT + f"[{config}]"
    elif config == "INFO":
        r = Fore.YELLOW + Style.BRIGHT + f"[{config}]"
    elif config == "Receive":
        r = Style.BRIGHT + f"[{config}]"
    elif config == "Send":
        r = Fore.GREEN + Style.BRIGHT + f"[{config}]"
    else:
        r = f"[{config}]"
    return r + RESET_ALL


