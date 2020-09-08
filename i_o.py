from bus_device import bus_device

class i_o(bus_device):
    def __init__(self):
        pass

    def write_through(self):
        return False

    def read(self, addr):
        return 0  # FIXME

    def write(self, addr, value):
        pass
