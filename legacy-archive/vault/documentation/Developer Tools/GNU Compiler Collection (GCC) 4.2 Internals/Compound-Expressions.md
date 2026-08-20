---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Compound-Expressions.html
archived_at: '2026-07-15T07:31:01.344688Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Compound Lvalues](Compound-Lvalues.md#apple-inxw24dpovxgilkmozqwy5lfom),
Up: [GIMPLE Expressions](GIMPLE-Expressions.md#apple-i5eu2ucmiuwuk6dqojsxg43jn5xhg)

---

##### 10.2.3.1 Compound Expressions

The left-hand side of a C comma expression is simply moved into a separate
statement.
