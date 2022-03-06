# (C) 2022 by Folkert van Heusden <mail@vanheusden.com>
# License: Apache License v2.0

from bus_device import bus_device
from cia import cia
import queue
import sdl2
from threading import Thread

class cia1(cia, Thread):
    def __init__(self, bus):
        Thread.__init__(self)
        cia.__init__(self, bus)

        self.cia_idx = 1

        self.keys_pressed = dict()

    def trigger_interrupt(self):
        self.bus.cpu.IRQ()

    def run(self):
        while True:
            event = self.bus.event_queue.get()

            if event.type == sdl2.SDL_KEYDOWN:
                self.keys_pressed[event.key.keysym.sym] = True

                self.bus.log.print('%d is pressed' % event.key.keysym.sym)

            elif event.type == sdl2.SDL_KEYUP:
                self.keys_pressed[event.key.keysym.sym] = False

                self.bus.log.print('%d is no longer pressed' % event.key.keysym.sym)

    def read(self, addr):
        register = addr & 0x000f

        if register == 1:
            if self.registers[2] == 0xff and self.registers[3] == 0x00:
                self.bus.log.print('check down %02x | %s' % (self.registers[0], self.keys_pressed))

                if self.registers[0] == 0xfd and sdl2.SDLK_a in self.keys_pressed and self.keys_pressed[sdl2.SDLK_a] == True:
                    return 0xfb       # 'a'

                elif self.registers[0] == 0xf7 and 66 in self.keys_pressed and self.keys_pressed[66] == True:
                    return 0xef       # 'b'

                elif self.registers[0] == 0xfb and 67 in self.keys_pressed and self.keys_pressed[67] == True:
                    return 0xef       # 'c'

                elif self.registers[0] == 0x7f and sdl2.SDLK_1 in self.keys_pressed and self.keys_pressed[sdl2.SDLK_1] == True:
                    return 0xfe       # '1'

                elif self.registers[0] == 0x7f and sdl2.SDLK_2 in self.keys_pressed and self.keys_pressed[sdl2.SDLK_2] == True:
                    return 0xf7       # '2'

                elif self.registers[0] == 0x7d and 51 in self.keys_pressed and self.keys_pressed[51] == True:
                    return 0xfe       # '3'

                elif self.registers[0] == 0x7f and 81 in self.keys_pressed and self.keys_pressed[81] == True:
                    return 0xbf       # 'q'

                elif self.registers[0] == 0x7f and 27 in self.keys_pressed and self.keys_pressed[27] == True:
                    return 0x7f       # 'run/stop'

                elif self.registers[0] == 0x7f and sdl2.SDLK_RETURN in self.keys_pressed and self.keys_pressed[sdl2.SDLK_RETURN] == True:
                    return 0xfd       # '←'

                elif self.registers[0] == 0x7f and 32 in self.keys_pressed and self.keys_pressed[32] == True:
                    return 0xef       # ' '

                elif self.registers[0] == 0xfb and 88 in self.keys_pressed and self.keys_pressed[88] == True:
                    return 0x7f       # 'x'

                elif self.registers[0] == 0xf7 and 86 in self.keys_pressed and self.keys_pressed[86] == True:
                    return 0x7f       # 'v'

                elif self.registers[0] == 0xef and 78 in self.keys_pressed and self.keys_pressed[78] == True:
                    return 0x7f       # 'n'

            if self.registers[2] == 0xff and self.registers[3] == 0x00:
                self.bus.log.print('check up')

                if self.registers[0] == 0xfd and 65 in self.keys_pressed and self.keys_pressed[65] == False:
                    return 0xff       # 'a'

                elif self.registers[0] == 0xf7 and 66 in self.keys_pressed and self.keys_pressed[66] == False:
                    return 0xff       # 'b'

                elif self.registers[0] == 0xfb and 67 in self.keys_pressed and self.keys_pressed[67] == False:
                    return 0xff       # 'c'

                elif self.registers[0] == 0x7f and 49 in self.keys_pressed and self.keys_pressed[49] == False:
                    return 0xff       # '1'

                elif self.registers[0] == 0x7f and 50 in self.keys_pressed and self.keys_pressed[50] == False:
                    return 0xff       # '2'

                elif self.registers[0] == 0x7d and 51 in self.keys_pressed and self.keys_pressed[51] == False:
                    return 0xff       # '3'

                elif self.registers[0] == 0x7f and 81 in self.keys_pressed and self.keys_pressed[81] == False:
                    return 0xff       # 'q'

                elif self.registers[0] == 0x7f and 27 in self.keys_pressed and self.keys_pressed[27] == False:
                    return 0xff       # 'run/stop'

                elif self.registers[0] == 0x7f and sdl2.SDLK_RETURN in self.keys_pressed and self.keys_pressed[sdl2.SDLK_RETURN] == False:
                    return 0xff       # '←'

                elif self.registers[0] == 0x7f and 32 in self.keys_pressed and self.keys_pressed[32] == False:
                    return 0xff       # ' '

                elif self.registers[0] == 0xfb and 88 in self.keys_pressed and self.keys_pressed[88] == False:
                    return 0xff       # 'x'

                elif self.registers[0] == 0xf7 and 86 in self.keys_pressed and self.keys_pressed[86] == False:
                    return 0xff       # 'v'

                elif self.registers[0] == 0xef and 78 in self.keys_pressed and self.keys_pressed[78] == False:
                    return 0xff       # 'n'

                return 0xff

        return cia.read(self, addr)
