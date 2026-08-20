---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/MIPS-Coprocessors.html
archived_at: '2026-07-15T07:31:02.270915Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [PCH Target](PCH-Target.md#apple-kbbuqlkumfzgozlu),
Previous: [Target Attributes](Target-Attributes.md#apple-krqxez3foqwuc5duojuwe5lumvzq),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.26 Defining coprocessor specifics for MIPS targets.

The MIPS specification allows MIPS implementations to have as many as 4
coprocessors, each with as many as 32 private registers. GCC supports
accessing these registers and transferring values between the registers
and memory using asm-ized variables. For example:

```
       register unsigned int cp0count asm ("c0r1");
       unsigned int d;

       d = cp0count + 3;
```

(“c0r1” is the default name of register 1 in coprocessor 0; alternate
names may be added as described below, or the default names may be
overridden entirely in `SUBTARGET_CONDITIONAL_REGISTER_USAGE`.)

Coprocessor registers are assumed to be epilogue-used; sets to them will
be preserved even if it does not appear that the register is used again
later in the function.

Another note: according to the MIPS spec, coprocessor 1 (if present) is
the FPU. One accesses COP1 registers through standard mips
floating-point support; they are not included in this mechanism.

There is one macro used in defining the MIPS coprocessor interface which
you may want to override in subtargets; it is described below.

— Macro: __ALL_COP_ADDITIONAL_REGISTER_NAMES__
> A comma-separated list (with leading comma) of pairs describing the
> alternate names of coprocessor registers. The format of each entry should be
>
> ```
>           { alternatename, register_number}
>
> ```
>
> Default: empty.
