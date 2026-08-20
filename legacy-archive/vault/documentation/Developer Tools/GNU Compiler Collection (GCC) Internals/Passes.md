---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Passes.html
archived_at: '2026-07-15T07:31:00.485418Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Trees](Trees.md#apple-krzgkzlt),
Previous: [Source Tree](Source-Tree.md#apple-knxxk4tdmuwvi4tfmu),
Up: [Top](index.md#apple-krxxa)

---

## 7 Passes and Files of the Compiler

This chapter is dedicated to giving an overview of the optimization and
code generation passes of the compiler. In the process, it describes
some of the language front end interface, though this description is no
where near complete.

- [Parsing pass](Parsing-pass.md#apple-kbqxe43jnzts24dbonzq): The language front end turns text into bits.
- [Gimplification pass](Gimplification-pass.md#apple-i5uw24dmnftgsy3boruw63rnobqxg4y): The bits are turned into something we can optimize.
- [Pass manager](Pass-manager.md#apple-kbqxg4znnvqw4ylhmvza): Sequencing the optimization passes.
- [Tree-SSA passes](Tree_002dSSA-passes.md#apple-krzgkzk7gaydezctknas24dbonzwk4y): Optimizations on a high-level representation.
- [RTL passes](RTL-passes.md#apple-kjkeyllqmfzxgzlt): Optimizations on a low-level representation.
