---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Statements.html
archived_at: '2026-07-15T07:31:02.904428Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [GIMPLE Example](GIMPLE-Example.md#apple-i5eu2ucmiuwuk6dbnvygyzi),
Previous: [GIMPLE Expressions](GIMPLE-Expressions.md#apple-i5eu2ucmiuwuk6dqojsxg43jn5xhg),
Up: [GIMPLE](GIMPLE.md#apple-i5eu2ucmiu)

---

#### 10.2.4 Statements

Most statements will be assignment statements, represented by
`MODIFY_EXPR`. A `CALL_EXPR` whose value is ignored can
also be a statement. No other C expressions can appear at statement level;
a reference to a volatile object is converted into a `MODIFY_EXPR`.
In GIMPLE form, type of `MODIFY_EXPR` is not meaningful. Instead, use type
of LHS or RHS.

There are also several varieties of complex statements.

- [Blocks](Blocks.md#apple-ijwg6y3lom)
- [Statement Sequences](Statement-Sequences.md#apple-kn2gc5dfnvsw45bnknsxc5lfnzrwk4y)
- [Empty Statements](Empty-Statements.md#apple-ivwxa5dzfvjxiylumvwwk3tuom)
- [Loops](Loops.md#apple-jrxw64dt)
- [Selection Statements](Selection-Statements.md#apple-knswyzldoruw63rnkn2gc5dfnvsw45dt)
- [Jumps](Jumps.md#apple-jj2w24dt)
- [Cleanups](Cleanups.md#apple-inwgkyloovyhg)
- [GIMPLE Exception Handling](GIMPLE-Exception-Handling.md#apple-i5eu2ucmiuwuk6ddmvyhi2lpnywuqylomrwgs3th)
