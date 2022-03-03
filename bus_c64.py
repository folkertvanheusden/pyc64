# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# License: Apache License v2.0

from bus_base import bus_base
from basic_rom import basic_rom
from cartridge_hi import cartridge_hi
from cartridge_lo import cartridge_lo
from character_rom import character_rom
from i_o import i_o
from kernal_rom import kernal_rom
from nothing import nothing
from ram import ram
import sys
from vic_ii import vic_ii

class bus_c64(bus_base):
    def __init__(self):
        bus_base.__init__(self)

        self.basic_rom = basic_rom()
        self.cartridge_hi = cartridge_hi(self)
        self.cartridge_lo = cartridge_lo(self)
        self.character_rom = character_rom()
        self.i_o = i_o(self)
        self.kernal_rom = kernal_rom()
        self.nothing = nothing()
        self.ram = ram()
        self.vic_ii = vic_ii()

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

        self.exp_port = 0x00
        if not self.cartridge_hi.activated() and not self.cartridge_lo.activated():
            self.exp_port = 0x18

        self.vic_ii.begin(self)

    def get_vic_ii(self):
        return self.vic_ii

    def reset(self):
        self.bs_setting = 31  # default

    def read(self, addr):
        if addr == 0x0001:  # bank switch register
            return self.bs_setting

        zone = self.zones[addr // 4096]
        device = self.bank_table[((self.bs_setting & 7) | self.exp_port) & 31][zone]

        return device.read(addr)

    def write(self, addr, value):
        if addr == 0x0001:  # bank switch register
            self.bs_setting = value
            self.log.print('write bank switch register (%02x)' % value)
            return

        if addr >= 0x0400 and addr < 0x0400 + 1024:
            self.vic_ii.write(addr, value)

        if addr >= 0xd800 and addr < 0xdbe8:
            self.vic_ii.write(addr, value)

        zone = self.zones[addr // 4096]
        device = self.bank_table[((self.bs_setting & 7) | self.exp_port) & 31][zone]

        if device.write_through():
            self.ram.write(addr, value)

        else:
            device.write(addr, value)
