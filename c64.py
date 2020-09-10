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
        p_irq_cycles = 0

        while True:
            self.cpu.tick()

            if self.cpu.cycles - p_irq_cycles >= 20000:
                p_irq_cycles = self.cpu.cycles
                self.cpu.IRQ()

c64 = cbm64()
c64.reset()
c64.run()
