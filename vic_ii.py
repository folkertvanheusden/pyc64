import curses

class vic_ii:
    def __init__(self):
        self.cycle = 0
        self.raster_line = 0

        self.screen_ram = [ 0 ] * 1024
        self.color_ram  = [ 0 ] * 1000

        self.window = curses.initscr()

        curses.start_color()
        curses.init_pair(0 + 1, curses.COLOR_WHITE  , curses.COLOR_BLACK)
        curses.init_pair(1 + 1, curses.COLOR_BLACK  , curses.COLOR_WHITE)
        curses.init_pair(2 + 1, curses.COLOR_RED    , curses.COLOR_BLACK)
        curses.init_pair(3 + 1, curses.COLOR_CYAN   , curses.COLOR_BLACK)
        curses.init_pair(4 + 1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(5 + 1, curses.COLOR_GREEN  , curses.COLOR_BLACK)
        curses.init_pair(6 + 1, curses.COLOR_BLUE   , curses.COLOR_BLACK)
        curses.init_pair(7 + 1, curses.COLOR_YELLOW , curses.COLOR_BLACK)

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
        if addr >= 0x0400 and addr < 0x0800:  # screen ram
            addr -= 0x0400

            self.screen_ram[addr] = value
            
            if value < 32:
                value |= 64

            self.window.addch(addr // 40, addr % 40, value)

        elif addr >= 0xd800 and addr < 0xdbe8:  # color ram
            addr -= 0xd800

            self.color_ram[addr] = value

            #self.window.chgat(addr // 40, addr % 40, curses.color_pair((value & 7) + 1))
