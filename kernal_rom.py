# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# License: AGPL 3.0

from bus_device import bus_device

class kernal_rom(bus_device):
    def __init__(self):
        fh = open('kernal.901227-01.bin', 'rb')
        self.rom: List[int] = [ int(b) for b in fh.read() ]
        fh.close()

    def write_through(self):
        return True

    def read(self, addr):
        return self.rom[addr - 0xe000]
