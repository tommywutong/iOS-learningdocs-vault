---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Logical-Operators.html
archived_at: '2026-07-15T07:31:02.233310Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [Conditional Expressions](Conditional-Expressions.md#apple-inxw4zdjoruw63tbnqwuk6dqojsxg43jn5xhg),
Up: [GIMPLE Expressions](GIMPLE-Expressions.md#apple-i5eu2ucmiuwuk6dqojsxg43jn5xhg)

---

##### 10.2.3.4 Logical Operators

Except when they appear in the condition operand of a `COND_EXPR`,
logical `and' and `or' operators are simplified as follows:
`a = b && c` becomes

```
       T1 = (bool)b;
       if (T1)
         T1 = (bool)c;
       a = T1;
```

Note that `T1` in this example cannot be an expression temporary,
because it has two different assignments.
