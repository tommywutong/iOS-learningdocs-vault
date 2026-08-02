---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Stack-Arguments.html
archived_at: '2026-07-15T07:31:00.763542Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Register Arguments](Register-Arguments.md#apple-kjswo2ltorsxelkbojtxk3lfnz2hg),
Previous: [Elimination](Elimination.md#apple-ivwgs3ljnzqxi2lpny),
Up: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq)

---

#### 13.9.6 Passing Function Arguments on the Stack

The macros in this section control how arguments are passed
on the stack. See the following section for other macros that
control passing certain arguments in registers.

— Target Hook: bool __TARGET_PROMOTE_PROTOTYPES__ (tree fntype)
> This target hook returns `true` if an argument declared in a
> prototype as an integral type smaller than `int` should actually be
> passed as an `int`. In addition to avoiding errors in certain
> cases of mismatch, it also makes for better code on certain machines.
> The default is to not promote prototypes.

— Macro: __PUSH_ARGS__
> A C expression. If nonzero, push insns will be used to pass
> outgoing arguments.
> If the target machine does not have a push instruction, set it to zero.
> That directs GCC to use an alternate strategy: to
> allocate the entire argument block and then store the arguments into
> it. When `PUSH_ARGS` is nonzero, `PUSH_ROUNDING` must be defined too.

— Macro: __PUSH_ARGS_REVERSED__
> A C expression. If nonzero, function arguments will be evaluated from
> last to first, rather than from first to last. If this macro is not
> defined, it defaults to `PUSH_ARGS` on targets where the stack
> and args grow in opposite directions, and 0 otherwise.

— Macro: __PUSH_ROUNDING__ (npushed)
> A C expression that is the number of bytes actually pushed onto the
> stack when an instruction attempts to push npushed bytes.
>
> On some machines, the definition
>
> ```
>           #define PUSH_ROUNDING(BYTES) (BYTES)
>
> ```
>
> will suffice. But on other machines, instructions that appear
> to push one byte actually push two bytes in an attempt to maintain
> alignment. Then the definition should be
>
> ```
>           #define PUSH_ROUNDING(BYTES) (((BYTES) + 1) & ~1)
>
> ```

— Macro: __ACCUMULATE_OUTGOING_ARGS__
> A C expression. If nonzero, the maximum amount of space required for outgoing arguments
> will be computed and placed into the variable
> `current_function_outgoing_args_size`. No space will be pushed
> onto the stack for each call; instead, the function prologue should
> increase the stack frame size by this amount.
>
> Setting both `PUSH_ARGS` and `ACCUMULATE_OUTGOING_ARGS`
> is not proper.

— Macro: __REG_PARM_STACK_SPACE__ (fndecl)
> Define this macro if functions should assume that stack space has been
> allocated for arguments even when their values are passed in
> registers.
>
> The value of this macro is the size, in bytes, of the area reserved for
> arguments passed in registers for the function represented by fndecl,
> which can be zero if GCC is calling a library function.
>
> This space can be allocated by the caller, or be a part of the
> machine-dependent stack frame: `OUTGOING_REG_PARM_STACK_SPACE` says
> which.

— Macro: __OUTGOING_REG_PARM_STACK_SPACE__
> Define this if it is the responsibility of the caller to allocate the area
> reserved for arguments passed in registers.
>
> If `ACCUMULATE_OUTGOING_ARGS` is defined, this macro controls
> whether the space for these arguments counts in the value of
> `current_function_outgoing_args_size`.

— Macro: __STACK_PARMS_IN_REG_PARM_AREA__
> Define this macro if `REG_PARM_STACK_SPACE` is defined, but the
> stack parameters don't skip the area specified by it.
>
> Normally, when a parameter is not passed in registers, it is placed on the
> stack beyond the `REG_PARM_STACK_SPACE` area. Defining this macro
> suppresses this behavior and causes the parameter to be passed on the
> stack in its natural location.

— Macro: __RETURN_POPS_ARGS__ (fundecl, funtype, stack-size)
> A C expression that should indicate the number of bytes of its own
> arguments that a function pops on returning, or 0 if the
> function pops no arguments and the caller must therefore pop them all
> after the function returns.
>
> fundecl is a C variable whose value is a tree node that describes
> the function in question. Normally it is a node of type
> `FUNCTION_DECL` that describes the declaration of the function.
> From this you can obtain the `DECL_ATTRIBUTES` of the function.
>
> funtype is a C variable whose value is a tree node that
> describes the function in question. Normally it is a node of type
> `FUNCTION_TYPE` that describes the data type of the function.
> From this it is possible to obtain the data types of the value and
> arguments (if known).
>
> When a call to a library function is being considered, fundecl
> will contain an identifier node for the library function. Thus, if
> you need to distinguish among various library functions, you can do so
> by their names. Note that “library function” in this context means
> a function used to perform arithmetic, whose name is known specially
> in the compiler and was not mentioned in the C code being compiled.
>
> stack-size is the number of bytes of arguments passed on the
> stack. If a variable number of bytes is passed, it is zero, and
> argument popping will always be the responsibility of the calling function.
>
> On the VAX, all functions always pop their arguments, so the definition
> of this macro is stack-size. On the 68000, using the standard
> calling convention, no functions pop their arguments, so the value of
> the macro is always 0 in this case. But an alternative calling
> convention is available in which functions that take a fixed number of
> arguments pop them but other functions (such as `printf`) pop
> nothing (the caller pops all). When this convention is in use,
> funtype is examined to determine whether a function takes a fixed
> number of arguments.

— Macro: __CALL_POPS_ARGS__ (cum)
> A C expression that should indicate the number of bytes a call sequence
> pops off the stack. It is added to the value of `RETURN_POPS_ARGS`
> when compiling a function call.
>
> cum is the variable in which all arguments to the called function
> have been accumulated.
>
> On certain architectures, such as the SH5, a call trampoline is used
> that pops certain registers off the stack, depending on the arguments
> that have been passed to the function. Since this is a property of the
> call site, not of the called function, `RETURN_POPS_ARGS` is not
> appropriate.
