from bus import bus

class cpu_6510:
    def __init__(self, bus):
        self.bus = bus

        self.opcodes = [ None ] * 256
        self.opcodes[0xea] = self.i_nop

    def reset(self):
        self.bus.reset()
        self.pc = (self.bus.read(0xfffc) << 8) | self.bus.read(0xfffd)

    def tick(self):
        opcode = self.bus.read(self.pc)

        if self.opcodes[opcode]:
            self.opcodes[opcode](opcode)

        self.pc += 1

    def i_nop(self, opcode):
        pass
