#! /usr/bin/python3

# (C) 2022 by Folkert van Heusden <mail@vanheusden.com>
# License: Apache License v2.0

from bus_c64 import bus_c64
import sys
import time

def read_8b_int(fh):
    b = fh.read(1)
    return int.from_bytes(b, 'little')

class cbm64:
    def __init__(self, prg = None, prg_addr = None):
        self.bus = bus_c64()

        if prg:
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

            #self.bus.cpu.pc = prg_addr

    def reset(self):
        self.cpu.reset()

    def run(self):
        while True:
            self.bus.tick()

#c64 = cbm64()
#c64 = cbm64('matrix_bugfix.prg', 2061)
#c64 = cbm64('AllSuiteA.prg', 2061)
c64 = cbm64('docs/ciadiag.prg', 2064)
c64.run()
