---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Liveness-information.html
archived_at: '2026-07-15T07:31:02.228301Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [Maintaining the CFG](Maintaining-the-CFG.md#apple-jvqws3tumfuw42lom4wxi2dffvbumry),
Up: [Control Flow](Control-Flow.md#apple-inxw45dsn5wc2rtmn53q)

---

### 13.5 Liveness information

Liveness information is useful to determine whether some register is
“live” at given point of program, i.e. that it contains a value that
may be used at a later point in the program. This information is
used, for instance, during register allocation, as the pseudo
registers only need to be assigned to a unique hard register or to a
stack slot if they are live. The hard registers and stack slots may
be freely reused for other values when a register is dead.

The liveness information is stored partly in the RTL instruction
stream and partly in the flow graph. Local information is stored in
the instruction stream:
Each instruction may contain `REG_DEAD` notes representing that
the value of a given register is no longer needed, or
`REG_UNUSED` notes representing that the value computed by the
instruction is never used. The second is useful for instructions
computing multiple values at once.

Global liveness information is stored in the control flow graph.
Each basic block contains two bitmaps, `global_live_at_start` and
`global_live_at_end` representing liveness of each register at
the entry and exit of the basic block. The file `flow.c`
contains functions to compute liveness of each register at any given
place in the instruction stream using this information.

Liveness is expensive to compute and thus it is desirable to keep it
up to date during code modifying passes. This can be easily
accomplished using the `flags` field of a basic block. Functions
modifying the instruction stream automatically set the `BB_DIRTY`
flag of a modifies basic block, so the pass may simply
use`clear_bb_flags` before doing any modifications and then ask
the data flow module to have liveness updated via the
`update_life_info_in_dirty_blocks` function.

This scheme works reliably as long as no control flow graph
transformations are done. The task of updating liveness after control
flow graph changes is more difficult as normal iterative data flow
analysis may produce invalid results or get into an infinite cycle
when the initial solution is not below the desired one. Only simple
transformations, like splitting basic blocks or inserting on edges,
are safe, as functions to implement them already know how to update
liveness information locally.
