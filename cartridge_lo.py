# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# License: Apache License v2.0

from cartridge import cartridge

class cartridge_lo(cartridge):
    def __init__(self, bus):
        cartridge.__init__(self, bus)

        fh = open('c64-diag-586220/diag-c64_586220.bin', 'rb')
        # fh = open('c64_burn-in_test.bin', 'rb')
        self.rom: List[int] = [ int(b) for b in fh.read() ]
        fh.close()

    def read(self, addr):
        return self.rom[addr - 0x8000]
