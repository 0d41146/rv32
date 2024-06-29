from amaranth import*
from amaranth.lib import wiring
from amaranth.lib.wiring import In, Out
from amaranth.cli import main

class pc(wiring.Component):
    def __init__(self):
        super().__init__({
            "addr": Out(32)
        })

    def elaborate(self, platform):
        m = Module()
        with m.If(ClockSignal()):
            m.d.sync += self.addr.eq(self.addr + 4)
        return m

if __name__ == "__main__":
    pc = pc()
    main(pc)