---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Comparisons.html
archived_at: '2026-07-15T07:30:59.387863Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Bit-Fields](Bit_002dFields.md#apple-ijuxixzqgazgirtjmvwgi4y),
Previous: [Arithmetic](Arithmetic.md#apple-ifzgs5dinvsxi2ld),
Up: [RTL](RTL.md#apple-kjkey)

---

### 10.10 Comparison Operations

Comparison operators test a relation on two operands and are considered
to represent a machine-dependent nonzero value described by, but not
necessarily equal to, `STORE_FLAG_VALUE` (see [Misc](Misc.md#apple-jvuxgyy))
if the relation holds, or zero if it does not, for comparison operators
whose results have a `MODE_INT' mode,
`FLOAT_STORE_FLAG_VALUE` (see [Misc](Misc.md#apple-jvuxgyy)) if the relation holds, or
zero if it does not, for comparison operators that return floating-point
values, and a vector of either `VECTOR_STORE_FLAG_VALUE` (see [Misc](Misc.md#apple-jvuxgyy))
if the relation holds, or of zeros if it does not, for comparison operators
that return vector results.
The mode of the comparison operation is independent of the mode
of the data being compared. If the comparison operation is being tested
(e.g., the first operand of an `if_then_else`), the mode must be
`VOIDmode`.

There are two ways that comparison operations may be used. The
comparison operators may be used to compare the condition codes
`(cc0)` against zero, as in `(eq (cc0) (const_int 0))`. Such
a construct actually refers to the result of the preceding instruction
in which the condition codes were set. The instruction setting the
condition code must be adjacent to the instruction using the condition
code; only `note` insns may separate them.

Alternatively, a comparison operation may directly compare two data
objects. The mode of the comparison is determined by the operands; they
must both be valid for a common machine mode. A comparison with both
operands constant would be invalid as the machine mode could not be
deduced from it, but such a comparison should never exist in RTL due to
constant folding.

In the example above, if `(cc0)` were last set to
`(compare` x y`)`, the comparison operation is
identical to `(eq` x y`)`. Usually only one style
of comparisons is supported on a particular machine, but the combine
pass will try to merge the operations to produce the `eq` shown
in case it exists in the context of the particular insn involved.

Inequality comparisons come in two flavors, signed and unsigned. Thus,
there are distinct expression codes `gt` and `gtu` for signed and
unsigned greater-than. These can produce different results for the same
pair of integer values: for example, 1 is signed greater-than −1 but not
unsigned greater-than, because −1 when regarded as unsigned is actually
`0xffffffff` which is greater than 1.

The signed comparisons are also used for floating point values. Floating
point comparisons are distinguished by the machine modes of the operands.

**`(eq:`m x y`)`**
: `STORE_FLAG_VALUE` if the values represented by x and y
are equal, otherwise 0.

**`(ne:`m x y`)`**
: `STORE_FLAG_VALUE` if the values represented by x and y
are not equal, otherwise 0.

**`(gt:`m x y`)`**
: `STORE_FLAG_VALUE` if the x is greater than y. If they
are fixed-point, the comparison is done in a signed sense.

**`(gtu:`m x y`)`**
: Like `gt` but does unsigned comparison, on fixed-point numbers only.

**`(lt:`m x y`)`

**`(ltu:`m x y`)`****
: Like `gt` and `gtu` but test for “less than”.

**`(ge:`m x y`)`

**`(geu:`m x y`)`****
: Like `gt` and `gtu` but test for “greater than or equal”.

**`(le:`m x y`)`

**`(leu:`m x y`)`****
: Like `gt` and `gtu` but test for “less than or equal”.

**`(if_then_else` cond then else`)`**
: This is not a comparison operation but is listed here because it is
always used in conjunction with a comparison operation. To be
precise, cond is a comparison expression. This expression
represents a choice, according to cond, between the value
represented by then and the one represented by else.

On most machines, `if_then_else` expressions are valid only
to express conditional jumps.

**`(cond [`test1 value1 test2 value2 `...]` default`)`**
: Similar to `if_then_else`, but more general. Each of test1,
test2, ... is performed in turn. The result of this expression is
the value corresponding to the first nonzero test, or default if
none of the tests are nonzero expressions.

This is currently not valid for instruction patterns and is supported only
for insn attributes. See [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt).
