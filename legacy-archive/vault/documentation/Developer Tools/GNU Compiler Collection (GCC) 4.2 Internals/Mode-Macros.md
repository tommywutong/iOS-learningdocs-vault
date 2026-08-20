---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Mode-Macros.html
archived_at: '2026-07-15T07:31:02.403444Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Code Macros](Code-Macros.md#apple-inxwizjnjvqwg4tpom),
Up: [Macros](Macros.md#apple-jvqwg4tpom)

---

#### 14.22.1 Mode Macros

Ports often need to define similar patterns for two or more different modes.
For example:

- If a processor has hardware support for both single and double
  floating-point arithmetic, the `SFmode` patterns tend to be
  very similar to the `DFmode` ones.
- If a port uses `SImode` pointers in one configuration and
  `DImode` pointers in another, it will usually have very similar
  `SImode` and `DImode` patterns for manipulating pointers.

Mode macros allow several patterns to be instantiated from one
`.md` file template. They can be used with any type of
rtx-based construct, such as a `define_insn`,
`define_split`, or `define_peephole2`.

- [Defining Mode Macros](Defining-Mode-Macros.md#apple-irswm2lonfxgolknn5sgklknmfrxe33t): Defining a new mode macro.
- [Substitutions](Substitutions.md#apple-kn2we43unf2hk5djn5xhg): Combining mode macros with substitutions
- [Examples](Examples.md#apple-iv4gc3lqnrsxg): Examples
