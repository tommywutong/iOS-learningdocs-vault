---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Uninitialized-Data.html
archived_at: '2026-07-15T07:31:03.069871Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Label Output](Label-Output.md#apple-jrqwezlmfvhxk5dqov2a),
Previous: [Data Output](Data-Output.md#apple-irqxiyjnj52xi4dvoq),
Up: [Assembler Format](Assembler-Format.md#apple-ifzxgzlnmjwgk4rnizxxe3lboq)

---

#### 15.21.3 Output of Uninitialized Variables

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
> There are two ways of handling global BSS. One is to define either
> this macro or its aligned counterpart, `ASM_OUTPUT_ALIGNED_BSS`.
> The other is to have `TARGET_ASM_SELECT_SECTION` return a
> switchable BSS section (see [TARGET_HAVE_SWITCHABLE_BSS_SECTIONS](https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/TARGET_005fHAVE_005fSWITCHABLE_005fBSS_005fSECTIONS.html#TARGET_005fHAVE_005fSWITCHABLE_005fBSS_005fSECTIONS)).
> You do not need to do both.
>
> Some languages do not have `common` data, and require a
> non-common form of global BSS in order to handle uninitialized globals
> efficiently. C++ is one example of this. However, if the target does
> not support global BSS, the front end may choose to make globals
> common in order to save space in the object file.

— Macro: __ASM_OUTPUT_ALIGNED_BSS__ (stream, decl, name, size, alignment)
> Like `ASM_OUTPUT_BSS` except takes the required alignment as a
> separate, explicit argument. If you define this macro, it is used in
> place of `ASM_OUTPUT_BSS`, and gives you more flexibility in
> handling the required alignment of the variable. The alignment is specified
> as the number of bits.
>
> Try to use function `asm_output_aligned_bss` defined in file
> `varasm.c` when defining this macro.

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
