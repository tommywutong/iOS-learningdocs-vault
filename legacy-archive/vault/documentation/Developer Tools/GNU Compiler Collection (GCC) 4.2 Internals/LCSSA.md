---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/LCSSA.html
archived_at: '2026-07-15T07:31:02.174791Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Scalar evolutions](Scalar-evolutions.md#apple-knrwc3dboiwwk5tpnr2xi2lpnzzq),
Previous: [Loop manipulation](Loop-manipulation.md#apple-jrxw64bnnvqw42lqovwgc5djn5xa),
Up: [Loop Analysis and Representation](Loop-Analysis-and-Representation.md#apple-jrxw64bnifxgc3dzonuxgllbnzsc2utfobzgk43fnz2gc5djn5xa)

---

### 11.4 Loop-closed SSA form

Throughout the loop optimizations on tree level, one extra condition is
enforced on the SSA form: No SSA name is used outside of the loop in
that it is defined. The SSA form satisfying this condition is called
“loop-closed SSA form” – LCSSA. To enforce LCSSA, PHI nodes must be
created at the exits of the loops for the SSA names that are used
outside of them. Only the real operands (not virtual SSA names) are
held in LCSSA, in order to save memory.

There are various benefits of LCSSA:

- Many optimizations (value range analysis, final value
  replacement) are interested in the values that are defined in the loop
  and used outside of it, i.e., exactly those for that we create new PHI
  nodes.
- In induction variable analysis, it is not necessary to specify the
  loop in that the analysis should be performed – the scalar evolution
  analysis always returns the results with respect to the loop in that the
  SSA name is defined.
- It makes updating of SSA form during loop transformations simpler.
  Without LCSSA, operations like loop unrolling may force creation of PHI
  nodes arbitrarily far from the loop, while in LCSSA, the SSA form can be
  updated locally. However, since we only keep real operands in LCSSA, we
  cannot use this advantage (we could have local updating of real
  operands, but it is not much more efficient than to use generic SSA form
  updating for it as well; the amount of changes to SSA is the same).

However, it also means LCSSA must be updated. This is usually
straightforward, unless you create a new value in loop and use it
outside, or unless you manipulate loop exit edges (functions are
provided to make these manipulations simple).
`rewrite_into_loop_closed_ssa` is used to rewrite SSA form to
LCSSA, and `verify_loop_closed_ssa` to check that the invariant of
LCSSA is preserved.
