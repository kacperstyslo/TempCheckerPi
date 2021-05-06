class LowPrivileges(Exception):
    def __str__(self):
        return "Required root privileges! Run config file again with sudo command!"
