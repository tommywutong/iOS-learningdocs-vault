---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Interfaces.html
archived_at: '2026-07-15T07:31:00.136636Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Temporaries](Temporaries.md#apple-krsw24dpojqxe2lfom),
Up: [GIMPLE](GIMPLE.md#apple-i5eu2ucmiu)

---

#### 9.2.1 Interfaces

The tree representation of a function is stored in
`DECL_SAVED_TREE`. It is lowered to GIMPLE by a call to
`gimplify_function_tree`.

If a front end wants to include language-specific tree codes in the tree
representation which it provides to the back end, it must provide a
definition of `LANG_HOOKS_GIMPLIFY_EXPR` which knows how to
convert the front end trees to GIMPLE. Usually such a hook will involve
much of the same code for expanding front end trees to RTL. This function
can return fully lowered GIMPLE, or it can return GENERIC trees and let the
main gimplifier lower them the rest of the way; this is often simpler.

The C and C++ front ends currently convert directly from front end
trees to GIMPLE, and hand that off to the back end rather than first
converting to GENERIC. Their gimplifier hooks know about all the
`_STMT` nodes and how to convert them to GENERIC forms. There
was some work done on a genericization pass which would run first, but
the existence of `STMT_EXPR` meant that in order to convert all
of the C statements into GENERIC equivalents would involve walking the
entire tree anyway, so it was simpler to lower all the way. This
might change in the future if someone writes an optimization pass
which would work better with higher-level trees, but currently the
optimizers all expect GIMPLE.

A front end which wants to use the tree optimizers (and already has
some sort of whole-function tree representation) only needs to provide
a definition of `LANG_HOOKS_GIMPLIFY_EXPR`, call
`gimplify_function_tree` to lower to GIMPLE, and then hand off to
`tree_rest_of_compilation` to compile and output the function.

You can tell the compiler to dump a C-like representation of the GIMPLE
form with the flag `-fdump-tree-gimple`.
