# (C) 2022 by Folkert van Heusden <mail@vanheusden.com>
# License: Apache License v2.0

from bus_device import bus_device
from cia import cia

class cia2(cia):
    def __init__(self, bus):
        cia.__init__(self, bus)

        self.cia_idx = 2

    def trigger_interrupt(self):
        #self.bus.log.print('NMI')
        pass
