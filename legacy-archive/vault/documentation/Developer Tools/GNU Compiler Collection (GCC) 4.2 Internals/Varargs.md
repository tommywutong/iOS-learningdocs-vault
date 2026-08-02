---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Varargs.html
archived_at: '2026-07-15T07:31:03.090168Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Trampolines](Trampolines.md#apple-krzgc3lqn5wgs3tfom),
Previous: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.11 Implementing the Varargs Macros

GCC comes with an implementation of `<varargs.h>` and
`<stdarg.h>` that work without change on machines that pass arguments
on the stack. Other machines require their own implementations of
varargs, and the two machine independent header files must have
conditionals to include it.

ISO `<stdarg.h>` differs from traditional `<varargs.h>` mainly in
the calling convention for `va_start`. The traditional
implementation takes just one argument, which is the variable in which
to store the argument pointer. The ISO implementation of
`va_start` takes an additional second argument. The user is
supposed to write the last named argument of the function here.

However, `va_start` should not use this argument. The way to find
the end of the named arguments is with the built-in functions described
below.

— Macro: ____builtin_saveregs__ ()
> Use this built-in function to save the argument registers in memory so
> that the varargs mechanism can access them. Both ISO and traditional
> versions of `va_start` must use `__builtin_saveregs`, unless
> you use `TARGET_SETUP_INCOMING_VARARGS` (see below) instead.
>
> On some machines, `__builtin_saveregs` is open-coded under the
> control of the target hook `TARGET_EXPAND_BUILTIN_SAVEREGS`. On
> other machines, it calls a routine written in assembler language,
> found in `libgcc2.c`.
>
> Code generated for the call to `__builtin_saveregs` appears at the
> beginning of the function, as opposed to where the call to
> `__builtin_saveregs` is written, regardless of what the code is.
> This is because the registers must be saved before the function starts
> to use them for its own purposes.

— Macro: ____builtin_args_info__ (category)
> Use this built-in function to find the first anonymous arguments in
> registers.
>
> In general, a machine may have several categories of registers used for
> arguments, each for a particular category of data types. (For example,
> on some machines, floating-point registers are used for floating-point
> arguments while other arguments are passed in the general registers.)
> To make non-varargs functions use the proper calling convention, you
> have defined the `CUMULATIVE_ARGS` data type to record how many
> registers in each category have been used so far
>
> `__builtin_args_info` accesses the same data structure of type
> `CUMULATIVE_ARGS` after the ordinary argument layout is finished
> with it, with category specifying which word to access. Thus, the
> value indicates the first unused register in a given category.
>
> Normally, you would use `__builtin_args_info` in the implementation
> of `va_start`, accessing each category just once and storing the
> value in the `va_list` object. This is because `va_list` will
> have to update the values, and there is no way to alter the
> values accessed by `__builtin_args_info`.

— Macro: ____builtin_next_arg__ (lastarg)
> This is the equivalent of `__builtin_args_info`, for stack
> arguments. It returns the address of the first anonymous stack
> argument, as type `void *`. If `ARGS_GROW_DOWNWARD`, it
> returns the address of the location above the first anonymous stack
> argument. Use it in `va_start` to initialize the pointer for
> fetching arguments from the stack. Also use it in `va_start` to
> verify that the second parameter lastarg is the last named argument
> of the current function.

— Macro: ____builtin_classify_type__ (object)
> Since each machine has its own conventions for which data types are
> passed in which kind of register, your implementation of `va_arg`
> has to embody these conventions. The easiest way to categorize the
> specified data type is to use `__builtin_classify_type` together
> with `sizeof` and `__alignof__`.
>
> `__builtin_classify_type` ignores the value of object,
> considering only its data type. It returns an integer describing what
> kind of type that is—integer, floating, pointer, structure, and so on.
>
> The file `typeclass.h` defines an enumeration that you can use to
> interpret the values of `__builtin_classify_type`.

These machine description macros help implement varargs:

— Target Hook: rtx __TARGET_EXPAND_BUILTIN_SAVEREGS__ (void)
> If defined, this hook produces the machine-specific code for a call to
> `__builtin_saveregs`. This code will be moved to the very
> beginning of the function, before any parameter access are made. The
> return value of this function should be an RTX that contains the value
> to use as the return of `__builtin_saveregs`.

— Target Hook: void __TARGET_SETUP_INCOMING_VARARGS__ (CUMULATIVE_ARGS \*args_so_far, enum machine_mode mode, tree type, int \*pretend_args_size, int second_time)
> This target hook offers an alternative to using
> `__builtin_saveregs` and defining the hook
> `TARGET_EXPAND_BUILTIN_SAVEREGS`. Use it to store the anonymous
> register arguments into the stack so that all the arguments appear to
> have been passed consecutively on the stack. Once this is done, you can
> use the standard implementation of varargs that works for machines that
> pass all their arguments on the stack.
>
> The argument args_so_far points to the `CUMULATIVE_ARGS` data
> structure, containing the values that are obtained after processing the
> named arguments. The arguments mode and type describe the
> last named argument—its machine mode and its data type as a tree node.
>
> The target hook should do two things: first, push onto the stack all the
> argument registers _not_ used for the named arguments, and second,
> store the size of the data thus pushed into the `int`-valued
> variable pointed to by pretend_args_size. The value that you
> store here will serve as additional offset for setting up the stack
> frame.
>
> Because you must generate code to push the anonymous arguments at
> compile time without knowing their data types,
> `TARGET_SETUP_INCOMING_VARARGS` is only useful on machines that
> have just a single category of argument register and use it uniformly
> for all data types.
>
> If the argument second_time is nonzero, it means that the
> arguments of the function are being analyzed for the second time. This
> happens for an inline function, which is not actually compiled until the
> end of the source file. The hook `TARGET_SETUP_INCOMING_VARARGS` should
> not generate any instructions in this case.

— Target Hook: bool __TARGET_STRICT_ARGUMENT_NAMING__ (CUMULATIVE_ARGS \*ca)
> Define this hook to return `true` if the location where a function
> argument is passed depends on whether or not it is a named argument.
>
> This hook controls how the named argument to `FUNCTION_ARG`
> is set for varargs and stdarg functions. If this hook returns
> `true`, the named argument is always true for named
> arguments, and false for unnamed arguments. If it returns `false`,
> but `TARGET_PRETEND_OUTGOING_VARARGS_NAMED` returns `true`,
> then all arguments are treated as named. Otherwise, all named arguments
> except the last are treated as named.
>
> You need not define this hook if it always returns zero.

— Target Hook: bool __TARGET_PRETEND_OUTGOING_VARARGS_NAMED__
> If you need to conditionally change ABIs so that one works with
> `TARGET_SETUP_INCOMING_VARARGS`, but the other works like neither
> `TARGET_SETUP_INCOMING_VARARGS` nor `TARGET_STRICT_ARGUMENT_NAMING` was
> defined, then define this hook to return `true` if
> `TARGET_SETUP_INCOMING_VARARGS` is used, `false` otherwise.
> Otherwise, you should not define this hook.
