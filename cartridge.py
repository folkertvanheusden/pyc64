from bus_device import bus_device

class cartridge(bus_device):
    def activated(self):
        return False

    def write_through(self):
        return True
