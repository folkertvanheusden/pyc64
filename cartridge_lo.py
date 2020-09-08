from bus_device import bus_device

class cartridge_lo(bus_device):
    def __init__(self):
        pass

    def write_through(self):
        return True

    def read(self, addr):
        return None
