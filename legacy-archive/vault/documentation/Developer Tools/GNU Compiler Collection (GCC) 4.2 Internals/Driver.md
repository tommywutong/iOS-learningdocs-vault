---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Driver.html
archived_at: '2026-07-15T07:31:01.746196Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Run-time Target](Run_002dtime-Target.md#apple-kj2w4xzqgazgi5djnvss2vdbojtwk5a),
Previous: [Target Structure](Target-Structure.md#apple-krqxez3foqwvg5dsovrxi5lsmu),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.2 Controlling the Compilation Driver, `gcc`

You can control the compilation driver.

— Macro: __SWITCH_TAKES_ARG__ (char)
> A C expression which determines whether the option `-char`
> takes arguments. The value should be the number of arguments that
> option takes–zero, for many options.
>
> By default, this macro is defined as
> `DEFAULT_SWITCH_TAKES_ARG`, which handles the standard options
> properly. You need not define `SWITCH_TAKES_ARG` unless you
> wish to add additional options which take arguments. Any redefinition
> should call `DEFAULT_SWITCH_TAKES_ARG` and then check for
> additional options.

— Macro: __WORD_SWITCH_TAKES_ARG__ (name)
> A C expression which determines whether the option `-name`
> takes arguments. The value should be the number of arguments that
> option takes–zero, for many options. This macro rather than
> `SWITCH_TAKES_ARG` is used for multi-character option names.
>
> By default, this macro is defined as
> `DEFAULT_WORD_SWITCH_TAKES_ARG`, which handles the standard options
> properly. You need not define `WORD_SWITCH_TAKES_ARG` unless you
> wish to add additional options which take arguments. Any redefinition
> should call `DEFAULT_WORD_SWITCH_TAKES_ARG` and then check for
> additional options.

— Macro: __SWITCH_CURTAILS_COMPILATION__ (char)
> A C expression which determines whether the option `-char`
> stops compilation before the generation of an executable. The value is
> boolean, nonzero if the option does stop an executable from being
> generated, zero otherwise.
>
> By default, this macro is defined as
> `DEFAULT_SWITCH_CURTAILS_COMPILATION`, which handles the standard
> options properly. You need not define
> `SWITCH_CURTAILS_COMPILATION` unless you wish to add additional
> options which affect the generation of an executable. Any redefinition
> should call `DEFAULT_SWITCH_CURTAILS_COMPILATION` and then check
> for additional options.

— Macro: __SWITCHES_NEED_SPACES__
> A string-valued C expression which enumerates the options for which
> the linker needs a space between the option and its argument.
>
> If this macro is not defined, the default value is `""`.

— Macro: __TARGET_OPTION_TRANSLATE_TABLE__
> If defined, a list of pairs of strings, the first of which is a
> potential command line target to the `gcc` driver program, and the
> second of which is a space-separated (tabs and other whitespace are not
> supported) list of options with which to replace the first option. The
> target defining this list is responsible for assuring that the results
> are valid. Replacement options may not be the `--opt` style, they
> must be the `-opt` style. It is the intention of this macro to
> provide a mechanism for substitution that affects the multilibs chosen,
> such as one option that enables many options, some of which select
> multilibs. Example nonsensical definition, where `-malt-abi`,
> `-EB`, and `-mspoo` cause different multilibs to be chosen:
>
> ```
>           #define TARGET_OPTION_TRANSLATE_TABLE \
>           { "-fast",   "-march=fast-foo -malt-abi -I/usr/fast-foo" }, \
>           { "-compat", "-EB -malign=4 -mspoo" }
>
> ```

— Macro: __DRIVER_SELF_SPECS__
> A list of specs for the driver itself. It should be a suitable
> initializer for an array of strings, with no surrounding braces.
>
> The driver applies these specs to its own command line between loading
> default `specs` files (but not command-line specified ones) and
> choosing the multilib directory or running any subcommands. It
> applies them in the order given, so each spec can depend on the
> options added by earlier ones. It is also possible to remove options
> using ``%<option`' in the usual way.
>
> This macro can be useful when a port has several interdependent target
> options. It provides a way of standardizing the command line so
> that the other specs are easier to write.
>
> Do not define this macro if it does not need to do anything.

— Macro: __OPTION_DEFAULT_SPECS__
> A list of specs used to support configure-time default options (i.e.
> `--with` options) in the driver. It should be a suitable initializer
> for an array of structures, each containing two strings, without the
> outermost pair of surrounding braces.
>
> The first item in the pair is the name of the default. This must match
> the code in `config.gcc` for the target. The second item is a spec
> to apply if a default with this name was specified. The string
> ``%(VALUE)`' in the spec will be replaced by the value of the default
> everywhere it occurs.
>
> The driver will apply these specs to its own command line between loading
> default `specs` files and processing `DRIVER_SELF_SPECS`, using
> the same mechanism as `DRIVER_SELF_SPECS`.
>
> Do not define this macro if it does not need to do anything.

— Macro: __CPP_SPEC__
> A C string constant that tells the GCC driver program options to
> pass to CPP. It can also specify how to translate options you
> give to GCC into options for GCC to pass to the CPP.
>
> Do not define this macro if it does not need to do anything.

— Macro: __CPLUSPLUS_CPP_SPEC__
> This macro is just like `CPP_SPEC`, but is used for C++, rather
> than C. If you do not define this macro, then the value of
> `CPP_SPEC` (if any) will be used instead.

— Macro: __CC1_SPEC__
> A C string constant that tells the GCC driver program options to
> pass to `cc1`, `cc1plus`, `f771`, and the other language
> front ends.
> It can also specify how to translate options you give to GCC into options
> for GCC to pass to front ends.
>
> Do not define this macro if it does not need to do anything.

— Macro: __CC1PLUS_SPEC__
> A C string constant that tells the GCC driver program options to
> pass to `cc1plus`. It can also specify how to translate options you
> give to GCC into options for GCC to pass to the `cc1plus`.
>
> Do not define this macro if it does not need to do anything.
> Note that everything defined in CC1_SPEC is already passed to
> `cc1plus` so there is no need to duplicate the contents of
> CC1_SPEC in CC1PLUS_SPEC.

— Macro: __ASM_SPEC__
> A C string constant that tells the GCC driver program options to
> pass to the assembler. It can also specify how to translate options
> you give to GCC into options for GCC to pass to the assembler.
> See the file `sun3.h` for an example of this.
>
> Do not define this macro if it does not need to do anything.

— Macro: __ASM_FINAL_SPEC__
> A C string constant that tells the GCC driver program how to
> run any programs which cleanup after the normal assembler.
> Normally, this is not needed. See the file `mips.h` for
> an example of this.
>
> Do not define this macro if it does not need to do anything.

— Macro: __AS_NEEDS_DASH_FOR_PIPED_INPUT__
> Define this macro, with no value, if the driver should give the assembler
> an argument consisting of a single dash, `-`, to instruct it to
> read from its standard input (which will be a pipe connected to the
> output of the compiler proper). This argument is given after any
> `-o` option specifying the name of the output file.
>
> If you do not define this macro, the assembler is assumed to read its
> standard input if given no non-option arguments. If your assembler
> cannot read standard input at all, use a ``%{pipe:%e}`' construct;
> see `mips.h` for instance.

— Macro: __LINK_SPEC__
> A C string constant that tells the GCC driver program options to
> pass to the linker. It can also specify how to translate options you
> give to GCC into options for GCC to pass to the linker.
>
> Do not define this macro if it does not need to do anything.

— Macro: __LIB_SPEC__
> Another C string constant used much like `LINK_SPEC`. The difference
> between the two is that `LIB_SPEC` is used at the end of the
> command given to the linker.
>
> If this macro is not defined, a default is provided that
> loads the standard C library from the usual place. See `gcc.c`.

— Macro: __LIBGCC_SPEC__
> Another C string constant that tells the GCC driver program
> how and when to place a reference to `libgcc.a` into the
> linker command line. This constant is placed both before and after
> the value of `LIB_SPEC`.
>
> If this macro is not defined, the GCC driver provides a default that
> passes the string `-lgcc` to the linker.

— Macro: __REAL_LIBGCC_SPEC__
> By default, if `ENABLE_SHARED_LIBGCC` is defined, the
> `LIBGCC_SPEC` is not directly used by the driver program but is
> instead modified to refer to different versions of `libgcc.a`
> depending on the values of the command line flags `-static`,
> `-shared`, `-static-libgcc`, and `-shared-libgcc`. On
> targets where these modifications are inappropriate, define
> `REAL_LIBGCC_SPEC` instead. `REAL_LIBGCC_SPEC` tells the
> driver how to place a reference to `libgcc` on the link command
> line, but, unlike `LIBGCC_SPEC`, it is used unmodified.

— Macro: __USE_LD_AS_NEEDED__
> A macro that controls the modifications to `LIBGCC_SPEC`
> mentioned in `REAL_LIBGCC_SPEC`. If nonzero, a spec will be
> generated that uses –as-needed and the shared libgcc in place of the
> static exception handler library, when linking without any of
> `-static`, `-static-libgcc`, or `-shared-libgcc`.

— Macro: __LINK_EH_SPEC__
> If defined, this C string constant is added to `LINK_SPEC`.
> When `USE_LD_AS_NEEDED` is zero or undefined, it also affects
> the modifications to `LIBGCC_SPEC` mentioned in
> `REAL_LIBGCC_SPEC`.

— Macro: __STARTFILE_SPEC__
> Another C string constant used much like `LINK_SPEC`. The
> difference between the two is that `STARTFILE_SPEC` is used at
> the very beginning of the command given to the linker.
>
> If this macro is not defined, a default is provided that loads the
> standard C startup file from the usual place. See `gcc.c`.

— Macro: __ENDFILE_SPEC__
> Another C string constant used much like `LINK_SPEC`. The
> difference between the two is that `ENDFILE_SPEC` is used at
> the very end of the command given to the linker.
>
> Do not define this macro if it does not need to do anything.

— Macro: __THREAD_MODEL_SPEC__
> GCC `-v` will print the thread model GCC was configured to use.
> However, this doesn't work on platforms that are multilibbed on thread
> models, such as AIX 4.3. On such platforms, define
> `THREAD_MODEL_SPEC` such that it evaluates to a string without
> blanks that names one of the recognized thread models. `%*`, the
> default value of this macro, will expand to the value of
> `thread_file` set in `config.gcc`.

— Macro: __SYSROOT_SUFFIX_SPEC__
> Define this macro to add a suffix to the target sysroot when GCC is
> configured with a sysroot. This will cause GCC to search for usr/lib,
> et al, within sysroot+suffix.

— Macro: __SYSROOT_HEADERS_SUFFIX_SPEC__
> Define this macro to add a headers_suffix to the target sysroot when
> GCC is configured with a sysroot. This will cause GCC to pass the
> updated sysroot+headers_suffix to CPP, causing it to search for
> usr/include, et al, within sysroot+headers_suffix.

— Macro: __EXTRA_SPECS__
> Define this macro to provide additional specifications to put in the
> `specs` file that can be used in various specifications like
> `CC1_SPEC`.
>
> The definition should be an initializer for an array of structures,
> containing a string constant, that defines the specification name, and a
> string constant that provides the specification.
>
> Do not define this macro if it does not need to do anything.
>
> `EXTRA_SPECS` is useful when an architecture contains several
> related targets, which have various `..._SPECS` which are similar
> to each other, and the maintainer would like one central place to keep
> these definitions.
>
> For example, the PowerPC System V.4 targets use `EXTRA_SPECS` to
> define either `_CALL_SYSV` when the System V calling sequence is
> used or `_CALL_AIX` when the older AIX-based calling sequence is
> used.
>
> The `config/rs6000/rs6000.h` target file defines:
>
> ```
>           #define EXTRA_SPECS \
>             { "cpp_sysv_default", CPP_SYSV_DEFAULT },
>
>           #define CPP_SYS_DEFAULT ""
>
> ```
>
> The `config/rs6000/sysv.h` target file defines:
>
> ```
>           #undef CPP_SPEC
>           #define CPP_SPEC \
>           "%{posix: -D_POSIX_SOURCE } \
>           %{mcall-sysv: -D_CALL_SYSV } \
>           %{!mcall-sysv: %(cpp_sysv_default) } \
>           %{msoft-float: -D_SOFT_FLOAT} %{mcpu=403: -D_SOFT_FLOAT}"
>
>           #undef CPP_SYSV_DEFAULT
>           #define CPP_SYSV_DEFAULT "-D_CALL_SYSV"
>
> ```
>
> while the `config/rs6000/eabiaix.h` target file defines
> `CPP_SYSV_DEFAULT` as:
>
> ```
>           #undef CPP_SYSV_DEFAULT
>           #define CPP_SYSV_DEFAULT "-D_CALL_AIX"
>
> ```

— Macro: __LINK_LIBGCC_SPECIAL_1__
> Define this macro if the driver program should find the library
> `libgcc.a`. If you do not define this macro, the driver program will pass
> the argument `-lgcc` to tell the linker to do the search.

— Macro: __LINK_GCC_C_SEQUENCE_SPEC__
> The sequence in which libgcc and libc are specified to the linker.
> By default this is `%G %L %G`.

— Macro: __LINK_COMMAND_SPEC__
> A C string constant giving the complete command line need to execute the
> linker. When you do this, you will need to update your port each time a
> change is made to the link command line within `gcc.c`. Therefore,
> define this macro only if you need to completely redefine the command
> line for invoking the linker and there is no other way to accomplish
> the effect you need. Overriding this macro may be avoidable by overriding
> `LINK_GCC_C_SEQUENCE_SPEC` instead.

— Macro: __LINK_ELIMINATE_DUPLICATE_LDIRECTORIES__
> A nonzero value causes `collect2` to remove duplicate `-Ldirectory` search
> directories from linking commands. Do not give it a nonzero value if
> removing duplicate search directories changes the linker's semantics.

— Macro: __MULTILIB_DEFAULTS__
> Define this macro as a C expression for the initializer of an array of
> string to tell the driver program which options are defaults for this
> target and thus do not need to be handled specially when using
> `MULTILIB_OPTIONS`.
>
> Do not define this macro if `MULTILIB_OPTIONS` is not defined in
> the target makefile fragment or if none of the options listed in
> `MULTILIB_OPTIONS` are set by default.
> See [Target Fragment](Target-Fragment.md#apple-krqxez3foqwum4tbm5wwk3tu).

— Macro: __RELATIVE_PREFIX_NOT_LINKDIR__
> Define this macro to tell `gcc` that it should only translate
> a `-B` prefix into a `-L` linker option if the prefix
> indicates an absolute file name.

— Macro: __MD_EXEC_PREFIX__
> If defined, this macro is an additional prefix to try after
> `STANDARD_EXEC_PREFIX`. `MD_EXEC_PREFIX` is not searched
> when the `-b` option is used, or the compiler is built as a cross
> compiler. If you define `MD_EXEC_PREFIX`, then be sure to add it
> to the list of directories used to find the assembler in `configure.in`.

— Macro: __STANDARD_STARTFILE_PREFIX__
> Define this macro as a C string constant if you wish to override the
> standard choice of `libdir` as the default prefix to
> try when searching for startup files such as `crt0.o`.
> `STANDARD_STARTFILE_PREFIX` is not searched when the compiler
> is built as a cross compiler.

— Macro: __STANDARD_STARTFILE_PREFIX_1__
> Define this macro as a C string constant if you wish to override the
> standard choice of `/lib` as a prefix to try after the default prefix
> when searching for startup files such as `crt0.o`.
> `STANDARD_STARTFILE_PREFIX_1` is not searched when the compiler
> is built as a cross compiler.

— Macro: __STANDARD_STARTFILE_PREFIX_2__
> Define this macro as a C string constant if you wish to override the
> standard choice of `/lib` as yet another prefix to try after the
> default prefix when searching for startup files such as `crt0.o`.
> `STANDARD_STARTFILE_PREFIX_2` is not searched when the compiler
> is built as a cross compiler.

— Macro: __MD_STARTFILE_PREFIX__
> If defined, this macro supplies an additional prefix to try after the
> standard prefixes. `MD_EXEC_PREFIX` is not searched when the
> `-b` option is used, or when the compiler is built as a cross
> compiler.

— Macro: __MD_STARTFILE_PREFIX_1__
> If defined, this macro supplies yet another prefix to try after the
> standard prefixes. It is not searched when the `-b` option is
> used, or when the compiler is built as a cross compiler.

— Macro: __INIT_ENVIRONMENT__
> Define this macro as a C string constant if you wish to set environment
> variables for programs called by the driver, such as the assembler and
> loader. The driver passes the value of this macro to `putenv` to
> initialize the necessary environment variables.

— Macro: __LOCAL_INCLUDE_DIR__
> Define this macro as a C string constant if you wish to override the
> standard choice of `/usr/local/include` as the default prefix to
> try when searching for local header files. `LOCAL_INCLUDE_DIR`
> comes before `SYSTEM_INCLUDE_DIR` in the search order.
>
> Cross compilers do not search either `/usr/local/include` or its
> replacement.

— Macro: __MODIFY_TARGET_NAME__
> Define this macro if you wish to define command-line switches that
> modify the default target name.
>
> For each switch, you can include a string to be appended to the first
> part of the configuration name or a string to be deleted from the
> configuration name, if present. The definition should be an initializer
> for an array of structures. Each array element should have three
> elements: the switch name (a string constant, including the initial
> dash), one of the enumeration codes `ADD` or `DELETE` to
> indicate whether the string should be inserted or deleted, and the string
> to be inserted or deleted (a string constant).
>
> For example, on a machine where ``64`' at the end of the
> configuration name denotes a 64-bit target and you want the `-32`
> and `-64` switches to select between 32- and 64-bit targets, you would
> code
>
> ```
>           #define MODIFY_TARGET_NAME \
>             { { "-32", DELETE, "64"}, \
>                {"-64", ADD, "64"}}
>
> ```

— Macro: __SYSTEM_INCLUDE_DIR__
> Define this macro as a C string constant if you wish to specify a
> system-specific directory to search for header files before the standard
> directory. `SYSTEM_INCLUDE_DIR` comes before
> `STANDARD_INCLUDE_DIR` in the search order.
>
> Cross compilers do not use this macro and do not search the directory
> specified.

— Macro: __STANDARD_INCLUDE_DIR__
> Define this macro as a C string constant if you wish to override the
> standard choice of `/usr/include` as the default prefix to
> try when searching for header files.
>
> Cross compilers ignore this macro and do not search either
> `/usr/include` or its replacement.

— Macro: __STANDARD_INCLUDE_COMPONENT__
> The “component” corresponding to `STANDARD_INCLUDE_DIR`.
> See `INCLUDE_DEFAULTS`, below, for the description of components.
> If you do not define this macro, no component is used.

— Macro: __INCLUDE_DEFAULTS__
> Define this macro if you wish to override the entire default search path
> for include files. For a native compiler, the default search path
> usually consists of `GCC_INCLUDE_DIR`, `LOCAL_INCLUDE_DIR`,
> `SYSTEM_INCLUDE_DIR`, `GPLUSPLUS_INCLUDE_DIR`, and
> `STANDARD_INCLUDE_DIR`. In addition, `GPLUSPLUS_INCLUDE_DIR`
> and `GCC_INCLUDE_DIR` are defined automatically by `Makefile`,
> and specify private search areas for GCC. The directory
> `GPLUSPLUS_INCLUDE_DIR` is used only for C++ programs.
>
> The definition should be an initializer for an array of structures.
> Each array element should have four elements: the directory name (a
> string constant), the component name (also a string constant), a flag
> for C++-only directories,
> and a flag showing that the includes in the directory don't need to be
> wrapped in `` extern ` ``C`'` when compiling C++. Mark the end of
> the array with a null element.
>
> The component name denotes what GNU package the include file is part of,
> if any, in all uppercase letters. For example, it might be ``GCC`'
> or ``BINUTILS`'. If the package is part of a vendor-supplied
> operating system, code the component name as ``0`'.
>
> For example, here is the definition used for VAX/VMS:
>
> ```
>           #define INCLUDE_DEFAULTS \
>           {                                       \
>             { "GNU_GXX_INCLUDE:", "G++", 1, 1},   \
>             { "GNU_CC_INCLUDE:", "GCC", 0, 0},    \
>             { "SYS$SYSROOT:[SYSLIB.]", 0, 0, 0},  \
>             { ".", 0, 0, 0},                      \
>             { 0, 0, 0, 0}                         \
>           }
>
> ```

Here is the order of prefixes tried for exec files:

1. Any prefixes specified by the user with `-B`.
2. The environment variable `GCC_EXEC_PREFIX`, if any.
3. The directories specified by the environment variable `COMPILER_PATH`.
4. The macro `STANDARD_EXEC_PREFIX`.
5. `/usr/lib/gcc/`.
6. The macro `MD_EXEC_PREFIX`, if any.

Here is the order of prefixes tried for startfiles:

1. Any prefixes specified by the user with `-B`.
2. The environment variable `GCC_EXEC_PREFIX`, if any.
3. The directories specified by the environment variable `LIBRARY_PATH`
   (or port-specific name; native only, cross compilers do not use this).
4. The macro `STANDARD_EXEC_PREFIX`.
5. `/usr/lib/gcc/`.
6. The macro `MD_EXEC_PREFIX`, if any.
7. The macro `MD_STARTFILE_PREFIX`, if any.
8. The macro `STANDARD_STARTFILE_PREFIX`.
9. `/lib/`.
10. `/usr/lib/`.
