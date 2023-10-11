# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# License: CC0

from bus_device import bus_device

import sys
class character_rom(bus_device):
    def __init__(self):
        fh = open('chargen.c64', 'rb')
        self.rom: List[int] = [ int(b) for b in fh.read() ]
        fh.close()

    def write_through(self):
        return True

    def read(self, addr):
        return self.rom[addr - 0xd000]
