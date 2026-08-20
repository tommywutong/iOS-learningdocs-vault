---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Statement-Operands.html
archived_at: '2026-07-15T07:31:00.810740Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [SSA](SSA.md#apple-knjuc),
Previous: [Annotations](Annotations.md#apple-ifxg433umf2gs33oom),
Up: [Tree SSA](Tree-SSA.md#apple-krzgkzjnknjuc)

---

### 9.4 Statement Operands

Almost every GIMPLE statement will contain a reference to a variable
or memory location. Since statements come in different shapes and
sizes, their operands are going to be located at various spots inside
the statement's tree. To facilitate access to the statement's
operands, they are organized into arrays associated inside each
statement's annotation. Each element in an operand array is a pointer
to a `VAR_DECL`, `PARM_DECL` or `SSA_NAME` tree node.
This provides a very convenient way of examining and replacing
operands.

Data flow analysis and optimization is done on all tree nodes
representing variables. Any node for which `SSA_VAR_P` returns
nonzero is considered when scanning statement operands. However, not
all `SSA_VAR_P` variables are processed in the same way. For the
purposes of optimization, we need to distinguish between references to
local scalar variables and references to globals, statics, structures,
arrays, aliased variables, etc. The reason is simple, the compiler
can gather complete data flow information for a local scalar. On the
other hand, a global variable may be modified by a function call, it
may not be possible to keep track of all the elements of an array or
the fields of a structure, etc.

The operand scanner gathers two kinds of operands: real and
virtual. An operand for which `is_gimple_reg` returns true
is considered real, otherwise it is a virtual operand. We also
distinguish between uses and definitions. An operand is used if its
value is loaded by the statement (e.g., the operand at the RHS of an
assignment). If the statement assigns a new value to the operand, the
operand is considered a definition (e.g., the operand at the LHS of
an assignment).

Virtual and real operands also have very different data flow
properties. Real operands are unambiguous references to the
full object that they represent. For instance, given

```
     {
       int a, b;
       a = b
     }
```

Since `a` and `b` are non-aliased locals, the statement
`a = b` will have one real definition and one real use because
variable `b` is completely modified with the contents of
variable `a`. Real definition are also known as killing
definitions. Similarly, the use of `a` reads all its bits.

In contrast, virtual operands are used with variables that can have
a partial or ambiguous reference. This includes structures, arrays,
globals, and aliased variables. In these cases, we have two types of
definitions. For globals, structures, and arrays, we can determine from
a statement whether a variable of these types has a killing definition.
If the variable does, then the statement is marked as having a
must definition of that variable. However, if a statement is only
defining a part of the variable (i.e. a field in a structure), or if we
know that a statement might define the variable but we cannot say for sure,
then we mark that statement as having a may definition. For
instance, given

```
     {
       int a, b, *p;

       if (...)
         p = &a;
       else
         p = &b;
       *p = 5;
       return *p;
     }
```

The assignment `*p = 5` may be a definition of `a` or
`b`. If we cannot determine statically where `p` is
pointing to at the time of the store operation, we create virtual
definitions to mark that statement as a potential definition site for
`a` and `b`. Memory loads are similarly marked with virtual
use operands. Virtual operands are shown in tree dumps right before
the statement that contains them. To request a tree dump with virtual
operands, use the `-vops` option to `-fdump-tree`:

```
     {
       int a, b, *p;

       if (...)
         p = &a;
       else
         p = &b;
       # a = V_MAY_DEF <a>
       # b = V_MAY_DEF <b>
       *p = 5;

       # VUSE <a>
       # VUSE <b>
       return *p;
     }
```

Notice that `V_MAY_DEF` operands have two copies of the referenced
variable. This indicates that this is not a killing definition of
that variable. In this case we refer to it as a may definition
or aliased store. The presence of the second copy of the
variable in the `V_MAY_DEF` operand will become important when the
function is converted into SSA form. This will be used to link all
the non-killing definitions to prevent optimizations from making
incorrect assumptions about them.

Operands are collected by `tree-ssa-operands.c`. They are stored
inside each statement's annotation and can be accessed with
`DEF_OPS`, `USE_OPS`, `V_MAY_DEF_OPS`,
`V_MUST_DEF_OPS` and `VUSE_OPS`. The following are all the
accessor macros available to access USE operands. To access all the
other operand arrays, just change the name accordingly. Note that
this interface to the operands is deprecated, and is slated for
removal in a future version of gcc. The preferred interface is the
operand iterator interface. Unless you need to discover the number of
operands of a given type on a statement, you are strongly urged not to
use this interface.

— Macro: __USE_OPS__ (ann)
> Returns the array of operands used by the statement with annotation
> ann.

— Macro: __STMT_USE_OPS__ (stmt)
> Alternate version of USE_OPS that takes the statement stmt as
> input.

— Macro: __NUM_USES__ (ops)
> Return the number of USE operands in array ops.

— Macro: __USE_OP_PTR__ (ops, i)
> Return a pointer to the ith operand in array ops.

— Macro: __USE_OP__ (ops, i)
> Return the ith operand in array ops.

The following function shows how to print all the operands of a given
statement:

```
     void
     print_ops (tree stmt)
     {
       vuse_optype vuses;
       v_may_def_optype v_may_defs;
       v_must_def_optype v_must_defs;
       def_optype defs;
       use_optype uses;
       stmt_ann_t ann;
       size_t i;

       get_stmt_operands (stmt);
       ann = stmt_ann (stmt);

       defs = DEF_OPS (ann);
       for (i = 0; i < NUM_DEFS (defs); i++)
         print_generic_expr (stderr, DEF_OP (defs, i), 0);

       uses = USE_OPS (ann);
       for (i = 0; i < NUM_USES (uses); i++)
         print_generic_expr (stderr, USE_OP (uses, i), 0);

       v_may_defs = V_MAY_DEF_OPS (ann);
       for (i = 0; i < NUM_V_MAY_DEFS (v_may_defs); i++)
         {
           print_generic_expr (stderr, V_MAY_DEF_OP (v_may_defs, i), 0);
           print_generic_expr (stderr, V_MAY_DEF_RESULT (v_may_defs, i), 0);
         }

       v_must_defs = V_MUST_DEF_OPS (ann);
       for (i = 0; i < NUM_V_MUST_DEFS (v_must_defs); i++)
         print_generic_expr (stderr, V_MUST_DEF_OP (v_must_defs, i), 0);

       vuses = VUSE_OPS (ann);
       for (i = 0; i < NUM_VUSES (vuses); i++)
         print_generic_expr (stderr, VUSE_OP (vuses, i), 0);
     }
```

To collect the operands, you first need to call
`get_stmt_operands`. Since that is a potentially expensive
operation, statements are only scanned if they have been marked
modified by a call to `modify_stmt`. So, if your pass replaces
operands in a statement, make sure to call `modify_stmt`.

#### 9.4.1 Operand Iterators

There is an alternative to iterating over the operands in a statement.
It is especially useful when you wish to perform the same operation on
more than one type of operand. The previous example could be
rewritten as follows:

```
     void
     print_ops (tree stmt)
     {
       ssa_op_iter;
       tree var;

       get_stmt_operands (stmt);
       FOR_EACH_SSA_TREE_OPERAND (var, stmt, iter, SSA_OP_ALL_OPERANDS)
         print_generic_expr (stderr, var, 0);
     }
```

1. Determine whether you are need to see the operand pointers, or just the
   trees, and choose the appropriate macro:

   ```
             Need            Macro:
             ----            -------
             use_operand_p   FOR_EACH_SSA_USE_OPERAND
             def_operand_p   FOR_EACH_SSA_DEF_OPERAND
             tree            FOR_EACH_SSA_TREE_OPERAND

   ```
2. You need to declare a variable of the type you are interested
   in, and an ssa_op_iter structure which serves as the loop
   controlling variable.
3. Determine which operands you wish to use, and specify the flags of
   those you are interested in. They are documented in
   `tree-ssa-operands.h`:

   ```
             #define SSA_OP_USE              0x01    /* Real USE operands.  */
             #define SSA_OP_DEF              0x02    /* Real DEF operands.  */
             #define SSA_OP_VUSE             0x04    /* VUSE operands.  */
             #define SSA_OP_VMAYUSE          0x08    /* USE portion of V_MAY_DEFS.  */
             #define SSA_OP_VMAYDEF          0x10    /* DEF portion of V_MAY_DEFS.  */
             #define SSA_OP_VMUSTDEF         0x20    /* V_MUST_DEF definitions.  */

             /* These are commonly grouped operand flags.  */
             #define SSA_OP_VIRTUAL_USES     (SSA_OP_VUSE | SSA_OP_VMAYUSE)
             #define SSA_OP_VIRTUAL_DEFS     (SSA_OP_VMAYDEF | SSA_OP_VMUSTDEF)
             #define SSA_OP_ALL_USES         (SSA_OP_VIRTUAL_USES | SSA_OP_USE)
             #define SSA_OP_ALL_DEFS         (SSA_OP_VIRTUAL_DEFS | SSA_OP_DEF)
             #define SSA_OP_ALL_OPERANDS     (SSA_OP_ALL_USES | SSA_OP_ALL_DEFS)

   ```

So if you want to look at the use pointers for all the `USE` and
`VUSE` operands, you would do something like:

```
       use_operand_p use_p;
       ssa_op_iter iter;

       FOR_EACH_SSA_USE_OPERAND (use_p, stmt, iter, (SSA_OP_USE | SSA_OP_VUSE))
         {
           process_use_ptr (use_p);
         }
```

The `_TREE_` macro is basically the same as the `USE` and
`DEF` macros, only with the use or def dereferenced via
`USE_FROM_PTR (use_p)` and `DEF_FROM_PTR (def_p)`. Since we
aren't using operand pointers, use and defs flags can be mixed.

```
       tree var;
       ssa_op_iter iter;

       FOR_EACH_SSA_TREE_OPERAND (var, stmt, iter, SSA_OP_VUSE | SSA_OP_VMUSTDEF)
         {
            print_generic_expr (stderr, var, TDF_SLIM);
         }
```

`V_MAY_DEF`s are broken into two flags, one for the
`DEF` portion (`SSA_OP_VMAYDEF`) and one for the USE portion
(`SSA_OP_VMAYUSE`). If all you want to look at are the
`V_MAY_DEF`s together, there is a fourth iterator macro for this,
which returns both a def_operand_p and a use_operand_p for each
`V_MAY_DEF` in the statement. Note that you don't need any flags for
this one.

```
       use_operand_p use_p;
       def_operand_p def_p;
       ssa_op_iter iter;

       FOR_EACH_SSA_MAYDEF_OPERAND (def_p, use_p, stmt, iter)
         {
           my_code;
         }
```

`V_MUST_DEF`s are broken into two flags, one for the
`DEF` portion (`SSA_OP_VMUSTDEF`) and one for the kill portion
(`SSA_OP_VMUSTDEFKILL`). If all you want to look at are the
`V_MUST_DEF`s together, there is a fourth iterator macro for this,
which returns both a def_operand_p and a use_operand_p for each
`V_MUST_DEF` in the statement. Note that you don't need any flags for
this one.

```
       use_operand_p kill_p;
       def_operand_p def_p;
       ssa_op_iter iter;

       FOR_EACH_SSA_MUSTDEF_OPERAND (def_p, kill_p, stmt, iter)
         {
           my_code;
         }
```

There are many examples in the code as well, as well as the
documentation in `tree-ssa-operands.h`.
