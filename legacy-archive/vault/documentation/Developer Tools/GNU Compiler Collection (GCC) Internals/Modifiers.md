---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Modifiers.html
archived_at: '2026-07-15T07:31:00.416981Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Machine Constraints](Machine-Constraints.md#apple-jvqwg2djnzss2q3pnzzxi4tbnfxhi4y),
Previous: [Class Preferences](Class-Preferences.md#apple-inwgc43tfvihezlgmvzgk3tdmvzq),
Up: [Constraints](Constraints.md#apple-inxw443uojqws3tuom)

---

#### 12.8.4 Constraint Modifier Characters

Here are constraint modifier characters.

**``=`'**
: Means that this operand is write-only for this instruction: the previous
value is discarded and replaced by output data.

**``+`'**
: Means that this operand is both read and written by the instruction.

When the compiler fixes up the operands to satisfy the constraints,
it needs to know which operands are inputs to the instruction and
which are outputs from it. ``=`' identifies an output; ``+`'
identifies an operand that is both input and output; all other operands
are assumed to be input only.

If you specify ``=`' or ``+`' in a constraint, you put it in the
first character of the constraint string.

**``&`'**
: Means (in a particular alternative) that this operand is an
earlyclobber operand, which is modified before the instruction is
finished using the input operands. Therefore, this operand may not lie
in a register that is used as an input operand or as part of any memory
address.

``&`' applies only to the alternative in which it is written. In
constraints with multiple alternatives, sometimes one alternative
requires ``&`' while others do not. See, for example, the
``movdf`' insn of the 68000.

An input operand can be tied to an earlyclobber operand if its only
use as an input occurs before the early result is written. Adding
alternatives of this form often allows GCC to produce better code
when only some of the inputs can be affected by the earlyclobber.
See, for example, the ``mulsi3`' insn of the ARM.

``&`' does not obviate the need to write ``=`'.

**``%`'**
: Declares the instruction to be commutative for this operand and the
following operand. This means that the compiler may interchange the
two operands if that is the cheapest way to make all operands fit the
constraints.
This is often used in patterns for addition instructions
that really have only two operands: the result must go in one of the
arguments. Here for example, is how the 68000 halfword-add
instruction is defined:

```
          (define_insn "addhi3"
            [(set (match_operand:HI 0 "general_operand" "=m,r")
               (plus:HI (match_operand:HI 1 "general_operand" "%0,0")
                        (match_operand:HI 2 "general_operand" "di,g")))]
            ...)

```

GCC can only handle one commutative pair in an asm; if you use more,
the compiler may fail. Note that you need not use the modifier if
the two alternatives are strictly identical; this would only waste
time in the reload pass.

**``#`'**
: Says that all following characters, up to the next comma, are to be
ignored as a constraint. They are significant only for choosing
register preferences.

**``*`'**
: Says that the following character should be ignored when choosing
register preferences. ``*`' has no effect on the meaning of the
constraint as a constraint, and no effect on reloading.

Here is an example: the 68000 has an instruction to sign-extend a
halfword in a data register, and can also sign-extend a value by
copying it into an address register. While either kind of register is
acceptable, the constraints on an address-register destination are
less strict, so it is best if register allocation makes an address
register its goal. Therefore, ``*`' is used so that the ``d`'
constraint letter (for data register) is ignored when computing
register preferences.

```
          (define_insn "extendhisi2"
            [(set (match_operand:SI 0 "general_operand" "=*d,a")
                  (sign_extend:SI
                   (match_operand:HI 1 "general_operand" "0,g")))]
            ...)

```
