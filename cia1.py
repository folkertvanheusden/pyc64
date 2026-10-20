# (C) 2022 by Folkert van Heusden <mail@vanheusden.com>
# License: CC0

from bus_device import bus_device
from cia import cia
import queue
import sdl2
from threading import Thread

rows = (
        (
            (sdl2.SDLK_RETURN, 2),
        ),
        (
            (sdl2.SDLK_3, 1),
            (sdl2.SDLK_w, 2),
            (sdl2.SDLK_a, 4),
            (sdl2.SDLK_4, 8),
            (sdl2.SDLK_z, 16),
            (sdl2.SDLK_s, 32),
            (sdl2.SDLK_e, 64),
            (sdl2.SDLK_LSHIFT, 128),
        ),
        (
            (sdl2.SDLK_5, 1),
            (sdl2.SDLK_r, 2),
            (sdl2.SDLK_d, 4),
            (sdl2.SDLK_6, 8),
            (sdl2.SDLK_c, 16),
            (sdl2.SDLK_f, 32),
            (sdl2.SDLK_t, 64),
            (sdl2.SDLK_x, 128),
        ),
        (
            (sdl2.SDLK_7, 1),
            (sdl2.SDLK_y, 2),
            (sdl2.SDLK_g, 4),
            (sdl2.SDLK_8, 8),
            (sdl2.SDLK_b, 16),
            (sdl2.SDLK_h, 32),
            (sdl2.SDLK_u, 64),
            (sdl2.SDLK_v, 128),
        ),
        (
            (sdl2.SDLK_9, 1),
            (sdl2.SDLK_i, 2),
            (sdl2.SDLK_j, 4),
            (sdl2.SDLK_0, 8),
            (sdl2.SDLK_m, 16),
            (sdl2.SDLK_k, 32),
            (sdl2.SDLK_o, 64),
            (sdl2.SDLK_n, 128),
        ),
        (
#            (sdl2.SDLK_+, 1),
            (sdl2.SDLK_p, 2),
            (sdl2.SDLK_l, 4),
#            (sdl2.SDLK_MIN, 8),
#            (sdl2.SDLK_DOT, 16),
#            (sdl2.SDLK_k, 32),
#            (sdl2.SDLK_o, 64),
#            (sdl2.SDLK_n, 128),
        ),
        (
#            (sdl2.SDLK_9, 1),
#            (sdl2.SDLK_i, 2),
#            (sdl2.SDLK_j, 4),
#            (sdl2.SDLK_0, 8),
#            (sdl2.SDLK_m, 16),
#            (sdl2.SDLK_k, 32),
#            (sdl2.SDLK_o, 64),
#            (sdl2.SDLK_n, 128),
        ),
        (
            (sdl2.SDLK_1, 1),
#            (sdl2.SDLK_p, 2),
#            (sdl2.SDLK_l, 4),
            (sdl2.SDLK_2, 8),
            (sdl2.SDLK_SPACE, 16),
            (sdl2.SDLK_c, 32),
            (sdl2.SDLK_q, 64),
#            (sdl2.SDLK_n, 128),
        ),
       )

def ffs(x):
    """Returns the index, counting from 0, of the
    least significant set bit in `x`.
    """
    return (x&-x).bit_length()-1

assert(len(rows) == 8)

class cia1(cia, Thread):
    def __init__(self, bus):
        Thread.__init__(self)
        cia.__init__(self, bus)

        self.cia_idx = 1
        self.keys_pressed = set()

        self.rt_kb = True
        self.keys_queue = []

    def trigger_interrupt(self):
        self.bus.cpu.IRQ()

    def set_kb_rt(self, state):
        self.rt_kb = state

    def run(self):
        while True:
            event = self.bus.event_queue.get()

            if event[0] == sdl2.SDL_KEYDOWN:
                if self.rt_kb:
                    self.keys_pressed.add(event[1])
                else:
                    self.keys_queue.append(event[1])
                self.bus.log.print('%d is pressed' % event[1])

            elif event[0] == sdl2.SDL_KEYUP:
                if self.rt_kb:
                    self.keys_pressed.remove(event[1])
                self.bus.log.print('%d is no longer pressed' % event[1])

    def read(self, addr):
        register = addr & 0x000f

        if register == 1:
            # if self.registers[2] == 0xff and self.registers[3] == 0x00:
            if True:
                pattern = 0
                for row in range(8):
                    if self.registers[0] & (1 << row):
                        continue
                    for keys in rows[row]:
                        if self.rt_kb:
                            if keys[0] in self.keys_pressed:
                                pattern |= keys[1]
                        else:
                            if len(self.keys_queue) > 0 and keys[0] == self.keys_queue[0]:
                                pattern = keys[1]
                                del self.keys_queue[0]
                                return pattern ^ 255
                return pattern ^ 255

        return cia.read(self, addr)
