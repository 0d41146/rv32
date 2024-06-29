from amaranth.sim import Simulator, Delay
import m_imem as m1

dut = m1.imem()

async def testbench(ctx):
    for i in range (10):
        ctx.set(dut.addr, i)
        data = ctx.get(dut.inst)
        print(f"addr: {i}, data: 0x{data:x}")

sim = Simulator(dut)
sim.add_testbench(testbench)
with sim.write_vcd("testbench.vcd"):
    sim.run()