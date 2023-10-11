# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# License: CC0

from cartridge import cartridge

class cartridge_hi(cartridge):
    def read(self, addr):
        return 0xee
