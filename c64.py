#! /usr/bin/python3

from bus_c64 import bus_c64
from cpu_6510 import cpu_6510

class cbm64:
    def __init__(self):
        self.bus = bus_c64()
        self.cpu = cpu_6510(self.bus)

    def reset(self):
        self.cpu.reset()

    def run(self):
        # for i in range(0, 1024):
        while True:
            # print('%04x' % self.cpu.pc)
            self.cpu.tick()

            if self.cpu.pc == 0xe5cd:
                break

c64 = cbm64()
c64.reset()
c64.run()
