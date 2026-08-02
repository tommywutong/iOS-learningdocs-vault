---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/File-Framework.html
archived_at: '2026-07-15T07:30:59.835451Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Data Output](Data-Output.md#apple-irqxiyjnj52xi4dvoq),
Up: [Assembler Format](Assembler-Format.md#apple-ifzxgzlnmjwgk4rnizxxe3lboq)

---

#### 13.19.1 The Overall Framework of an Assembler File

This describes the overall framework of an assembly file.

— Target Hook: void __TARGET_ASM_FILE_START__ ()
> Output to `asm_out_file` any text which the assembler expects to
> find at the beginning of a file. The default behavior is controlled
> by two flags, documented below. Unless your target's assembler is
> quite unusual, if you override the default, you should call
> `default_file_start` at some point in your target hook. This
> lets other target files rely on these variables.

— Target Hook: bool __TARGET_ASM_FILE_START_APP_OFF__
> If this flag is true, the text of the macro `ASM_APP_OFF` will be
> printed as the very first line in the assembly file, unless
> `-fverbose-asm` is in effect. (If that macro has been defined
> to the empty string, this variable has no effect.) With the normal
> definition of `ASM_APP_OFF`, the effect is to notify the GNU
> assembler that it need not bother stripping comments or extra
> whitespace from its input. This allows it to work a bit faster.
>
> The default is false. You should not set it to true unless you have
> verified that your port does not generate any extra whitespace or
> comments that will cause GAS to issue errors in NO_APP mode.

— Target Hook: bool __TARGET_ASM_FILE_START_FILE_DIRECTIVE__
> If this flag is true, `output_file_directive` will be called
> for the primary source file, immediately after printing
> `ASM_APP_OFF` (if that is enabled). Most ELF assemblers expect
> this to be done. The default is false.

— Target Hook: void __TARGET_ASM_FILE_END__ ()
> Output to `asm_out_file` any text which the assembler expects
> to find at the end of a file. The default is to output nothing.

— Function: void __file_end_indicate_exec_stack__ ()
> Some systems use a common convention, the ``.note.GNU-stack`'
> special section, to indicate whether or not an object file relies on
> the stack being executable. If your system uses this convention, you
> should define `TARGET_ASM_FILE_END` to this function. If you
> need to do other things in that hook, have your hook function call
> this function.

— Macro: __ASM_COMMENT_START__
> A C string constant describing how to begin a comment in the target
> assembler language. The compiler assumes that the comment will end at
> the end of the line.

— Macro: __ASM_APP_ON__
> A C string constant for text to be output before each `asm`
> statement or group of consecutive ones. Normally this is
> `"#APP"`, which is a comment that has no effect on most
> assemblers but tells the GNU assembler that it must check the lines
> that follow for all valid assembler constructs.

— Macro: __ASM_APP_OFF__
> A C string constant for text to be output after each `asm`
> statement or group of consecutive ones. Normally this is
> `"#NO_APP"`, which tells the GNU assembler to resume making the
> time-saving assumptions that are valid for ordinary compiler output.

— Macro: __ASM_OUTPUT_SOURCE_FILENAME__ (stream, name)
> A C statement to output COFF information or DWARF debugging information
> which indicates that filename name is the current source file to
> the stdio stream stream.
>
> This macro need not be defined if the standard form of output
> for the file format in use is appropriate.

— Macro: __OUTPUT_QUOTED_STRING__ (stream, string)
> A C statement to output the string string to the stdio stream
> stream. If you do not call the function `output_quoted_string`
> in your config files, GCC will only call it to output filenames to
> the assembler source. So you can use it to canonicalize the format
> of the filename using this macro.

— Macro: __ASM_OUTPUT_IDENT__ (stream, string)
> A C statement to output something to the assembler file to handle a
> ``#ident`' directive containing the text string. If this
> macro is not defined, nothing is output for a ``#ident`' directive.

— Target Hook: void __TARGET_ASM_NAMED_SECTION__ (const char \*name, unsigned int flags, unsigned int align)
> Output assembly directives to switch to section name. The section
> should have attributes as specified by flags, which is a bit mask
> of the `SECTION_*` flags defined in `output.h`. If align
> is nonzero, it contains an alignment in bytes to be used for the section,
> otherwise some target default should be used. Only targets that must
> specify an alignment within the section directive need pay attention to
> align – we will still use `ASM_OUTPUT_ALIGN`.

— Target Hook: bool __TARGET_HAVE_NAMED_SECTIONS__
> This flag is true if the target supports `TARGET_ASM_NAMED_SECTION`.

— Target Hook: unsigned int __TARGET_SECTION_TYPE_FLAGS__ (tree decl, const char \*name, int reloc)
> Choose a set of section attributes for use by `TARGET_ASM_NAMED_SECTION`
> based on a variable or function decl, a section name, and whether or not the
> declaration's initializer may contain runtime relocations. decl may be
> null, in which case read-write data should be assumed.
>
> The default version if this function handles choosing code vs data,
> read-only vs read-write data, and `flag_pic`. You should only
> need to override this if your target has special flags that might be
> set via `__attribute__`.
