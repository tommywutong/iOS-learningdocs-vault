---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Regs-and-Memory.html
archived_at: '2026-07-15T07:31:00.643551Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Arithmetic](Arithmetic.md#apple-ifzgs5dinvsxi2ld),
Previous: [Constants](Constants.md#apple-inxw443umfxhi4y),
Up: [RTL](RTL.md#apple-kjkey)

---

### 10.8 Registers and Memory

Here are the RTL expression types for describing access to machine
registers and to main memory.

**`(reg:`m n`)`**
: For small values of the integer n (those that are less than
`FIRST_PSEUDO_REGISTER`), this stands for a reference to machine
register number n: a hard register. For larger values of
n, it stands for a temporary value or pseudo register.
The compiler's strategy is to generate code assuming an unlimited
number of such pseudo registers, and later convert them into hard
registers or into memory references.

m is the machine mode of the reference. It is necessary because
machines can generally refer to each register in more than one mode.
For example, a register may contain a full word but there may be
instructions to refer to it as a half word or as a single byte, as
well as instructions to refer to it as a floating point number of
various precisions.

Even for a register that the machine can access in only one mode,
the mode must always be specified.

The symbol `FIRST_PSEUDO_REGISTER` is defined by the machine
description, since the number of hard registers on the machine is an
invariant characteristic of the machine. Note, however, that not
all of the machine registers must be general registers. All the
machine registers that can be used for storage of data are given
hard register numbers, even those that can be used only in certain
instructions or can hold only certain types of data.

A hard register may be accessed in various modes throughout one
function, but each pseudo register is given a natural mode
and is accessed only in that mode. When it is necessary to describe
an access to a pseudo register using a nonnatural mode, a `subreg`
expression is used.

A `reg` expression with a machine mode that specifies more than
one word of data may actually stand for several consecutive registers.
If in addition the register number specifies a hardware register, then
it actually represents several consecutive hardware registers starting
with the specified one.

Each pseudo register number used in a function's RTL code is
represented by a unique `reg` expression.

Some pseudo register numbers, those within the range of
`FIRST_VIRTUAL_REGISTER` to `LAST_VIRTUAL_REGISTER` only
appear during the RTL generation phase and are eliminated before the
optimization phases. These represent locations in the stack frame that
cannot be determined until RTL generation for the function has been
completed. The following virtual register numbers are defined:

**`VIRTUAL_INCOMING_ARGS_REGNUM`**
: This points to the first word of the incoming arguments passed on the
stack. Normally these arguments are placed there by the caller, but the
callee may have pushed some arguments that were previously passed in
registers.

When RTL generation is complete, this virtual register is replaced
by the sum of the register given by `ARG_POINTER_REGNUM` and the
value of `FIRST_PARM_OFFSET`.

**`VIRTUAL_STACK_VARS_REGNUM`**
: If `FRAME_GROWS_DOWNWARD` is defined, this points to immediately
above the first variable on the stack. Otherwise, it points to the
first variable on the stack.

`VIRTUAL_STACK_VARS_REGNUM` is replaced with the sum of the
register given by `FRAME_POINTER_REGNUM` and the value
`STARTING_FRAME_OFFSET`.

**`VIRTUAL_STACK_DYNAMIC_REGNUM`**
: This points to the location of dynamically allocated memory on the stack
immediately after the stack pointer has been adjusted by the amount of
memory desired.

This virtual register is replaced by the sum of the register given by
`STACK_POINTER_REGNUM` and the value `STACK_DYNAMIC_OFFSET`.

**`VIRTUAL_OUTGOING_ARGS_REGNUM`**
: This points to the location in the stack at which outgoing arguments
should be written when the stack is pre-pushed (arguments pushed using
push insns should always use `STACK_POINTER_REGNUM`).

This virtual register is replaced by the sum of the register given by
`STACK_POINTER_REGNUM` and the value `STACK_POINTER_OFFSET`.

**`(subreg:`m reg bytenum`)`**
: `subreg` expressions are used to refer to a register in a machine
mode other than its natural one, or to refer to one register of
a multi-part `reg` that actually refers to several registers.

Each pseudo-register has a natural mode. If it is necessary to
operate on it in a different mode—for example, to perform a fullword
move instruction on a pseudo-register that contains a single
byte—the pseudo-register must be enclosed in a `subreg`. In
such a case, bytenum is zero.

Usually m is at least as narrow as the mode of reg, in which
case it is restricting consideration to only the bits of reg that
are in m.

Sometimes m is wider than the mode of reg. These
`subreg` expressions are often called paradoxical. They are
used in cases where we want to refer to an object in a wider mode but do
not care what value the additional bits have. The reload pass ensures
that paradoxical references are only made to hard registers.

The other use of `subreg` is to extract the individual registers of
a multi-register value. Machine modes such as `DImode` and
`TImode` can indicate values longer than a word, values which
usually require two or more consecutive registers. To access one of the
registers, use a `subreg` with mode `SImode` and a
bytenum offset that says which register.

Storing in a non-paradoxical `subreg` has undefined results for
bits belonging to the same word as the `subreg`. This laxity makes
it easier to generate efficient code for such instructions. To
represent an instruction that preserves all the bits outside of those in
the `subreg`, use `strict_low_part` around the `subreg`.

The compilation parameter `WORDS_BIG_ENDIAN`, if set to 1, says
that byte number zero is part of the most significant word; otherwise,
it is part of the least significant word.

The compilation parameter `BYTES_BIG_ENDIAN`, if set to 1, says
that byte number zero is the most significant byte within a word;
otherwise, it is the least significant byte within a word.

On a few targets, `FLOAT_WORDS_BIG_ENDIAN` disagrees with
`WORDS_BIG_ENDIAN`.
However, most parts of the compiler treat floating point values as if
they had the same endianness as integer values. This works because
they handle them solely as a collection of integer values, with no
particular numerical value. Only real.c and the runtime libraries
care about `FLOAT_WORDS_BIG_ENDIAN`.

Between the combiner pass and the reload pass, it is possible to have a
paradoxical `subreg` which contains a `mem` instead of a
`reg` as its first operand. After the reload pass, it is also
possible to have a non-paradoxical `subreg` which contains a
`mem`; this usually occurs when the `mem` is a stack slot
which replaced a pseudo register.

Note that it is not valid to access a `DFmode` value in `SFmode`
using a `subreg`. On some machines the most significant part of a
`DFmode` value does not have the same format as a single-precision
floating value.

It is also not valid to access a single word of a multi-word value in a
hard register when less registers can hold the value than would be
expected from its size. For example, some 32-bit machines have
floating-point registers that can hold an entire `DFmode` value.
If register 10 were such a register `(subreg:SI (reg:DF 10) 4)`
would be invalid because there is no way to convert that reference to
a single machine register. The reload pass prevents `subreg`
expressions such as these from being formed.

The first operand of a `subreg` expression is customarily accessed
with the `SUBREG_REG` macro and the second operand is customarily
accessed with the `SUBREG_BYTE` macro.

**`(scratch:`m`)`**
: This represents a scratch register that will be required for the
execution of a single instruction and not used subsequently. It is
converted into a `reg` by either the local register allocator or
the reload pass.

`scratch` is usually present inside a `clobber` operation
(see [Side Effects](Side-Effects.md#apple-knuwizjnivtgmzldorzq)).

**`(cc0)`**
: This refers to the machine's condition code register. It has no
operands and may not have a machine mode. There are two ways to use it:

- To stand for a complete set of condition code flags. This is best on
  most machines, where each comparison sets the entire series of flags.

  With this technique, `(cc0)` may be validly used in only two
  contexts: as the destination of an assignment (in test and compare
  instructions) and in comparison operators comparing against zero
  (`const_int` with value zero; that is to say, `const0_rtx`).
- To stand for a single flag that is the result of a single condition.
  This is useful on machines that have only a single flag bit, and in
  which comparison instructions must specify the condition to test.

  With this technique, `(cc0)` may be validly used in only two
  contexts: as the destination of an assignment (in test and compare
  instructions) where the source is a comparison operator, and as the
  first operand of `if_then_else` (in a conditional branch).

There is only one expression object of code `cc0`; it is the
value of the variable `cc0_rtx`. Any attempt to create an
expression of code `cc0` will return `cc0_rtx`.

Instructions can set the condition code implicitly. On many machines,
nearly all instructions set the condition code based on the value that
they compute or store. It is not necessary to record these actions
explicitly in the RTL because the machine description includes a
prescription for recognizing the instructions that do so (by means of
the macro `NOTICE_UPDATE_CC`). See [Condition Code](Condition-Code.md#apple-inxw4zdjoruw63rninxwizi). Only
instructions whose sole purpose is to set the condition code, and
instructions that use the condition code, need mention `(cc0)`.

On some machines, the condition code register is given a register number
and a `reg` is used instead of `(cc0)`. This is usually the
preferable approach if only a small subset of instructions modify the
condition code. Other machines store condition codes in general
registers; in such cases a pseudo register should be used.

Some machines, such as the SPARC and RS/6000, have two sets of
arithmetic instructions, one that sets and one that does not set the
condition code. This is best handled by normally generating the
instruction that does not set the condition code, and making a pattern
that both performs the arithmetic and sets the condition code register
(which would not be `(cc0)` in this case). For examples, search
for ``addcc`' and ``andcc`' in `sparc.md`.

**`(pc)`**
: This represents the machine's program counter. It has no operands and
may not have a machine mode. `(pc)` may be validly used only in
certain specific contexts in jump instructions.

There is only one expression object of code `pc`; it is the value
of the variable `pc_rtx`. Any attempt to create an expression of
code `pc` will return `pc_rtx`.

All instructions that do not jump alter the program counter implicitly
by incrementing it, but there is no need to mention this in the RTL.

**`(mem:`m addr alias`)`**
: This RTX represents a reference to main memory at an address
represented by the expression addr. m specifies how large
a unit of memory is accessed. alias specifies an alias set for the
reference. In general two items are in different alias sets if they cannot
reference the same memory address.

The construct `(mem:BLK (scratch))` is considered to alias all
other memories. Thus it may be used as a memory barrier in epilogue
stack deallocation patterns.

**`(addressof:`m reg`)`**
: This RTX represents a request for the address of register reg. Its mode
is always `Pmode`. If there are any `addressof`
expressions left in the function after CSE, reg is forced into the
stack and the `addressof` expression is replaced with a `plus`
expression for the address of its stack slot.
