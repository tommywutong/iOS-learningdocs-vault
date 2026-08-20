---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/GIMPLE.html
archived_at: '2026-07-15T07:31:02.006379Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Annotations](Annotations.md#apple-ifxg433umf2gs33oom),
Previous: [GENERIC](GENERIC.md#apple-i5cu4rksjfbq),
Up: [Tree SSA](Tree-SSA.md#apple-krzgkzjnknjuc)

---

### 10.2 GIMPLE

GIMPLE is a simplified subset of GENERIC for use in optimization. The
particular subset chosen (and the name) was heavily influenced by the
SIMPLE IL used by the McCAT compiler project at McGill University,
though we have made some different choices. For one thing, SIMPLE
doesn't support `goto`; a production compiler can't afford that
kind of restriction.

GIMPLE retains much of the structure of the parse trees: lexical
scopes are represented as containers, rather than markers. However,
expressions are broken down into a 3-address form, using temporary
variables to hold intermediate values. Also, control structures are
lowered to gotos.

In GIMPLE no container node is ever used for its value; if a
`COND_EXPR` or `BIND_EXPR` has a value, it is stored into a
temporary within the controlled blocks, and that temporary is used in
place of the container.

The compiler pass which lowers GENERIC to GIMPLE is referred to as the
``gimplifier`'. The gimplifier works recursively, replacing complex
statements with sequences of simple statements.

- [Interfaces](Interfaces.md#apple-jfxhizlsmzqwgzlt)
- [Temporaries](Temporaries.md#apple-krsw24dpojqxe2lfom)
- [GIMPLE Expressions](GIMPLE-Expressions.md#apple-i5eu2ucmiuwuk6dqojsxg43jn5xhg)
- [Statements](Statements.md#apple-kn2gc5dfnvsw45dt)
- [GIMPLE Example](GIMPLE-Example.md#apple-i5eu2ucmiuwuk6dbnvygyzi)
- [Rough GIMPLE Grammar](Rough-GIMPLE-Grammar.md#apple-kjxxkz3ifvdustkqjrcs2r3smfww2yls)
