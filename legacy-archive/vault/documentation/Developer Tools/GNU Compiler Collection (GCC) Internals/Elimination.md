---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Elimination.html
archived_at: '2026-07-15T07:30:59.767843Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Stack Arguments](Stack-Arguments.md#apple-kn2gcy3lfvaxez3vnvsw45dt),
Previous: [Frame Registers](Frame-Registers.md#apple-izzgc3lffvjgkz3jon2gk4tt),
Up: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq)

---

#### 13.9.5 Eliminating Frame Pointer and Arg Pointer

This is about eliminating the frame pointer and arg pointer.

— Macro: __FRAME_POINTER_REQUIRED__
> A C expression which is nonzero if a function must have and use a frame
> pointer. This expression is evaluated in the reload pass. If its value is
> nonzero the function will have a frame pointer.
>
> The expression can in principle examine the current function and decide
> according to the facts, but on most machines the constant 0 or the
> constant 1 suffices. Use 0 when the machine allows code to be generated
> with no frame pointer, and doing so saves some time or space. Use 1
> when there is no possible advantage to avoiding a frame pointer.
>
> In certain cases, the compiler does not know how to produce valid code
> without a frame pointer. The compiler recognizes those cases and
> automatically gives the function a frame pointer regardless of what
> `FRAME_POINTER_REQUIRED` says. You don't need to worry about
> them.
>
> In a function that does not require a frame pointer, the frame pointer
> register can be allocated for ordinary usage, unless you mark it as a
> fixed register. See `FIXED_REGISTERS` for more information.

— Macro: __INITIAL_FRAME_POINTER_OFFSET__ (depth-var)
> A C statement to store in the variable depth-var the difference
> between the frame pointer and the stack pointer values immediately after
> the function prologue. The value would be computed from information
> such as the result of `get_frame_size ()` and the tables of
> registers `regs_ever_live` and `call_used_regs`.
>
> If `ELIMINABLE_REGS` is defined, this macro will be not be used and
> need not be defined. Otherwise, it must be defined even if
> `FRAME_POINTER_REQUIRED` is defined to always be true; in that
> case, you may set depth-var to anything.

— Macro: __ELIMINABLE_REGS__
> If defined, this macro specifies a table of register pairs used to
> eliminate unneeded registers that point into the stack frame. If it is not
> defined, the only elimination attempted by the compiler is to replace
> references to the frame pointer with references to the stack pointer.
>
> The definition of this macro is a list of structure initializations, each
> of which specifies an original and replacement register.
>
> On some machines, the position of the argument pointer is not known until
> the compilation is completed. In such a case, a separate hard register
> must be used for the argument pointer. This register can be eliminated by
> replacing it with either the frame pointer or the argument pointer,
> depending on whether or not the frame pointer has been eliminated.
>
> In this case, you might specify:
>
> ```
>           #define ELIMINABLE_REGS  \
>           {{ARG_POINTER_REGNUM, STACK_POINTER_REGNUM}, \
>            {ARG_POINTER_REGNUM, FRAME_POINTER_REGNUM}, \
>            {FRAME_POINTER_REGNUM, STACK_POINTER_REGNUM}}
>
> ```
>
> Note that the elimination of the argument pointer with the stack pointer is
> specified first since that is the preferred elimination.

— Macro: __CAN_ELIMINATE__ (from-reg, to-reg)
> A C expression that returns nonzero if the compiler is allowed to try
> to replace register number from-reg with register number
> to-reg. This macro need only be defined if `ELIMINABLE_REGS`
> is defined, and will usually be the constant 1, since most of the cases
> preventing register elimination are things that the compiler already
> knows about.

— Macro: __INITIAL_ELIMINATION_OFFSET__ (from-reg, to-reg, offset-var)
> This macro is similar to `INITIAL_FRAME_POINTER_OFFSET`. It
> specifies the initial difference between the specified pair of
> registers. This macro must be defined if `ELIMINABLE_REGS` is
> defined.
