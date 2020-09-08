# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# released under AGPL v3.0

from basic_rom import basic_rom
from cartridge_hi import cartridge_hi
from cartridge_lo import cartridge_lo
from character_rom import character_rom
from i_o import i_o
from kernal_rom import kernal_rom
from nothing import nothing
from ram import ram

class bus:
    def __init__(self):
        self.basic_rom = basic_rom()
        self.cartridge_hi = cartridge_hi()
        self.cartridge_lo = cartridge_lo()
        self.character_rom = character_rom()
        self.i_o = i_o()
        self.kernal_rom = kernal_rom()
        self.nothing = nothing()
        self.ram = ram()

        self.bank_table = [ None ] * 32
        self.bank_table[0] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.ram, self.ram ]
        self.bank_table[1] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.ram, self.ram ]
        self.bank_table[2] = [ self.ram, self.ram, self.ram, self.cartridge_hi, self.ram, self.character_rom, self.kernal_rom ]
        self.bank_table[3] = [ self.ram, self.ram, self.cartridge_lo, self.cartridge_hi, self.ram, self.character_rom, self.kernal_rom ]
        self.bank_table[4] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.ram, self.ram ]
        self.bank_table[5] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.i_o, self.ram ]
        self.bank_table[6] = [ self.ram, self.ram, self.ram, self.cartridge_hi, self.ram, self.i_o, self.kernal_rom ]
        self.bank_table[7] = [ self.ram, self.ram, self.cartridge_lo, self.cartridge_hi, self.ram, self.i_o, self.kernal_rom ]
        self.bank_table[8] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.ram, self.ram ]
        self.bank_table[9] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.character_rom, self.ram ]
        self.bank_table[10] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.character_rom, self.kernal_rom ]
        self.bank_table[11] = [ self.ram, self.ram, self.cartridge_lo, self.basic_rom, self.ram, self.character_rom, self.kernal_rom ]
        self.bank_table[12] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.ram, self.ram ]
        self.bank_table[13] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.i_o, self.ram ]
        self.bank_table[14] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.i_o, self.kernal_rom ]
        self.bank_table[15] = [ self.ram, self.ram, self.cartridge_lo, self.basic_rom, self.ram, self.i_o, self.kernal_rom ]
        self.bank_table[16] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        self.bank_table[17] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        self.bank_table[18] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        self.bank_table[19] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        self.bank_table[20] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        self.bank_table[21] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        self.bank_table[22] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        self.bank_table[23] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        self.bank_table[24] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.ram, self.ram ]
        self.bank_table[25] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.character_rom, self.ram ]
        self.bank_table[26] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.character_rom, self.kernal_rom ]
        self.bank_table[27] = [ self.ram, self.ram, self.ram, self.basic_rom, self.ram, self.character_rom, self.kernal_rom ]
        self.bank_table[28] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.ram, self.ram ]
        self.bank_table[29] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.i_o, self.ram ]
        self.bank_table[30] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.i_o, self.kernal_rom ]
        self.bank_table[31] = [ self.ram, self.ram, self.ram, self.basic_rom, self.ram, self.i_o, self.kernal_rom ]

        self.zones = [ 0 ] * 16
        self.zones[0] = 0
        self.zones[1] = self.zones[2] = self.zones[3] = self.zones[4] = self.zones[5] = self.zones[6] = self.zones[7] = 1
        self.zones[8] = self.zones[9] = 2
        self.zones[10] = self.zones[11] = 3
        self.zones[12] = 4
        self.zones[13] = 5
        self.zones[14] = self.zones[15] = 6

    def reset(self):
        self.bs_setting = 31  # default

    def read(self, addr):
        if addr == 0x0001:  # bank switch register
            return self.bs_setting

        zone = self.zones[addr // 4096]
        device = self.bank_table[self.bs_setting][zone]

        return device.read(addr)

    def write(self, addr, value):
        if addr == 0x0001:  # bank switch register
            print('BS was: %02x' % self.bs_setting)
            # use only lower 3 bits
            self.bs_setting &= 0x18
            self.bs_setting |= value & 7
            print('BS  is: %02x by setting %02x' % (self.bs_setting, value))
            return

        if addr >= 0x0400 and addr < 0x0400 + 1024:  # FIXME check from d018
            print('%c' % value, end='', flush=True)

        zone = self.zones[addr // 4096]
        device = self.bank_table[self.bs_setting][zone]

        if device.write_through():
            self.ram.write(addr, value)

        else:
            device.write(addr, value)