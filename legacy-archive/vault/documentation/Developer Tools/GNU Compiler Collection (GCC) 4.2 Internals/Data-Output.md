---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Data-Output.html
archived_at: '2026-07-15T07:31:01.653565Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Uninitialized Data](Uninitialized-Data.md#apple-kvxgs3tjoruwc3djpjswilkemf2gc),
Previous: [File Framework](File-Framework.md#apple-izuwyzjnizzgc3lfo5xxe2y),
Up: [Assembler Format](Assembler-Format.md#apple-ifzxgzlnmjwgk4rnizxxe3lboq)

---

#### 15.21.2 Output of Data

— Target Hook: const char \* __TARGET_ASM_BYTE_OP__
— Target Hook: const char \* __TARGET_ASM_ALIGNED_HI_OP__
— Target Hook: const char \* __TARGET_ASM_ALIGNED_SI_OP__
— Target Hook: const char \* __TARGET_ASM_ALIGNED_DI_OP__
— Target Hook: const char \* __TARGET_ASM_ALIGNED_TI_OP__
— Target Hook: const char \* __TARGET_ASM_UNALIGNED_HI_OP__
— Target Hook: const char \* __TARGET_ASM_UNALIGNED_SI_OP__
— Target Hook: const char \* __TARGET_ASM_UNALIGNED_DI_OP__
— Target Hook: const char \* __TARGET_ASM_UNALIGNED_TI_OP__
> These hooks specify assembly directives for creating certain kinds
> of integer object. The `TARGET_ASM_BYTE_OP` directive creates a
> byte-sized object, the `TARGET_ASM_ALIGNED_HI_OP` one creates an
> aligned two-byte object, and so on. Any of the hooks may be
> `NULL`, indicating that no suitable directive is available.
>
> The compiler will print these strings at the start of a new line,
> followed immediately by the object's initial value. In most cases,
> the string should contain a tab, a pseudo-op, and then another tab.

— Target Hook: bool __TARGET_ASM_INTEGER__ (rtx x, unsigned int size, int aligned_p)
> The `assemble_integer` function uses this hook to output an
> integer object. x is the object's value, size is its size
> in bytes and aligned_p indicates whether it is aligned. The
> function should return `true` if it was able to output the
> object. If it returns false, `assemble_integer` will try to
> split the object into smaller parts.
>
> The default implementation of this hook will use the
> `TARGET_ASM_BYTE_OP` family of strings, returning `false`
> when the relevant string is `NULL`.

— Macro: __OUTPUT_ADDR_CONST_EXTRA__ (stream, x, fail)
> A C statement to recognize rtx patterns that
> `output_addr_const` can't deal with, and output assembly code to
> stream corresponding to the pattern x. This may be used to
> allow machine-dependent `UNSPEC`s to appear within constants.
>
> If `OUTPUT_ADDR_CONST_EXTRA` fails to recognize a pattern, it must
> `goto fail`, so that a standard error message is printed. If it
> prints an error message itself, by calling, for example,
> `output_operand_lossage`, it may just complete normally.

— Macro: __ASM_OUTPUT_ASCII__ (stream, ptr, len)
> A C statement to output to the stdio stream stream an assembler
> instruction to assemble a string constant containing the len
> bytes at ptr. ptr will be a C expression of type
> `char *` and len a C expression of type `int`.
>
> If the assembler has a `.ascii` pseudo-op as found in the
> Berkeley Unix assembler, do not define the macro
> `ASM_OUTPUT_ASCII`.

— Macro: __ASM_OUTPUT_FDESC__ (stream, decl, n)
> A C statement to output word n of a function descriptor for
> decl. This must be defined if `TARGET_VTABLE_USES_DESCRIPTORS`
> is defined, and is otherwise unused.

— Macro: __CONSTANT_POOL_BEFORE_FUNCTION__
> You may define this macro as a C expression. You should define the
> expression to have a nonzero value if GCC should output the constant
> pool for a function before the code for the function, or a zero value if
> GCC should output the constant pool after the function. If you do
> not define this macro, the usual case, GCC will output the constant
> pool before the function.

— Macro: __ASM_OUTPUT_POOL_PROLOGUE__ (file, funname, fundecl, size)
> A C statement to output assembler commands to define the start of the
> constant pool for a function. funname is a string giving
> the name of the function. Should the return type of the function
> be required, it can be obtained via fundecl. size
> is the size, in bytes, of the constant pool that will be written
> immediately after this call.
>
> If no constant-pool prefix is required, the usual case, this macro need
> not be defined.

— Macro: __ASM_OUTPUT_SPECIAL_POOL_ENTRY__ (file, x, mode, align, labelno, jumpto)
> A C statement (with or without semicolon) to output a constant in the
> constant pool, if it needs special treatment. (This macro need not do
> anything for RTL expressions that can be output normally.)
>
> The argument file is the standard I/O stream to output the
> assembler code on. x is the RTL expression for the constant to
> output, and mode is the machine mode (in case x is a
> ``const_int`'). align is the required alignment for the value
> x; you should output an assembler directive to force this much
> alignment.
>
> The argument labelno is a number to use in an internal label for
> the address of this pool entry. The definition of this macro is
> responsible for outputting the label definition at the proper place.
> Here is how to do this:
>
> ```
>           (*targetm.asm_out.internal_label) (file, "LC", labelno);
>
> ```
>
> When you output a pool entry specially, you should end with a
> `goto` to the label jumpto. This will prevent the same pool
> entry from being output a second time in the usual manner.
>
> You need not define this macro if it would do nothing.

— Macro: __ASM_OUTPUT_POOL_EPILOGUE__ (file funname fundecl size)
> A C statement to output assembler commands to at the end of the constant
> pool for a function. funname is a string giving the name of the
> function. Should the return type of the function be required, you can
> obtain it via fundecl. size is the size, in bytes, of the
> constant pool that GCC wrote immediately before this call.
>
> If no constant-pool epilogue is required, the usual case, you need not
> define this macro.

— Macro: __IS_ASM_LOGICAL_LINE_SEPARATOR__ (C)
> Define this macro as a C expression which is nonzero if C is
> used as a logical line separator by the assembler.
>
> If you do not define this macro, the default is that only
> the character ``;`' is treated as a logical line separator.

— Target Hook: const char \* __TARGET_ASM_OPEN_PAREN__
— Target Hook: const char \* __TARGET_ASM_CLOSE_PAREN__
> These target hooks are C string constants, describing the syntax in the
> assembler for grouping arithmetic expressions. If not overridden, they
> default to normal parentheses, which is correct for most assemblers.

These macros are provided by `real.h` for writing the definitions
of `ASM_OUTPUT_DOUBLE` and the like:

— Macro: __REAL_VALUE_TO_TARGET_SINGLE__ (x, l)
— Macro: __REAL_VALUE_TO_TARGET_DOUBLE__ (x, l)
— Macro: __REAL_VALUE_TO_TARGET_LONG_DOUBLE__ (x, l)
— Macro: __REAL_VALUE_TO_TARGET_DECIMAL32__ (x, l)
— Macro: __REAL_VALUE_TO_TARGET_DECIMAL64__ (x, l)
— Macro: __REAL_VALUE_TO_TARGET_DECIMAL128__ (x, l)
> These translate x, of type `REAL_VALUE_TYPE`, to the
> target's floating point representation, and store its bit pattern in
> the variable l. For `REAL_VALUE_TO_TARGET_SINGLE` and
> `REAL_VALUE_TO_TARGET_DECIMAL32`, this variable should be a
> simple `long int`. For the others, it should be an array of
> `long int`. The number of elements in this array is determined
> by the size of the desired target floating point data type: 32 bits of
> it go in each `long int` array element. Each array element holds
> 32 bits of the result, even if `long int` is wider than 32 bits
> on the host machine.
>
> The array element values are designed so that you can print them out
> using `fprintf` in the order they should appear in the target
> machine's memory.
