import curses
import sdl2
import sdl2.ext
from threading import Thread

class vic_ii(Thread):
    def __init__(self):
        super().__init__()

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

    def begin(self, bus):
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

        #self.bus.write(0xd012, self.raster_line & 255)

        #org_value = self.bus.read(0xd011)
        #self.bus.write(0xd011, org_value | ((self.raster_line & 0x0100) >> 1))

    def write(self, addr, value):
        if addr >= 0x0400 and addr < 0x0800:  # screen ram
            addr -= 0x0400

            value = int(value)

            self.screen_ram[addr] = value
            
            if value < 32:
                value |= 64

            self.window.addch(addr // 40, addr % 40, value)

        elif addr >= 0xd800 and addr < 0xdbe8:  # color ram
            addr -= 0xd800

            self.color_ram[addr] = value

            #self.window.chgat(addr // 40, addr % 40, curses.color_pair((value & 7) + 1))

    def run(self):
        sdl2.ext.init()

        window = sdl2.ext.Window('PyC64', size=(640, 480))
        window.show()

        windowsurface = window.get_surface()

        pixelview = sdl2.ext.PixelView(windowsurface)

        palette = [
                sdl2.ext.Color(0, 0, 0),
                sdl2.ext.Color(255, 255, 255),
                sdl2.ext.Color(136, 0, 0),
                sdl2.ext.Color(170, 255, 238),
                sdl2.ext.Color(204, 68, 204),
                sdl2.ext.Color(0, 204, 85),
                sdl2.ext.Color(0, 0, 170),
                sdl2.ext.Color(238, 238, 119),
                sdl2.ext.Color(221, 136, 85),
                sdl2.ext.Color(102, 68, 0),
                sdl2.ext.Color(255, 119, 119),
                sdl2.ext.Color(51, 51, 51),
                sdl2.ext.Color(119, 119, 119),
                sdl2.ext.Color(170, 255, 102),
                sdl2.ext.Color(0, 136, 255),
                sdl2.ext.Color(187, 187, 187)
                ]

        line = 0

        running = True

        while running:
            events = sdl2.ext.get_events()

            for event in events:
                if event.type == sdl2.SDL_QUIT:
                    running = False

            if not running:
                continue

            bg_color_index = self.bus.i_o.read(0xd021)
            bg_color = palette[bg_color_index]

            for line in range(0, 25):
                offset = line * 40

                for x in range(0, 40):
                    b = self.bus.read(0x0400 + offset + x)

                    addr_chargen = 0xd000 + b * 8

                    fg_color_index = self.color_ram[offset + x] & 15
                    fg_color = palette[fg_color_index]

                    for row in range(0, 8):
                        char_scan_line = self.bus.character_rom.read(addr_chargen + row)

                        y = line * 8 + row

                        xc = x * 8

                        mask = 128

                        for col in range(xc, xc + 8):
                            pixelview[y][col] = fg_color if char_scan_line & mask else bg_color

                            mask >>= 1

            del pixelview
            pixelview = sdl2.ext.PixelView(windowsurface)

            window.refresh()

        sdl2.SDL_DestroyWindow(window)

        sdl2.SDL_Quit()
