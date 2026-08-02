---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Arithmetic.html
archived_at: '2026-07-15T07:31:01.206417Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Comparisons](Comparisons.md#apple-inxw24dbojuxg33oom),
Previous: [Regs and Memory](Regs-and-Memory.md#apple-kjswo4znmfxgilknmvww64tz),
Up: [RTL](RTL.md#apple-kjkey)

---

### 12.9 RTL Expressions for Arithmetic

Unless otherwise specified, all the operands of arithmetic expressions
must be valid for mode m. An operand is valid for mode m
if it has mode m, or if it is a `const_int` or
`const_double` and m is a mode of class `MODE_INT`.

For commutative binary operations, constants should be placed in the
second operand.

**`(plus:`m x y`)`

**`(ss_plus:`m x y`)`

**`(us_plus:`m x y`)`******
: These three expressions all represent the sum of the values
represented by x and y carried out in machine mode
m. They differ in their behavior on overflow of integer modes.
`plus` wraps round modulo the width of m; `ss_plus`
saturates at the maximum signed value representable in m;
`us_plus` saturates at the maximum unsigned value.

**`(lo_sum:`m x y`)`**
: This expression represents the sum of x and the low-order bits
of y. It is used with `high` (see [Constants](Constants.md#apple-inxw443umfxhi4y)) to
represent the typical two-instruction sequence used in RISC machines
to reference a global memory location.

The number of low order bits is machine-dependent but is
normally the number of bits in a `Pmode` item minus the number of
bits set by `high`.

m should be `Pmode`.

**`(minus:`m x y`)`

**`(ss_minus:`m x y`)`

**`(us_minus:`m x y`)`******
: These three expressions represent the result of subtracting y
from x, carried out in mode M. Behavior on overflow is
the same as for the three variants of `plus` (see above).

**`(compare:`m x y`)`**
: Represents the result of subtracting y from x for purposes
of comparison. The result is computed without overflow, as if with
infinite precision.

Of course, machines can't really subtract with infinite precision.
However, they can pretend to do so when only the sign of the result will
be used, which is the case when the result is stored in the condition
code. And that is the _only_ way this kind of expression may
validly be used: as a value to be stored in the condition codes, either
`(cc0)` or a register. See [Comparisons](Comparisons.md#apple-inxw24dbojuxg33oom).

The mode m is not related to the modes of x and y, but
instead is the mode of the condition code value. If `(cc0)` is
used, it is `VOIDmode`. Otherwise it is some mode in class
`MODE_CC`, often `CCmode`. See [Condition Code](Condition-Code.md#apple-inxw4zdjoruw63rninxwizi). If m
is `VOIDmode` or `CCmode`, the operation returns sufficient
information (in an unspecified format) so that any comparison operator
can be applied to the result of the `COMPARE` operation. For other
modes in class `MODE_CC`, the operation only returns a subset of
this information.

Normally, x and y must have the same mode. Otherwise,
`compare` is valid only if the mode of x is in class
`MODE_INT` and y is a `const_int` or
`const_double` with mode `VOIDmode`. The mode of x
determines what mode the comparison is to be done in; thus it must not
be `VOIDmode`.

If one of the operands is a constant, it should be placed in the
second operand and the comparison code adjusted as appropriate.

A `compare` specifying two `VOIDmode` constants is not valid
since there is no way to know in what mode the comparison is to be
performed; the comparison must either be folded during the compilation
or the first operand must be loaded into a register while its mode is
still known.

**`(neg:`m x`)`

**`(ss_neg:`m x`)`****
: These two expressions represent the negation (subtraction from zero) of
the value represented by x, carried out in mode m. They
differ in the behavior on overflow of integer modes. In the case of
`neg`, the negation of the operand may be a number not representable
in mode m, in which case it is truncated to m. `ss_neg`
ensures that an out-of-bounds result saturates to the maximum or minimum
representable value.

**`(mult:`m x y`)`**
: Represents the signed product of the values represented by x and
y carried out in machine mode m.

Some machines support a multiplication that generates a product wider
than the operands. Write the pattern for this as

```
          (mult:m (sign_extend:m x) (sign_extend:m y))

```

where m is wider than the modes of x and y, which need
not be the same.

For unsigned widening multiplication, use the same idiom, but with
`zero_extend` instead of `sign_extend`.

**`(div:`m x y`)`**
: Represents the quotient in signed division of x by y,
carried out in machine mode m. If m is a floating point
mode, it represents the exact quotient; otherwise, the integerized
quotient.

Some machines have division instructions in which the operands and
quotient widths are not all the same; you should represent
such instructions using `truncate` and `sign_extend` as in,

```
          (truncate:m1 (div:m2 x (sign_extend:m2 y)))

```


**`(udiv:`m x y`)`**
: Like `div` but represents unsigned division.

**`(mod:`m x y`)`

**`(umod:`m x y`)`****
: Like `div` and `udiv` but represent the remainder instead of
the quotient.

**`(smin:`m x y`)`

**`(smax:`m x y`)`****
: Represents the smaller (for `smin`) or larger (for `smax`) of
x and y, interpreted as signed values in mode m.
When used with floating point, if both operands are zeros, or if either
operand is `NaN`, then it is unspecified which of the two operands
is returned as the result.

**`(umin:`m x y`)`

**`(umax:`m x y`)`****
: Like `smin` and `smax`, but the values are interpreted as unsigned
integers.

**`(not:`m x`)`**
: Represents the bitwise complement of the value represented by x,
carried out in mode m, which must be a fixed-point machine mode.

**`(and:`m x y`)`**
: Represents the bitwise logical-and of the values represented by
x and y, carried out in machine mode m, which must be
a fixed-point machine mode.

**`(ior:`m x y`)`**
: Represents the bitwise inclusive-or of the values represented by x
and y, carried out in machine mode m, which must be a
fixed-point mode.

**`(xor:`m x y`)`**
: Represents the bitwise exclusive-or of the values represented by x
and y, carried out in machine mode m, which must be a
fixed-point mode.

**`(ashift:`m x c`)`

**`(ss_ashift:`m x c`)`****
: These two expressions represent the result of arithmetically shifting x
left by c places. They differ in their behavior on overflow of integer
modes. An `ashift` operation is a plain shift with no special behavior
in case of a change in the sign bit; `ss_ashift` saturates to the minimum
or maximum representable value if any of the bits shifted out differs from the
final sign bit.

x have mode m, a fixed-point machine mode. c
be a fixed-point mode or be a constant with mode `VOIDmode`; which
mode is determined by the mode called for in the machine description
entry for the left-shift instruction. For example, on the VAX, the mode
of c is `QImode` regardless of m.

**`(lshiftrt:`m x c`)`

**`(ashiftrt:`m x c`)`****
: Like `ashift` but for right shift. Unlike the case for left shift,
these two operations are distinct.

**`(rotate:`m x c`)`

**`(rotatert:`m x c`)`****
: Similar but represent left and right rotate. If c is a constant,
use `rotate`.

**`(abs:`m x`)`**
: Represents the absolute value of x, computed in mode m.

**`(sqrt:`m x`)`**
: Represents the square root of x, computed in mode m.
Most often m will be a floating point mode.

**`(ffs:`m x`)`**
: Represents one plus the index of the least significant 1-bit in
x, represented as an integer of mode m. (The value is
zero if x is zero.) The mode of x need not be m;
depending on the target machine, various mode combinations may be
valid.

**`(clz:`m x`)`**
: Represents the number of leading 0-bits in x, represented as an
integer of mode m, starting at the most significant bit position.
If x is zero, the value is determined by
`CLZ_DEFINED_VALUE_AT_ZERO`. Note that this is one of
the few expressions that is not invariant under widening. The mode of
x will usually be an integer mode.

**`(ctz:`m x`)`**
: Represents the number of trailing 0-bits in x, represented as an
integer of mode m, starting at the least significant bit position.
If x is zero, the value is determined by
`CTZ_DEFINED_VALUE_AT_ZERO`. Except for this case,
`ctz(x)` is equivalent to `ffs(`x`) - 1`. The mode of
x will usually be an integer mode.

**`(popcount:`m x`)`**
: Represents the number of 1-bits in x, represented as an integer of
mode m. The mode of x will usually be an integer mode.

**`(parity:`m x`)`**
: Represents the number of 1-bits modulo 2 in x, represented as an
integer of mode m. The mode of x will usually be an integer
mode.
