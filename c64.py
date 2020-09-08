#! /usr/bin/python3

from bus import bus
from cpu_6510 import cpu_6510

class cbm64:
    def __init__(self):
        self.bus = bus()
        self.cpu = cpu_6510(self.bus)

    def reset(self):
        self.cpu.reset()

c64 = cbm64()
c64.reset()
