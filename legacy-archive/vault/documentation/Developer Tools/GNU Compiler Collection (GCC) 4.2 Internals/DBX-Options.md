---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/DBX-Options.html
archived_at: '2026-07-15T07:31:01.646248Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [DBX Hooks](DBX-Hooks.md#apple-irbfqlkin5xww4y),
Previous: [All Debuggers](All-Debuggers.md#apple-ifwgylkemvrhkz3hmvzhg),
Up: [Debugging Info](Debugging-Info.md#apple-irswe5lhm5uw4zznjfxgm3y)

---

#### 15.22.2 Specific Options for DBX Output

These are specific options for DBX output.

— Macro: __DBX_DEBUGGING_INFO__
> Define this macro if GCC should produce debugging output for DBX
> in response to the `-g` option.

— Macro: __XCOFF_DEBUGGING_INFO__
> Define this macro if GCC should produce XCOFF format debugging output
> in response to the `-g` option. This is a variant of DBX format.

— Macro: __DEFAULT_GDB_EXTENSIONS__
> Define this macro to control whether GCC should by default generate
> GDB's extended version of DBX debugging information (assuming DBX-format
> debugging information is enabled at all). If you don't define the
> macro, the default is 1: always generate the extended information
> if there is any occasion to.

— Macro: __DEBUG_SYMS_TEXT__
> Define this macro if all `.stabs` commands should be output while
> in the text section.

— Macro: __ASM_STABS_OP__
> A C string constant, including spacing, naming the assembler pseudo op to
> use instead of `"\t.stabs\t"` to define an ordinary debugging symbol.
> If you don't define this macro, `"\t.stabs\t"` is used. This macro
> applies only to DBX debugging information format.

— Macro: __ASM_STABD_OP__
> A C string constant, including spacing, naming the assembler pseudo op to
> use instead of `"\t.stabd\t"` to define a debugging symbol whose
> value is the current location. If you don't define this macro,
> `"\t.stabd\t"` is used. This macro applies only to DBX debugging
> information format.

— Macro: __ASM_STABN_OP__
> A C string constant, including spacing, naming the assembler pseudo op to
> use instead of `"\t.stabn\t"` to define a debugging symbol with no
> name. If you don't define this macro, `"\t.stabn\t"` is used. This
> macro applies only to DBX debugging information format.

— Macro: __DBX_NO_XREFS__
> Define this macro if DBX on your system does not support the construct
> ``xstagname`'. On some systems, this construct is used to
> describe a forward reference to a structure named tagname.
> On other systems, this construct is not supported at all.

— Macro: __DBX_CONTIN_LENGTH__
> A symbol name in DBX-format debugging information is normally
> continued (split into two separate `.stabs` directives) when it
> exceeds a certain length (by default, 80 characters). On some
> operating systems, DBX requires this splitting; on others, splitting
> must not be done. You can inhibit splitting by defining this macro
> with the value zero. You can override the default splitting-length by
> defining this macro as an expression for the length you desire.

— Macro: __DBX_CONTIN_CHAR__
> Normally continuation is indicated by adding a ``\`' character to
> the end of a `.stabs` string when a continuation follows. To use
> a different character instead, define this macro as a character
> constant for the character you want to use. Do not define this macro
> if backslash is correct for your system.

— Macro: __DBX_STATIC_STAB_DATA_SECTION__
> Define this macro if it is necessary to go to the data section before
> outputting the ``.stabs`' pseudo-op for a non-global static
> variable.

— Macro: __DBX_TYPE_DECL_STABS_CODE__
> The value to use in the “code” field of the `.stabs` directive
> for a typedef. The default is `N_LSYM`.

— Macro: __DBX_STATIC_CONST_VAR_CODE__
> The value to use in the “code” field of the `.stabs` directive
> for a static variable located in the text section. DBX format does not
> provide any “right” way to do this. The default is `N_FUN`.

— Macro: __DBX_REGPARM_STABS_CODE__
> The value to use in the “code” field of the `.stabs` directive
> for a parameter passed in registers. DBX format does not provide any
> “right” way to do this. The default is `N_RSYM`.

— Macro: __DBX_REGPARM_STABS_LETTER__
> The letter to use in DBX symbol data to identify a symbol as a parameter
> passed in registers. DBX format does not customarily provide any way to
> do this. The default is `'P'`.

— Macro: __DBX_FUNCTION_FIRST__
> Define this macro if the DBX information for a function and its
> arguments should precede the assembler code for the function. Normally,
> in DBX format, the debugging information entirely follows the assembler
> code.

— Macro: __DBX_BLOCKS_FUNCTION_RELATIVE__
> Define this macro, with value 1, if the value of a symbol describing
> the scope of a block (`N_LBRAC` or `N_RBRAC`) should be
> relative to the start of the enclosing function. Normally, GCC uses
> an absolute address.

— Macro: __DBX_LINES_FUNCTION_RELATIVE__
> Define this macro, with value 1, if the value of a symbol indicating
> the current line number (`N_SLINE`) should be relative to the
> start of the enclosing function. Normally, GCC uses an absolute address.

— Macro: __DBX_USE_BINCL__
> Define this macro if GCC should generate `N_BINCL` and
> `N_EINCL` stabs for included header files, as on Sun systems. This
> macro also directs GCC to output a type number as a pair of a file
> number and a type number within the file. Normally, GCC does not
> generate `N_BINCL` or `N_EINCL` stabs, and it outputs a single
> number for a type number.
