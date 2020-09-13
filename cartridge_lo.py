from cartridge import cartridge

class cartridge_lo(cartridge):
    def read(self, addr):
        return 0xee
