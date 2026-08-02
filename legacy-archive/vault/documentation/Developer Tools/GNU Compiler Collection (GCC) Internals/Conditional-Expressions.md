---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Conditional-Expressions.html
archived_at: '2026-07-15T07:30:59.570218Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Logical Operators](Logical-Operators.md#apple-jrxwo2ldmfwc2t3qmvzgc5dpojzq),
Previous: [Compound Lvalues](Compound-Lvalues.md#apple-inxw24dpovxgilkmozqwy5lfom),
Up: [GIMPLE Expressions](GIMPLE-Expressions.md#apple-i5eu2ucmiuwuk6dqojsxg43jn5xhg)

---

##### 9.2.3.3 Conditional Expressions

A C `?:` expression is converted into an `if` statement with
each branch assigning to the same temporary. So,

```
       a = b ? c : d;
```

becomes

```
       if (b)
         T1 = c;
       else
         T1 = d;
       a = T1;
```

Tree level if-conversion pass re-introduces `?:` expression, if appropriate.
It is used to vectorize loops with conditions using vector conditional operations.

Note that in GIMPLE, `if` statements are also represented using
`COND_EXPR`, as described below.
