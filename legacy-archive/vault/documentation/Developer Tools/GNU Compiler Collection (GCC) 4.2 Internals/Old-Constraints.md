---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Old-Constraints.html
archived_at: '2026-07-15T07:31:02.437667Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq),
Previous: [Register Classes](Register-Classes.md#apple-kjswo2ltorsxelkdnrqxg43fom),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.9 Obsolete Macros for Defining Constraints

Machine-specific constraints can be defined with these macros instead
of the machine description constructs described in [Define Constraints](Define-Constraints.md#apple-irswm2lomuwug33oon2heyljnz2hg). This mechanism is obsolete. New ports should not use
it; old ports should convert to the new mechanism.

— Macro: __CONSTRAINT_LEN__ (char, str)
> For the constraint at the start of str, which starts with the letter
> c, return the length. This allows you to have register class /
> constant / extra constraints that are longer than a single letter;
> you don't need to define this macro if you can do with single-letter
> constraints only. The definition of this macro should use
> DEFAULT_CONSTRAINT_LEN for all the characters that you don't want
> to handle specially.
> There are some sanity checks in genoutput.c that check the constraint lengths
> for the md file, so you can also use this macro to help you while you are
> transitioning from a byzantine single-letter-constraint scheme: when you
> return a negative length for a constraint you want to re-use, genoutput
> will complain about every instance where it is used in the md file.

— Macro: __REG_CLASS_FROM_LETTER__ (char)
> A C expression which defines the machine-dependent operand constraint
> letters for register classes. If char is such a letter, the
> value should be the register class corresponding to it. Otherwise,
> the value should be `NO_REGS`. The register letter ``r`',
> corresponding to class `GENERAL_REGS`, will not be passed
> to this macro; you do not need to handle it.

— Macro: __REG_CLASS_FROM_CONSTRAINT__ (char, str)
> Like `REG_CLASS_FROM_LETTER`, but you also get the constraint string
> passed in str, so that you can use suffixes to distinguish between
> different variants.

— Macro: __CONST_OK_FOR_LETTER_P__ (value, c)
> A C expression that defines the machine-dependent operand constraint
> letters (``I`', ``J`', ``K`', ... ``P`') that specify
> particular ranges of integer values. If c is one of those
> letters, the expression should check that value, an integer, is in
> the appropriate range and return 1 if so, 0 otherwise. If c is
> not one of those letters, the value should be 0 regardless of
> value.

— Macro: __CONST_OK_FOR_CONSTRAINT_P__ (value, c, str)
> Like `CONST_OK_FOR_LETTER_P`, but you also get the constraint
> string passed in str, so that you can use suffixes to distinguish
> between different variants.

— Macro: __CONST_DOUBLE_OK_FOR_LETTER_P__ (value, c)
> A C expression that defines the machine-dependent operand constraint
> letters that specify particular ranges of `const_double` values
> (``G`' or ``H`').
>
> If c is one of those letters, the expression should check that
> value, an RTX of code `const_double`, is in the appropriate
> range and return 1 if so, 0 otherwise. If c is not one of those
> letters, the value should be 0 regardless of value.
>
> `const_double` is used for all floating-point constants and for
> `DImode` fixed-point constants. A given letter can accept either
> or both kinds of values. It can use `GET_MODE` to distinguish
> between these kinds.

— Macro: __CONST_DOUBLE_OK_FOR_CONSTRAINT_P__ (value, c, str)
> Like `CONST_DOUBLE_OK_FOR_LETTER_P`, but you also get the constraint
> string passed in str, so that you can use suffixes to distinguish
> between different variants.

— Macro: __EXTRA_CONSTRAINT__ (value, c)
> A C expression that defines the optional machine-dependent constraint
> letters that can be used to segregate specific types of operands, usually
> memory references, for the target machine. Any letter that is not
> elsewhere defined and not matched by `REG_CLASS_FROM_LETTER` /
> `REG_CLASS_FROM_CONSTRAINT`
> may be used. Normally this macro will not be defined.
>
> If it is required for a particular target machine, it should return 1
> if value corresponds to the operand type represented by the
> constraint letter c. If c is not defined as an extra
> constraint, the value returned should be 0 regardless of value.
>
> For example, on the ROMP, load instructions cannot have their output
> in r0 if the memory reference contains a symbolic address. Constraint
> letter ``Q`' is defined as representing a memory address that does
> _not_ contain a symbolic address. An alternative is specified with
> a ``Q`' constraint on the input and ``r`' on the output. The next
> alternative specifies ``m`' on the input and a register class that
> does not include r0 on the output.

— Macro: __EXTRA_CONSTRAINT_STR__ (value, c, str)
> Like `EXTRA_CONSTRAINT`, but you also get the constraint string passed
> in str, so that you can use suffixes to distinguish between different
> variants.

— Macro: __EXTRA_MEMORY_CONSTRAINT__ (c, str)
> A C expression that defines the optional machine-dependent constraint
> letters, amongst those accepted by `EXTRA_CONSTRAINT`, that should
> be treated like memory constraints by the reload pass.
>
> It should return 1 if the operand type represented by the constraint
> at the start of str, the first letter of which is the letter c,
> comprises a subset of all memory references including
> all those whose address is simply a base register. This allows the reload
> pass to reload an operand, if it does not directly correspond to the operand
> type of c, by copying its address into a base register.
>
> For example, on the S/390, some instructions do not accept arbitrary
> memory references, but only those that do not make use of an index
> register. The constraint letter ``Q`' is defined via
> `EXTRA_CONSTRAINT` as representing a memory address of this type.
> If the letter ``Q`' is marked as `EXTRA_MEMORY_CONSTRAINT`,
> a ``Q`' constraint can handle any memory operand, because the
> reload pass knows it can be reloaded by copying the memory address
> into a base register if required. This is analogous to the way
> a ``o`' constraint can handle any memory operand.

— Macro: __EXTRA_ADDRESS_CONSTRAINT__ (c, str)
> A C expression that defines the optional machine-dependent constraint
> letters, amongst those accepted by `EXTRA_CONSTRAINT` /
> `EXTRA_CONSTRAINT_STR`, that should
> be treated like address constraints by the reload pass.
>
> It should return 1 if the operand type represented by the constraint
> at the start of str, which starts with the letter c, comprises
> a subset of all memory addresses including
> all those that consist of just a base register. This allows the reload
> pass to reload an operand, if it does not directly correspond to the operand
> type of str, by copying it into a base register.
>
> Any constraint marked as `EXTRA_ADDRESS_CONSTRAINT` can only
> be used with the `address_operand` predicate. It is treated
> analogously to the ``p`' constraint.
