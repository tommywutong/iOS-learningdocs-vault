---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Library-Calls.html
archived_at: '2026-07-15T07:31:00.181894Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Addressing Modes](Addressing-Modes.md#apple-ifsgi4tfonzws3thfvgw6zdfom),
Previous: [Trampolines](Trampolines.md#apple-krzgc3lqn5wgs3tfom),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 13.12 Implicit Calls to Library Routines

Here is an explanation of implicit calls to library routines.

— Macro: __DECLARE_LIBRARY_RENAMES__
> This macro, if defined, should expand to a piece of C code that will get
> expanded when compiling functions for libgcc.a. It can be used to
> provide alternate names for GCC's internal library functions if there
> are ABI-mandated names that the compiler should provide.

— Target Hook: void __TARGET_INIT_LIBFUNCS__ (void)
> This hook should declare additional library routines or rename
> existing ones, using the functions `set_optab_libfunc` and
> `init_one_libfunc` defined in `optabs.c`.
> `init_optabs` calls this macro after initializing all the normal
> library routines.
>
> The default is to do nothing. Most ports don't need to define this hook.

— Macro: __FLOAT_LIB_COMPARE_RETURNS_BOOL__ (mode, comparison)
> This macro should return `true` if the library routine that
> implements the floating point comparison operator comparison in
> mode mode will return a boolean, and false if it will
> return a tristate.
>
> GCC's own floating point libraries return tristates from the
> comparison operators, so the default returns false always. Most ports
> don't need to define this macro.

— Macro: __TARGET_LIB_INT_CMP_BIASED__
> This macro should evaluate to `true` if the integer comparison
> functions (like `__cmpdi2`) return 0 to indicate that the first
> operand is smaller than the second, 1 to indicate that they are equal,
> and 2 to indicate that the first operand is greater than the second.
> If this macro evaluates to `false` the comparison functions return
> −1, 0, and 1 instead of 0, 1, and 2. If the target uses the routines
> in `libgcc.a`, you do not need to define this macro.

— Macro: __US_SOFTWARE_GOFAST__
> Define this macro if your system C library uses the US Software GOFAST
> library to provide floating point emulation.
>
> In addition to defining this macro, your architecture must set
> `TARGET_INIT_LIBFUNCS` to `gofast_maybe_init_libfuncs`, or
> else call that function from its version of that hook. It is defined
> in `config/gofast.h`, which must be included by your
> architecture's `cpu.c` file. See `sparc/sparc.c` for
> an example.
>
> If this macro is defined, the
> `TARGET_FLOAT_LIB_COMPARE_RETURNS_BOOL` target hook must return
> false for `SFmode` and `DFmode` comparisons.

— Macro: __TARGET_EDOM__
> The value of `EDOM` on the target machine, as a C integer constant
> expression. If you don't define this macro, GCC does not attempt to
> deposit the value of `EDOM` into `errno` directly. Look in
> `/usr/include/errno.h` to find the value of `EDOM` on your
> system.
>
> If you do not define `TARGET_EDOM`, then compiled code reports
> domain errors by calling the library function and letting it report the
> error. If mathematical functions on your system use `matherr` when
> there is an error, then you should leave `TARGET_EDOM` undefined so
> that `matherr` is used normally.

— Macro: __GEN_ERRNO_RTX__
> Define this macro as a C expression to create an rtl expression that
> refers to the global “variable” `errno`. (On certain systems,
> `errno` may not actually be a variable.) If you don't define this
> macro, a reasonable default is used.

— Macro: __TARGET_C99_FUNCTIONS__
> When this macro is nonzero, GCC will implicitly optimize `sin` calls into
> `sinf` and similarly for other functions defined by C99 standard. The
> default is nonzero that should be proper value for most modern systems, however
> number of existing systems lacks support for these functions in the runtime so
> they needs this macro to be redefined to 0.

— Macro: __NEXT_OBJC_RUNTIME__
> Define this macro to generate code for Objective-C message sending using
> the calling convention of the NeXT system. This calling convention
> involves passing the object, the selector and the method arguments all
> at once to the method-lookup library function.
>
> The default calling convention passes just the object and the selector
> to the lookup function, which returns a pointer to the method.
