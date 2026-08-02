---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Tree_002dSSA-passes.html
archived_at: '2026-07-15T07:31:00.944010Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [RTL passes](RTL-passes.md#apple-kjkeyllqmfzxgzlt),
Previous: [Pass manager](Pass-manager.md#apple-kbqxg4znnvqw4ylhmvza),
Up: [Passes](Passes.md#apple-kbqxg43fom)

---

### 7.4 Tree-SSA passes

The following briefly describes the tree optimization passes that are
run after gimplification and what source files they are located in.

- Remove useless statements

  This pass is an extremely simple sweep across the gimple code in which
  we identify obviously dead code and remove it. Here we do things like
  simplify `if` statements with constant conditions, remove
  exception handling constructs surrounding code that obviously cannot
  throw, remove lexical bindings that contain no variables, and other
  assorted simplistic cleanups. The idea is to get rid of the obvious
  stuff quickly rather than wait until later when it's more work to get
  rid of it. This pass is located in `tree-cfg.c` and described by
  `pass_remove_useless_stmts`.
- Mudflap declaration registration

  If mudflap (see [-fmudflap -fmudflapth -fmudflapir](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gcc/Optimize-Options.html#Optimize-Options)) is
  enabled, we generate code to register some variable declarations with
  the mudflap runtime. Specifically, the runtime tracks the lifetimes of
  those variable declarations that have their addresses taken, or whose
  bounds are unknown at compile time (`extern`). This pass generates
  new exception handling constructs (`try`/`finally`), and so
  must run before those are lowered. In addition, the pass enqueues
  declarations of static variables whose lifetimes extend to the entire
  program. The pass is located in `tree-mudflap.c` and is described
  by `pass_mudflap_1`.
- Lower control flow

  This pass flattens `if` statements (`COND_EXPR`) and
  and moves lexical bindings (`BIND_EXPR`) out of line. After
  this pass, all `if` statements will have exactly two `goto`
  statements in its `then` and `else` arms. Lexical binding
  information for each statement will be found in `TREE_BLOCK` rather
  than being inferred from its position under a `BIND_EXPR`. This
  pass is found in `gimple-low.c` and is described by
  `pass_lower_cf`.
- Lower exception handling control flow

  This pass decomposes high-level exception handling constructs
  (`TRY_FINALLY_EXPR` and `TRY_CATCH_EXPR`) into a form
  that explicitly represents the control flow involved. After this
  pass, `lookup_stmt_eh_region` will return a non-negative
  number for any statement that may have EH control flow semantics;
  examine `tree_can_throw_internal` or `tree_can_throw_external`
  for exact semantics. Exact control flow may be extracted from
  `foreach_reachable_handler`. The EH region nesting tree is defined
  in `except.h` and built in `except.c`. The lowering pass
  itself is in `tree-eh.c` and is described by `pass_lower_eh`.
- Build the control flow graph

  This pass decomposes a function into basic blocks and creates all of
  the edges that connect them. It is located in `tree-cfg.c` and
  is described by `pass_build_cfg`.
- Find all referenced variables

  This pass walks the entire function and collects an array of all
  variables referenced in the function, `referenced_vars`. The
  index at which a variable is found in the array is used as a UID
  for the variable within this function. This data is needed by the
  SSA rewriting routines. The pass is located in `tree-dfa.c`
  and is described by `pass_referenced_vars`.
- Enter static single assignment form

  This pass rewrites the function such that it is in SSA form. After
  this pass, all `is_gimple_reg` variables will be referenced by
  `SSA_NAME`, and all occurrences of other variables will be
  annotated with `VDEFS` and `VUSES`; phi nodes will have
  been inserted as necessary for each basic block. This pass is
  located in `tree-ssa.c` and is described by `pass_build_ssa`.
- Warn for uninitialized variables

  This pass scans the function for uses of `SSA_NAME`s that
  are fed by default definition. For non-parameter variables, such
  uses are uninitialized. The pass is run twice, before and after
  optimization. In the first pass we only warn for uses that are
  positively uninitialized; in the second pass we warn for uses that
  are possibly uninitialized. The pass is located in `tree-ssa.c`
  and is defined by `pass_early_warn_uninitialized` and
  `pass_late_warn_uninitialized`.
- Dead code elimination

  This pass scans the function for statements without side effects whose
  result is unused. It does not do memory life analysis, so any value
  that is stored in memory is considered used. The pass is run multiple
  times throughout the optimization process. It is located in
  `tree-ssa-dce.c` and is described by `pass_dce`.
- Dominator optimizations

  This pass performs trivial dominator-based copy and constant propagation,
  expression simplification, and jump threading. It is run multiple times
  throughout the optimization process. It it located in `tree-ssa-dom.c`
  and is described by `pass_dominator`.
- Redundant phi elimination

  This pass removes phi nodes for which all of the arguments are the same
  value, excluding feedback. Such degenerate forms are typically created
  by removing unreachable code. The pass is run multiple times throughout
  the optimization process. It is located in `tree-ssa.c` and is
  described by `pass_redundant_phi`.o
- Forward propagation of single-use variables

  This pass attempts to remove redundant computation by substituting
  variables that are used once into the expression that uses them and
  seeing if the result can be simplified. It is located in
  `tree-ssa-forwprop.c` and is described by `pass_forwprop`.
- Copy Renaming

  This pass attempts to change the name of compiler temporaries involved in
  copy operations such that SSA->normal can coalesce the copy away. When compiler
  temporaries are copies of user variables, it also renames the compiler
  temporary to the user variable resulting in better use of user symbols. It is
  located in `tree-ssa-copyrename.c` and is described by
  `pass_copyrename`.
- PHI node optimizations

  This pass recognizes forms of phi inputs that can be represented as
  conditional expressions and rewrites them into straight line code.
  It is located in `tree-ssa-phiopt.c` and is described by
  `pass_phiopt`.
- May-alias optimization

  This pass performs a flow sensitive SSA-based points-to analysis.
  The resulting may-alias, must-alias, and escape analysis information
  is used to promote variables from in-memory addressable objects to
  non-aliased variables that can be renamed into SSA form. We also
  update the `VDEF`/`VUSE` memory tags for non-renamable
  aggregates so that we get fewer false kills. The pass is located
  in `tree-ssa-alias.c` and is described by `pass_may_alias`.
- Profiling

  This pass rewrites the function in order to collect runtime block
  and value profiling data. Such data may be fed back into the compiler
  on a subsequent run so as to allow optimization based on expected
  execution frequencies. The pass is located in `predict.c` and
  is described by `pass_profile`.
- Lower complex arithmetic

  This pass rewrites complex arithmetic operations into their component
  scalar arithmetic operations. The pass is located in `tree-complex.c`
  and is described by `pass_lower_complex`.
- Scalar replacement of aggregates

  This pass rewrites suitable non-aliased local aggregate variables into
  a set of scalar variables. The resulting scalar variables are
  rewritten into SSA form, which allows subsequent optimization passes
  to do a significantly better job with them. The pass is located in
  `tree-sra.c` and is described by `pass_sra`.
- Dead store elimination

  This pass eliminates stores to memory that are subsequently overwritten
  by another store, without any intervening loads. The pass is located
  in `tree-ssa-dse.c` and is described by `pass_dse`.
- Tail recursion elimination

  This pass transforms tail recursion into a loop. It is located in
  `tree-tailcall.c` and is described by `pass_tail_recursion`.
- Partial redundancy elimination

  This pass eliminates partially redundant computations, as well as
  performing load motion. The pass is located in `tree-ssa-pre.c`
  and is described by `pass_pre`.
- Loop optimization

  The main driver of the pass is placed in `tree-ssa-loop.c`
  and described by `pass_loop`.

  The optimizations performed by this pass are:

  Loop invariant motion. This pass moves only invariants that
  would be hard to handle on rtl level (function calls, operations that expand to
  nontrivial sequences of insns). With `-funswitch-loops` it also moves
  operands of conditions that are invariant out of the loop, so that we can use
  just trivial invariantness analysis in loop unswitching. The pass also includes
  store motion. The pass is implemented in `tree-ssa-loop-im.c`.

  Canonical induction variable creation. This pass creates a simple counter
  for number of iterations of the loop and replaces the exit condition of the
  loop using it, in case when a complicated analysis is necessary to determine
  the number of iterations. Later optimizations then may determine the number
  easily. The pass is implemented in `tree-ssa-loop-ivcanon.c`.

  Induction variable optimizations. This pass performs standard induction
  variable optimizations, including strength reduction, induction variable
  merging and induction variable elimination. The pass is implemented in
  `tree-ssa-loop-ivopts.c`.

  Loop unswitching. This pass moves the conditional jumps that are invariant
  out of the loops. To achieve this, a duplicate of the loop is created for
  each possible outcome of conditional jump(s). The pass is implemented in
  `tree-ssa-loop-unswitch.c`. This pass should eventually replace the
  rtl-level loop unswitching in `loop-unswitch.c`, but currently
  the rtl-level pass is not completely redundant yet due to deficiencies
  in tree level alias analysis.

  The optimizations also use various utility functions contained in
  `tree-ssa-loop-manip.c`, `cfgloop.c`, `cfgloopanal.c` and
  `cfgloopmanip.c`.

  Vectorization. This pass transforms loops to operate on vector types
  instead of scalar types. Data parallelism across loop iterations is exploited
  to group data elements from consecutive iterations into a vector and operate
  on them in parallel. Depending on available target support the loop is
  conceptually unrolled by a factor `VF` (vectorization factor), which is
  the number of elements operated upon in parallel in each iteration, and the
  `VF` copies of each scalar operation are fused to form a vector operation.
  Additional loop transformations such as peeling and versioning may take place
  to align the number of iterations, and to align the memory accesses in the loop.
  The pass is implemented in `tree-vectorizer.c` (the main driver and general
  utilities), `tree-vect-analyze.c` and `tree-vect-tranform.c`.
  Analysis of data references is in `tree-data-ref.c`.
- Tree level if-conversion for vectorizer

  This pass applies if-conversion to simple loops to help vectorizer.
  We identify if convertable loops, if-convert statements and merge
  basic blocks in one big block. The idea is to present loop in such
  form so that vectorizer can have one to one mapping between statements
  and available vector operations. This patch re-introduces COND_EXPR
  at GIMPLE level. This pass is located in `tree-if-conv.c`.
- Conditional constant propagation

  This pass relaxes a lattice of values in order to identify those
  that must be constant even in the presence of conditional branches.
  The pass is located in `tree-ssa-ccp.c` and is described
  by `pass_ccp`.
- Folding builtin functions

  This pass simplifies builtin functions, as applicable, with constant
  arguments or with inferrable string lengths. It is located in
  `tree-ssa-ccp.c` and is described by `pass_fold_builtins`.
- Split critical edges

  This pass identifies critical edges and inserts empty basic blocks
  such that the edge is no longer critical. The pass is located in
  `tree-cfg.c` and is described by `pass_split_crit_edges`.
- Partial redundancy elimination

  This pass answers the question “given a hypothetical temporary
  variable, what expressions could we eliminate?” It is located
  in `tree-ssa-pre.c` and is described by `pass_pre`.
- Control dependence dead code elimination

  This pass is a stronger form of dead code elimination that can
  eliminate unnecessary control flow statements. It is located
  in `tree-ssa-dce.c` and is described by `pass_cd_dce`.
- Tail call elimination

  This pass identifies function calls that may be rewritten into
  jumps. No code transformation is actually applied here, but the
  data and control flow problem is solved. The code transformation
  requires target support, and so is delayed until RTL. In the
  meantime `CALL_EXPR_TAILCALL` is set indicating the possibility.
  The pass is located in `tree-tailcall.c` and is described by
  `pass_tail_calls`. The RTL transformation is handled by
  `fixup_tail_calls` in `calls.c`.
- Warn for function return without value

  For non-void functions, this pass locates return statements that do
  not specify a value and issues a warning. Such a statement may have
  been injected by falling off the end of the function. This pass is
  run last so that we have as much time as possible to prove that the
  statement is not reachable. It is located in `tree-cfg.c` and
  is described by `pass_warn_function_return`.
- Mudflap statement annotation

  If mudflap is enabled, we rewrite some memory accesses with code to
  validate that the memory access is correct. In particular, expressions
  involving pointer dereferences (`INDIRECT_REF`, `ARRAY_REF`,
  etc.) are replaced by code that checks the selected address range
  against the mudflap runtime's database of valid regions. This check
  includes an inline lookup into a direct-mapped cache, based on
  shift/mask operations of the pointer value, with a fallback function
  call into the runtime. The pass is located in `tree-mudflap.c` and
  is described by `pass_mudflap_2`.
- Leave static single assignment form

  This pass rewrites the function such that it is in normal form. At
  the same time, we eliminate as many single-use temporaries as possible,
  so the intermediate language is no longer GIMPLE, but GENERIC. The
  pass is located in `tree-ssa.c` and is described by `pass_del_ssa`.
