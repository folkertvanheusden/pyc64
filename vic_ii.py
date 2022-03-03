import curses

class vic_ii:
    def __init__(self):
        self.cycle = 0
        self.raster_line = 0

        self.vid_ram = [ 0 ] * 1024

        self.window = curses.initscr()

    def start(self, bus):
        self.bus = bus

    def tick(self):
        self.cycle += 1

        if self.cycle == 64:
            self.cycle = 0

            self.raster_line += 1

            if self.raster_line == 312:
                self.raster_line = 0

                self.window.refresh()
                curses.doupdate()

        self.bus.write(0xd012, self.raster_line & 255)

        org_value = self.bus.read(0xd011)
        self.bus.write(0xd011, org_value | ((self.raster_line & 0x0100) >> 1))

    def write(self, addr, value):
        addr -= 0x0400

        self.vid_ram[addr] = value
        
        if value < 32:
            value |= 64

        self.window.addch(addr // 40, addr % 40, value)
