from amaranth import*
from amaranth.sim import*

class ProgramCounter(Elaboratable):
    def __init__(self):
        self.PC = Signal(32)
    
    def elaborate(self, platform):
        m = Module()
        with m.If(ClockSignal()):
            m.d.sync += self.PC.eq(self.PC + 4)
        return m