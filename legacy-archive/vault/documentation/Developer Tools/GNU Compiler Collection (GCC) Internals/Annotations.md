---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Annotations.html
archived_at: '2026-07-15T07:30:59.264369Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Statement Operands](Statement-Operands.md#apple-kn2gc5dfnvsw45bnj5ygk4tbnzshg),
Previous: [GIMPLE](GIMPLE.md#apple-i5eu2ucmiu),
Up: [Tree SSA](Tree-SSA.md#apple-krzgkzjnknjuc)

---

### 9.3 Annotations

The optimizers need to associate attributes with statements and
variables during the optimization process. For instance, we need to
know what basic block a statement belongs to or whether a variable
has aliases. All these attributes are stored in data structures
called annotations which are then linked to the field `ann` in
`struct tree_common`.

Presently, we define annotations for statements (`stmt_ann_t`),
variables (`var_ann_t`) and SSA names (`ssa_name_ann_t`).
Annotations are defined and documented in `tree-flow.h`.
