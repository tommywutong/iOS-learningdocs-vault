---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Libgcc.html
archived_at: '2026-07-15T07:31:02.211228Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Languages](Languages.md#apple-jrqw4z3vmftwk4y),
Previous: [Interface](Interface.md#apple-jfxhizlsmzqwgzi),
Up: [Top](index.md#apple-krxxa)

---

## 4 The GCC low-level runtime library

GCC provides a low-level runtime library, `libgcc.a` or
`libgcc_s.so.1` on some platforms. GCC generates calls to
routines in this library automatically, whenever it needs to perform
some operation that is too complicated to emit inline code for.

Most of the routines in `libgcc` handle arithmetic operations
that the target processor cannot perform directly. This includes
integer multiply and divide on some machines, and all floating-point
operations on other machines. `libgcc` also includes routines
for exception handling, and a handful of miscellaneous operations.

Some of these routines can be defined in mostly machine-independent C.
Others must be hand-written in assembly language for each processor
that needs them.

GCC will also generate calls to C library routines, such as
`memcpy` and `memset`, in some cases. The set of routines
that GCC may possibly use is documented in [Other Builtins](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gcc/Other-Builtins.html#Other-Builtins).

These routines take arguments and return values of a specific machine
mode, not a specific C type. See [Machine Modes](Machine-Modes.md#apple-jvqwg2djnzss2tlpmrsxg), for an explanation
of this concept. For illustrative purposes, in this chapter the
floating point type `float` is assumed to correspond to `SFmode`;
`double` to `DFmode`; and `long double` to both
`TFmode` and `XFmode`. Similarly, the integer types `int`
and `unsigned int` correspond to `SImode`; `long` and
`unsigned long` to `DImode`; and `long long` and
`unsigned long long` to `TImode`.

- [Integer library routines](Integer-library-routines.md#apple-jfxhizlhmvzc23djmjzgc4tzfvzg65lunfxgk4y)
- [Soft float library routines](Soft-float-library-routines.md#apple-knxwm5bnmzwg6ylufvwgsytsmfzhsllsn52xi2lomvzq)
- [Decimal float library routines](Decimal-float-library-routines.md#apple-irswg2lnmfwc2ztmn5qxillmnfrheylspewxe33voruw4zlt)
- [Exception handling routines](Exception-handling-routines.md#apple-iv4ggzlqoruw63rnnbqw4zdmnfxgollsn52xi2lomvzq)
- [Miscellaneous routines](Miscellaneous-routines.md#apple-jvuxgy3fnrwgc3tfn52xgllsn52xi2lomvzq)
