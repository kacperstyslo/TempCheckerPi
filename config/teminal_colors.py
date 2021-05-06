from dataclasses import dataclass


@dataclass
class Bcolors:
    """
    Notification colors
    """
    MAGENTA: str = "\033[35m"
    PASS: str = "\033[32m"
    ERROR: str = "\033[31m"
    WARNING: str = "\033[33m"
    LGRAY: str = "\033[0;37m"
    ENDC: str = '\033[0m'
