---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Uninitialized-Data.html
archived_at: '2026-07-15T07:31:00.983535Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Label Output](Label-Output.md#apple-jrqwezlmfvhxk5dqov2a),
Previous: [Data Output](Data-Output.md#apple-irqxiyjnj52xi4dvoq),
Up: [Assembler Format](Assembler-Format.md#apple-ifzxgzlnmjwgk4rnizxxe3lboq)

---

#### 13.19.3 Output of Uninitialized Variables

Each of the macros in this section is used to do the whole job of
outputting a single uninitialized variable.

— Macro: __ASM_OUTPUT_COMMON__ (stream, name, size, rounded)
> A C statement (sans semicolon) to output to the stdio stream
> stream the assembler definition of a common-label named
> name whose size is size bytes. The variable rounded
> is the size rounded up to whatever alignment the caller wants.
>
> Use the expression `assemble_name (`stream`,` name`)` to
> output the name itself; before and after that, output the additional
> assembler syntax for defining the name, and a newline.
>
> This macro controls how the assembler definitions of uninitialized
> common global variables are output.

— Macro: __ASM_OUTPUT_ALIGNED_COMMON__ (stream, name, size, alignment)
> Like `ASM_OUTPUT_COMMON` except takes the required alignment as a
> separate, explicit argument. If you define this macro, it is used in
> place of `ASM_OUTPUT_COMMON`, and gives you more flexibility in
> handling the required alignment of the variable. The alignment is specified
> as the number of bits.

— Macro: __ASM_OUTPUT_ALIGNED_DECL_COMMON__ (stream, decl, name, size, alignment)
> Like `ASM_OUTPUT_ALIGNED_COMMON` except that decl of the
> variable to be output, if there is one, or `NULL_TREE` if there
> is no corresponding variable. If you define this macro, GCC will use it
> in place of both `ASM_OUTPUT_COMMON` and
> `ASM_OUTPUT_ALIGNED_COMMON`. Define this macro when you need to see
> the variable's decl in order to chose what to output.

— Macro: __ASM_OUTPUT_SHARED_COMMON__ (stream, name, size, rounded)
> If defined, it is similar to `ASM_OUTPUT_COMMON`, except that it
> is used when name is shared. If not defined, `ASM_OUTPUT_COMMON`
> will be used.

— Macro: __ASM_OUTPUT_BSS__ (stream, decl, name, size, rounded)
> A C statement (sans semicolon) to output to the stdio stream
> stream the assembler definition of uninitialized global decl named
> name whose size is size bytes. The variable rounded
> is the size rounded up to whatever alignment the caller wants.
>
> Try to use function `asm_output_bss` defined in `varasm.c` when
> defining this macro. If unable, use the expression
> `assemble_name (`stream`,` name`)` to output the name itself;
> before and after that, output the additional assembler syntax for defining
> the name, and a newline.
>
> This macro controls how the assembler definitions of uninitialized global
> variables are output. This macro exists to properly support languages like
> C++ which do not have `common` data. However, this macro currently
> is not defined for all targets. If this macro and
> `ASM_OUTPUT_ALIGNED_BSS` are not defined then `ASM_OUTPUT_COMMON`
> or `ASM_OUTPUT_ALIGNED_COMMON` or
> `ASM_OUTPUT_ALIGNED_DECL_COMMON` is used.

— Macro: __ASM_OUTPUT_ALIGNED_BSS__ (stream, decl, name, size, alignment)
> Like `ASM_OUTPUT_BSS` except takes the required alignment as a
> separate, explicit argument. If you define this macro, it is used in
> place of `ASM_OUTPUT_BSS`, and gives you more flexibility in
> handling the required alignment of the variable. The alignment is specified
> as the number of bits.
>
> Try to use function `asm_output_aligned_bss` defined in file
> `varasm.c` when defining this macro.

— Macro: __ASM_OUTPUT_SHARED_BSS__ (stream, decl, name, size, rounded)
> If defined, it is similar to `ASM_OUTPUT_BSS`, except that it
> is used when name is shared. If not defined, `ASM_OUTPUT_BSS`
> will be used.

— Macro: __ASM_OUTPUT_LOCAL__ (stream, name, size, rounded)
> A C statement (sans semicolon) to output to the stdio stream
> stream the assembler definition of a local-common-label named
> name whose size is size bytes. The variable rounded
> is the size rounded up to whatever alignment the caller wants.
>
> Use the expression `assemble_name (`stream`,` name`)` to
> output the name itself; before and after that, output the additional
> assembler syntax for defining the name, and a newline.
>
> This macro controls how the assembler definitions of uninitialized
> static variables are output.

— Macro: __ASM_OUTPUT_ALIGNED_LOCAL__ (stream, name, size, alignment)
> Like `ASM_OUTPUT_LOCAL` except takes the required alignment as a
> separate, explicit argument. If you define this macro, it is used in
> place of `ASM_OUTPUT_LOCAL`, and gives you more flexibility in
> handling the required alignment of the variable. The alignment is specified
> as the number of bits.

— Macro: __ASM_OUTPUT_ALIGNED_DECL_LOCAL__ (stream, decl, name, size, alignment)
> Like `ASM_OUTPUT_ALIGNED_DECL` except that decl of the
> variable to be output, if there is one, or `NULL_TREE` if there
> is no corresponding variable. If you define this macro, GCC will use it
> in place of both `ASM_OUTPUT_DECL` and
> `ASM_OUTPUT_ALIGNED_DECL`. Define this macro when you need to see
> the variable's decl in order to chose what to output.

— Macro: __ASM_OUTPUT_SHARED_LOCAL__ (stream, name, size, rounded)
> If defined, it is similar to `ASM_OUTPUT_LOCAL`, except that it
> is used when name is shared. If not defined, `ASM_OUTPUT_LOCAL`
> will be used.
