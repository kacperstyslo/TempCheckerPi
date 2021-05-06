import paramiko
from typing import List
from .teminal_colors import Bcolors
from .terminal_clear import Clear


class ConnectDevice:

    def __init__(self, **kwargs):
        self.device_ip: str = kwargs['device_ip']
        self.device_port: int = kwargs['device_port']
        self.login_ssh: str = ''
        self.password_ssh: str = ''

    def connect_to_device(self) -> List[str]:
        """
        This module checks the user-provided credentials for the ssh server.
        If the credentials are correct, the device data is entered into the database.
        """
        Clear.clear()
        print(f"Login in to device: {Bcolors.MAGENTA}{self.device_ip}{Bcolors.ENDC} via ssh.")
        self.login_ssh: str = str(input("Type ssh login: "))
        self.password_ssh: str = str(input("Type ssh password: "))
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.device_ip, port=self.device_port, username=self.login_ssh, password=self.password_ssh,
                           timeout=5)
            ssh_session = client.get_transport().open_session()
            if ssh_session.active:
                print(f"\nCorrect login and password! App is almost {Bcolors.PASS}configured{Bcolors.ENDC}!")
                client.close()
                return [self.login_ssh, self.password_ssh]
        except paramiko.ssh_exception.AuthenticationException:
            print(f"{Bcolors.ERROR}Wrong credentials!{Bcolors.ENDC}")
            print(70 * '-')
