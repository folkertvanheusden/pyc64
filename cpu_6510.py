class cpu_6510:
    def __init__(self, bus):
        self.bus = bus

        self.opcodes = [ None ] * 256
        self.opcodes[0x01] = self.ORA_indirect_x
        self.opcodes[0x04] = self.NOP_zeropage
        self.opcodes[0x05] = self.ORA_zeropage
        self.opcodes[0x06] = self.ASL_zeropage
        self.opcodes[0x08] = self.PHP
        self.opcodes[0x09] = self.ORA_immediate
        self.opcodes[0x0a] = self.ASL_accumulator
        self.opcodes[0x0C] = self.NOP_absolute
        self.opcodes[0x0d] = self.ORA_absolute
        self.opcodes[0x0e] = self.ASL_absolute
        self.opcodes[0x10] = self.BPL
        self.opcodes[0x11] = self.ORA_indirect_y
        self.opcodes[0x14] = self.NOP_zeropage_x
        self.opcodes[0x15] = self.ORA_zeropage_x
        self.opcodes[0x16] = self.ASL_zeropage_x
        self.opcodes[0x18] = self.CLC
        self.opcodes[0x19] = self.ORA_absolute_y
        self.opcodes[0x1A] = self.NOP
        self.opcodes[0x1C] = self.NOP_absolute
        self.opcodes[0x1d] = self.ORA_absolute_x
        self.opcodes[0x1e] = self.ASL_absolute_x
        self.opcodes[0x20] = self.JSR
        self.opcodes[0x21] = self.AND_indirect_x
        self.opcodes[0x24] = self.BIT_zeropage
        self.opcodes[0x25] = self.AND_zeropage
        self.opcodes[0x26] = self.ROL
        self.opcodes[0x28] = self.PLP
        self.opcodes[0x29] = self.AND_immediate
        self.opcodes[0x2a] = self.ROL
        self.opcodes[0x2c] = self.BIT_absolute
        self.opcodes[0x2d] = self.AND_absolute
        self.opcodes[0x2e] = self.ROL
        self.opcodes[0x30] = self.BMI
        self.opcodes[0x31] = self.AND_indirect_y
        self.opcodes[0x34] = self.NOP_zeropage_x
        self.opcodes[0x35] = self.AND_zeropage_x
        self.opcodes[0x36] = self.ROL
        self.opcodes[0x38] = self.SEC
        self.opcodes[0x39] = self.AND_absolute_y
        self.opcodes[0x3A] = self.NOP
        self.opcodes[0x3C] = self.NOP_absolute
        self.opcodes[0x3d] = self.AND_absolute_x
        self.opcodes[0xee] = self.ROL
        self.opcodes[0x41] = self.EOR_indirect_x
        self.opcodes[0x44] = self.NOP_zeropage
        self.opcodes[0x45] = self.EOR_zeropage
        self.opcodes[0x46] = self.LSR_zeropage
        self.opcodes[0x48] = self.PHA
        self.opcodes[0x49] = self.EOR_immediate
        self.opcodes[0x4a] = self.LSR_accumulator
        self.opcodes[0x4c] = self.JMP_absolute
        self.opcodes[0x4d] = self.EOR_absolute
        self.opcodes[0x4e] = self.LSR_absolute
        self.opcodes[0x51] = self.EOR_indirect_y
        self.opcodes[0x54] = self.NOP_zeropage_x
        self.opcodes[0x55] = self.EOR_zeropage_x
        self.opcodes[0x56] = self.LSR_zeropage_x
        self.opcodes[0x58] = self.CLI
        self.opcodes[0x59] = self.EOR_absolute_y
        self.opcodes[0x5A] = self.NOP
        self.opcodes[0x5C] = self.NOP_absolute
        self.opcodes[0x5d] = self.EOR_absolute_x
        self.opcodes[0x5e] = self.LSR_absolute_x
        self.opcodes[0x60] = self.RTS
        self.opcodes[0x61] = self.ADC_indirect_x
        self.opcodes[0x64] = self.NOP_zeropage
        self.opcodes[0x65] = self.ADC_zeropage
        self.opcodes[0x68] = self.PLA
        self.opcodes[0x69] = self.ADC_immediate
        self.opcodes[0x6c] = self.JMP_absolute_indirect
        self.opcodes[0x6d] = self.ADC_absolute
        self.opcodes[0x71] = self.ADC_indirect_y
        self.opcodes[0x74] = self.NOP_zeropage_x
        self.opcodes[0x75] = self.ADC_zeropage_x
        self.opcodes[0x78] = self.SEI
        self.opcodes[0x79] = self.ADC_absolute_y
        self.opcodes[0x7A] = self.NOP
        self.opcodes[0x7C] = self.NOP_absolute
        self.opcodes[0x7d] = self.ADC_absolute_x
        self.opcodes[0x80] = self.NOP_immediate
        self.opcodes[0x81] = self.ST_indirect_x
        self.opcodes[0x82] = self.NOP_immediate
        self.opcodes[0x84] = self.ST_zeropage
        self.opcodes[0x85] = self.ST_zeropage
        self.opcodes[0x86] = self.ST_zeropage
        self.opcodes[0x88] = self.DEY
        self.opcodes[0x89] = self.NOP_immediate
        self.opcodes[0x8a] = self.TXA
        self.opcodes[0x8c] = self.ST_absolute
        self.opcodes[0x8d] = self.ST_absolute
        self.opcodes[0x8e] = self.ST_absolute
        self.opcodes[0x90] = self.BCC
        self.opcodes[0x91] = self.ST_indirect_y
        self.opcodes[0x94] = self.ST_zeropage_x
        self.opcodes[0x95] = self.ST_zeropage_x
        self.opcodes[0x96] = self.ST_zeropage_y
        self.opcodes[0x98] = self.TYA
        self.opcodes[0x99] = self.ST_absolute_y
        self.opcodes[0x9a] = self.TXS
        self.opcodes[0x9d] = self.ST_absolute_x
        self.opcodes[0xa0] = self.LDY_immediate
        self.opcodes[0xa1] = self.LDA_indirect_x
        self.opcodes[0xa2] = self.LDX_immediate
        self.opcodes[0xa4] = self.LDY_zeropage
        self.opcodes[0xa5] = self.LDA_zeropage
        self.opcodes[0xa6] = self.LDX_zeropage
        self.opcodes[0xa8] = self.TAY
        self.opcodes[0xa9] = self.LDA_immediate
        self.opcodes[0xaa] = self.TAX
        self.opcodes[0xac] = self.LDY_absolute
        self.opcodes[0xad] = self.LDA_absolute
        self.opcodes[0xae] = self.LDX_absolute
        self.opcodes[0xb0] = self.BCS
        self.opcodes[0xb1] = self.LDA_indirect_y
        self.opcodes[0xb4] = self.LDY_zeropage_x
        self.opcodes[0xb5] = self.LDA_zeropage_x
        self.opcodes[0xb6] = self.LDX_zeropage_y
        self.opcodes[0xb9] = self.LDA_absolute_y
        self.opcodes[0xba] = self.TSX
        self.opcodes[0xbc] = self.LDY_absolute_x
        self.opcodes[0xbd] = self.LDA_absolute_x
        self.opcodes[0xbe] = self.LDX_absolute_y
        self.opcodes[0xc0] = self.CMP_immediate
        self.opcodes[0xc1] = self.CMP_indirect_x
        self.opcodes[0xC2] = self.NOP_immediate
        self.opcodes[0xc4] = self.CMP_zeropage
        self.opcodes[0xc5] = self.CMP_zeropage
        self.opcodes[0xc6] = self.DEC_zeropage
        self.opcodes[0xc8] = self.INY
        self.opcodes[0xc9] = self.CMP_immediate
        self.opcodes[0xca] = self.DEX
        self.opcodes[0xcc] = self.CMP_absolute
        self.opcodes[0xcd] = self.CMP_absolute
        self.opcodes[0xce] = self.DEC_absolute
        self.opcodes[0xd0] = self.BNE
        self.opcodes[0xd1] = self.CMP_indirect_y
        self.opcodes[0xD4] = self.NOP_zeropage_x
        self.opcodes[0xd5] = self.CMP_zeropage_x
        self.opcodes[0xd6] = self.DEC_zeropage_x
        self.opcodes[0xd8] = self.CLD
        self.opcodes[0xd9] = self.CMP_absolute_y
        self.opcodes[0xDA] = self.NOP
        self.opcodes[0xDC] = self.NOP_absolute
        self.opcodes[0xdd] = self.CMP_absolute_x
        self.opcodes[0xde] = self.DEC_absolute_x
        self.opcodes[0xe0] = self.CMP_immediate
        self.opcodes[0xe1] = self.SBC_indirect_x
        self.opcodes[0xE2] = self.NOP_immediate
        self.opcodes[0xe4] = self.CMP_zeropage
        self.opcodes[0xe5] = self.SBC_zeropage
        self.opcodes[0xe6] = self.INC_zeropage
        self.opcodes[0xe8] = self.INX
        self.opcodes[0xe9] = self.SBC_immediate
        self.opcodes[0xea] = self.NOP
        self.opcodes[0xec] = self.CMP_absolute
        self.opcodes[0xed] = self.SBC_absolute
        self.opcodes[0xee] = self.INC_absolute
        self.opcodes[0xf0] = self.BEQ
        self.opcodes[0xf1] = self.SBC_indirect_y
        self.opcodes[0xF4] = self.NOP_zeropage_x
        self.opcodes[0xf5] = self.SBC_zeropage_x
        self.opcodes[0xf6] = self.INC_zeropage_x
        self.opcodes[0xf9] = self.SBC_absolute_y
        self.opcodes[0xFA] = self.NOP
        self.opcodes[0xFC] = self.NOP_absolute_x
        self.opcodes[0xfd] = self.SBC_absolute_x
        self.opcodes[0xfe] = self.INC_absolute_x

    def reset(self):
        self.bus.reset()

        self.pc = self.bus.read(0xfffc) | (self.bus.read(0xfffd) << 8)
        self.a = self.x = self.y = 0
        self.sp = 0
        self.p = 0

        self.cycles = 0

    def tick(self):
        old_addr = self.pc
        opcode = self.read_pc()
        print('%04x %02x' % (old_addr, opcode))

        if self.opcodes[opcode]:
            self.opcodes[opcode](opcode)
        else:
            print('UNKNOWN OPCODE ^')
            assert False

        assert self.pc >= 0x0000 and self.pc < 0x10000
        assert self.a >= 0 and self.a < 256
        assert self.x >= 0 and self.x < 256
        assert self.y >= 0 and self.y < 256
        assert self.sp >= 0 and self.sp < 256
        assert self.p >= 0 and self.p < 256

    def push_stack(self, val):
        self.bus.write(self.sp + 0x100, val)
        self.sp -= 1
        self.sp &= 0xff

    def push_stack_16b(self, val):
        self.bus.write(self.sp + 0x100, val >> 8)
        self.sp -= 1
        self.sp &= 0xff

        self.bus.write(self.sp + 0x100, val & 255)
        self.sp -= 1
        self.sp &= 0xff

    def pop_stack(self):
        self.sp += 1
        self.sp &= 0xff

        return self.bus.read(self.sp + 0x100)

    def pop_stack_16b(self):
        self.sp += 1
        self.sp &= 0xff
        addr = self.bus.read(self.sp + 0x100)

        self.sp += 1
        self.sp &= 0xff
        addr += self.bus.read(self.sp + 0x100) << 8

        return addr

    def set_NZ_flags(self, result_value):
        if result_value > 127:  # NEGATIVE
            self.p |= 128
        else:
            self.p &= ~128

        if result_value == 0:  # ZERO
            self.p |= 2
        else:
            self.p &= ~2

    def set_CZN_flags(self, register, value):
        if value > register:  # CARRY
            self.p |= 1
        else:
            self.p &= ~1

        if value == register:  # ZERO
            self.p |= 2
        else:
            self.p &= ~2

        sub = register - value
        if sub < 0 or sub > 127:  # NEGATIVE
            self.p |= 128
        else:
            self.p &= ~128

    def read16b(self, addr):
        return self.bus.read(addr) | (self.bus.read((addr + 1) & 0xffff) << 8)

    def read_pc(self):
        value = self.bus.read(self.pc)
        self.pc += 1
        self.pc &= 0xffff
        return value

    def read_pc_16b(self):
        value = self.read16b(self.pc)
        self.pc += 2
        self.pc &= 0xffff
        return value

    def data_immediate(self):
        return self.read_pc()

    def data_absolute(self):
        return self.bus.read(self.addr_absolute())

    def addr_absolute(self):
        return self.read_pc_16b()

    def addr_absolute_x(self):
        addr = self.read_pc_16b()
        addr += self.x
        addr &= 0xffff
        return addr

    def data_absolute_x(self):
        return self.bus.read(self.addr_absolute_x())

    def addr_absolute_y(self):
        addr = self.read_pc_16b()
        addr += self.y
        addr &= 0xffff
        return addr

    def data_absolute_y(self):
        return self.bus.read(self.addr_absolute_y())

    def addr_indirect_x(self):
        addr = self.x
        addr += self.read_pc()
        addr2 = self.read16b(addr)
        return addr2

    def data_indirect_x(self):
        return self.bus.read(self.addr_indirect_x())

    def addr_indirect_y(self):
        addr = self.read_pc()
        addr2 = self.read16b(addr)
        addr3 = (addr2 + self.y) & 0xffff
        return addr3

    def data_indirect_y(self):
        addr = self.addr_indirect_y()
        data = self.bus.read(addr)
        return data

    def data_zeropage(self):
        addr = self.addr_zeropage()
        data = self.bus.read(addr)
        return data

    def addr_zeropage(self):
        return self.read_pc()

    def addr_zeropage_x(self):
        addr = self.read_pc()
        return (addr + self.x) & 0xffff

    def data_zeropage_x(self):
        return self.bus.read(self.addr_zeropage_x())

    def addr_zeropage_y(self):
        addr = self.read_pc()
        return (addr + self.y) & 0xffff

    def data_zeropage_y(self):
        return self.bus.read(self.addr_zeropage_y())

    def do_DEC(self, addr):
        data = self.bus.read(addr)
        data -= 1
        data &= 255
        self.bus.write(addr, data)
        self.set_NZ_flags(data)

    def do_INC(self, addr):
        data = self.bus.read(addr)
        data += 1
        data &= 255
        self.bus.write(addr, data)
        self.set_NZ_flags(data)

    def do_Bxx(self, flag, set_):
        distance = self.read_pc()

        if (self.p & flag) == set_:
            if distance >= 128:
                distance = -(256 - distance)
            self.pc += distance
            self.pc &= 0xffff

        self.cycles += 2  # FIXME

    def BCC(self, opcode):
        self.do_Bxx(1, 0)

    def BCS(self, opcode):
        self.do_Bxx(1, 1)

    def BEQ(self, opcode):
        self.do_Bxx(2, 2)

    def BNE(self, opcode):
        self.do_Bxx(2, 0)

    def BMI(self, opcode):
        self.do_Bxx(128, 128)

    def BPL(self, opcode):
        self.do_Bxx(128, 0)

    def do_ADC(self, value):
        olda = self.a
        value += self.p & 1
        self.a += value
        self.p &= ~(1 | 64);  # clear carry and sign

        if self.a > 255:
            self.p |= 1

        if (olda ^ self.a) & (value ^ self.a) & 0x80:
            self.p |= 64

        self.a &= 0xff
        self.set_NZ_flags(self.a)

    def do_SBC(self, value):
        olda = self.a
        self.a -= value + 1 - (self.p & 1)
        self.p &= ~(1 | 64);  # clear carry and sign

        if self.a < 0:
            self.p |= 1

        if (olda ^ self.a) & (value ^ self.a) & 0x80:
            self.p |= 64

        self.a &= 0xff
        self.set_NZ_flags(self.a)

    def do_ASL(self, value):
        if value & 128:
            self.p |= 1
        else:
            self.p &= ~1
        value <<= 1
        value &= 0xff
        self.set_NZ_flags(value)
        return value

    def do_LSR(self, value):
        if value & 1:
            self.p |= 1
        else:
            self.p &= ~1
        value >>= 1
        self.set_NZ_flags(value)
        return value

    def do_BIT(self, value):
        self.p |= value & 192
        if (self.a & value) == 0:
            self.p |= 2
        else:
            self.p &= ~2

    def LDA_immediate(self, opcode):
        self.a = self.read_pc()
        self.set_NZ_flags(self.a)
        self.cycles += 2

    def LDX_immediate(self, opcode):
        self.x = self.read_pc()
        self.set_NZ_flags(self.x)
        self.cycles += 2

    def LDY_immediate(self, opcode):
        self.y = self.read_pc()
        self.set_NZ_flags(self.y)
        self.cycles += 2

    def LDA_zeropage(self, opcode):
        self.a = self.data_zeropage()
        self.set_NZ_flags(self.a)
        self.cycles += 3

    def LDX_zeropage(self, opcode):
        self.x = self.data_zeropage()
        self.set_NZ_flags(self.x)
        self.cycles += 3

    def LDY_zeropage(self, opcode):
        self.y = self.data_zeropage()
        self.set_NZ_flags(self.y)
        self.cycles += 3

    def LDA_zeropage_x(self, opcode):
        self.a = self.data_zeropage_x()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def LDY_zeropage_x(self, opcode):
        self.y = self.data_zeropage_x()
        self.set_NZ_flags(self.y)
        self.cycles += 4

    def LDX_zeropage_y(self, opcode):
        self.x = self.data_zeropage_y()
        self.set_NZ_flags(self.x)
        self.cycles += 4

    def LDA_absolute(self, opcode):
        self.a = self.data_absolute()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def LDX_absolute(self, opcode):
        self.x = self.data_absolute()
        self.set_NZ_flags(self.x)
        self.cycles += 4

    def LDY_absolute(self, opcode):
        self.y = self.data_absolute()
        self.set_NZ_flags(self.y)
        self.cycles += 4

    def LDA_absolute_x(self, opcode):
        self.a = self.data_absolute_x()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def LDY_absolute_x(self, opcode):
        self.y = self.data_absolute_x()
        self.set_NZ_flags(self.y)
        self.cycles += 4

    def LDA_absolute_y(self, opcode):
        self.a = self.data_absolute_y()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def LDX_absolute_y(self, opcode):
        self.x = self.data_absolute_y()
        self.set_NZ_flags(self.x)
        self.cycles += 4

    def LDA_indirect_x(self, opcode):
        self.a = self.data_indirect_x()
        self.set_NZ_flags(self.a)
        self.cycles += 6

    def LDA_indirect_y(self, opcode):
        self.a = self.data_indirect_y()
        self.set_NZ_flags(self.a)
        self.cycles += 5

    def ST_zeropage(self, opcode):
        if opcode == 0x85:
            register = self.a
        elif opcode == 0x86:
            register = self.x
        elif opcode == 0x84:
            register = self.y
        else:
            assert False
        addr = self.read_pc()
        self.bus.write(addr, register)
        self.cycles += 3

    def ST_zeropage_x(self, opcode):
        self.bus.write(self.addr_zeropage_x(), self.y)
        self.cycles += 4

    def ST_zeropage_y(self, opcode):
        self.bus.write(self.addr_zeropage_y(), self.x)
        self.cycles += 4

    def ST_absolute(self, opcode):
        if opcode == 0x8d:
            val = self.a
        elif opcode == 0x8e:
            val = self.x
        elif opcode == 0x8c:
            val = self.y
        else:
            assert False
        self.bus.write(self.read_pc_16b(), val)
        self.cycles += 4

    def ST_absolute_x(self, opcode):
        self.bus.write(self.addr_absolute_x(), self.a)
        self.cycles += 5

    def ST_absolute_y(self, opcode):
        self.bus.write(self.addr_absolute_y(), self.a)
        self.cycles += 5

    def ST_indirect_x(self, opcode):
        self.bus.write(self.addr_indirect_x(), self.a)
        self.cycles += 6

    def ST_indirect_y(self, opcode):
        self.bus.write(self.addr_indirect_y(), self.a)
        self.cycles += 6

    def CMP_immediate(self, opcode):
        if opcode == 0xc9:
            register = self.a
        elif opcode == 0xe0:
            register = self.x
        elif opcode == 0xc0:
            register = self.y
        else:
            assert False
        self.set_CZN_flags(register, self.data_immediate())
        self.cycles += 2

    def CMP_zeropage(self, opcode):
        if opcode == 0xc5:
            register = self.a
        elif opcode == 0xe4:
            register = self.x
        elif opcode == 0xc4:
            register = self.y
        else:
            assert False
        self.set_CZN_flags(register, self.data_zeropage())
        self.cycles += 3

    def CMP_zeropage_x(self, opcode):
        self.set_CZN_flags(self.a, self.data_zeropage_x())
        self.cycles += 4

    def CMP_absolute(self, opcode):
        if opcode == 0xcd:
            register = self.a
        elif opcode == 0xec:
            register = self.x
        elif opcode == 0xc4:
            register = self.y
        else:
            assert False
        self.set_CZN_flags(register, self.data_absolute())
        self.cycles += 4

    def CMP_absolute_x(self, opcode):
        self.set_CZN_flags(self.a, self.data_absolute_x())
        self.cycles += 4

    def CMP_absolute_y(self, opcode):
        self.set_CZN_flags(self.a, self.data_absolute_y())
        self.cycles += 4

    def CMP_indirect_x(self, opcode):
        self.set_CZN_flags(self.a, self.data_indirect_x())
        self.cycles += 6

    def CMP_indirect_y(self, opcode):
        self.set_CZN_flags(self.a, self.data_indirect_y())
        self.cycles += 5

    def DEC_zeropage(self, opcode):
        self.do_DEC(self.addr_zeropage())
        self.cycles += 5

    def DEC_zeropage_x(self, opcode):
        self.do_DEC(self.addr_zeropage_x())
        self.cycles += 6

    def DEC_absolute(self, opcode):
        self.do_DEC(self.addr_absolute())
        self.cycles += 6

    def DEC_absolute_x(self, opcode):
        self.do_DEC(self.addr_absolute_x())
        self.cycles += 7

    def DEX(self, opcode):
        self.x -= 1
        self.x &= 255
        self.set_NZ_flags(self.x)
        self.cycles += 2

    def DEY(self, opcode):
        self.y -= 1
        self.y &= 255
        self.set_NZ_flags(self.y)
        self.cycles += 2

    def INC_zeropage(self, opcode):
        self.do_INC(self.addr_zeropage())
        self.cycles += 5

    def INC_zeropage_x(self, opcode):
        self.do_INC(self.addr_zeropage_x())
        self.cycles += 6

    def INC_absolute(self, opcode):
        self.do_INC(self.addr_absolute())
        self.cycles += 6

    def INC_absolute_x(self, opcode):
        self.do_INC(self.addr_absolute_x())
        self.cycles += 7

    def INX(self, opcode):
        self.x += 1
        self.x &= 255
        self.set_NZ_flags(self.x)
        self.cycles += 2

    def INY(self, opcode):
        self.y += 1
        self.y &= 255
        self.set_NZ_flags(self.y)
        self.cycles += 2

    def NOP(self, opcode):
        self.cycles += 2

    def NOP_immediate(self, opcode):
        self.data_immediate()
        self.cycles += 2

    def NOP_zeropage(self, opcode):
        self.data_zeropage()
        self.cycles += 3

    def NOP_zeropage_x(self, opcode):
        self.data_zeropage_x()
        self.cycles += 4

    def NOP_absolute(self, opcode):
        self.data_absolute()
        self.cycles += 4

    def NOP_absolute_x(self, opcode):
        self.data_absolute_x()
        self.cycles += 4

    def JMP_absolute(self, opcode):
        self.pc = self.read_pc_16b()
        self.cycles += 3

    def JMP_absolute_indirect(self, opcode):
        addr = self.read_pc_16b()
        self.pc = self.read16b(addr)
        self.cycles += 5

    def EOR_immediate(self, opcode):
        self.a ^= self.read_pc()
        self.set_NZ_flags(self.a)
        self.cycles += 2

    def EOR_zeropage(self, opcode):
        self.a ^= self.data_zeropage()
        self.set_NZ_flags(self.a)
        self.cycles += 3

    def EOR_zeropage_x(self, opcode):
        self.a ^= self.data_zeropage_x()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def EOR_absolute(self, opcode):
        self.a ^= self.data_absolute()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def EOR_absolute_x(self, opcode):
        self.a ^= self.data_absolute_x()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def EOR_absolute_y(self, opcode):
        self.a ^= self.data_absolute_y()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def EOR_indirect_x(self, opcode):
        self.a ^= self.data_indirect_x()
        self.set_NZ_flags(self.a)
        self.cycles += 6

    def EOR_indirect_y(self, opcode):
        self.a ^= self.data_indirect_y()
        self.set_NZ_flags(self.a)
        self.cycles += 5

    def AND_immediate(self, opcode):
        self.a &= self.read_pc()
        self.set_NZ_flags(self.a)
        self.cycles += 2

    def AND_zeropage(self, opcode):
        self.a &= self.data_zeropage()
        self.set_NZ_flags(self.a)
        self.cycles += 3

    def AND_zeropage_x(self, opcode):
        self.a &= self.data_zeropage_x()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def AND_absolute(self, opcode):
        self.a &= self.data_absolute()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def AND_absolute_x(self, opcode):
        self.a &= self.data_absolute_x()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def AND_absolute_y(self, opcode):
        self.a &= self.data_absolute_y()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def AND_indirect_x(self, opcode):
        self.a &= self.data_indirect_x()
        self.set_NZ_flags(self.a)
        self.cycles += 6

    def AND_indirect_y(self, opcode):
        self.a &= self.data_indirect_y()
        self.set_NZ_flags(self.a)
        self.cycles += 5

    def ORA_immediate(self, opcode):
        self.a |= self.read_pc()
        self.set_NZ_flags(self.a)
        self.cycles += 2

    def ORA_zeropage(self, opcode):
        self.a |= self.data_zeropage()
        self.set_NZ_flags(self.a)
        self.cycles += 3

    def ORA_zeropage_x(self, opcode):
        self.a |= self.data_zeropage_x()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def ORA_absolute(self, opcode):
        self.a |= self.data_absolute()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def ORA_absolute_x(self, opcode):
        self.a |= self.data_absolute_x()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def ORA_absolute_y(self, opcode):
        self.a |= self.data_absolute_y()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def ORA_indirect_x(self, opcode):
        self.a |= self.data_indirect_x()
        self.set_NZ_flags(self.a)
        self.cycles += 6

    def ORA_indirect_y(self, opcode):
        self.a |= self.data_indirect_y()
        self.set_NZ_flags(self.a)
        self.cycles += 5

    def JSR(self, opcode):
        new_addr = self.read_pc_16b()
        self.push_stack_16b((self.pc - 1) & 0xffff)
        self.pc = new_addr
        self.cycles += 6

    def SEI(self, opcode):
        self.p |= 4
        self.cycles += 2

    def TXA(self, opcode):
        self.a = self.x
        self.set_NZ_flags(self.a)
        self.cycles += 2

    def TXS(self, opcode):
        self.sp = self.x
        self.cycles += 2

    def TAX(self, opcode):
        self.x = self.a
        self.set_NZ_flags(self.x)
        self.cycles += 2

    def TAY(self, opcode):
        self.y = self.a
        self.set_NZ_flags(self.y)
        self.cycles += 2

    def TSX(self, opcode):
        self.x = self.sp
        self.set_NZ_flags(self.x)
        self.cycles += 2

    def TYA(self, opcode):
        self.a = self.y
        self.set_NZ_flags(self.a)
        self.cycles += 2

    def RTS(self, opcode):
        self.pc = (self.pop_stack_16b() + 1) & 0xffff
        self.cycles += 6

    def CLD(self, opcode):
        self.p &= ~8
        self.cycles += 2

    def CLC(self, opcode):
        self.p &= ~1
        self.cycles += 2

    def ADC_immediate(self, opcode):
        self.do_ADC(self.read_pc())
        self.cycles += 2

    def ADC_zeropage(self, opcode):
        self.do_ADC(self.data_zeropage())
        self.cycles += 3

    def ADC_zeropage_x(self, opcode):
        self.do_ADC(self.data_zeropage_x())
        self.cycles += 4

    def ADC_absolute(self, opcode):
        self.do_ADC(self.data_absolute())
        self.cycles += 4

    def ADC_absolute_x(self, opcode):
        self.do_ADC(self.data_absolute_x())
        self.cycles += 4

    def ADC_absolute_y(self, opcode):
        self.do_ADC(self.data_absolute_y())
        self.cycles += 4

    def ADC_indirect_x(self, opcode):
        self.do_ADC(self.data_indirect_x())
        self.cycles += 6

    def ADC_indirect_y(self, opcode):
        self.do_ADC(self.data_indirect_y())
        self.cycles += 5

    def CLI(self, opcode):
        self.p &= ~4
        self.cycles += 2

    def SEC(self, opcode):
        self.p |= 1
        self.cycles += 2

    def SBC_immediate(self, opcode):
        self.do_ADC(self.read_pc())
        self.cycles += 2

    def SBC_zeropage(self, opcode):
        self.do_SBC(self.data_zeropage())
        self.cycles += 3

    def SBC_zeropage_x(self, opcode):
        self.do_SBC(self.data_zeropage_x())
        self.cycles += 4

    def SBC_absolute(self, opcode):
        self.do_SBC(self.data_absolute())
        self.cycles += 4

    def SBC_absolute_x(self, opcode):
        self.do_SBC(self.data_absolute_x())
        self.cycles += 4

    def SBC_absolute_y(self, opcode):
        self.do_SBC(self.data_absolute_y())
        self.cycles += 4

    def SBC_indirect_x(self, opcode):
        self.do_SBC(self.data_indirect_x())
        self.cycles += 6

    def SBC_indirect_y(self, opcode):
        self.do_SBC(self.data_indirect_y())
        self.cycles += 5

    def PHP(self, opcode):
        self.push_stack(self.p)
        self.cycles += 3

    def PHA(self, opcode):
        self.push_stack(self.a)
        self.cycles += 3

    def PLA(self, opcode):
        self.a = self.pop_stack()
        self.set_NZ_flags(self.a)
        self.cycles += 4

    def PLP(self, opcode):
        self.p = self.pop_stack()
        self.cycles += 4

    def ASL_accumulator(self, opcode):
        self.a = self.do_ASL(self.a)
        self.cycles += 2

    def ASL_zeropage(self, opcode):
        addr = self.addr_zeropage()
        self.bus.write(addr, self.do_ASL(self.bus.read(addr)))
        self.cycles += 5

    def ASL_zeropage_x(self, opcode):
        addr = self.addr_zeropage_x()
        self.bus.write(addr, self.do_ASL(self.bus.read(addr)))
        self.cycles += 6

    def ASL_absolute(self, opcode):
        addr = self.addr_absolute()
        self.bus.write(addr, self.do_ASL(self.bus.read(addr)))
        self.cycles += 6

    def ASL_absolute_x(self, opcode):
        addr = self.addr_absolute_x()
        self.bus.write(addr, self.do_ASL(self.bus.read(addr)))
        self.cycles += 7

    def LSR_accumulator(self, opcode):
        self.a = self.do_LSR(self.a)
        self.cycles += 2

    def LSR_zeropage(self, opcode):
        addr = self.addr_zeropage()
        self.bus.write(addr, self.do_LSR(self.bus.read(addr)))
        self.cycles += 5

    def LSR_zeropage_x(self, opcode):
        addr = self.addr_zeropage_x()
        self.bus.write(addr, self.do_LSR(self.bus.read(addr)))
        self.cycles += 6

    def LSR_absolute(self, opcode):
        addr = self.addr_absolute()
        self.bus.write(addr, self.do_LSR(self.bus.read(addr)))
        self.cycles += 6

    def LSR_absolute_x(self, opcode):
        addr = self.addr_absolute_x()
        self.bus.write(addr, self.do_LSR(self.bus.read(addr)))
        self.cycles += 7

    def BIT_zeropage(self, opcode):
        self.do_BIT(self.data_zeropage())

    def BIT_absolute(self, opcode):
        self.do_BIT(self.data_absolute())

    def ROL(self, opcode):
        old_carry = self.p & 1

        if opcode == 0x2a:
            self.p |= self.a >> 7
            self.a <<= 1
            self.a &= 255
            self.a |= old_carry

        elif opcode == 0x26 or opcode == 0x36:
            zp_addr = self.addr_zeropage() if opcode == 0x26 else self.addr_zeropage_x()
            val = self.bus.read(zp_addr)
            self.p |= val >> 7
            val <<= 1
            val &= 255
            val |= old_carry
            self.bus.write(zp_addr, val)

        elif opcode == 0x2e or opcode == 0x3e:
            zp_addr = self.addr_absolute() if opcode == 0x2e else self.addr_absolute_x()
            val = self.bus.read(zp_addr)
            self.p |= val >> 7
            val <<= 1
            val &= 255
            val |= old_carry
            self.bus.write(zp_addr, val)

        else:
            assert False
