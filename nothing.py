# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# License: AGPL 3.0

from bus_device import bus_device

class nothing(bus_device):
    def __init__(self):
        pass

    def write_through(self):
        return True

    def read(self, addr):
        return 0xee
