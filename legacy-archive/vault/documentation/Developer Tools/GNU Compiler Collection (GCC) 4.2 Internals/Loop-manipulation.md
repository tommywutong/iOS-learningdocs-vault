---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Loop-manipulation.html
archived_at: '2026-07-15T07:31:02.243891Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [LCSSA](LCSSA.md#apple-jrbvgu2b),
Previous: [Loop querying](Loop-querying.md#apple-jrxw64bnof2wk4tznfxgo),
Up: [Loop Analysis and Representation](Loop-Analysis-and-Representation.md#apple-jrxw64bnifxgc3dzonuxgllbnzsc2utfobzgk43fnz2gc5djn5xa)

---

### 11.3 Loop manipulation

The loops tree can be manipulated using the following functions:

- `flow_loop_tree_node_add`: Adds a node to the tree.
- `flow_loop_tree_node_remove`: Removes a node from the tree.
- `add_bb_to_loop`: Adds a basic block to a loop.
- `remove_bb_from_loops`: Removes a basic block from loops.

The specialized versions of several low-level CFG functions that also
update loop structures are provided:

- `loop_split_edge_with`: Splits an edge, and places a
  specified RTL code on it. On GIMPLE, the function can still be used,
  but the code must be NULL.
- `bsi_insert_on_edge_immediate_loop`: Inserts code on edge,
  splitting it if necessary. Only works on GIMPLE.
- `remove_path`: Removes an edge and all blocks it dominates.
- `loop_commit_inserts`: Commits insertions scheduled on edges,
  and sets loops for the new blocks. This function can only be used on
  GIMPLE.
- `split_loop_exit_edge`: Splits exit edge of the loop,
  ensuring that PHI node arguments remain in the loop (this ensures that
  loop-closed SSA form is preserved). Only useful on GIMPLE.

Finally, there are some higher-level loop transformations implemented.
While some of them are written so that they should work on non-innermost
loops, they are mostly untested in that case, and at the moment, they
are only reliable for the innermost loops:

- `create_iv`: Creates a new induction variable. Only works on
  GIMPLE. `standard_iv_increment_position` can be used to find a
  suitable place for the iv increment.
- `duplicate_loop_to_header_edge`,
  `tree_duplicate_loop_to_header_edge`: These functions (on RTL and
  on GIMPLE) duplicate the body of the loop prescribed number of times on
  one of the edges entering loop header, thus performing either loop
  unrolling or loop peeling. `can_duplicate_loop_p`
  (`can_unroll_loop_p` on GIMPLE) must be true for the duplicated
  loop.
- `loop_version`, `tree_ssa_loop_version`: These function
  create a copy of a loop, and a branch before them that selects one of
  them depending on the prescribed condition. This is useful for
  optimizations that need to verify some assumptions in runtime (one of
  the copies of the loop is usually left unchanged, while the other one is
  transformed in some way).
- `tree_unroll_loop`: Unrolls the loop, including peeling the
  extra iterations to make the number of iterations divisible by unroll
  factor, updating the exit condition, and removing the exits that now
  cannot be taken. Works only on GIMPLE.
