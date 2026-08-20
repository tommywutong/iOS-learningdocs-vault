---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/SSA.html
archived_at: '2026-07-15T07:31:00.670687Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Alias analysis](Alias-analysis.md#apple-ifwgsyltfvqw4ylmpfzws4y),
Previous: [Statement Operands](Statement-Operands.md#apple-kn2gc5dfnvsw45bnj5ygk4tbnzshg),
Up: [Tree SSA](Tree-SSA.md#apple-krzgkzjnknjuc)

---

### 9.5 Static Single Assignment

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

#### 9.5.1 Preserving the SSA form

Some optimization passes make changes to the function that
invalidate the SSA property. This can happen when a pass has
added new variables or changed the program so that variables that
were previously aliased aren't anymore.

Whenever something like this happens, the affected variables must
be renamed into SSA form again. To do this, you should mark the
new variables in the global bitmap `vars_to_rename`. Once
your pass has finished, the pass manager will invoke the SSA
renamer to put the program into SSA once more.

#### 9.5.2 Examining `SSA_NAME` nodes

The following macros can be used to examine `SSA_NAME` nodes

— Macro: __SSA_NAME_DEF_STMT__ (var)
> Returns the statement s that creates the `SSA_NAME`
> var. If s is an empty statement (i.e., `IS_EMPTY_STMT
> (`s`)` returns `true`), it means that the first reference to
> this variable is a USE or a VUSE.

— Macro: __SSA_NAME_VERSION__ (var)
> Returns the version number of the `SSA_NAME` object var.

#### 9.5.3 Walking use-def chains

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

#### 9.5.4 Walking the dominator tree

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
