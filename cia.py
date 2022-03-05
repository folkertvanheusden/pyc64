# (C) 2022 by Folkert van Heusden <mail@vanheusden.com>
# License: Apache License v2.0

from bus_device import bus_device

class cia(bus_device):
    def __init__(self, bus):
        bus_device.__init__(self, bus)

        self.clock_frequency = 985248
        self.raster_interrupt_frequency = 50

        self.a_latch = self.timer_a_value = 65535
        self.b_latch = self.timer_b_value = 65535

        self.int_mask = 0
        self.int_data = 0

        self.cia_idx = None
        
        self.registers = [ 0 ] * 16

    def tick(self):
        self.timer_a_value -= 1

        if self.timer_a_value <= 0:
            self.timer_a_value = self.a_latch

            self.int_data |= 1 << 0

            if self.int_mask & (1 << 0):
                self.int_data |= 1 << 7

                self.trigger_interrupt()

        self.timer_b_value -= 1

        if self.timer_b_value <= 0:
            self.timer_b_value = self.b_latch

            self.int_data |= 1 << 1

            if self.int_mask & (1 << 1):
                self.int_data |= 1 << 7

                self.trigger_interrupt()

    def trigger_interrupt(self):
        pass

    def read(self, addr):
        register = addr & 0x000f

        self.bus.log.print(f'CIA{self.cia_idx} read register {register:x}')

        if register == 4:
            return self.timer_a_value & 255

        elif register == 5:
            return (self.timer_a_value >> 8) & 255

        elif register == 6:
            return self.timer_b_value & 255

        elif register == 7:
            return (self.timer_b_value >> 8) & 255

        elif register == 13:
            rc = self.int_data
            self.int_data = 0
            return rc

        elif register == 14:
            return 1 << 7  # 50Hz

        return self.registers[register]

    def write(self, addr, val):
        register = addr & 0x000f

        self.bus.log.print(f'CIA{self.cia_idx} write register {register:x} {val:02x}')

        self.registers[register] = val  # fallback

        if register == 4:
            self.a_latch = (self.a_latch & 0xff00) | val

        elif register == 5:
            self.a_latch = (self.a_latch & 0x00ff) | (val << 8)

        elif register == 6:
            self.b_latch = (self.b_latch & 0xff00) | val

        elif register == 7:
            self.b_latch = (self.b_latch & 0x00ff) | (val << 8)

        elif register == 13:  # 0x0d
            self.int_mask = val
