---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/GIMPLE-Expressions.html
archived_at: '2026-07-15T07:30:59.985380Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Statements](Statements.md#apple-kn2gc5dfnvsw45dt),
Previous: [Temporaries](Temporaries.md#apple-krsw24dpojqxe2lfom),
Up: [GIMPLE](GIMPLE.md#apple-i5eu2ucmiu)

---

#### 9.2.3 Expressions

In general, expressions in GIMPLE consist of an operation and the
appropriate number of simple operands; these operands must either be a
GIMPLE rvalue (`is_gimple_val`), i.e. a constant or a register
variable. More complex operands are factored out into temporaries, so
that

```
       a = b + c + d
```

becomes

```
       T1 = b + c;
       a = T1 + d;
```

The same rule holds for arguments to a `CALL_EXPR`.

The target of an assignment is usually a variable, but can also be an
`INDIRECT_REF` or a compound lvalue as described below.

- [Compound Expressions](Compound-Expressions.md#apple-inxw24dpovxgilkfpbyhezltonuw63tt)
- [Compound Lvalues](Compound-Lvalues.md#apple-inxw24dpovxgilkmozqwy5lfom)
- [Conditional Expressions](Conditional-Expressions.md#apple-inxw4zdjoruw63tbnqwuk6dqojsxg43jn5xhg)
- [Logical Operators](Logical-Operators.md#apple-jrxwo2ldmfwc2t3qmvzgc5dpojzq)
