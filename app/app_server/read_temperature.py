import paramiko


class ReadTemperature:
    def __init__(self, **kwargs):
        self.device_ip: str = kwargs['device_ip']
        self.port_number: int = kwargs['device_port']
        self.ssh_login: str = kwargs['ssh_login']
        self.ssh_password: str = kwargs['ssh_password']
        self.file_name: str = __file__.replace('read_temperature.py', 'get_temperature.py')

    def read_temperature(self) -> str:
        """
        This method send get_temperature script to chosen device via ssh to get temperature. After sending script,
        method receive temperature and convert temperature from bytes to string.
        """
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.device_ip, port=self.port_number, username=self.ssh_login, password=self.ssh_password)
            sftp = ssh.open_sftp()
            sftp.put(localpath=self.file_name, remotepath='get_temperature.py')
            stdin, stdout, stderr = ssh.exec_command("python3 get_temperature.py")
            return "{:.1f}".format(float(stdout.channel.recv(1024).decode()))
        except TimeoutError as e:
            raise Exception("Can't connect to chosen host!") from e
        finally:
            ssh.close()


if __name__ == '__main__':
    ReadTemperature().read_temperature()
