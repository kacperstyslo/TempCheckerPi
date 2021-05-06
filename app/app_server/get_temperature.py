import smbus


class ReadTemperature:
    def __init__(self):
        self.address: int = 0x48

    def read_temperature(self) -> bytes:
        """
        This method will reads and return temperature near by device in bytes.
        """
        bus = smbus.SMBus(1)
        data = bus.read_word_data(self.address, 0)
        data = ((data << 8) & 0xFF00) | (data >> 8)
        data = data >> 5
        temperature = ((data & 0x400) * -128 + data & (~0x4000)) * 0.125
        return temperature


if __name__ == '__main__':
    print(ReadTemperature().read_temperature())
