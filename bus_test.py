# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# released under Apache License v2.0

from bus_base import bus_base

class bus_test(bus_base):
    def __init__(self):
        bus_base.__init__(self)

        fh = open('6502_functional_test.bin', 'rb')
        self.ram: List[int] = [ int(b) for b in fh.read() ]
        fh.close()

    def reset(self):
        pass

    def read(self, addr):
        return self.ram[addr]

    def write(self, addr, value):
        self.ram[addr] = value
