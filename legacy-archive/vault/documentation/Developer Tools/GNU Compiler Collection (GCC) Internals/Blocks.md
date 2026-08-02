---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Blocks.html
archived_at: '2026-07-15T07:30:59.323769Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Statement Sequences](Statement-Sequences.md#apple-kn2gc5dfnvsw45bnknsxc5lfnzrwk4y),
Up: [Statements](Statements.md#apple-kn2gc5dfnvsw45dt)

---

##### 9.2.4.1 Blocks

Block scopes and the variables they declare in GENERIC and GIMPLE are
expressed using the `BIND_EXPR` code, which in previous versions of
GCC was primarily used for the C statement-expression extension.

Variables in a block are collected into `BIND_EXPR_VARS` in
declaration order. Any runtime initialization is moved out of
`DECL_INITIAL` and into a statement in the controlled block. When
gimplifying from C or C++, this initialization replaces the
`DECL_STMT`.

Variable-length arrays (VLAs) complicate this process, as their size often
refers to variables initialized earlier in the block. To handle this, we
currently split the block at that point, and move the VLA into a new, inner
`BIND_EXPR`. This strategy may change in the future.

`DECL_SAVED_TREE` for a GIMPLE function will always be a
`BIND_EXPR` which contains declarations for the temporary variables
used in the function.

A C++ program will usually contain more `BIND_EXPR`s than there are
syntactic blocks in the source code, since several C++ constructs have
implicit scopes associated with them. On the other hand, although the C++
front end uses pseudo-scopes to handle cleanups for objects with
destructors, these don't translate into the GIMPLE form; multiple
declarations at the same level use the same `BIND_EXPR`.
