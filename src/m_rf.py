from amaranth import*
from amaranth.lib import wiring
from amaranth.lib.memory import Memory
from amaranth.lib.wiring import In, Out

class RF(wiring.Component):
    def __init__(self):
        super().__init__({
            "a1": In(5),
            "a2": In(5),
            "a3": In(5),
            "rd1": Out(32),
            "rd2": Out(32),
            "wd3": In(32),
            "we3": In(1),
        })
    
    def elaborate(self, platform):
        m = Module()
        m.submodules.memory = memory = \
            Memory(shape=unsigned(32), depth=32, init=[])
        
        wr_port = memory.write_port()
        m.d.comb += wr_port.en.eq(self.we3)
        m.d.comb += wr_port.addr.eq(self.a3)
        m.d.comb += wr_port.data.eq(self.wd3)

        rd_port1 = memory.read_port(domain="comb")
        m.d.comb += rd_port1.addr.eq(self.a1)
        m.d.comb += self.rd1.eq(rd_port1.data)

        rd_port2 = memory.read_port(domain="comb")
        m.d.comb += rd_port2.addr.eq(self.a2)
        m.d.comb += self.rd2.eq(rd_port2.data)

        return m