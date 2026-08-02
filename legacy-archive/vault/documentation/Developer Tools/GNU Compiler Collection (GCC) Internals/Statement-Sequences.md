---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Statement-Sequences.html
archived_at: '2026-07-15T07:31:00.818391Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Empty Statements](Empty-Statements.md#apple-ivwxa5dzfvjxiylumvwwk3tuom),
Previous: [Blocks](Blocks.md#apple-ijwg6y3lom),
Up: [Statements](Statements.md#apple-kn2gc5dfnvsw45dt)

---

##### 9.2.4.2 Statement Sequences

Multiple statements at the same nesting level are collected into a
`STATEMENT_LIST`. Statement lists are modified and traversed
using the interface in ``tree-iterator.h`'.
