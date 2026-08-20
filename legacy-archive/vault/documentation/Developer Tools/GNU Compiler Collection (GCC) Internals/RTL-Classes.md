---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/RTL-Classes.html
archived_at: '2026-07-15T07:31:00.568127Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Accessors](Accessors.md#apple-ifrwgzltonxxe4y),
Previous: [RTL Objects](RTL-Objects.md#apple-kjkeylkpmjvgky3uom),
Up: [RTL](RTL.md#apple-kjkey)

---

### 10.2 RTL Classes and Formats

The various expression codes are divided into several classes,
which are represented by single characters. You can determine the class
of an RTX code with the macro `GET_RTX_CLASS (`code`)`.
Currently, `rtx.def` defines these classes:

**`RTX_OBJ`**
: An RTX code that represents an actual object, such as a register
(`REG`) or a memory location (`MEM`, `SYMBOL_REF`).
`LO_SUM`) is also included; instead, `SUBREG` and
`STRICT_LOW_PART` are not in this class, but in class `x`.

**`RTX_CONST_OBJ`**
: An RTX code that represents a constant object. `HIGH` is also
included in this class.

**`RTX_COMPARE`**
: An RTX code for a non-symmetric comparison, such as `GEU` or
`LT`.

**`RTX_COMM_COMPARE`**
: An RTX code for a symmetric (commutative) comparison, such as `EQ`
or `ORDERED`.

**`RTX_UNARY`**
: An RTX code for a unary arithmetic operation, such as `NEG`,
`NOT`, or `ABS`. This category also includes value extension
(sign or zero) and conversions between integer and floating point.

**`RTX_COMM_ARITH`**
: An RTX code for a commutative binary operation, such as `PLUS` or
`AND`. `NE` and `EQ` are comparisons, so they have class
`<`.

**`RTX_BIN_ARITH`**
: An RTX code for a non-commutative binary operation, such as `MINUS`,
`DIV`, or `ASHIFTRT`.

**`RTX_BITFIELD_OPS`**
: An RTX code for a bit-field operation. Currently only
`ZERO_EXTRACT` and `SIGN_EXTRACT`. These have three inputs
and are lvalues (so they can be used for insertion as well).
See [Bit-Fields](Bit_002dFields.md#apple-ijuxixzqgazgirtjmvwgi4y).

**`RTX_TERNARY`**
: An RTX code for other three input operations. Currently only
`IF_THEN_ELSE` and `VEC_MERGE`.

**`RTX_INSN`**
: An RTX code for an entire instruction: `INSN`, `JUMP_INSN`, and
`CALL_INSN`. See [Insns](Insns.md#apple-jfxhg3tt).

**`RTX_MATCH`**
: An RTX code for something that matches in insns, such as
`MATCH_DUP`. These only occur in machine descriptions.

**`RTX_AUTOINC`**
: An RTX code for an auto-increment addressing mode, such as
`POST_INC`.

**`RTX_EXTRA`**
: All other RTX codes. This category includes the remaining codes used
only in machine descriptions (`DEFINE_*`, etc.). It also includes
all the codes describing side effects (`SET`, `USE`,
`CLOBBER`, etc.) and the non-insns that may appear on an insn
chain, such as `NOTE`, `BARRIER`, and `CODE_LABEL`.
`SUBREG` is also part of this class.

For each expression code, `rtl.def` specifies the number of
contained objects and their kinds using a sequence of characters
called the format of the expression code. For example,
the format of `subreg` is ``ei`'.

These are the most commonly used format characters:

**`e`**
: An expression (actually a pointer to an expression).

**`i`**
: An integer.

**`w`**
: A wide integer.

**`s`**
: A string.

**`E`**
: A vector of expressions.

A few other format characters are used occasionally:

**`u`**
: ``u`' is equivalent to ``e`' except that it is printed differently
in debugging dumps. It is used for pointers to insns.

**`n`**
: ``n`' is equivalent to ``i`' except that it is printed differently
in debugging dumps. It is used for the line number or code number of a
`note` insn.

**`S`**
: ``S`' indicates a string which is optional. In the RTL objects in
core, ``S`' is equivalent to ``s`', but when the object is read,
from an ``md`' file, the string value of this operand may be omitted.
An omitted string is taken to be the null string.

**`V`**
: ``V`' indicates a vector which is optional. In the RTL objects in
core, ``V`' is equivalent to ``E`', but when the object is read
from an ``md`' file, the vector value of this operand may be omitted.
An omitted vector is effectively the same as a vector of no elements.

**`B`**
: ``B`' indicates a pointer to basic block structure.

**`0`**
: ``0`' means a slot whose contents do not fit any normal category.
``0`' slots are not printed at all in dumps, and are often used in
special ways by small parts of the compiler.

There are macros to get the number of operands and the format
of an expression code:

**`GET_RTX_LENGTH (`code`)`**
: Number of operands of an RTX of code code.

**`GET_RTX_FORMAT (`code`)`**
: The format of an RTX of code code, as a C string.

Some classes of RTX codes always have the same format. For example, it
is safe to assume that all comparison operations have format `ee`.

**`1`**
: All codes of this class have format `e`.

**`<`

**`c`

**`2`******
: All codes of these classes have format `ee`.

**`b`

**`3`****
: All codes of these classes have format `eee`.

**`i`**
: All codes of this class have formats that begin with `iuueiee`.
See [Insns](Insns.md#apple-jfxhg3tt). Note that not all RTL objects linked onto an insn chain
are of class `i`.

**`o`

**`m`

**`x`******
: You can make no assumptions about the format of these codes.
