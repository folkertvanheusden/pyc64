# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# License: CC0

class bus_device:
    def __init__(self, bus):
        self.bus = bus

    def write_through(self):
        return None

    def read(self, addr):
        return None

    def write(self, addr, value):
        pass
