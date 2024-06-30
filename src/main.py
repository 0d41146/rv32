from amaranth.sim import Simulator, Delay
import m_rf as m1

dut = m1.RF()

async def testbench(ctx):
    for i in range(10):
        ctx.set(dut.a3, i)
        ctx.set(dut.we3, i % 2)
        ctx.set(dut.wd3, i * 2 + 1)
        await ctx.tick()
    
    for i in range(10):
        ctx.set(dut.a1, i)
        ctx.set(dut.a2, i)
        rd1 = ctx.get(dut.rd1)
        rd2 = ctx.get(dut.rd2)
        assert rd1 == rd2

sim = Simulator(dut)
sim.add_testbench(testbench)
sim.add_clock(1e-6)
with sim.write_vcd("testbench.vcd"):
    sim.run_until(1e-6 * 15)