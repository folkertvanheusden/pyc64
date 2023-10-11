# (C) 2020-2022 by Folkert van Heusden <mail@vanheusden.com>
# License: CC0

from datetime import datetime
from ram import ram

class filelf():
    def __init__(self, name, mode = 'r'):
        self.fh = open(name, mode)

        self.ts = True 

    def emit_ts(self):
        if self.ts:
            self.fh.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') + '] ')

    def print(self, string):
        self.emit_ts()

        self.ts = True

        self.fh.write(string + '\n')

    def print_no_lf(self, string):
        self.emit_ts()

        self.ts = False

        self.fh.write(string)

class bus_base:
    def __init__(self):
        self.ram = None

        self.log = filelf('log.dat', 'a')

    def reset(self):
        self.ram = ram()

    def read(self, addr):
        return self.ram.read(addr)

    def write(self, addr, value):
        self.ram.write(addr, value)
