---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Loop-representation.html
archived_at: '2026-07-15T07:31:02.254154Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Loop querying](Loop-querying.md#apple-jrxw64bnof2wk4tznfxgo),
Up: [Loop Analysis and Representation](Loop-Analysis-and-Representation.md#apple-jrxw64bnifxgc3dzonuxgllbnzsc2utfobzgk43fnz2gc5djn5xa)

---

### 11.1 Loop representation

This chapter describes the representation of loops in GCC, and functions
that can be used to build, modify and analyze this representation. Most
of the interfaces and data structures are declared in `cfgloop.h`.
At the moment, loop structures are analyzed and this information is
updated only by the optimization passes that deal with loops, but some
efforts are being made to make it available throughout most of the
optimization passes.

In general, a natural loop has one entry block (header) and possibly
several back edges (latches) leading to the header from the inside of
the loop. Loops with several latches may appear if several loops share
a single header, or if there is a branching in the middle of the loop.
The representation of loops in GCC however allows only loops with a
single latch. During loop analysis, headers of such loops are split and
forwarder blocks are created in order to disambiguate their structures.
A heuristic based on profile information is used to determine whether
the latches correspond to sub-loops or to control flow in a single loop.
This means that the analysis sometimes changes the CFG, and if you run
it in the middle of an optimization pass, you must be able to deal with
the new blocks.

Body of the loop is the set of blocks that are dominated by its header,
and reachable from its latch against the direction of edges in CFG. The
loops are organized in a containment hierarchy (tree) such that all the
loops immediately contained inside loop L are the children of L in the
tree. This tree is represented by the `struct loops` structure.
The root of this tree is a fake loop that contains all blocks in the
function. Each of the loops is represented in a `struct loop`
structure. Each loop is assigned an index (`num` field of the
`struct loop` structure), and the pointer to the loop is stored in
the corresponding field of the `parray` field of the loops
structure. Index of a sub-loop is always greater than the index of its
super-loop. The indices do not have to be continuous, there may be
empty (`NULL`) entries in the `parray` created by deleting
loops. The index of a loop never changes. The first unused index is
stored in the `num` field of the loops structure.

Each basic block contains the reference to the innermost loop it belongs
to (`loop_father`). For this reason, it is only possible to have
one `struct loops` structure initialized at the same time for each
CFG. It is recommended to use the global variable `current_loops`
to contain the `struct loops` structure, especially if the loop
structures are updated throughout several passes. Many of the loop
manipulation functions assume that dominance information is up-to-date.

The loops are analyzed through `loop_optimizer_init` function. The
argument of this function is a set of flags represented in an integer
bitmask. These flags specify what other properties of the loop
structures should be calculated/enforced and preserved later:

- `LOOPS_HAVE_PREHEADERS`: Forwarder blocks are created in such
  a way that each loop has only one entry edge, and additionally, the
  source block of this entry edge has only one successor. This creates a
  natural place where the code can be moved out of the loop, and ensures
  that the entry edge of the loop leads from its immediate super-loop.
- `LOOPS_HAVE_SIMPLE_LATCHES`: Forwarder blocks are created to
  force the latch block of each loop to have only one successor. This
  ensures that the latch of the loop does not belong to any of its
  sub-loops, and makes manipulation with the loops significantly easier.
  Most of the loop manipulation functions assume that the loops are in
  this shape. Note that with this flag, the “normal” loop without any
  control flow inside and with one exit consists of two basic blocks.
- `LOOPS_HAVE_MARKED_IRREDUCIBLE_REGIONS`: Basic blocks and
  edges in the strongly connected components that are not natural loops
  (have more than one entry block) are marked with
  `BB_IRREDUCIBLE_LOOP` and `EDGE_IRREDUCIBLE_LOOP` flags. The
  flag is not set for blocks and edges that belong to natural loops that
  are in such an irreducible region (but it is set for the entry and exit
  edges of such a loop, if they lead to/from this region).
- `LOOPS_HAVE_MARKED_SINGLE_EXITS`: If a loop has exactly one
  exit edge, this edge is stored in `single_exit` field of the loop
  structure. `NULL` is stored there otherwise.

These properties may also be computed/enforced later, using functions
`create_preheaders`, `force_single_succ_latches`,
`mark_irreducible_loops` and `mark_single_exit_loops`.

The memory occupied by the loops structures should be freed with
`loop_optimizer_finalize` function.

The CFG manipulation functions in general do not update loop structures.
Specialized versions that additionally do so are provided for the most
common tasks. On GIMPLE, `cleanup_tree_cfg_loop` function can be
used to cleanup CFG while updating the loops structures if
`current_loops` is set.
