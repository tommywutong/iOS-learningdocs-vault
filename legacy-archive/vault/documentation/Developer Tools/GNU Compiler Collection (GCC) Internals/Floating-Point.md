---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Floating-Point.html
archived_at: '2026-07-15T07:30:59.888187Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Mode Switching](Mode-Switching.md#apple-jvxwizjnkn3ws5ddnbuw4zy),
Previous: [Debugging Info](Debugging-Info.md#apple-irswe5lhm5uw4zznjfxgm3y),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 13.21 Cross Compilation and Floating Point

While all modern machines use twos-complement representation for integers,
there are a variety of representations for floating point numbers. This
means that in a cross-compiler the representation of floating point numbers
in the compiled program may be different from that used in the machine
doing the compilation.

Because different representation systems may offer different amounts of
range and precision, all floating point constants must be represented in
the target machine's format. Therefore, the cross compiler cannot
safely use the host machine's floating point arithmetic; it must emulate
the target's arithmetic. To ensure consistency, GCC always uses
emulation to work with floating point values, even when the host and
target floating point formats are identical.

The following macros are provided by `real.h` for the compiler to
use. All parts of the compiler which generate or optimize
floating-point calculations must use these macros. They may evaluate
their operands more than once, so operands must not have side effects.

— Macro: __REAL_VALUE_TYPE__
> The C data type to be used to hold a floating point value in the target
> machine's format. Typically this is a `struct` containing an
> array of `HOST_WIDE_INT`, but all code should treat it as an opaque
> quantity.

— Macro: int __REAL_VALUES_EQUAL__ (REAL_VALUE_TYPE x, REAL_VALUE_TYPE y)
> Compares for equality the two values, x and y. If the target
> floating point format supports negative zeroes and/or NaNs,
> ``REAL_VALUES_EQUAL (-0.0, 0.0)`' is true, and
> ``REAL_VALUES_EQUAL (NaN, NaN)`' is false.

— Macro: int __REAL_VALUES_LESS__ (REAL_VALUE_TYPE x, REAL_VALUE_TYPE y)
> Tests whether x is less than y.

— Macro: HOST_WIDE_INT __REAL_VALUE_FIX__ (REAL_VALUE_TYPE x)
> Truncates x to a signed integer, rounding toward zero.

— Macro: unsigned HOST_WIDE_INT __REAL_VALUE_UNSIGNED_FIX__ (REAL_VALUE_TYPE x)
> Truncates x to an unsigned integer, rounding toward zero. If
> x is negative, returns zero.

— Macro: REAL_VALUE_TYPE __REAL_VALUE_ATOF__ (const char \*string, enum machine_mode mode)
> Converts string into a floating point number in the target machine's
> representation for mode mode. This routine can handle both
> decimal and hexadecimal floating point constants, using the syntax
> defined by the C language for both.

— Macro: int __REAL_VALUE_NEGATIVE__ (REAL_VALUE_TYPE x)
> Returns 1 if x is negative (including negative zero), 0 otherwise.

— Macro: int __REAL_VALUE_ISINF__ (REAL_VALUE_TYPE x)
> Determines whether x represents infinity (positive or negative).

— Macro: int __REAL_VALUE_ISNAN__ (REAL_VALUE_TYPE x)
> Determines whether x represents a “NaN” (not-a-number).

— Macro: void __REAL_ARITHMETIC__ (REAL_VALUE_TYPE output, enum tree_code code, REAL_VALUE_TYPE x, REAL_VALUE_TYPE y)
> Calculates an arithmetic operation on the two floating point values
> x and y, storing the result in output (which must be a
> variable).
>
> The operation to be performed is specified by code. Only the
> following codes are supported: `PLUS_EXPR`, `MINUS_EXPR`,
> `MULT_EXPR`, `RDIV_EXPR`, `MAX_EXPR`, `MIN_EXPR`.
>
> If `REAL_ARITHMETIC` is asked to evaluate division by zero and the
> target's floating point format cannot represent infinity, it will call
> `abort`. Callers should check for this situation first, using
> `MODE_HAS_INFINITIES`. See [Storage Layout](Storage-Layout.md#apple-kn2g64tbm5ss2tdbpfxxk5a).

— Macro: REAL_VALUE_TYPE __REAL_VALUE_NEGATE__ (REAL_VALUE_TYPE x)
> Returns the negative of the floating point value x.

— Macro: REAL_VALUE_TYPE __REAL_VALUE_ABS__ (REAL_VALUE_TYPE x)
> Returns the absolute value of x.

— Macro: REAL_VALUE_TYPE __REAL_VALUE_TRUNCATE__ (REAL_VALUE_TYPE mode, enum machine_mode x)
> Truncates the floating point value x to fit in mode. The
> return value is still a full-size `REAL_VALUE_TYPE`, but it has an
> appropriate bit pattern to be output asa floating constant whose
> precision accords with mode mode.

— Macro: void __REAL_VALUE_TO_INT__ (HOST_WIDE_INT low, HOST_WIDE_INT high, REAL_VALUE_TYPE x)
> Converts a floating point value x into a double-precision integer
> which is then stored into low and high. If the value is not
> integral, it is truncated.

— Macro: void __REAL_VALUE_FROM_INT__ (REAL_VALUE_TYPE x, HOST_WIDE_INT low, HOST_WIDE_INT high, enum machine_mode mode)
> Converts a double-precision integer found in low and high,
> into a floating point value which is then stored into x. The
> value is truncated to fit in mode mode.
