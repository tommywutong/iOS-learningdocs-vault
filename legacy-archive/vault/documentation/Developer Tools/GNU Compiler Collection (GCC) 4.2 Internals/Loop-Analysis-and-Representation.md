---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Loop-Analysis-and-Representation.html
archived_at: '2026-07-15T07:31:02.238955Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq),
Previous: [Tree SSA](Tree-SSA.md#apple-krzgkzjnknjuc),
Up: [Top](index.md#apple-krxxa)

---

## 11 Analysis and Representation of Loops

GCC provides extensive infrastructure for work with natural loops, i.e.,
strongly connected components of CFG with only one entry block. This
chapter describes representation of loops in GCC, both on GIMPLE and in
RTL, as well as the interfaces to loop-related analyses (induction
variable analysis and number of iterations analysis).

- [Loop representation](Loop-representation.md#apple-jrxw64bnojsxa4tfonsw45dboruw63q): Representation and analysis of loops.
- [Loop querying](Loop-querying.md#apple-jrxw64bnof2wk4tznfxgo): Getting information about loops.
- [Loop manipulation](Loop-manipulation.md#apple-jrxw64bnnvqw42lqovwgc5djn5xa): Loop manipulation functions.
- [LCSSA](LCSSA.md#apple-jrbvgu2b): Loop-closed SSA form.
- [Scalar evolutions](Scalar-evolutions.md#apple-knrwc3dboiwwk5tpnr2xi2lpnzzq): Induction variables on GIMPLE.
- [loop-iv](loop_002div.md#apple-nrxw64c7gaydezdjoy): Induction variables on RTL.
- [Number of iterations](Number-of-iterations.md#apple-jz2w2ytfoiww6zrnnf2gk4tboruw63tt): Number of iterations analysis.
- [Dependency analysis](Dependency-analysis.md#apple-irsxazlomrsw4y3zfvqw4ylmpfzws4y): Data dependency analysis.
- [Lambda](Lambda.md#apple-jrqw2yteme): Linear loop transformations framework.
