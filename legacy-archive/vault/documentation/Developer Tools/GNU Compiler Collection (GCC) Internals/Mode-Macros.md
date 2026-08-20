---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Mode-Macros.html
archived_at: '2026-07-15T07:31:00.401104Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Code Macros](Code-Macros.md#apple-inxwizjnjvqwg4tpom),
Up: [Macros](Macros.md#apple-jvqwg4tpom)

---

#### 12.22.1 Mode Macros

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
- [String Substitutions](String-Substitutions.md#apple-kn2he2lom4wvg5lcon2gs5dvoruw63tt): Combining mode macros with string substitutions
- [Examples](Examples.md#apple-iv4gc3lqnrsxg): Examples
