---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Run_002dtime-Target.html
archived_at: '2026-07-15T07:31:02.720578Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Per-Function Data](Per_002dFunction-Data.md#apple-kbsxexzqgazgirtvnzrxi2lpnywuiylume),
Previous: [Driver](Driver.md#apple-irzgs5tfoi),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.3 Run-time Target Specification

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
> This variable is declared in `options.h`, which is included before
> any target-specific headers.

— Variable: Target Hook __int__ TARGET_DEFAULT_TARGET_FLAGS
> This variable specifies the initial value of `target_flags`.
> Its default setting is 0.

— Target Hook: bool __TARGET_HANDLE_OPTION__ (size_t code, const char \*arg, int value)
> This hook is called whenever the user specifies one of the
> target-specific options described by the `.opt` definition files
> (see [Options](Options.md#apple-j5yhi2lpnzzq)). It has the opportunity to do some option-specific
> processing and should return true if the option is valid. The default
> definition does nothing but return true.
>
> code specifies the `OPT_`name enumeration value
> associated with the selected option; name is just a rendering of
> the option name in which non-alphanumeric characters are replaced by
> underscores. arg specifies the string argument and is null if
> no argument was given. If the option is flagged as a `UInteger`
> (see [Option properties](Option-properties.md#apple-j5yhi2lpnywxa4tpobsxe5djmvzq)), value is the numeric value of the
> argument. Otherwise value is 1 if the positive form of the
> option was used and 0 if the “no-” form was.

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
