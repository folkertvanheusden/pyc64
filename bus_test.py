# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# released under CC0

from bus_base import bus_base

class bus_test(bus_base):
    def __init__(self, load_func_test):
        bus_base.__init__(self)

        if load_func_test == True:
            fh = open('docs/6502_functional_test.bin', 'rb')
            self.ram: List[int] = [ int(b) for b in fh.read() ]
            fh.close()

    def read(self, addr):
        return self.ram.read(addr)

    def write(self, addr, value):
        self.ram.write(addr, value)
