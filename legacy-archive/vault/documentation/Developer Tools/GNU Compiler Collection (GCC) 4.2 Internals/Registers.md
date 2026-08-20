---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Registers.html
archived_at: '2026-07-15T07:31:02.703035Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Register Classes](Register-Classes.md#apple-kjswo2ltorsxelkdnrqxg43fom),
Previous: [Type Layout](Type-Layout.md#apple-kr4xazjnjrqxs33voq),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.7 Register Usage

This section explains how to describe what registers the target machine
has, and how (in general) they can be used.

The description of which registers a specific instruction can use is
done with register classes; see [Register Classes](Register-Classes.md#apple-kjswo2ltorsxelkdnrqxg43fom). For information
on using registers to access a stack frame, see [Frame Registers](Frame-Registers.md#apple-izzgc3lffvjgkz3jon2gk4tt).
For passing values in registers, see [Register Arguments](Register-Arguments.md#apple-kjswo2ltorsxelkbojtxk3lfnz2hg).
For returning values in registers, see [Scalar Return](Scalar-Return.md#apple-knrwc3dboiwvezluovzg4).

- [Register Basics](Register-Basics.md#apple-kjswo2ltorsxelkcmfzwsy3t): Number and kinds of registers.
- [Allocation Order](Allocation-Order.md#apple-ifwgy33dmf2gs33ofvhxezdfoi): Order in which registers are allocated.
- [Values in Registers](Values-in-Registers.md#apple-kzqwy5lfomwws3rnkjswo2ltorsxe4y): What kinds of values each reg can hold.
- [Leaf Functions](Leaf-Functions.md#apple-jrswczrniz2w4y3unfxw44y): Renumbering registers for leaf functions.
- [Stack Registers](Stack-Registers.md#apple-kn2gcy3lfvjgkz3jon2gk4tt): Handling a register stack such as 80387.
