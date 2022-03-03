#! /usr/bin/python3

# (C) 2022 by Folkert van Heusden <mail@vanheusden.com>
# License: Apache License v2.0

from bus_c64 import bus_c64
from cpu_6510 import cpu_6510

class cbm64:
    def __init__(self):
        self.bus = bus_c64()
        self.cpu = cpu_6510(self.bus)

        self.clock_frequency = 985248
        self.raster_interrupt_frequency = 50

    def reset(self):
        self.cpu.reset()

    def run(self):
        p_nmi_cycles = 0
        p_irq_cycles = 0

        while True:
            self.cpu.tick()

            self.bus.get_vic_ii().tick()

            if self.cpu.cycles - p_nmi_cycles >= 20000:
                p_nmi_cycles = self.cpu.cycles
                #self.cpu.NMI()

            if self.cpu.cycles - p_irq_cycles >= self.clock_frequency / self.raster_interrupt_frequency:
                p_irq_cycles = self.cpu.cycles
                #self.cpu.IRQ()

c64 = cbm64()
c64.reset()
c64.run()
