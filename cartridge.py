# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# License: CC0

from bus_device import bus_device

class cartridge(bus_device):
    def activated(self):
        return False

    def write_through(self):
        return True
