---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Profiling.html
archived_at: '2026-07-15T07:31:00.562499Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Tail Calls](Tail-Calls.md#apple-krqws3bninqwy3dt),
Previous: [Function Entry](Function-Entry.md#apple-iz2w4y3unfxw4lkfnz2he6i),
Up: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq)

---

#### 13.9.12 Generating Code for Profiling

These macros will help you generate code for profiling.

— Macro: __FUNCTION_PROFILER__ (file, labelno)
> A C statement or compound statement to output to file some
> assembler code to call the profiling subroutine `mcount`.
>
> The details of how `mcount` expects to be called are determined by
> your operating system environment, not by GCC. To figure them out,
> compile a small program for profiling using the system's installed C
> compiler and look at the assembler code that results.
>
> Older implementations of `mcount` expect the address of a counter
> variable to be loaded into some register. The name of this variable is
> ``LP`' followed by the number labelno, so you would generate
> the name using ``LP%d`' in a `fprintf`.

— Macro: __PROFILE_HOOK__
> A C statement or compound statement to output to file some assembly
> code to call the profiling subroutine `mcount` even the target does
> not support profiling.

— Macro: __NO_PROFILE_COUNTERS__
> Define this macro if the `mcount` subroutine on your system does
> not need a counter variable allocated for each function. This is true
> for almost all modern implementations. If you define this macro, you
> must not use the labelno argument to `FUNCTION_PROFILER`.

— Macro: __PROFILE_BEFORE_PROLOGUE__
> Define this macro if the code for function profiling should come before
> the function prologue. Normally, the profiling code comes after.
