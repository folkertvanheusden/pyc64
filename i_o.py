# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# License: Apache License v2.0

from bus_device import bus_device

class i_o(bus_device):
    def __init__(self):
        self.data = [ 0 for k in range(65536)]
        self.data[0xdd00] = 0x80

    def write_through(self):
        return False

    def read(self, addr):
        # print('I/O read from %04x' % addr)
        if addr == 0xd012:
            return 0xff
        return self.data[addr]  # FIXME

    def write(self, addr, value):
        # print('I/O write to %04x: %02x' % (addr, value))
        self.data[addr] = value  # FIXME
