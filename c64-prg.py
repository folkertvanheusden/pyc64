#! /usr/bin/python3

# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# License: Apache License v2.0

from bus_c64 import bus_c64
from cpu_6510 import cpu_6510

# https://michaelcmartin.github.io/Ophis/book/x72.html

def read_8b_int(fh):
    b = fh.read(1)
    return int.from_bytes(b, 'little')

class cbm64:
    def __init__(self, prg, start):
        self.bus = bus_c64()
        self.bus.reset()
        self.cpu = cpu_6510(self.bus)

        fh = open(prg, 'rb')
        la = read_8b_int(fh) | (read_8b_int(fh) << 8)
        print('load address: %04x' % la)

        while True:
            b = fh.read(1)
            if len(b) == 0:
                break
            self.bus.write(la, int.from_bytes(b, 'little'))
            la += 1

        fh.close()

        self.cpu.reset()

        self.cpu.pc = start

    def run(self):
        p_irq_cycles = 0

        while True:
            self.cpu.tick()

#c64 = cbm64('AllSuiteA.prg', 2061)
#c64 = cbm64('6502_functional_test.prg', 2061)
c64 = cbm64('matrix_bugfix.prg', 2061)
c64.run()
