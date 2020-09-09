# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# released under AGPL v3.0

from ram import ram

class bus_base:
    def __init__(self):
        self.ram = None

    def reset(self):
        self.ram = ram()

    def read(self, addr):
        return self.ram.read(addr)

    def write(self, addr, value):
        self.ram.write(addr, value)
