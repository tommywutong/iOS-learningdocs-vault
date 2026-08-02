---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/RTL-passes.html
archived_at: '2026-07-15T07:31:00.593843Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [Tree-SSA passes](Tree_002dSSA-passes.md#apple-krzgkzk7gaydezctknas24dbonzwk4y),
Up: [Passes](Passes.md#apple-kbqxg43fom)

---

### 7.5 RTL passes

The following briefly describes the rtl generation and optimization
passes that are run after tree optimization.

- RTL generation

  The source files for RTL generation include
  `stmt.c`,
  `calls.c`,
  `expr.c`,
  `explow.c`,
  `expmed.c`,
  `function.c`,
  `optabs.c`
  and `emit-rtl.c`.
  Also, the file
  `insn-emit.c`, generated from the machine description by the
  program `genemit`, is used in this pass. The header file
  `expr.h` is used for communication within this pass.

  The header files `insn-flags.h` and `insn-codes.h`,
  generated from the machine description by the programs `genflags`
  and `gencodes`, tell this pass which standard names are available
  for use and which patterns correspond to them.
- Generate exception handling landing pads

  This pass generates the glue that handles communication between the
  exception handling library routines and the exception handlers within
  the function. Entry points in the function that are invoked by the
  exception handling library are called landing pads. The code
  for this pass is located within `except.c`.
- Cleanup control flow graph

  This pass removes unreachable code, simplifies jumps to next, jumps to
  jump, jumps across jumps, etc. The pass is run multiple times.
  For historical reasons, it is occasionally referred to as the “jump
  optimization pass”. The bulk of the code for this pass is in
  `cfgcleanup.c`, and there are support routines in `cfgrtl.c`
  and `jump.c`.
- Common subexpression elimination

  This pass removes redundant computation within basic blocks, and
  optimizes addressing modes based on cost. The pass is run twice.
  The source is located in `cse.c`.
- Global common subexpression elimination.

  This pass performs two
  different types of GCSE depending on whether you are optimizing for
  size or not (LCM based GCSE tends to increase code size for a gain in
  speed, while Morel-Renvoise based GCSE does not).
  When optimizing for size, GCSE is done using Morel-Renvoise Partial
  Redundancy Elimination, with the exception that it does not try to move
  invariants out of loops—that is left to the loop optimization pass.
  If MR PRE GCSE is done, code hoisting (aka unification) is also done, as
  well as load motion.
  If you are optimizing for speed, LCM (lazy code motion) based GCSE is
  done. LCM is based on the work of Knoop, Ruthing, and Steffen. LCM
  based GCSE also does loop invariant code motion. We also perform load
  and store motion when optimizing for speed.
  Regardless of which type of GCSE is used, the GCSE pass also performs
  global constant and copy propagation.
  The source file for this pass is `gcse.c`, and the LCM routines
  are in `lcm.c`.
- Loop optimization

  This pass moves constant expressions out of loops, and optionally does
  strength-reduction as well. The pass is located in `loop.c`.
  Loop dependency analysis routines are contained in `dependence.c`.
  This pass is seriously out-of-date and is supposed to be replaced by
  a new one described below in near future.

  A second loop optimization pass takes care of basic block level
  optimizations—unrolling, peeling and unswitching loops. The source
  files are `cfgloopanal.c` and `cfgloopmanip.c` containing
  generic loop analysis and manipulation code, `loop-init.c` with
  initialization and finalization code, `loop-unswitch.c` for loop
  unswitching and `loop-unroll.c` for loop unrolling and peeling.
  It also contains a separate loop invariant motion pass implemented in
  `loop-invariant.c`.
- Jump bypassing

  This pass is an aggressive form of GCSE that transforms the control
  flow graph of a function by propagating constants into conditional
  branch instructions. The source file for this pass is `gcse.c`.
- If conversion

  This pass attempts to replace conditional branches and surrounding
  assignments with arithmetic, boolean value producing comparison
  instructions, and conditional move instructions. In the very last
  invocation after reload, it will generate predicated instructions
  when supported by the target. The pass is located in `ifcvt.c`.
- Web construction

  This pass splits independent uses of each pseudo-register. This can
  improve effect of the other transformation, such as CSE or register
  allocation. Its source files are `web.c`.
- Life analysis

  This pass computes which pseudo-registers are live at each point in
  the program, and makes the first instruction that uses a value point
  at the instruction that computed the value. It then deletes
  computations whose results are never used, and combines memory
  references with add or subtract instructions to make autoincrement or
  autodecrement addressing. The pass is located in `flow.c`.
- Instruction combination

  This pass attempts to combine groups of two or three instructions that
  are related by data flow into single instructions. It combines the
  RTL expressions for the instructions by substitution, simplifies the
  result using algebra, and then attempts to match the result against
  the machine description. The pass is located in `combine.c`.
- Register movement

  This pass looks for cases where matching constraints would force an
  instruction to need a reload, and this reload would be a
  register-to-register move. It then attempts to change the registers
  used by the instruction to avoid the move instruction.
  The pass is located in `regmove.c`.
- Optimize mode switching

  This pass looks for instructions that require the processor to be in a
  specific “mode” and minimizes the number of mode changes required to
  satisfy all users. What these modes are, and what they apply to are
  completely target-specific. The source is located in `lcm.c`.

- Modulo scheduling

  This pass looks at innermost loops and reorders their instructions
  by overlapping different iterations. Modulo scheduling is performed
  immediately before instruction scheduling.
  The pass is located in (`modulo-sched.c`).
- Instruction scheduling

  This pass looks for instructions whose output will not be available by
  the time that it is used in subsequent instructions. Memory loads and
  floating point instructions often have this behavior on RISC machines.
  It re-orders instructions within a basic block to try to separate the
  definition and use of items that otherwise would cause pipeline
  stalls. This pass is performed twice, before and after register
  allocation. The pass is located in `haifa-sched.c`,
  `sched-deps.c`, `sched-ebb.c`, `sched-rgn.c` and
  `sched-vis.c`.
- Register allocation

  These passes make sure that all occurrences of pseudo registers are
  eliminated, either by allocating them to a hard register, replacing
  them by an equivalent expression (e.g. a constant) or by placing
  them on the stack. This is done in several subpasses:

  - Register class preferencing. The RTL code is scanned to find out
    which register class is best for each pseudo register. The source
    file is `regclass.c`.
  - Local register allocation. This pass allocates hard registers to
    pseudo registers that are used only within one basic block. Because
    the basic block is linear, it can use fast and powerful techniques to
    do a decent job. The source is located in `local-alloc.c`.
  - Global register allocation. This pass allocates hard registers for
    the remaining pseudo registers (those whose life spans are not
    contained in one basic block). The pass is located in `global.c`.

  - Reloading. This pass renumbers pseudo registers with the hardware
    registers numbers they were allocated. Pseudo registers that did not
    get hard registers are replaced with stack slots. Then it finds
    instructions that are invalid because a value has failed to end up in
    a register, or has ended up in a register of the wrong kind. It fixes
    up these instructions by reloading the problematical values
    temporarily into registers. Additional instructions are generated to
    do the copying.

    The reload pass also optionally eliminates the frame pointer and inserts
    instructions to save and restore call-clobbered registers around calls.

    Source files are `reload.c` and `reload1.c`, plus the header
    `reload.h` used for communication between them.
- Basic block reordering

  This pass implements profile guided code positioning. If profile
  information is not available, various types of static analysis are
  performed to make the predictions normally coming from the profile
  feedback (IE execution frequency, branch probability, etc). It is
  implemented in the file `bb-reorder.c`, and the various
  prediction routines are in `predict.c`.
- Variable tracking

  This pass computes where the variables are stored at each
  position in code and generates notes describing the variable locations
  to RTL code. The location lists are then generated according to these
  notes to debug information if the debugging information format supports
  location lists.
- Delayed branch scheduling

  This optional pass attempts to find instructions that can go into the
  delay slots of other instructions, usually jumps and calls. The
  source file name is `reorg.c`.
- Branch shortening

  On many RISC machines, branch instructions have a limited range.
  Thus, longer sequences of instructions must be used for long branches.
  In this pass, the compiler figures out what how far each instruction
  will be from each other instruction, and therefore whether the usual
  instructions, or the longer sequences, must be used for each branch.
- Register-to-stack conversion

  Conversion from usage of some hard registers to usage of a register
  stack may be done at this point. Currently, this is supported only
  for the floating-point registers of the Intel 80387 coprocessor. The
  source file name is `reg-stack.c`.
- Final

  This pass outputs the assembler code for the function. The source files
  are `final.c` plus `insn-output.c`; the latter is generated
  automatically from the machine description by the tool `genoutput`.
  The header file `conditions.h` is used for communication between
  these files. If mudflap is enabled, the queue of deferred declarations
  and any addressed constants (e.g., string literals) is processed by
  `mudflap_finish_file` into a synthetic constructor function
  containing calls into the mudflap runtime.
- Debugging information output

  This is run after final because it must output the stack slot offsets
  for pseudo registers that did not get hard registers. Source files
  are `dbxout.c` for DBX symbol table format, `sdbout.c` for
  SDB symbol table format, `dwarfout.c` for DWARF symbol table
  format, files `dwarf2out.c` and `dwarf2asm.c` for DWARF2
  symbol table format, and `vmsdbgout.c` for VMS debug symbol table
  format.
