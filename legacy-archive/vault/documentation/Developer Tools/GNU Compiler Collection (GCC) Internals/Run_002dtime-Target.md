---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Run_002dtime-Target.html
archived_at: '2026-07-15T07:31:00.656439Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Per-Function Data](Per_002dFunction-Data.md#apple-kbsxexzqgazgirtvnzrxi2lpnywuiylume),
Previous: [Driver](Driver.md#apple-irzgs5tfoi),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 13.3 Run-time Target Specification

Here are run-time target specifications.

— Macro: __TARGET_CPU_CPP_BUILTINS__ ()
> This function-like macro expands to a block of code that defines
> built-in preprocessor macros and assertions for the target cpu, using
> the functions `builtin_define`, `builtin_define_std` and
> `builtin_assert`. When the front end
> calls this macro it provides a trailing semicolon, and since it has
> finished command line option processing your code can use those
> results freely.
>
> `builtin_assert` takes a string in the form you pass to the
> command-line option `-A`, such as `cpu=mips`, and creates
> the assertion. `builtin_define` takes a string in the form
> accepted by option `-D` and unconditionally defines the macro.
>
> `builtin_define_std` takes a string representing the name of an
> object-like macro. If it doesn't lie in the user's namespace,
> `builtin_define_std` defines it unconditionally. Otherwise, it
> defines a version with two leading underscores, and another version
> with two leading and trailing underscores, and defines the original
> only if an ISO standard was not requested on the command line. For
> example, passing `unix` defines `__unix`, `__unix__`
> and possibly `unix`; passing `_mips` defines `__mips`,
> `__mips__` and possibly `_mips`, and passing `_ABI64`
> defines only `_ABI64`.
>
> You can also test for the C dialect being compiled. The variable
> `c_language` is set to one of `clk_c`, `clk_cplusplus`
> or `clk_objective_c`. Note that if we are preprocessing
> assembler, this variable will be `clk_c` but the function-like
> macro `preprocessing_asm_p()` will return true, so you might want
> to check for that first. If you need to check for strict ANSI, the
> variable `flag_iso` can be used. The function-like macro
> `preprocessing_trad_p()` can be used to check for traditional
> preprocessing.

— Macro: __TARGET_OS_CPP_BUILTINS__ ()
> Similarly to `TARGET_CPU_CPP_BUILTINS` but this macro is optional
> and is used for the target operating system instead.

— Macro: __TARGET_OBJFMT_CPP_BUILTINS__ ()
> Similarly to `TARGET_CPU_CPP_BUILTINS` but this macro is optional
> and is used for the target object format. `elfos.h` uses this
> macro to define `__ELF__`, so you probably do not need to define
> it yourself.

— Variable: extern int __target_flags__
> This declaration should be present.

— Macro: __TARGET___featurename
> This series of macros is to allow compiler command arguments to
> enable or disable the use of optional features of the target machine.
> For example, one machine description serves both the 68000 and
> the 68020; a command argument tells the compiler whether it should
> use 68020-only instructions or not. This command argument works
> by means of a macro `TARGET_68020` that tests a bit in
> `target_flags`.
>
> Define a macro `TARGET_`featurename for each such option.
> Its definition should test a bit in `target_flags`. It is
> recommended that a helper macro `MASK_`featurename
> is defined for each bit-value to test, and used in
> `TARGET_`featurename and `TARGET_SWITCHES`. For
> example:
>
> ```
>           #define TARGET_MASK_68020 1
>           #define TARGET_68020 (target_flags & MASK_68020)
>
> ```
>
> One place where these macros are used is in the condition-expressions
> of instruction patterns. Note how `TARGET_68020` appears
> frequently in the 68000 machine description file, `m68k.md`.
> Another place they are used is in the definitions of the other
> macros in the `machine.h` file.

— Macro: __TARGET_SWITCHES__
> This macro defines names of command options to set and clear
> bits in `target_flags`. Its definition is an initializer
> with a subgrouping for each command option.
>
> Each subgrouping contains a string constant, that defines the option
> name, a number, which contains the bits to set in
> `target_flags`, and a second string which is the description
> displayed by `--help`. If the number is negative then the bits specified
> by the number are cleared instead of being set. If the description
> string is present but empty, then no help information will be displayed
> for that option, but it will not count as an undocumented option. The
> actual option name is made by appending ``-m`' to the specified name.
> Non-empty description strings should be marked with `N_(...)` for
> `xgettext`. Please do not mark empty strings because the empty
> string is reserved by GNU gettext. `gettext("")` returns the header entry
> of the message catalog with meta information, not the empty string.
>
> In addition to the description for `--help`,
> more detailed documentation for each option should be added to
> `invoke.texi`.
>
> One of the subgroupings should have a null string. The number in
> this grouping is the default value for `target_flags`. Any
> target options act starting with that value.
>
> Here is an example which defines `-m68000` and `-m68020`
> with opposite meanings, and picks the latter as the default:
>
> ```
>           #define TARGET_SWITCHES \
>             { { "68020", MASK_68020, "" },     \
>               { "68000", -MASK_68020,          \
>                 N_("Compile for the 68000") }, \
>               { "", MASK_68020, "" },          \
>             }
>
> ```

— Macro: __TARGET_OPTIONS__
> This macro is similar to `TARGET_SWITCHES` but defines names of command
> options that have values. Its definition is an initializer with a
> subgrouping for each command option.
>
> Each subgrouping contains a string constant, that defines the option
> name, the address of a variable, a description string, and a value.
> Non-empty description strings should be marked with `N_(...)`
> for `xgettext`. Please do not mark empty strings because the
> empty string is reserved by GNU gettext. `gettext("")` returns the
> header entry of the message catalog with meta information, not the empty
> string.
>
> If the value listed in the table is `NULL`, then the variable, type
> `char *`, is set to the variable part of the given option if the
> fixed part matches. In other words, if the first part of the option
> matches what's in the table, the variable will be set to point to the
> rest of the option. This allows the user to specify a value for that
> option. The actual option name is made by appending ``-m`' to the
> specified name. Again, each option should also be documented in
> `invoke.texi`.
>
> If the value listed in the table is non-`NULL`, then the option
> must match the option in the table exactly (with ``-m`'), and the
> variable is set to point to the value listed in the table.
>
> Here is an example which defines `-mshort-data-number`. If the
> given option is `-mshort-data-512`, the variable `m88k_short_data`
> will be set to the string `"512"`.
>
> ```
>           extern char *m88k_short_data;
>           #define TARGET_OPTIONS \
>            { { "short-data-", &m88k_short_data, \
>                N_("Specify the size of the short data section"), 0 } }
>
> ```
>
> Here is a variant of the above that allows the user to also specify
> just `-mshort-data` where a default of `"64"` is used.
>
> ```
>           extern char *m88k_short_data;
>           #define TARGET_OPTIONS \
>            { { "short-data-", &m88k_short_data, \
>                N_("Specify the size of the short data section"), 0 } \
>               { "short-data", &m88k_short_data, "", "64" },
>               }
>
> ```
>
> Here is an example which defines `-mno-alu`, `-malu1`, and
> `-malu2` as a three-state switch, along with suitable macros for
> checking the state of the option (documentation is elided for brevity).
>
> ```
>           [chip.c]
>           char *chip_alu = ""; /* Specify default here.  */
>
>           [chip.h]
>           extern char *chip_alu;
>           #define TARGET_OPTIONS \
>             { { "no-alu", &chip_alu, "", "" }, \
>                { "alu1", &chip_alu, "", "1" }, \
>                { "alu2", &chip_alu, "", "2" }, }
>           #define TARGET_ALU (chip_alu[0] != '\0')
>           #define TARGET_ALU1 (chip_alu[0] == '1')
>           #define TARGET_ALU2 (chip_alu[0] == '2')
>
> ```

— Macro: __TARGET_VERSION__
> This macro is a C statement to print on `stderr` a string
> describing the particular machine description choice. Every machine
> description should define `TARGET_VERSION`. For example:
>
> ```
>           #ifdef MOTOROLA
>           #define TARGET_VERSION \
>             fprintf (stderr, " (68k, Motorola syntax)");
>           #else
>           #define TARGET_VERSION \
>             fprintf (stderr, " (68k, MIT syntax)");
>           #endif
>
> ```

— Macro: __OVERRIDE_OPTIONS__
> Sometimes certain combinations of command options do not make sense on
> a particular target machine. You can define a macro
> `OVERRIDE_OPTIONS` to take account of this. This macro, if
> defined, is executed once just after all the command options have been
> parsed.
>
> Don't use this macro to turn on various extra optimizations for
> `-O`. That is what `OPTIMIZATION_OPTIONS` is for.

— Macro: __C_COMMON_OVERRIDE_OPTIONS__
> This is similar to `OVERRIDE_OPTIONS` but is only used in the C
> language frontends (C, Objective-C, C++, Objective-C++) and so can be
> used to alter option flag variables which only exist in those
> frontends.

— Macro: __OPTIMIZATION_OPTIONS__ (level, size)
> Some machines may desire to change what optimizations are performed for
> various optimization levels. This macro, if defined, is executed once
> just after the optimization level is determined and before the remainder
> of the command options have been parsed. Values set in this macro are
> used as the default values for the other command line options.
>
> level is the optimization level specified; 2 if `-O2` is
> specified, 1 if `-O` is specified, and 0 if neither is specified.
>
> size is nonzero if `-Os` is specified and zero otherwise.
>
> You should not use this macro to change options that are not
> machine-specific. These should uniformly selected by the same
> optimization level on all supported machines. Use this macro to enable
> machine-specific optimizations.
>
> __Do not examine__ `write_symbols` __in
> this macro!__ The debugging options are not supposed to alter the
> generated code.

— Macro: __CAN_DEBUG_WITHOUT_FP__
> Define this macro if debugging can be performed even without a frame
> pointer. If this macro is defined, GCC will turn on the
> `-fomit-frame-pointer` option whenever `-O` is specified.
