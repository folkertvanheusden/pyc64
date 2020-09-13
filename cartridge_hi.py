# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# License: AGPL 3.0

from cartridge import cartridge

class cartridge_hi(cartridge):
    def read(self, addr):
        return 0xee
