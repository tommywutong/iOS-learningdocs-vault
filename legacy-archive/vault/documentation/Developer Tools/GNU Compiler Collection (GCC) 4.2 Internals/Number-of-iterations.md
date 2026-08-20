---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Number-of-iterations.html
archived_at: '2026-07-15T07:31:02.431335Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Dependency analysis](Dependency-analysis.md#apple-irsxazlomrsw4y3zfvqw4ylmpfzws4y),
Previous: [loop-iv](loop_002div.md#apple-nrxw64c7gaydezdjoy),
Up: [Loop Analysis and Representation](Loop-Analysis-and-Representation.md#apple-jrxw64bnifxgc3dzonuxgllbnzsc2utfobzgk43fnz2gc5djn5xa)

---

### 11.7 Number of iterations analysis

Both on GIMPLE and on RTL, there are functions available to determine
the number of iterations of a loop, with a similar interface. In many
cases, it is not possible to determine number of iterations
unconditionally – the determined number is correct only if some
assumptions are satisfied. The analysis tries to verify these
conditions using the information contained in the program; if it fails,
the conditions are returned together with the result. The following
information and conditions are provided by the analysis:

- `assumptions`: If this condition is false, the rest of
  the information is invalid.
- `noloop_assumptions` on RTL, `may_be_zero` on GIMPLE: If
  this condition is true, the loop exits in the first iteration.
- `infinite`: If this condition is true, the loop is infinite.
  This condition is only available on RTL. On GIMPLE, conditions for
  finiteness of the loop are included in `assumptions`.
- `niter_expr` on RTL, `niter` on GIMPLE: The expression
  that gives number of iterations. The number of iterations is defined as
  the number of executions of the loop latch.

Both on GIMPLE and on RTL, it necessary for the induction variable
analysis framework to be initialized (SCEV on GIMPLE, loop-iv on RTL).
On GIMPLE, the results are stored to `struct tree_niter_desc`
structure. Number of iterations before the loop is exited through a
given exit can be determined using `number_of_iterations_exit`
function. On RTL, the results are returned in `struct niter_desc`
structure. The corresponding function is named
`check_simple_exit`. There are also functions that pass through
all the exits of a loop and try to find one with easy to determine
number of iterations – `find_loop_niter` on GIMPLE and
`find_simple_exit` on RTL. Finally, there are functions that
provide the same information, but additionally cache it, so that
repeated calls to number of iterations are not so costly –
`number_of_iterations_in_loop` on GIMPLE and
`get_simple_loop_desc` on RTL.

Note that some of these functions may behave slightly differently than
others – some of them return only the expression for the number of
iterations, and fail if there are some assumptions. The function
`number_of_iterations_in_loop` works only for single-exit loops,
and it returns the value for number of iterations higher by one with
respect to all other functions (i.e., it returns number of executions of
the exit statement, not of the loop latch).
