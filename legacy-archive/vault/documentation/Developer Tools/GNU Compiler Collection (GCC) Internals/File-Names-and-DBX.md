---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/File-Names-and-DBX.html
archived_at: '2026-07-15T07:30:59.842232Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [SDB and DWARF](SDB-and-DWARF.md#apple-knceellbnzsc2rcxifjem),
Previous: [DBX Hooks](DBX-Hooks.md#apple-irbfqlkin5xww4y),
Up: [Debugging Info](Debugging-Info.md#apple-irswe5lhm5uw4zznjfxgm3y)

---

#### 13.20.4 File Names in DBX Format

This describes file names in DBX format.

— Macro: __DBX_OUTPUT_MAIN_SOURCE_FILENAME__ (stream, name)
> A C statement to output DBX debugging information to the stdio stream
> stream, which indicates that file name is the main source
> file—the file specified as the input file for compilation.
> This macro is called only once, at the beginning of compilation.
>
> This macro need not be defined if the standard form of output
> for DBX debugging information is appropriate.
>
> It may be necessary to refer to a label equal to the beginning of the
> text section. You can use ``assemble_name (stream, ltext_label_name)`'
> to do so. If you do this, you must also set the variable
> used_ltext_label_name to `true`.

— Macro: __NO_DBX_MAIN_SOURCE_DIRECTORY__
> Define this macro, with value 1, if GCC should not emit an indication
> of the current directory for compilation and current source language at
> the beginning of the file.

— Macro: __NO_DBX_GCC_MARKER__
> Define this macro, with value 1, if GCC should not emit an indication
> that this object file was compiled by GCC. The default is to emit
> an `N_OPT` stab at the beginning of every source file, with
> ``gcc2_compiled.`' for the string and value 0.

— Macro: __DBX_OUTPUT_MAIN_SOURCE_FILE_END__ (stream, name)
> A C statement to output DBX debugging information at the end of
> compilation of the main source file name. Output should be
> written to the stdio stream stream.
>
> If you don't define this macro, nothing special is output at the end
> of compilation, which is correct for most machines.

— Macro: __DBX_OUTPUT_NULL_N_SO_AT_MAIN_SOURCE_FILE_END__
> Define this macro _instead of_ defining
> `DBX_OUTPUT_MAIN_SOURCE_FILE_END`, if what needs to be output at
> the end of compilation is a `N_SO` stab with an empty string,
> whose value is the highest absolute text address in the file.
