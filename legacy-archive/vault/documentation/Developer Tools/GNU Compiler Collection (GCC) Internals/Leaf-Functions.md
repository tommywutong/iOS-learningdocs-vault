---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Leaf-Functions.html
archived_at: '2026-07-15T07:31:00.170759Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Stack Registers](Stack-Registers.md#apple-kn2gcy3lfvjgkz3jon2gk4tt),
Previous: [Values in Registers](Values-in-Registers.md#apple-kzqwy5lfomwws3rnkjswo2ltorsxe4y),
Up: [Registers](Registers.md#apple-kjswo2ltorsxe4y)

---

#### 13.7.4 Handling Leaf Functions

On some machines, a leaf function (i.e., one which makes no calls) can run
more efficiently if it does not make its own register window. Often this
means it is required to receive its arguments in the registers where they
are passed by the caller, instead of the registers where they would
normally arrive.

The special treatment for leaf functions generally applies only when
other conditions are met; for example, often they may use only those
registers for its own variables and temporaries. We use the term “leaf
function” to mean a function that is suitable for this special
handling, so that functions with no calls are not necessarily “leaf
functions”.

GCC assigns register numbers before it knows whether the function is
suitable for leaf function treatment. So it needs to renumber the
registers in order to output a leaf function. The following macros
accomplish this.

— Macro: __LEAF_REGISTERS__
> Name of a char vector, indexed by hard register number, which
> contains 1 for a register that is allowable in a candidate for leaf
> function treatment.
>
> If leaf function treatment involves renumbering the registers, then the
> registers marked here should be the ones before renumbering—those that
> GCC would ordinarily allocate. The registers which will actually be
> used in the assembler code, after renumbering, should not be marked with 1
> in this vector.
>
> Define this macro only if the target machine offers a way to optimize
> the treatment of leaf functions.

— Macro: __LEAF_REG_REMAP__ (regno)
> A C expression whose value is the register number to which regno
> should be renumbered, when a function is treated as a leaf function.
>
> If regno is a register number which should not appear in a leaf
> function before renumbering, then the expression should yield −1, which
> will cause the compiler to abort.
>
> Define this macro only if the target machine offers a way to optimize the
> treatment of leaf functions, and registers need to be renumbered to do
> this.

`TARGET_ASM_FUNCTION_PROLOGUE` and
`TARGET_ASM_FUNCTION_EPILOGUE` must usually treat leaf functions
specially. They can test the C variable `current_function_is_leaf`
which is nonzero for leaf functions. `current_function_is_leaf` is
set prior to local register allocation and is valid for the remaining
compiler passes. They can also test the C variable
`current_function_uses_only_leaf_regs` which is nonzero for leaf
functions which only use leaf registers.
`current_function_uses_only_leaf_regs` is valid after all passes
that modify the instructions have been run and is only useful if
`LEAF_REGISTERS` is defined.
