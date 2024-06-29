from amaranth import *
from amaranth.lib import wiring
from amaranth.lib.wiring import In, Out
from amaranth.cli import main
from amaranth.lib.memory import Memory

class imem(wiring.Component):
    def __init__(self):
        super().__init__({
            "addr": In(32),
            "inst": Out(32)
        })
        self.config = [0x00450693, #  0 addi a3, a0, 4 
                       0x00100713, #  4 addi a4, a0, 1
                       0x00b76463, #  8 bltu a4, a1, 10
                       0x00008067, #  c jalr a0, x1, 0
                       0x0006a803, # 10 lw   a6, 0(a3)
                       0x00068613, # 14 addi a2, a3, 0
                       0x00070793, # 18 addi a5, a4, 0
                       0xffc62883, # 1c lw   a7, -4(a2)
                       0x01185a63, # 20 bge  a6, a7, 34
                       0x01162023, # 24 sw   a7, 0(a2)
                       0xfff78793, # 28 addi a5, a5, -1
                       0xffc60613, # 2c addi a2, a2, -4
                       0xfe0796e3, # 30 bne  a5, x0, 1c
                       0x00279793, # 34 slli a5, a5, 0x2
                       0x00f507b3, # 38 add  a5, a0, a5
                       0x0107a023, # 3c sw   a6, 0(a5)
                       0x00170713, # 40 addi a4, a4, 1
                       0x00468693, # 44 addi a3, a3, 4
                       0xfc1ff06f] # 48 jal  x0, 8
    
    def elaborate(self, platform):
        m = Module()
        message = b"Hello world\n"
        m.submodules.memory = memory = \
            Memory(shape=unsigned(32), depth=1024, init=self.config)
        
        rd_port = memory.read_port(domain="comb")
        m.d.comb += rd_port.addr.eq(self.addr)
        m.d.comb += self.inst.eq(rd_port.data)
        return m