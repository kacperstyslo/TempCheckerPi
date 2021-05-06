import sqlite3
from typing import List


class DevicesDatabase:
    """
    This class store all methods to the database management.
    """

    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.__create_table_device_data()

    def __enter__(self):
        self.connect = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.connect.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.connect.commit()
        self.connect.close()

    def __create_table_device_data(self):
        """
        This method creates a table for all devices data.
        """
        with self as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS device_data (
                                device_id INTEGER(2) PRIMARY KEY NOT NULL,
                                device_ip VARCHAR(15) NOT NULL,
                                device_port INTEGER(2) NOT NULL,
                                device_ssh_login TEXT(20) NOT NULL,
                                device_ssh_password TEXT,
                                data_refresh_interval INTEGER NOT NULL,                                    
                                UNIQUE(device_id))""")

    def insert_values_into_device_data_table(self, **kwargs) -> None:
        with self as cursor:
            cursor.execute(
                "INSERT INTO device_data (device_id, device_ip, device_port, device_ssh_login, device_ssh_password, "
                "data_refresh_interval) VALUES (?,?,?,?,?,?)",
                (kwargs['device_id'], kwargs['device_ip'], kwargs['device_port'], kwargs['device_ssh_login'],
                 kwargs['device_ssh_password'], kwargs['data_refresh_interval']))

    def update_value_of_data_refresh_interval(self, refresh_data, chosen_device) -> None:
        with self as cursor:
            cursor.execute(f"UPDATE device_data SET data_refresh_interval='{refresh_data}'"
                           f" WHERE device_id='{chosen_device}'")

    def select_data_from_chosen_device(self, device_ip) -> List[List['str']]:
        with self as cursor:
            cursor.execute(f"SELECT * FROM device_data WHERE device_ip='{device_ip}'")
            return cursor.fetchall()
