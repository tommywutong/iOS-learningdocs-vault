---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Macros.html
archived_at: '2026-07-15T07:31:00.338350Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [Constant Definitions](Constant-Definitions.md#apple-inxw443umfxhilkemvtgs3tjoruw63tt),
Up: [Machine Desc](Machine-Desc.md#apple-jvqwg2djnzss2rdfonrq)

---

### 12.22 Macros

Ports often need to define similar patterns for more than one machine
mode or for more than one rtx code. GCC provides some simple macro
facilities to make this process easier.

- [Mode Macros](Mode-Macros.md#apple-jvxwizjnjvqwg4tpom): Generating variations of patterns for different modes.
- [Code Macros](Code-Macros.md#apple-inxwizjnjvqwg4tpom): Doing the same for codes.
