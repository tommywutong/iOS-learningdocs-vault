---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Anchored-Addresses.html
archived_at: '2026-07-15T07:31:01.195513Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Condition Code](Condition-Code.md#apple-inxw4zdjoruw63rninxwizi),
Previous: [Addressing Modes](Addressing-Modes.md#apple-ifsgi4tfonzws3thfvgw6zdfom),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.15 Anchored Addresses

GCC usually addresses every static object as a separate entity.
For example, if we have:

```
     static int a, b, c;
     int foo (void) { return a + b + c; }
```

the code for `foo` will usually calculate three separate symbolic
addresses: those of `a`, `b` and `c`. On some targets,
it would be better to calculate just one symbolic address and access
the three variables relative to it. The equivalent pseudocode would
be something like:

```
     int foo (void)
     {
       register int *xr = &x;
       return xr[&a - &x] + xr[&b - &x] + xr[&c - &x];
     }
```

(which isn't valid C). We refer to shared addresses like `x` as
“section anchors”. Their use is controlled by `-fsection-anchors`.

The hooks below describe the target properties that GCC needs to know
in order to make effective use of section anchors. It won't use
section anchors at all unless either `TARGET_MIN_ANCHOR_OFFSET`
or `TARGET_MAX_ANCHOR_OFFSET` is set to a nonzero value.

— Variable: Target Hook __HOST_WIDE_INT__ TARGET_MIN_ANCHOR_OFFSET
> The minimum offset that should be applied to a section anchor.
> On most targets, it should be the smallest offset that can be
> applied to a base register while still giving a legitimate address
> for every mode. The default value is 0.

— Variable: Target Hook __HOST_WIDE_INT__ TARGET_MAX_ANCHOR_OFFSET
> Like `TARGET_MIN_ANCHOR_OFFSET`, but the maximum (inclusive)
> offset that should be applied to section anchors. The default
> value is 0.

— Target Hook: void __TARGET_ASM_OUTPUT_ANCHOR__ (rtx x)
> Write the assembly code to define section anchor x, which is a
> `SYMBOL_REF` for which ``SYMBOL_REF_ANCHOR_P (x)`' is true.
> The hook is called with the assembly output position set to the beginning
> of `SYMBOL_REF_BLOCK (`x`)`.
>
> If `ASM_OUTPUT_DEF` is available, the hook's default definition uses
> it to define the symbol as ``. + SYMBOL_REF_BLOCK_OFFSET (x)`'.
> If `ASM_OUTPUT_DEF` is not available, the hook's default definition
> is `NULL`, which disables the use of section anchors altogether.

— Target Hook: bool __TARGET_USE_ANCHORS_FOR_SYMBOL_P__ (rtx x)
> Return true if GCC should attempt to use anchors to access `SYMBOL_REF`
> x. You can assume ``SYMBOL_REF_HAS_BLOCK_INFO_P (x)`' and
> ``!SYMBOL_REF_ANCHOR_P (x)`'.
>
> The default version is correct for most targets, but you might need to
> intercept this hook to handle things like target-specific attributes
> or target-specific sections.
