---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Control-Flow.html
archived_at: '2026-07-15T07:31:01.607983Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Tree SSA](Tree-SSA.md#apple-krzgkzjnknjuc),
Previous: [RTL](RTL.md#apple-kjkey),
Up: [Top](index.md#apple-krxxa)

---

## 13 Control Flow Graph

A control flow graph (CFG) is a data structure built on top of the
intermediate code representation (the RTL or `tree` instruction
stream) abstracting the control flow behavior of a function that is
being compiled. The CFG is a directed graph where the vertices
represent basic blocks and edges represent possible transfer of
control flow from one basic block to another. The data structures
used to represent the control flow graph are defined in
`basic-block.h`.

- [Basic Blocks](Basic-Blocks.md#apple-ijqxg2ldfvbgy33dnnzq): The definition and representation of basic blocks.
- [Edges](Edges.md#apple-ivsgozlt): Types of edges and their representation.
- [Profile information](Profile-information.md#apple-kbzg6ztjnrss22lomzxxe3lboruw63q): Representation of frequencies and probabilities.
- [Maintaining the CFG](Maintaining-the-CFG.md#apple-jvqws3tumfuw42lom4wxi2dffvbumry): Keeping the control flow graph and up to date.
- [Liveness information](Liveness-information.md#apple-jruxmzlomvzxglljnztg64tnmf2gs33o): Using and maintaining liveness information.
