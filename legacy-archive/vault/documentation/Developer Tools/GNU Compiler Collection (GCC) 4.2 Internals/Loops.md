---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Loops.html
archived_at: '2026-07-15T07:31:02.266510Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Selection Statements](Selection-Statements.md#apple-knswyzldoruw63rnkn2gc5dfnvsw45dt),
Previous: [Empty Statements](Empty-Statements.md#apple-ivwxa5dzfvjxiylumvwwk3tuom),
Up: [Statements](Statements.md#apple-kn2gc5dfnvsw45dt)

---

##### 10.2.4.4 Loops

At one time loops were expressed in GIMPLE using `LOOP_EXPR`, but
now they are lowered to explicit gotos.
