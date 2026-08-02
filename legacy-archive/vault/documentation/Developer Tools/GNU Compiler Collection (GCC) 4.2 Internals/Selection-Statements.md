---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Selection-Statements.html
archived_at: '2026-07-15T07:31:02.778945Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Jumps](Jumps.md#apple-jj2w24dt),
Previous: [Loops](Loops.md#apple-jrxw64dt),
Up: [Statements](Statements.md#apple-kn2gc5dfnvsw45dt)

---

##### 10.2.4.5 Selection Statements

A simple selection statement, such as the C `if` statement, is
expressed in GIMPLE using a void `COND_EXPR`. If only one branch is
used, the other is filled with an empty statement.

Normally, the condition expression is reduced to a simple comparison. If
it is a shortcut (`&&` or `||`) expression, however, we try to
break up the `if` into multiple `if`s so that the implied shortcut
is taken directly, much like the transformation done by `do_jump` in
the RTL expander.

A `SWITCH_EXPR` in GIMPLE contains the condition and a
`TREE_VEC` of `CASE_LABEL_EXPR`s describing the case values
and corresponding `LABEL_DECL`s to jump to. The body of the
`switch` is moved after the `SWITCH_EXPR`.
