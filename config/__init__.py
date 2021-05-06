import time
import sys
from colorama import init
from typing import Dict, List
from .network_scanner import ActiveDevices
from .connect_to_device import ConnectDevice
from .terminal_clear import Clear
from .teminal_colors import Bcolors
from app.app_db.devices_database import DevicesDatabase


class AppConfig:
    def __init__(self):
        init(strip=not sys.stdout.isatty())
        self.active_devices = ActiveDevices()
        self.db = DevicesDatabase('Devices.db')
        self.chosen_device_id: int = 0
        self.correct_ssh_login: str = ''
        self.correct_ssh_password: str = ''
        self.chosen_device_ip_address: str = ''
        self.chosen_device_port: int = 22
        self.data_refresh_interval: int = 60
        self.email_addresses: List[str] = []
        self.filtered_active_devices: Dict[int, str] = self.active_devices()

    def __call__(self):
        self.__check_connection_to_device()
        self.__save_device_data_into_database()
        self.__change_refresh_data_interval()
        self.show_end_configuration_message()

    def __check_connection_to_device(self):
        """
        This module will check connection between user and device.
        """
        while True:
            Clear.clear()
            print(20 * '=', "Choose device by number", 20 * '=')
            self.active_devices.list_scanned_device_with_open_ssh()
            print(f"[{Bcolors.WARNING}0{Bcolors.ENDC}] Exit from configuration!")
            print(65 * '=')
            chosen_device: int = int(input("Chose number: "))
            if not chosen_device:
                sys.exit(0)
            else:
                check_credentials: list = ConnectDevice(device_ip=self.filtered_active_devices.get(chosen_device),
                                                        device_port=self.chosen_device_port).connect_to_device()
                time.sleep(2)
            if check_credentials:
                self.chosen_device_ip_address: str = self.filtered_active_devices.get(chosen_device)
                self.correct_ssh_login, self.correct_ssh_password = check_credentials[0], check_credentials[1]
                self.chosen_device_id = chosen_device
                break

    def __save_device_data_into_database(self):
        """
        This method send variables into database.
        """
        self.db.insert_values_into_device_data_table(device_id=self.chosen_device_id,
                                                     device_ip=self.chosen_device_ip_address,
                                                     device_port=self.chosen_device_port,
                                                     device_ssh_login=self.correct_ssh_login,
                                                     device_ssh_password=self.correct_ssh_password,
                                                     data_refresh_interval=self.data_refresh_interval)

    def __change_refresh_data_interval(self):
        refresh_data_interval = input("\nBy default, the application will download data to the chart every 60 seconds,"
                                      "\nif you want to change this data refresh time set new value here(in seconds): ")
        try:
            refresh_data_interval = int(refresh_data_interval)
        except ValueError:
            print(f"Downloading data to the chart has been set to: {Bcolors.WARNING}60{Bcolors.ENDC}")
        else:
            self.db.update_value_of_data_refresh_interval(refresh_data_interval, self.chosen_device_id)

    @staticmethod
    def show_end_configuration_message():
        print(f"\n{Bcolors.PASS}Success{Bcolors.ENDC}! Application has completed the initial configuration."
              "\nNow you can run application! In application just type ip address of device to see live "
              "updating graph!")
