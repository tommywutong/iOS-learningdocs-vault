---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Loop-querying.html
archived_at: '2026-07-15T07:31:02.248954Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Loop manipulation](Loop-manipulation.md#apple-jrxw64bnnvqw42lqovwgc5djn5xa),
Previous: [Loop representation](Loop-representation.md#apple-jrxw64bnojsxa4tfonsw45dboruw63q),
Up: [Loop Analysis and Representation](Loop-Analysis-and-Representation.md#apple-jrxw64bnifxgc3dzonuxgllbnzsc2utfobzgk43fnz2gc5djn5xa)

---

### 11.2 Loop querying

The functions to query the information about loops are declared in
`cfgloop.h`. Some of the information can be taken directly from
the structures. `loop_father` field of each basic block contains
the innermost loop to that the block belongs. The most useful fields of
loop structure (that are kept up-to-date at all times) are:

- `header`, `latch`: Header and latch basic blocks of the
  loop.
- `num_nodes`: Number of basic blocks in the loop (including
  the basic blocks of the sub-loops).
- `depth`: The depth of the loop in the loops tree, i.e., the
  number of super-loops of the loop.
- `outer`, `inner`, `next`: The super-loop, the first
  sub-loop, and the sibling of the loop in the loops tree.
- `single_exit`: The exit edge of the loop, if the loop has
  exactly one exit and the loops were analyzed with
  LOOPS_HAVE_MARKED_SINGLE_EXITS.

There are other fields in the loop structures, many of them used only by
some of the passes, or not updated during CFG changes; in general, they
should not be accessed directly.

The most important functions to query loop structures are:

- `flow_loops_dump`: Dumps the information about loops to a
  file.
- `verify_loop_structure`: Checks consistency of the loop
  structures.
- `loop_latch_edge`: Returns the latch edge of a loop.
- `loop_preheader_edge`: If loops have preheaders, returns
  the preheader edge of a loop.
- `flow_loop_nested_p`: Tests whether loop is a sub-loop of
  another loop.
- `flow_bb_inside_loop_p`: Tests whether a basic block belongs
  to a loop (including its sub-loops).
- `find_common_loop`: Finds the common super-loop of two loops.
- `superloop_at_depth`: Returns the super-loop of a loop with
  the given depth.
- `tree_num_loop_insns`, `num_loop_insns`: Estimates the
  number of insns in the loop, on GIMPLE and on RTL.
- `loop_exit_edge_p`: Tests whether edge is an exit from a
  loop.
- `mark_loop_exit_edges`: Marks all exit edges of all loops
  with `EDGE_LOOP_EXIT` flag.
- `get_loop_body`, `get_loop_body_in_dom_order`,
  `get_loop_body_in_bfs_order`: Enumerates the basic blocks in the
  loop in depth-first search order in reversed CFG, ordered by dominance
  relation, and breath-first search order, respectively.
- `get_loop_exit_edges`: Enumerates the exit edges of a loop.
- `just_once_each_iteration_p`: Returns true if the basic block
  is executed exactly once during each iteration of a loop (that is, it
  does not belong to a sub-loop, and it dominates the latch of the loop).
