from bus_device import bus_device

class ram(bus_device):
    def __init__(self):
        self.ram = [ 0 for k in range(65536)]

    def write_through(self):
        return False

    def read(self, addr):
        return self.ram[addr]

    def write(self, addr, value):
        self.ram[addr] = value
