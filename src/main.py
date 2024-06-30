from amaranth.sim import Simulator, Delay
import m_ALU as m1

dut = m1.ALU()

async def testbench(ctx):
    for i in range (10):
        for j in range (10):
            ctx.set(dut.a, i)
            ctx.set(dut.b, j)
            ctx.set(dut.opcode, 0b0110011)
            ctx.set(dut.func3, 0b000)
            ctx.set(dut.func7, 0b0000000)
            o = ctx.get(dut.out)
            print(f"{i} + {j} = {o}")
            

sim = Simulator(dut)
sim.add_testbench(testbench)
with sim.write_vcd("testbench.vcd"):
    sim.run()