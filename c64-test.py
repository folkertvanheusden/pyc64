#! /usr/bin/python3

# (C) 2020 by Folkert van Heusden <mail@vanheusden.com>
# License: Apache License v2.0

from bus_test import bus_test
from cpu_6510 import cpu_6510

class cbm64:
    def __init__(self):
        self.bus = bus_test()
        self.cpu = cpu_6510(self.bus)

    def reset(self):
        self.cpu.reset()
        self.cpu.pc = 0x0400

    def run(self):
        while True:
            self.cpu.tick()

            if self.bus.read(0x200) == 0xf0:
                break

c64 = cbm64()
c64.reset()
c64.run()
