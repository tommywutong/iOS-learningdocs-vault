---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Peephole-Definitions.html
archived_at: '2026-07-15T07:31:00.527520Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt),
Previous: [Including Patterns](Including-Patterns.md#apple-jfxgg3dvmruw4zznkbqxi5dfojxhg),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 12.18 Machine-Specific Peephole Optimizers

In addition to instruction patterns the `md` file may contain
definitions of machine-specific peephole optimizations.

The combiner does not notice certain peephole optimizations when the data
flow in the program does not suggest that it should try them. For example,
sometimes two consecutive insns related in purpose can be combined even
though the second one does not appear to use a register computed in the
first one. A machine-specific peephole optimizer can detect such
opportunities.

There are two forms of peephole definitions that may be used. The
original `define_peephole` is run at assembly output time to
match insns and substitute assembly text. Use of `define_peephole`
is deprecated.

A newer `define_peephole2` matches insns and substitutes new
insns. The `peephole2` pass is run after register allocation
but before scheduling, which may result in much better code for
targets that do scheduling.

- [define_peephole](define_005fpeephole.md#apple-mrswm2lomvptambvmzygkzlqnbxwyzi): RTL to Text Peephole Optimizers
- [define_peephole2](define_005fpeephole2.md#apple-mrswm2lomvptambvmzygkzlqnbxwyzjs): RTL to RTL Peephole Optimizers
