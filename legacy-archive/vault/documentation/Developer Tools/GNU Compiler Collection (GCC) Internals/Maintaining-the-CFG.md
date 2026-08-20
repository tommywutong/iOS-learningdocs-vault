---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Maintaining-the-CFG.html
archived_at: '2026-07-15T07:31:00.345316Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Liveness information](Liveness-information.md#apple-jruxmzlomvzxglljnztg64tnmf2gs33o),
Previous: [Profile information](Profile-information.md#apple-kbzg6ztjnrss22lomzxxe3lboruw63q),
Up: [Control Flow](Control-Flow.md#apple-inxw45dsn5wc2rtmn53q)

---

### 11.4 Maintaining the CFG

An important task of each compiler pass is to keep both the control
flow graph and all profile information up-to-date. Reconstruction of
the control flow graph after each pass is not an option, since it may be
very expensive and lost profile information cannot be reconstructed at
all.

GCC has two major intermediate representations, and both use the
`basic_block` and `edge` data types to represent control
flow. Both representations share as much of the CFG maintenance code
as possible. For each representation, a set of hooks is defined
so that each representation can provide its own implementation of CFG
manipulation routines when necessary. These hooks are defined in
`cfghooks.h`. There are hooks for almost all common CFG
manipulations, including block splitting and merging, edge redirection
and creating and deleting basic blocks. These hooks should provide
everything you need to maintain and manipulate the CFG in both the RTL
and `tree` representation.

At the moment, the basic block boundaries are maintained transparently
when modifying instructions, so there rarely is a need to move them
manually (such as in case someone wants to output instruction outside
basic block explicitly).
Often the CFG may be better viewed as integral part of instruction
chain, than structure built on the top of it. However, in principle
the control flow graph for the `tree` representation is
_not_ an integral part of the representation, in that a function
tree may be expanded without first building a flow graph for the
`tree` representation at all. This happens when compiling
without any `tree` optimization enabled. When the `tree`
optimizations are enabled and the instruction stream is rewritten in
SSA form, the CFG is very tightly coupled with the instruction stream.
In particular, statement insertion and removal has to be done with
care. In fact, the whole `tree` representation can not be easily
used or maintained without proper maintenance of the CFG
simultaneously.

In the RTL representation, each instruction has a
`BLOCK_FOR_INSN` value that represents pointer to the basic block
that contains the instruction. In the `tree` representation, the
function `bb_for_stmt` returns a pointer to the basic block
containing the queried statement.

When changes need to be applied to a function in its `tree`
representation, block statement iterators should be used. These
iterators provide an integrated abstraction of the flow graph and the
instruction stream. Block statement iterators iterators are
constructed using the `block_stmt_iterator` data structure and
several modifier are available, including the following:

**`bsi_start`**
: This function initializes a `block_stmt_iterator` that points to
the first non-empty statement in a basic block.

**`bsi_last`**
: This function initializes a `block_stmt_iterator` that points to
the last statement in a basic block.

**`bsi_end_p`**
: This predicate is `true` if a `block_stmt_iterator`
represents the end of a basic block.

**`bsi_next`**
: This function takes a `block_stmt_iterator` and makes it point to
its successor.

**`bsi_prev`**
: This function takes a `block_stmt_iterator` and makes it point to
its predecessor.

**`bsi_insert_after`**
: This function inserts a statement after the `block_stmt_iterator`
passed in. The final parameter determines whether the statement
iterator is updated to point to the newly inserted statement, or left
pointing to the original statement.

**`bsi_insert_before`**
: This function inserts a statement before the `block_stmt_iterator`
passed in. The final parameter determines whether the statement
iterator is updated to point to the newly inserted statement, or left
pointing to the original statement.

**`bsi_remove`**
: This function removes the `block_stmt_iterator` passed in and
rechains the remaining statements in a basic block, if any.

In the RTL representation, the macros `BB_HEAD` and `BB_END`
may be used to get the head and end `rtx` of a basic block. No
abstract iterators are defined for traversing the insn chain, but you
can just use `NEXT_INSN` and `PREV_INSN` instead. See
See [Insns](Insns.md#apple-jfxhg3tt).

Usually a code manipulating pass simplifies the instruction stream and
the flow of control, possibly eliminating some edges. This may for
example happen when a conditional jump is replaced with an
unconditional jump, but also when simplifying possibly trapping
instruction to non-trapping while compiling Java. Updating of edges
is not transparent and each optimization pass is required to do so
manually. However only few cases occur in practice. The pass may
call `purge_dead_edges` on a given basic block to remove
superfluous edges, if any.

Another common scenario is redirection of branch instructions, but
this is best modeled as redirection of edges in the control flow graph
and thus use of `redirect_edge_and_branch` is preferred over more
low level functions, such as `redirect_jump` that operate on RTL
chain only. The CFG hooks defined in `cfghooks.h` should provide
the complete API required for manipulating and maintaining the CFG.

It is also possible that a pass has to insert control flow instruction
into the middle of a basic block, thus creating an entry point in the
middle of the basic block, which is impossible by definition: The
block must be split to make sure it only has one entry point, i.e. the
head of the basic block. In the RTL representation, the
`find_sub_basic_blocks` may be used to split existing basic block
and add necessary edges. The CFG hook `split_block` may be used
when an instruction in the middle of a basic block has to become the
target of a jump or branch instruction.

For a global optimizer, a common operation is to split edges in the
flow graph and insert instructions on them. In the RTL
representation, this can be easily done using the
`insert_insn_on_edge` function that emits an instruction
“on the edge”, caching it for a later `commit_edge_insertions`
call that will take care of moving the inserted instructions off the
edge into the instruction stream contained in a basic block. This
includes the creation of new basic blocks where needed. In the
`tree` representation, the equivalent functions are
`bsi_insert_on_edge` which inserts a block statement
iterator on an edge, and `bsi_commit_edge_inserts` which flushes
the instruction to actual instruction stream.

While debugging the optimization pass, an `verify_flow_info`
function may be useful to find bugs in the control flow graph updating
code.

Note that at present, the representation of control flow in the
`tree` representation is discarded before expanding to RTL.
Long term the CFG should be maintained and “expanded” to the
RTL representation along with the function `tree` itself.
