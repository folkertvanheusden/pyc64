# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# released under AGPL v3.0

from basic_rom import basic_rom
from cartridge_hi import cartridge_hi
from cartridge_lo import cartridge_lo
from character_rom import character_rom
from i_o import i_o
from kernal_rom import kernal_rom
from ram import ram

class bus:
    zones = [ 0 ] * 16
    zones[0] = 0
    zones[1] = zones[2] = zones[3] = zones[4] = zones[5] = zones[6] = zones[7] = 1
    zones[8] = zones[9] = 2
    zones[10] = zones[11] = 3
    zones[12] = 4
    zones[13] = 5
    zones[14] = zones[15] = 6

    def __init__(self):
        self.ram = ram()
        self.basic_rom = basic_rom()
        self.kernal_rom = kernal_rom()

        bank_table = [ ] * 32
        bank_table[0] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.ram, self.ram ]
        bank_table[1] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.ram, self.ram ]
        bank_table[2] = [ self.ram, self.ram, self.ram, self.cartridge_hi, self.ram, self.character_rom, self.kernal_rom ]
        bank_table[3] = [ self.ram, self.ram, self.cartridge_lo, self.cartridge_hi, self.ram, self.character_rom, self.kernal_rom ]
        bank_table[4] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.ram, self.ram ]
        bank_table[5] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.i_o, self.ram ]
        bank_table[6] = [ self.ram, self.ram, self.ram, self.cartridge_hi, self.ram, self.i_o, self.kernal_rom ]
        bank_table[7] = [ self.ram, self.ram, self.cartridge_lo, self.cartridge_hi, self.ram, self.i_o, self.kernal_rom ]
        bank_table[8] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.ram, self.ram ]
        bank_table[9] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.character_rom, self.ram ]
        bank_table[10] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.character_rom, self.kernal_rom ]
        bank_table[11] = [ self.ram, self.ram, self.cartridge_lo, self.basic_rom, self.ram, self.character_rom, self.kernal_rom ]
        bank_table[12] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.ram, self.ram ]
        bank_table[13] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.i_o, self.ram ]
        bank_table[14] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.i_o, self.kernal_rom ]
        bank_table[15] = [ self.ram, self.ram, self.cartridge_lo, self.basic_rom, self.ram, self.i_o, self.kernal_rom ]
        bank_table[16] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        bank_table[17] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        bank_table[18] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        bank_table[19] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        bank_table[20] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        bank_table[21] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        bank_table[22] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        bank_table[23] = [ self.ram, self.nothing, self.cartridge_lo, self.nothing, self.nothing, self.i_o, self.cartridge_hi ]
        bank_table[24] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.ram, self.ram ]
        bank_table[25] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.character_rom, self.ram ]
        bank_table[26] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.character_rom, self.kernal_rom ]
        bank_table[27] = [ self.ram, self.ram, self.ram, self.basic_rom, self.ram, self.character_rom, self.kernal_rom ]
        bank_table[28] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.ram, self.ram ]
        bank_table[29] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.i_o, self.ram ]
        bank_table[30] = [ self.ram, self.ram, self.ram, self.ram, self.ram, self.i_o, self.kernal_rom ]
        bank_table[31] = [ self.ram, self.ram, self.ram, self.basic_rom, self.ram, self.i_o, self.kernal_rom ]

    def read(self, addr):
        device = bank_table[zones[addr / 4096]]

        return device(addr)

    def write(self, addr, value):
        device = bank_table[zones[addr / 4096]]

        if device.write_through():
            self.ram.write(addr, value)

        else:
            device(addr, value)
