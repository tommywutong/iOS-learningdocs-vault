---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Constants.html
archived_at: '2026-07-15T07:31:01.574029Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Regs and Memory](Regs-and-Memory.md#apple-kjswo4znmfxgilknmvww64tz),
Previous: [Machine Modes](Machine-Modes.md#apple-jvqwg2djnzss2tlpmrsxg),
Up: [RTL](RTL.md#apple-kjkey)

---

### 12.7 Constant Expression Types

The simplest RTL expressions are those that represent constant values.

**`(const_int` i`)`**
: This type of expression represents the integer value i. i
is customarily accessed with the macro `INTVAL` as in
`INTVAL (`exp`)`, which is equivalent to `XWINT (`exp`, 0)`.

Constants generated for modes with fewer bits than `HOST_WIDE_INT`
must be sign extended to full width (e.g., with `gen_int_mode`).

There is only one expression object for the integer value zero; it is
the value of the variable `const0_rtx`. Likewise, the only
expression for integer value one is found in `const1_rtx`, the only
expression for integer value two is found in `const2_rtx`, and the
only expression for integer value negative one is found in
`constm1_rtx`. Any attempt to create an expression of code
`const_int` and value zero, one, two or negative one will return
`const0_rtx`, `const1_rtx`, `const2_rtx` or
`constm1_rtx` as appropriate.

Similarly, there is only one object for the integer whose value is
`STORE_FLAG_VALUE`. It is found in `const_true_rtx`. If
`STORE_FLAG_VALUE` is one, `const_true_rtx` and
`const1_rtx` will point to the same object. If
`STORE_FLAG_VALUE` is −1, `const_true_rtx` and
`constm1_rtx` will point to the same object.

**`(const_double:`m addr i0 i1 `...)`**
: Represents either a floating-point constant of mode m or an
integer constant too large to fit into `HOST_BITS_PER_WIDE_INT`
bits but small enough to fit within twice that number of bits (GCC
does not provide a mechanism to represent even larger constants). In
the latter case, m will be `VOIDmode`.

**`(const_vector:`m `[`x0 x1 `...])`**
: Represents a vector constant. The square brackets stand for the vector
containing the constant elements. x0, x1 and so on are
the `const_int` or `const_double` elements.

The number of units in a `const_vector` is obtained with the macro
`CONST_VECTOR_NUNITS` as in `CONST_VECTOR_NUNITS (`v`)`.

Individual elements in a vector constant are accessed with the macro
`CONST_VECTOR_ELT` as in `CONST_VECTOR_ELT (`v`,` n`)`
where v is the vector constant and n is the element
desired.

addr is used to contain the `mem` expression that corresponds
to the location in memory that at which the constant can be found. If
it has not been allocated a memory location, but is on the chain of all
`const_double` expressions in this compilation (maintained using an
undisplayed field), addr contains `const0_rtx`. If it is not
on the chain, addr contains `cc0_rtx`. addr is
customarily accessed with the macro `CONST_DOUBLE_MEM` and the
chain field via `CONST_DOUBLE_CHAIN`.

If m is `VOIDmode`, the bits of the value are stored in
i0 and i1. i0 is customarily accessed with the macro
`CONST_DOUBLE_LOW` and i1 with `CONST_DOUBLE_HIGH`.

If the constant is floating point (regardless of its precision), then
the number of integers used to store the value depends on the size of
`REAL_VALUE_TYPE` (see [Floating Point](Floating-Point.md#apple-izwg6ylunfxgolkqn5uw45a)). The integers
represent a floating point number, but not precisely in the target
machine's or host machine's floating point format. To convert them to
the precise bit pattern used by the target machine, use the macro
`REAL_VALUE_TO_TARGET_DOUBLE` and friends (see [Data Output](Data-Output.md#apple-irqxiyjnj52xi4dvoq)).

The macro `CONST0_RTX (`mode`)` refers to an expression with
value 0 in mode mode. If mode mode is of mode class
`MODE_INT`, it returns `const0_rtx`. If mode mode is of
mode class `MODE_FLOAT`, it returns a `CONST_DOUBLE`
expression in mode mode. Otherwise, it returns a
`CONST_VECTOR` expression in mode mode. Similarly, the macro
`CONST1_RTX (`mode`)` refers to an expression with value 1 in
mode mode and similarly for `CONST2_RTX`. The
`CONST1_RTX` and `CONST2_RTX` macros are undefined
for vector modes.

**`(const_string` str`)`**
: Represents a constant string with value str. Currently this is
used only for insn attributes (see [Insn Attributes](Insn-Attributes.md#apple-jfxhg3rnif2hi4tjmj2xizlt)) since constant
strings in C are placed in memory.

**`(symbol_ref:`mode symbol`)`**
: Represents the value of an assembler label for data. symbol is
a string that describes the name of the assembler label. If it starts
with a ``*`', the label is the rest of symbol not including
the ``*`'. Otherwise, the label is symbol, usually prefixed
with ``_`'.

The `symbol_ref` contains a mode, which is usually `Pmode`.
Usually that is the only mode for which a symbol is directly valid.

**`(label_ref:`mode label`)`**
: Represents the value of an assembler label for code. It contains one
operand, an expression, which must be a `code_label` or a `note`
of type `NOTE_INSN_DELETED_LABEL` that appears in the instruction
sequence to identify the place where the label should go.

The reason for using a distinct expression type for code label
references is so that jump optimization can distinguish them.

The `label_ref` contains a mode, which is usually `Pmode`.
Usually that is the only mode for which a label is directly valid.

**`(const:`m exp`)`**
: Represents a constant that is the result of an assembly-time
arithmetic computation. The operand, exp, is an expression that
contains only constants (`const_int`, `symbol_ref` and
`label_ref` expressions) combined with `plus` and
`minus`. However, not all combinations are valid, since the
assembler cannot do arbitrary arithmetic on relocatable symbols.

m should be `Pmode`.

**`(high:`m exp`)`**
: Represents the high-order bits of exp, usually a
`symbol_ref`. The number of bits is machine-dependent and is
normally the number of bits specified in an instruction that initializes
the high order bits of a register. It is used with `lo_sum` to
represent the typical two-instruction sequence used in RISC machines to
reference a global memory location.

m should be `Pmode`.
