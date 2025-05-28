from amaranth import *
from amaranth.lib import wiring
from amaranth.lib.wiring import In, Out
from amaranth.sim import Simulator, Period
from amaranth.back import verilog

###############
# Main module #
###############
class template(wiring.Component):
    """
    A 16-bit up counter with a fixed limit.

    Parameters
    ----------
    limit : int
        The value at which the counter overflows.

    Attributes
    ----------
    en : Signal, in
        The counter is incremented if ``en`` is asserted, and retains
        its value otherwise.
    ovf : Signal, out
        ``ovf`` is asserted when the counter reaches its limit.
    """

    en: In(1)
    ovf: Out(1)

    def __init__(self, limit):
        self.limit = limit
        self.count = Signal(16, name="count") # Added name for clarity in traces/formal

        super().__init__()

    def elaborate(self, platform):
        m = Module()

        m.d.comb += self.ovf.eq(self.count == self.limit)

        with m.If(self.en):
            with m.If(self.ovf):
                m.d.sync += self.count.eq(0)
            with m.Else():
                m.d.sync += self.count.eq(self.count + 1)

        return m
# --- TEST ---
dut = template(25)
async def bench(ctx):
    # Disabled counter should not overflow.
    ctx.set(dut.en, 0)
    for _ in range(30):
        await ctx.tick()
        assert not ctx.get(dut.ovf)

    # Once enabled, the counter should overflow in 25 cycles.
    ctx.set(dut.en, 1)
    for _ in range(24):
        await ctx.tick()
        assert not ctx.get(dut.ovf)
    await ctx.tick()
    assert ctx.get(dut.ovf)

    # The overflow should clear in one cycle.
    await ctx.tick()
    assert not ctx.get(dut.ovf)

##############
# Simulation #
##############
sim = Simulator(dut)
sim.add_clock(Period(MHz=1))
sim.add_testbench(bench)
with sim.write_vcd("template.vcd"):
    sim.run()
# --- CONVERT ---
top = template(25)
with open("template.v", "w") as f:
    f.write(verilog.convert(top))

#######################
# Formal Verification #
#######################
from amaranth.asserts import Assert, Assume, Cover # These might still be here (deprecated but present)
from amaranth.hdl import Past, Rose, Fell, Stable # Past, Rose, Fell, Stable are now in amaranth.hdl
from amaranth.cli import main_parser, main_runner

if __name__ == "__main__":
    parser = main_parser()
    args = parser.parse_args()

    m = Module()
    m.submodules.counter = counter = template(limit=25)

    # --- Formal Properties ---

    # Assert: Define properties that must *always* be true.

    # 1. If enable is low, count does not change.
    # This assertion ensures that if 'en' was low in the previous cycle, 'count' remains unchanged.
    # If 'en' just rose, the counter starts counting from the next cycle, so this doesn't apply.
    m.d.sync += Assert((counter.count == Past(counter.count, 1)) | (counter.en & ~Past(counter.en, 1)))


    # 2. If enable is high AND not overflow, count increments.
    m.d.sync += Assert(
        (counter.en & ~counter.ovf).implies(counter.count == Past(counter.count, 1) + 1)
    )

    # 3. If enable is high AND overflow, count resets to 0.
    m.d.sync += Assert(
        (counter.en & counter.ovf).implies(counter.count == 0)
    )

    # 4. Overflow is asserted only when count reaches limit.
    m.d.comb += Assert(counter.ovf.implies(counter.count == counter.limit))


    # Cover: Define scenarios you want to see covered by the formal tool.

    # 1. Cover the counter reaching its limit (ovf going high).
    m.d.sync += Cover(counter.ovf & ~Past(counter.ovf, 1)) # Explicit Rose definition

    # 2. Cover the counter incrementing.
    m.d.sync += Cover(counter.count == Past(counter.count, 1) + 1) # More explicit than Rose(counter.count)

    # 3. Cover the counter resetting after overflow.
    # ovf goes high AND count goes low (due to reset).
    m.d.sync += Cover((counter.ovf & ~Past(counter.ovf, 1)) & (counter.count == 0)) # Explicit Rose and Fell

    # 4. Cover the counter being enabled and NOT overflowing yet.
    m.d.sync += Cover(counter.en & ~counter.ovf)

    # Pass the module and its ports to the main runner.
    main_runner(parser, args, m, ports=[] + counter.ports())