---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Caller-Saves.html
archived_at: '2026-07-15T07:30:59.346758Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Function Entry](Function-Entry.md#apple-iz2w4y3unfxw4lkfnz2he6i),
Previous: [Aggregate Return](Aggregate-Return.md#apple-iftwo4tfm5qxizjnkjsxi5lsny),
Up: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq)

---

#### 13.9.10 Caller-Saves Register Allocation

If you enable it, GCC can save registers around function calls. This
makes it possible to use call-clobbered registers to hold variables that
must live across calls.

— Macro: __CALLER_SAVE_PROFITABLE__ (refs, calls)
> A C expression to determine whether it is worthwhile to consider placing
> a pseudo-register in a call-clobbered hard register and saving and
> restoring it around each function call. The expression should be 1 when
> this is worth doing, and 0 otherwise.
>
> If you don't define this macro, a default is used which is good on most
> machines: `4 *` calls `<` refs.

— Macro: __HARD_REGNO_CALLER_SAVE_MODE__ (regno, nregs)
> A C expression specifying which mode is required for saving nregs
> of a pseudo-register in call-clobbered hard register regno. If
> regno is unsuitable for caller save, `VOIDmode` should be
> returned. For most machines this macro need not be defined since GCC
> will select the smallest suitable mode.
