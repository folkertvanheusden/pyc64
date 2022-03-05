# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# License: Apache License v2.0

from bus_device import bus_device

class i_o(bus_device):
    def __init__(self, bus):
        bus_device.__init__(self, bus)

        self.data = [ 0 for k in range(65536)]
        #self.data[0xdd00] = 0x80

    def write_through(self):
        return False

    def read(self, addr):
        if addr == 0xd012:
            return 0x00

        if addr & 0xff00 == 0xdc00:
            return self.bus.cia1.read(addr & 0x000f)

        if addr & 0xff00 == 0xdd00:
            return self.bus.cia2.read(addr & 0x000f)

        self.bus.log.print('I/O read from %04x' % addr)

        #print(f'read: {self.data[0xdc00]} {self.data[0xdc01]} {self.data[0xdc02]} {self.data[0xdc03]}')

        return self.data[addr]

    def write(self, addr, value):
        if addr & 0xff00 == 0xdc00:
            return self.bus.cia1.write(addr, value)

        if addr & 0xff00 == 0xdd00:
            return self.bus.cia2.write(addr, value)

        self.bus.log.print('I/O write to %04x: %02x' % (addr, value))

        self.data[addr] = value
