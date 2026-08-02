---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/DBX-Hooks.html
archived_at: '2026-07-15T07:31:01.640430Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [File Names and DBX](File-Names-and-DBX.md#apple-izuwyzjnjzqw2zltfvqw4zbnirbfq),
Previous: [DBX Options](DBX-Options.md#apple-irbfqlkpob2gs33oom),
Up: [Debugging Info](Debugging-Info.md#apple-irswe5lhm5uw4zznjfxgm3y)

---

#### 15.22.3 Open-Ended Hooks for DBX Format

These are hooks for DBX format.

— Macro: __DBX_OUTPUT_LBRAC__ (stream, name)
> Define this macro to say how to output to stream the debugging
> information for the start of a scope level for variable names. The
> argument name is the name of an assembler symbol (for use with
> `assemble_name`) whose value is the address where the scope begins.

— Macro: __DBX_OUTPUT_RBRAC__ (stream, name)
> Like `DBX_OUTPUT_LBRAC`, but for the end of a scope level.

— Macro: __DBX_OUTPUT_NFUN__ (stream, lscope_label, decl)
> Define this macro if the target machine requires special handling to
> output an `N_FUN` entry for the function decl.

— Macro: __DBX_OUTPUT_SOURCE_LINE__ (stream, line, counter)
> A C statement to output DBX debugging information before code for line
> number line of the current source file to the stdio stream
> stream. counter is the number of time the macro was
> invoked, including the current invocation; it is intended to generate
> unique labels in the assembly output.
>
> This macro should not be defined if the default output is correct, or
> if it can be made correct by defining `DBX_LINES_FUNCTION_RELATIVE`.

— Macro: __NO_DBX_FUNCTION_END__
> Some stabs encapsulation formats (in particular ECOFF), cannot handle the
> `.stabs "",N_FUN,,0,0,Lscope-function-1` gdb dbx extension construct.
> On those machines, define this macro to turn this feature off without
> disturbing the rest of the gdb extensions.

— Macro: __NO_DBX_BNSYM_ENSYM__
> Some assemblers cannot handle the `.stabd BNSYM/ENSYM,0,0` gdb dbx
> extension construct. On those machines, define this macro to turn this
> feature off without disturbing the rest of the gdb extensions.
