from amaranth.sim import Simulator
import m_pc as pc

dut = pc.ProgramCounter()
sim = Simulator(dut)
sim.add_clock(1e-6)
with sim.write_vcd("pc.vcd"):
    sim.run_until(1e-6 * 15)