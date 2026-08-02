---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Compound-Lvalues.html
archived_at: '2026-07-15T07:30:59.399656Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Conditional Expressions](Conditional-Expressions.md#apple-inxw4zdjoruw63tbnqwuk6dqojsxg43jn5xhg),
Previous: [Compound Expressions](Compound-Expressions.md#apple-inxw24dpovxgilkfpbyhezltonuw63tt),
Up: [GIMPLE Expressions](GIMPLE-Expressions.md#apple-i5eu2ucmiuwuk6dqojsxg43jn5xhg)

---

##### 9.2.3.2 Compound Lvalues

Currently compound lvalues involving array and structure field references
are not broken down; an expression like `a.b[2] = 42` is not reduced
any further (though complex array subscripts are). This restriction is a
workaround for limitations in later optimizers; if we were to convert this
to

```
       T1 = &a.b;
       T1[2] = 42;
```

alias analysis would not remember that the reference to `T1[2]` came
by way of `a.b`, so it would think that the assignment could alias
another member of `a`; this broke `struct-alias-1.c`. Future
optimizer improvements may make this limitation unnecessary.
