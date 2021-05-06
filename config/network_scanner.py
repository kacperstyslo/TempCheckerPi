import sys
import socket
from pythonping import ping
from typing import Dict, List
from .config_exceptions import LowPrivileges
from .teminal_colors import Bcolors


class ActiveDevices:

    def __init__(self):
        self.user_network_area: str = '.'.join(
            list(filter(None, socket.gethostbyname(socket.gethostname()).split('.')))[0:3])
        self.active_devices: List[str] = []
        self.active_devices_with_ssh: Dict[int, str] = {}

    def __call__(self) -> Dict[int, str]:
        self.__scan_user_network_area()
        self.check_open_ports_of_active_devices()
        return self.active_devices_with_ssh

    def __scan_user_network_area(self) -> None:
        """
        This module will search for active devices in user network area.
        """
        try:
            for num in range(1, 255):
                command = ping(f'{self.user_network_area}.{num}', timeout=0.01, count=1)
                if command.success():
                    self.active_devices.append(f'{self.user_network_area}.{num}')
        except PermissionError:
            print(LowPrivileges())
            sys.exit(0)

    def check_open_ports_of_active_devices(self) -> None:
        """
        This module will check if active devices has open port ssh(22).
        """
        for num, device_to_check in enumerate(self.active_devices, 1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.0001)
                result = sock.connect_ex((device_to_check, 22))
                sock.close()
            except (ConnectionRefusedError, OSError):
                pass
            finally:
                if not result:
                    self.active_devices_with_ssh[num] = device_to_check

    def list_scanned_device_with_open_ssh(self) -> None:
        """
        This module lists all devices in user network area with open port ssh(22).
        """
        for device_id, device_ip in self.active_devices_with_ssh.items():
            print(f"[{Bcolors.WARNING}{device_id}{Bcolors.ENDC}] Device with IP: {Bcolors.PASS}{device_ip}{Bcolors.ENDC}"
                  f" has open port {Bcolors.PASS}ssh(22){Bcolors.ENDC}")
