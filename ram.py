# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# License: CC0

from bus_device import bus_device

class ram(bus_device):
    def __init__(self):
        self.ram = [ ]

        for i in range(0, 1024):
            pattern = 0xff if i & 1 else 0x00

            for p in range(0, 64):
                self.ram.append(pattern)

        assert len(self.ram) == 65536

    def write_through(self):
        return False

    def read(self, addr):
        assert self.ram[addr] >= 0
        assert self.ram[addr] <= 255
        return self.ram[addr]

    def write(self, addr, value):
        assert value >= 0
        assert value <= 255
        self.ram[addr] = value
