---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Conversions.html
archived_at: '2026-07-15T07:30:59.648596Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [RTL Declarations](RTL-Declarations.md#apple-kjkeylkemvrwyylsmf2gs33oom),
Previous: [Vector Operations](Vector-Operations.md#apple-kzswg5dpoiwu64dfojqxi2lpnzzq),
Up: [RTL](RTL.md#apple-kjkey)

---

### 10.13 Conversions

All conversions between machine modes must be represented by
explicit conversion operations. For example, an expression
which is the sum of a byte and a full word cannot be written as
`(plus:SI (reg:QI 34) (reg:SI 80))` because the `plus`
operation requires two operands of the same machine mode.
Therefore, the byte-sized operand is enclosed in a conversion
operation, as in

```
     (plus:SI (sign_extend:SI (reg:QI 34)) (reg:SI 80))
```

The conversion operation is not a mere placeholder, because there
may be more than one way of converting from a given starting mode
to the desired final mode. The conversion operation code says how
to do it.

For all conversion operations, x must not be `VOIDmode`
because the mode in which to do the conversion would not be known.
The conversion must either be done at compile-time or x
must be placed into a register.

**`(sign_extend:`m x`)`**
: Represents the result of sign-extending the value x
to machine mode m. m must be a fixed-point mode
and x a fixed-point value of a mode narrower than m.

**`(zero_extend:`m x`)`**
: Represents the result of zero-extending the value x
to machine mode m. m must be a fixed-point mode
and x a fixed-point value of a mode narrower than m.

**`(float_extend:`m x`)`**
: Represents the result of extending the value x
to machine mode m. m must be a floating point mode
and x a floating point value of a mode narrower than m.

**`(truncate:`m x`)`**
: Represents the result of truncating the value x
to machine mode m. m must be a fixed-point mode
and x a fixed-point value of a mode wider than m.

**`(ss_truncate:`m x`)`**
: Represents the result of truncating the value x
to machine mode m, using signed saturation in the case of
overflow. Both m and the mode of x must be fixed-point
modes.

**`(us_truncate:`m x`)`**
: Represents the result of truncating the value x
to machine mode m, using unsigned saturation in the case of
overflow. Both m and the mode of x must be fixed-point
modes.

**`(float_truncate:`m x`)`**
: Represents the result of truncating the value x
to machine mode m. m must be a floating point mode
and x a floating point value of a mode wider than m.

**`(float:`m x`)`**
: Represents the result of converting fixed point value x,
regarded as signed, to floating point mode m.

**`(unsigned_float:`m x`)`**
: Represents the result of converting fixed point value x,
regarded as unsigned, to floating point mode m.

**`(fix:`m x`)`**
: When m is a fixed point mode, represents the result of
converting floating point value x to mode m, regarded as
signed. How rounding is done is not specified, so this operation may
be used validly in compiling C code only for integer-valued operands.

**`(unsigned_fix:`m x`)`**
: Represents the result of converting floating point value x to
fixed point mode m, regarded as unsigned. How rounding is done
is not specified.

**`(fix:`m x`)`**
: When m is a floating point mode, represents the result of
converting floating point value x (valid for mode m) to an
integer, still represented in floating point mode m, by rounding
towards zero.
