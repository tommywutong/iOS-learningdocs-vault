---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Jumps.html
archived_at: '2026-07-15T07:31:00.147644Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Cleanups](Cleanups.md#apple-inwgkyloovyhg),
Previous: [Selection Statements](Selection-Statements.md#apple-knswyzldoruw63rnkn2gc5dfnvsw45dt),
Up: [Statements](Statements.md#apple-kn2gc5dfnvsw45dt)

---

##### 9.2.4.6 Jumps

Other jumps are expressed by either `GOTO_EXPR` or `RETURN_EXPR`.

The operand of a `GOTO_EXPR` must be either a label or a variable
containing the address to jump to.

The operand of a `RETURN_EXPR` is either `NULL_TREE` or a
`MODIFY_EXPR` which sets the return value. It would be nice to
move the `MODIFY_EXPR` into a separate statement, but the special
return semantics in `expand_return` make that difficult. It may
still happen in the future, perhaps by moving most of that logic into
`expand_assignment`.
