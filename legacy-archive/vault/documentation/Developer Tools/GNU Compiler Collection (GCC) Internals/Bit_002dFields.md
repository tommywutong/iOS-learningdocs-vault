---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Bit_002dFields.html
archived_at: '2026-07-15T07:30:59.317723Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Vector Operations](Vector-Operations.md#apple-kzswg5dpoiwu64dfojqxi2lpnzzq),
Previous: [Comparisons](Comparisons.md#apple-inxw24dbojuxg33oom),
Up: [RTL](RTL.md#apple-kjkey)

---

### 10.11 Bit-Fields

Special expression codes exist to represent bit-field instructions.

**`(sign_extract:`m loc size pos`)`**
: This represents a reference to a sign-extended bit-field contained or
starting in loc (a memory or register reference). The bit-field
is size bits wide and starts at bit pos. The compilation
option `BITS_BIG_ENDIAN` says which end of the memory unit
pos counts from.

If loc is in memory, its mode must be a single-byte integer mode.
If loc is in a register, the mode to use is specified by the
operand of the `insv` or `extv` pattern
(see [Standard Names](Standard-Names.md#apple-kn2gc3temfzgilkomfwwk4y)) and is usually a full-word integer mode,
which is the default if none is specified.

The mode of pos is machine-specific and is also specified
in the `insv` or `extv` pattern.

The mode m is the same as the mode that would be used for
loc if it were a register.

A `sign_extract` can not appear as an lvalue, or part thereof,
in RTL.

**`(zero_extract:`m loc size pos`)`**
: Like `sign_extract` but refers to an unsigned or zero-extended
bit-field. The same sequence of bits are extracted, but they
are filled to an entire word with zeros instead of by sign-extension.

Unlike `sign_extract`, this type of expressions can be lvalues
in RTL; they may appear on the left side of an assignment, indicating
insertion of a value into the specified bit-field.
