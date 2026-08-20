---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Temporaries.html
archived_at: '2026-07-15T07:31:00.892742Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [GIMPLE Expressions](GIMPLE-Expressions.md#apple-i5eu2ucmiuwuk6dqojsxg43jn5xhg),
Previous: [Interfaces](Interfaces.md#apple-jfxhizlsmzqwgzlt),
Up: [GIMPLE](GIMPLE.md#apple-i5eu2ucmiu)

---

#### 9.2.2 Temporaries

When gimplification encounters a subexpression which is too complex, it
creates a new temporary variable to hold the value of the subexpression,
and adds a new statement to initialize it before the current statement.
These special temporaries are known as ``expression temporaries`', and are
allocated using `get_formal_tmp_var`. The compiler tries to
always evaluate identical expressions into the same temporary, to simplify
elimination of redundant calculations.

We can only use expression temporaries when we know that it will not be
reevaluated before its value is used, and that it will not be otherwise
modified[1](#apple-mzxc2mi).
Other temporaries can be allocated using
`get_initialized_tmp_var` or `create_tmp_var`.

Currently, an expression like `a = b + 5` is not reduced any
further. We tried converting it to something like

```
       T1 = b + 5;
       a = T1;
```

but this bloated the representation for minimal benefit. However, a
variable which must live in memory cannot appear in an expression; its
value is explicitly loaded into a temporary first. Similarly, storing
the value of an expression to a memory variable goes through a
temporary.

---

#### Footnotes

[[1](#apple-mzxgiljr)] These restrictions are derived from those in Morgan 4.8.

---
