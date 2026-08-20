---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Class-Preferences.html
archived_at: '2026-07-15T07:30:59.358024Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Modifiers](Modifiers.md#apple-jvxwi2lgnfsxe4y),
Previous: [Multi-Alternative](Multi_002dAlternative.md#apple-jv2wy5djl4ydamteifwhizlsnzqxi2lwmu),
Up: [Constraints](Constraints.md#apple-inxw443uojqws3tuom)

---

#### 12.8.3 Register Class Preferences

The operand constraints have another function: they enable the compiler
to decide which kind of hardware register a pseudo register is best
allocated to. The compiler examines the constraints that apply to the
insns that use the pseudo register, looking for the machine-dependent
letters such as ``d`' and ``a`' that specify classes of registers.
The pseudo register is put in whichever class gets the most “votes”.
The constraint letters ``g`' and ``r`' also vote: they vote in
favor of a general register. The machine description says which registers
are considered general.

Of course, on some machines all registers are equivalent, and no register
classes are defined. Then none of this complexity is relevant.
