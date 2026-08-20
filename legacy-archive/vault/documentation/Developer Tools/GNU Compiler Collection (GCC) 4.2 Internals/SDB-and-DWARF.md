---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/SDB-and-DWARF.html
archived_at: '2026-07-15T07:31:02.727381Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [VMS Debug](VMS-Debug.md#apple-kzgvglkemvrhkzy),
Previous: [File Names and DBX](File-Names-and-DBX.md#apple-izuwyzjnjzqw2zltfvqw4zbnirbfq),
Up: [Debugging Info](Debugging-Info.md#apple-irswe5lhm5uw4zznjfxgm3y)

---

#### 15.22.5 Macros for SDB and DWARF Output

Here are macros for SDB and DWARF output.

— Macro: __SDB_DEBUGGING_INFO__
> Define this macro if GCC should produce COFF-style debugging output
> for SDB in response to the `-g` option.

— Macro: __DWARF2_DEBUGGING_INFO__
> Define this macro if GCC should produce dwarf version 2 format
> debugging output in response to the `-g` option.
>
> — Target Hook: int __TARGET_DWARF_CALLING_CONVENTION__ (tree function)
> > Define this to enable the dwarf attribute `DW_AT_calling_convention` to
> > be emitted for each function. Instead of an integer return the enum
> > value for the `DW_CC_` tag.
>
> To support optional call frame debugging information, you must also
> define `INCOMING_RETURN_ADDR_RTX` and either set
> `RTX_FRAME_RELATED_P` on the prologue insns if you use RTL for the
> prologue, or call `dwarf2out_def_cfa` and `dwarf2out_reg_save`
> as appropriate from `TARGET_ASM_FUNCTION_PROLOGUE` if you don't.

— Macro: __DWARF2_FRAME_INFO__
> Define this macro to a nonzero value if GCC should always output
> Dwarf 2 frame information. If `DWARF2_UNWIND_INFO`
> (see [Exception Region Output](Exception-Region-Output.md#apple-iv4ggzlqoruw63rnkjswo2lpnywu65luob2xi) is nonzero, GCC will output this
> information not matter how you define `DWARF2_FRAME_INFO`.

— Macro: __DWARF2_ASM_LINE_DEBUG_INFO__
> Define this macro to be a nonzero value if the assembler can generate Dwarf 2
> line debug info sections. This will result in much more compact line number
> tables, and hence is desirable if it works.

— Macro: __ASM_OUTPUT_DWARF_DELTA__ (stream, size, label1, label2)
> A C statement to issue assembly directives that create a difference
> lab1 minus lab2, using an integer of the given size.

— Macro: __ASM_OUTPUT_DWARF_OFFSET__ (stream, size, label, section)
> A C statement to issue assembly directives that create a
> section-relative reference to the given label, using an integer of the
> given size. The label is known to be defined in the given section.

— Macro: __ASM_OUTPUT_DWARF_PCREL__ (stream, size, label)
> A C statement to issue assembly directives that create a self-relative
> reference to the given label, using an integer of the given size.

— Target Hook: void __TARGET_ASM_OUTPUT_DWARF_DTPREL__ (FILE \*FILE, int size, rtx x)
> If defined, this target hook is a function which outputs a DTP-relative
> reference to the given TLS symbol of the specified size.

— Macro: __PUT_SDB___...
> Define these macros to override the assembler syntax for the special
> SDB assembler directives. See `sdbout.c` for a list of these
> macros and their arguments. If the standard syntax is used, you need
> not define them yourself.

— Macro: __SDB_DELIM__
> Some assemblers do not support a semicolon as a delimiter, even between
> SDB assembler directives. In that case, define this macro to be the
> delimiter to use (usually ``\n`'). It is not necessary to define
> a new set of `PUT_SDB_`op macros if this is the only change
> required.

— Macro: __SDB_ALLOW_UNKNOWN_REFERENCES__
> Define this macro to allow references to unknown structure,
> union, or enumeration tags to be emitted. Standard COFF does not
> allow handling of unknown references, MIPS ECOFF has support for
> it.

— Macro: __SDB_ALLOW_FORWARD_REFERENCES__
> Define this macro to allow references to structure, union, or
> enumeration tags that have not yet been seen to be handled. Some
> assemblers choke if forward tags are used, while some require it.

— Macro: __SDB_OUTPUT_SOURCE_LINE__ (stream, line)
> A C statement to output SDB debugging information before code for line
> number line of the current source file to the stdio stream
> stream. The default is to emit an `.ln` directive.
