from amaranth import *
from amaranth.lib import wiring
from amaranth.lib.wiring import In, Out

class ALU(wiring.Component):
    def __init__(self):
        super().__init__({
            "a": In(32),
            "b": In(32),
            "opcode": In(6),
            "func3": In(3),
            "func7": In(7),
            "out": Out(32)
        })
        self.OP = (self.opcode == 0b0110011)

    def elaborate(self, platform):
        m = Module()
        with m.If(self.OP):
            with m.Switch(self.func3):
                with m.Case(0b000):
                    with m.Switch(self.func7):
                        with m.Case(0b0000000):
                            m.d.comb += self.out.eq(self.a + self.b)
                        with m.Case(0b0100000):
                            m.d.comb += self.out.eq(self.a - self.b)
                with m.Case(0b001):
                    m.d.comb += self.out.eq(self.a << self.b[0:4])
                with m.Case(0b010):
                    m.d.comb += self.out.eq(self.a < self.b)
                with m.Case(0b011):
                    m.d.comb += self.out.eq(self.a < self.b)
                with m.Case(0b100):
                    m.d.comb += self.out.eq(self.a ^ self.b)
                with m.Case(0b101):
                    with m.Switch(self.func7):
                        with m.Case(0b0000000):
                            m.d.comb += self.out.eq(self.a.as_unsigned() >> self.b[0:4])
                        with m.Case(0b0100000):
                            m.d.comb += self.out.eq(self.a >> self.b[0:4])
                with m.Case(0b110):
                    m.d.comb += self.out.eq(self.a | self.b)
                with m.Case(0b111):
                    m.d.comb += self.out.eq(self.a & self.b)
                with m.Default():
                    m.d.comb += self.out.eq(-1)
        with m.Else():
            m.d.comb += self.out.eq(-1)
        return m