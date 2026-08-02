---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Stack-Checking.html
archived_at: '2026-07-15T07:31:00.769658Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Frame Registers](Frame-Registers.md#apple-izzgc3lffvjgkz3jon2gk4tt),
Previous: [Exception Handling](Exception-Handling.md#apple-iv4ggzlqoruw63rnjbqw4zdmnfxgo),
Up: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq)

---

#### 13.9.3 Specifying How Stack Checking is Done

GCC will check that stack references are within the boundaries of
the stack, if the `-fstack-check` is specified, in one of three ways:

1. If the value of the `STACK_CHECK_BUILTIN` macro is nonzero, GCC
   will assume that you have arranged for stack checking to be done at
   appropriate places in the configuration files, e.g., in
   `TARGET_ASM_FUNCTION_PROLOGUE`. GCC will do not other special
   processing.
2. If `STACK_CHECK_BUILTIN` is zero and you defined a named pattern
   called `check_stack` in your `md` file, GCC will call that
   pattern with one argument which is the address to compare the stack
   value against. You must arrange for this pattern to report an error if
   the stack pointer is out of range.
3. If neither of the above are true, GCC will generate code to periodically
   “probe” the stack pointer using the values of the macros defined below.

Normally, you will use the default values of these macros, so GCC
will use the third approach.

— Macro: __STACK_CHECK_BUILTIN__
> A nonzero value if stack checking is done by the configuration files in a
> machine-dependent manner. You should define this macro if stack checking
> is require by the ABI of your machine or if you would like to have to stack
> checking in some more efficient way than GCC's portable approach.
> The default value of this macro is zero.

— Macro: __STACK_CHECK_PROBE_INTERVAL__
> An integer representing the interval at which GCC must generate stack
> probe instructions. You will normally define this macro to be no larger
> than the size of the “guard pages” at the end of a stack area. The
> default value of 4096 is suitable for most systems.

— Macro: __STACK_CHECK_PROBE_LOAD__
> A integer which is nonzero if GCC should perform the stack probe
> as a load instruction and zero if GCC should use a store instruction.
> The default is zero, which is the most efficient choice on most systems.

— Macro: __STACK_CHECK_PROTECT__
> The number of bytes of stack needed to recover from a stack overflow,
> for languages where such a recovery is supported. The default value of
> 75 words should be adequate for most machines.

— Macro: __STACK_CHECK_MAX_FRAME_SIZE__
> The maximum size of a stack frame, in bytes. GCC will generate probe
> instructions in non-leaf functions to ensure at least this many bytes of
> stack are available. If a stack frame is larger than this size, stack
> checking will not be reliable and GCC will issue a warning. The
> default is chosen so that GCC only generates one instruction on most
> systems. You should normally not change the default value of this macro.

— Macro: __STACK_CHECK_FIXED_FRAME_SIZE__
> GCC uses this value to generate the above warning message. It
> represents the amount of fixed frame used by a function, not including
> space for any callee-saved registers, temporaries and user variables.
> You need only specify an upper bound for this amount and will normally
> use the default of four words.

— Macro: __STACK_CHECK_MAX_VAR_SIZE__
> The maximum size, in bytes, of an object that GCC will place in the
> fixed area of the stack frame when the user specifies
> `-fstack-check`.
> GCC computed the default from the values of the above macros and you will
> normally not need to override that default.
