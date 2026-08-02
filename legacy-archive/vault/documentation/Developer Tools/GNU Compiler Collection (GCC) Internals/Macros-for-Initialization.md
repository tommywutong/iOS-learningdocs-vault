---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Macros-for-Initialization.html
archived_at: '2026-07-15T07:31:00.330645Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Instruction Output](Instruction-Output.md#apple-jfxhg5dsovrxi2lpnywu65luob2xi),
Previous: [Initialization](Initialization.md#apple-jfxgs5djmfwgs6tboruw63q),
Up: [Assembler Format](Assembler-Format.md#apple-ifzxgzlnmjwgk4rnizxxe3lboq)

---

#### 13.19.6 Macros Controlling Initialization Routines

Here are the macros that control how the compiler handles initialization
and termination functions:

— Macro: __INIT_SECTION_ASM_OP__
> If defined, a C string constant, including spacing, for the assembler
> operation to identify the following data as initialization code. If not
> defined, GCC will assume such a section does not exist. When you are
> using special sections for initialization and termination functions, this
> macro also controls how `crtstuff.c` and `libgcc2.c` arrange to
> run the initialization functions.

— Macro: __HAS_INIT_SECTION__
> If defined, `main` will not call `__main` as described above.
> This macro should be defined for systems that control start-up code
> on a symbol-by-symbol basis, such as OSF/1, and should not
> be defined explicitly for systems that support `INIT_SECTION_ASM_OP`.

— Macro: __LD_INIT_SWITCH__
> If defined, a C string constant for a switch that tells the linker that
> the following symbol is an initialization routine.

— Macro: __LD_FINI_SWITCH__
> If defined, a C string constant for a switch that tells the linker that
> the following symbol is a finalization routine.

— Macro: __COLLECT_SHARED_INIT_FUNC__ (stream, func)
> If defined, a C statement that will write a function that can be
> automatically called when a shared library is loaded. The function
> should call func, which takes no arguments. If not defined, and
> the object format requires an explicit initialization function, then a
> function called `_GLOBAL__DI` will be generated.
>
> This function and the following one are used by collect2 when linking a
> shared library that needs constructors or destructors, or has DWARF2
> exception tables embedded in the code.

— Macro: __COLLECT_SHARED_FINI_FUNC__ (stream, func)
> If defined, a C statement that will write a function that can be
> automatically called when a shared library is unloaded. The function
> should call func, which takes no arguments. If not defined, and
> the object format requires an explicit finalization function, then a
> function called `_GLOBAL__DD` will be generated.

— Macro: __INVOKE__main__
> If defined, `main` will call `__main` despite the presence of
> `INIT_SECTION_ASM_OP`. This macro should be defined for systems
> where the init section is not actually run automatically, but is still
> useful for collecting the lists of constructors and destructors.

— Macro: __SUPPORTS_INIT_PRIORITY__
> If nonzero, the C++ `init_priority` attribute is supported and the
> compiler should emit instructions to control the order of initialization
> of objects. If zero, the compiler will issue an error message upon
> encountering an `init_priority` attribute.

— Target Hook: bool __TARGET_HAVE_CTORS_DTORS__
> This value is true if the target supports some “native” method of
> collecting constructors and destructors to be run at startup and exit.
> It is false if we must use `collect2`.

— Target Hook: void __TARGET_ASM_CONSTRUCTOR__ (rtx symbol, int priority)
> If defined, a function that outputs assembler code to arrange to call
> the function referenced by symbol at initialization time.
>
> Assume that symbol is a `SYMBOL_REF` for a function taking
> no arguments and with no return value. If the target supports initialization
> priorities, priority is a value between 0 and `MAX_INIT_PRIORITY`;
> otherwise it must be `DEFAULT_INIT_PRIORITY`.
>
> If this macro is not defined by the target, a suitable default will
> be chosen if (1) the target supports arbitrary section names, (2) the
> target defines `CTORS_SECTION_ASM_OP`, or (3) `USE_COLLECT2`
> is not defined.

— Target Hook: void __TARGET_ASM_DESTRUCTOR__ (rtx symbol, int priority)
> This is like `TARGET_ASM_CONSTRUCTOR` but used for termination
> functions rather than initialization functions.

If `TARGET_HAVE_CTORS_DTORS` is true, the initialization routine
generated for the generated object file will have static linkage.

If your system uses `collect2` as the means of processing
constructors, then that program normally uses `nm` to scan
an object file for constructor functions to be called.

On certain kinds of systems, you can define this macro to make
`collect2` work faster (and, in some cases, make it work at all):

— Macro: __OBJECT_FORMAT_COFF__
> Define this macro if the system uses COFF (Common Object File Format)
> object files, so that `collect2` can assume this format and scan
> object files directly for dynamic constructor/destructor functions.
>
> This macro is effective only in a native compiler; `collect2` as
> part of a cross compiler always uses `nm` for the target machine.

— Macro: __REAL_NM_FILE_NAME__
> Define this macro as a C string constant containing the file name to use
> to execute `nm`. The default is to search the path normally for
> `nm`.
>
> If your system supports shared libraries and has a program to list the
> dynamic dependencies of a given library or executable, you can define
> these macros to enable support for running initialization and
> termination functions in shared libraries:

— Macro: __LDD_SUFFIX__
> Define this macro to a C string constant containing the name of the program
> which lists dynamic dependencies, like `"ldd"` under SunOS 4.

— Macro: __PARSE_LDD_OUTPUT__ (ptr)
> Define this macro to be C code that extracts filenames from the output
> of the program denoted by `LDD_SUFFIX`. ptr is a variable
> of type `char *` that points to the beginning of a line of output
> from `LDD_SUFFIX`. If the line lists a dynamic dependency, the
> code must advance ptr to the beginning of the filename on that
> line. Otherwise, it must set ptr to `NULL`.
