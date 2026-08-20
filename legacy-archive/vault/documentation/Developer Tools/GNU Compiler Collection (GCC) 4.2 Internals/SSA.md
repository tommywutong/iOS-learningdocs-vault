---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/SSA.html
archived_at: '2026-07-15T07:31:02.733990Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Alias analysis](Alias-analysis.md#apple-ifwgsyltfvqw4ylmpfzws4y),
Previous: [Statement Operands](Statement-Operands.md#apple-kn2gc5dfnvsw45bnj5ygk4tbnzshg),
Up: [Tree SSA](Tree-SSA.md#apple-krzgkzjnknjuc)

---

### 10.5 Static Single Assignment

Most of the tree optimizers rely on the data flow information provided
by the Static Single Assignment (SSA) form. We implement the SSA form
as described in R. Cytron, J. Ferrante, B. Rosen, M. Wegman, and
K. Zadeck. Efficiently Computing Static Single Assignment Form and the
Control Dependence Graph. ACM Transactions on Programming Languages
and Systems, 13(4):451-490, October 1991.

The SSA form is based on the premise that program variables are
assigned in exactly one location in the program. Multiple assignments
to the same variable create new versions of that variable. Naturally,
actual programs are seldom in SSA form initially because variables
tend to be assigned multiple times. The compiler modifies the program
representation so that every time a variable is assigned in the code,
a new version of the variable is created. Different versions of the
same variable are distinguished by subscripting the variable name with
its version number. Variables used in the right-hand side of
expressions are renamed so that their version number matches that of
the most recent assignment.

We represent variable versions using `SSA_NAME` nodes. The
renaming process in `tree-ssa.c` wraps every real and
virtual operand with an `SSA_NAME` node which contains
the version number and the statement that created the
`SSA_NAME`. Only definitions and virtual definitions may
create new `SSA_NAME` nodes.

Sometimes, flow of control makes it impossible to determine what is the
most recent version of a variable. In these cases, the compiler
inserts an artificial definition for that variable called
PHI function or PHI node. This new definition merges
all the incoming versions of the variable to create a new name
for it. For instance,

```
     if (...)
       a_1 = 5;
     else if (...)
       a_2 = 2;
     else
       a_3 = 13;

     # a_4 = PHI <a_1, a_2, a_3>
     return a_4;
```

Since it is not possible to determine which of the three branches
will be taken at runtime, we don't know which of `a_1`,
`a_2` or `a_3` to use at the return statement. So, the
SSA renamer creates a new version `a_4` which is assigned
the result of “merging” `a_1`, `a_2` and `a_3`.
Hence, PHI nodes mean “one of these operands. I don't know
which”.

The following macros can be used to examine PHI nodes

— Macro: __PHI_RESULT__ (phi)
> Returns the `SSA_NAME` created by PHI node phi (i.e.,
> phi's LHS).

— Macro: __PHI_NUM_ARGS__ (phi)
> Returns the number of arguments in phi. This number is exactly
> the number of incoming edges to the basic block holding phi.

— Macro: __PHI_ARG_ELT__ (phi, i)
> Returns a tuple representing the ith argument of phi.
> Each element of this tuple contains an `SSA_NAME` var and
> the incoming edge through which var flows.

— Macro: __PHI_ARG_EDGE__ (phi, i)
> Returns the incoming edge for the ith argument of phi.

— Macro: __PHI_ARG_DEF__ (phi, i)
> Returns the `SSA_NAME` for the ith argument of phi.

#### 10.5.1 Preserving the SSA form

Some optimization passes make changes to the function that
invalidate the SSA property. This can happen when a pass has
added new symbols or changed the program so that variables that
were previously aliased aren't anymore. Whenever something like this
happens, the affected symbols must be renamed into SSA form again.
Transformations that emit new code or replicate existing statements
will also need to update the SSA form.

Since GCC implements two different SSA forms for register and virtual
variables, keeping the SSA form up to date depends on whether you are
updating register or virtual names. In both cases, the general idea
behind incremental SSA updates is similar: when new SSA names are
created, they typically are meant to replace other existing names in
the program.

For instance, given the following code:

```
          1	L0:
          2	x_1 = PHI (0, x_5)
          3	if (x_1 < 10)
          4	  if (x_1 > 7)
          5	    y_2 = 0
          6	  else
          7	    y_3 = x_1 + x_7
          8	  endif
          9	  x_5 = x_1 + 1
          10   goto L0;
          11	endif
```

Suppose that we insert new names `x_10` and `x_11` (lines
`4` and `8`).

```
          1	L0:
          2	x_1 = PHI (0, x_5)
          3	if (x_1 < 10)
          4	  x_10 = ...
          5	  if (x_1 > 7)
          6	    y_2 = 0
          7	  else
          8	    x_11 = ...
          9	    y_3 = x_1 + x_7
          10	  endif
          11	  x_5 = x_1 + 1
          12	  goto L0;
          13	endif
```

We want to replace all the uses of `x_1` with the new definitions
of `x_10` and `x_11`. Note that the only uses that should
be replaced are those at lines `5`, `9` and `11`.
Also, the use of `x_7` at line `9` should _not_ be
replaced (this is why we cannot just mark symbol `x` for
renaming).

Additionally, we may need to insert a PHI node at line `11`
because that is a merge point for `x_10` and `x_11`. So the
use of `x_1` at line `11` will be replaced with the new PHI
node. The insertion of PHI nodes is optional. They are not strictly
necessary to preserve the SSA form, and depending on what the caller
inserted, they may not even be useful for the optimizers.

Updating the SSA form is a two step process. First, the pass has to
identify which names need to be updated and/or which symbols need to
be renamed into SSA form for the first time. When new names are
introduced to replace existing names in the program, the mapping
between the old and the new names are registered by calling
`register_new_name_mapping` (note that if your pass creates new
code by duplicating basic blocks, the call to `tree_duplicate_bb`
will set up the necessary mappings automatically). On the other hand,
if your pass exposes a new symbol that should be put in SSA form for
the first time, the new symbol should be registered with
`mark_sym_for_renaming`.

After the replacement mappings have been registered and new symbols
marked for renaming, a call to `update_ssa` makes the registered
changes. This can be done with an explicit call or by creating
`TODO` flags in the `tree_opt_pass` structure for your pass.
There are several `TODO` flags that control the behavior of
`update_ssa`:

- `TODO_update_ssa`. Update the SSA form inserting PHI nodes
  for newly exposed symbols and virtual names marked for updating.
  When updating real names, only insert PHI nodes for a real name
  `O_j` in blocks reached by all the new and old definitions for
  `O_j`. If the iterated dominance frontier for `O_j`
  is not pruned, we may end up inserting PHI nodes in blocks that
  have one or more edges with no incoming definition for
  `O_j`. This would lead to uninitialized warnings for
  `O_j`'s symbol.
- `TODO_update_ssa_no_phi`. Update the SSA form without
  inserting any new PHI nodes at all. This is used by passes that
  have either inserted all the PHI nodes themselves or passes that
  need only to patch use-def and def-def chains for virtuals
  (e.g., DCE).
- `TODO_update_ssa_full_phi`. Insert PHI nodes everywhere
  they are needed. No pruning of the IDF is done. This is used
  by passes that need the PHI nodes for `O_j` even if it
  means that some arguments will come from the default definition
  of `O_j`'s symbol (e.g., `pass_linear_transform`).

  WARNING: If you need to use this flag, chances are that your
  pass may be doing something wrong. Inserting PHI nodes for an
  old name where not all edges carry a new replacement may lead to
  silent codegen errors or spurious uninitialized warnings.
- `TODO_update_ssa_only_virtuals`. Passes that update the
  SSA form on their own may want to delegate the updating of
  virtual names to the generic updater. Since FUD chains are
  easier to maintain, this simplifies the work they need to do.
  NOTE: If this flag is used, any OLD->NEW mappings for real names
  are explicitly destroyed and only the symbols marked for
  renaming are processed.

#### 10.5.2 Preserving the virtual SSA form

The virtual SSA form is harder to preserve than the non-virtual SSA form
mainly because the set of virtual operands for a statement may change at
what some would consider unexpected times. In general, any time you
have modified a statement that has virtual operands, you should verify
whether the list of virtual operands has changed, and if so, mark the
newly exposed symbols by calling `mark_new_vars_to_rename`.

There is one additional caveat to preserving virtual SSA form. When the
entire set of virtual operands may be eliminated due to better
disambiguation, a bare SMT will be added to the list of virtual
operands, to signify the non-visible aliases that the are still being
referenced. If the set of bare SMT's may change,
`TODO_update_smt_usage` should be added to the todo flags.

With the current pruning code, this can only occur when constants are
propagated into array references that were previously non-constant, or
address expressions are propagated into their uses.

#### 10.5.3 Examining `SSA_NAME` nodes

The following macros can be used to examine `SSA_NAME` nodes

— Macro: __SSA_NAME_DEF_STMT__ (var)
> Returns the statement s that creates the `SSA_NAME`
> var. If s is an empty statement (i.e., `IS_EMPTY_STMT
> (`s`)` returns `true`), it means that the first reference to
> this variable is a USE or a VUSE.

— Macro: __SSA_NAME_VERSION__ (var)
> Returns the version number of the `SSA_NAME` object var.

#### 10.5.4 Walking use-def chains

— Tree SSA function: void __walk_use_def_chains__ (var, fn, data)
> Walks use-def chains starting at the `SSA_NAME` node var.
> Calls function fn at each reaching definition found. Function
> FN takes three arguments: var, its defining statement
> (def_stmt) and a generic pointer to whatever state information
> that fn may want to maintain (data). Function fn is
> able to stop the walk by returning `true`, otherwise in order to
> continue the walk, fn should return `false`.
>
> Note, that if def_stmt is a `PHI` node, the semantics are
> slightly different. For each argument arg of the PHI node, this
> function will:
>
> 1. Walk the use-def chains for arg.
> 2. Call `FN (`arg`,` phi`,` data`)`.
>
> Note how the first argument to fn is no longer the original
> variable var, but the PHI argument currently being examined.
> If fn wants to get at var, it should call
> `PHI_RESULT` (phi).

#### 10.5.5 Walking the dominator tree

— Tree SSA function: void __walk_dominator_tree__ (walk_data, bb)
> This function walks the dominator tree for the current CFG calling a
> set of callback functions defined in struct dom_walk_data in
> `domwalk.h`. The call back functions you need to define give you
> hooks to execute custom code at various points during traversal:
>
> 1. Once to initialize any local data needed while processing
>    bb and its children. This local data is pushed into an
>    internal stack which is automatically pushed and popped as the
>    walker traverses the dominator tree.
> 2. Once before traversing all the statements in the bb.
> 3. Once for every statement inside bb.
> 4. Once after traversing all the statements and before recursing
>    into bb's dominator children.
> 5. It then recurses into all the dominator children of bb.
> 6. After recursing into all the dominator children of bb it
>    can, optionally, traverse every statement in bb again
>    (i.e., repeating steps 2 and 3).
> 7. Once after walking the statements in bb and bb's
>    dominator children. At this stage, the block local data stack
>    is popped.
