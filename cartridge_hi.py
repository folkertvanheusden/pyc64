from cartridge import cartridge

class cartridge_hi(cartridge):
    def read(self, addr):
        return 0xee
