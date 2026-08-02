---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Register-Arguments.html
archived_at: '2026-07-15T07:31:00.610599Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Scalar Return](Scalar-Return.md#apple-knrwc3dboiwvezluovzg4),
Previous: [Stack Arguments](Stack-Arguments.md#apple-kn2gcy3lfvaxez3vnvsw45dt),
Up: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq)

---

#### 13.9.7 Passing Arguments in Registers

This section describes the macros which let you control how various
types of arguments are passed in registers or how they are arranged in
the stack.

— Macro: __FUNCTION_ARG__ (cum, mode, type, named)
> A C expression that controls whether a function argument is passed
> in a register, and which register.
>
> The arguments are cum, which summarizes all the previous
> arguments; mode, the machine mode of the argument; type,
> the data type of the argument as a tree node or 0 if that is not known
> (which happens for C support library functions); and named,
> which is 1 for an ordinary argument and 0 for nameless arguments that
> correspond to ``...`' in the called function's prototype.
> type can be an incomplete type if a syntax error has previously
> occurred.
>
> The value of the expression is usually either a `reg` RTX for the
> hard register in which to pass the argument, or zero to pass the
> argument on the stack.
>
> For machines like the VAX and 68000, where normally all arguments are
> pushed, zero suffices as a definition.
>
> The value of the expression can also be a `parallel` RTX. This is
> used when an argument is passed in multiple locations. The mode of the
> `parallel` should be the mode of the entire argument. The
> `parallel` holds any number of `expr_list` pairs; each one
> describes where part of the argument is passed. In each
> `expr_list` the first operand must be a `reg` RTX for the hard
> register in which to pass this part of the argument, and the mode of the
> register RTX indicates how large this part of the argument is. The
> second operand of the `expr_list` is a `const_int` which gives
> the offset in bytes into the entire argument of where this part starts.
> As a special exception the first `expr_list` in the `parallel`
> RTX may have a first operand of zero. This indicates that the entire
> argument is also stored on the stack.
>
> The last time this macro is called, it is called with `MODE ==
> VOIDmode`, and its result is passed to the `call` or `call_value`
> pattern as operands 2 and 3 respectively.
>
> The usual way to make the ISO library `stdarg.h` work on a machine
> where some arguments are usually passed in registers, is to cause
> nameless arguments to be passed on the stack instead. This is done
> by making `FUNCTION_ARG` return 0 whenever named is 0.
>
> You may use the hook `targetm.calls.must_pass_in_stack`
> in the definition of this macro to determine if this argument is of a
> type that must be passed in the stack. If `REG_PARM_STACK_SPACE`
> is not defined and `FUNCTION_ARG` returns nonzero for such an
> argument, the compiler will abort. If `REG_PARM_STACK_SPACE` is
> defined, the argument will be computed in the stack and then loaded into
> a register.

— Target Hook: bool __TARGET_MUST_PASS_IN_STACK__ (enum machine_mode mode, tree type)
> This target hook should return `true` if we should not pass type
> solely in registers. The file `expr.h` defines a
> definition that is usually appropriate, refer to `expr.h` for additional
> documentation.

— Macro: __FUNCTION_INCOMING_ARG__ (cum, mode, type, named)
> Define this macro if the target machine has “register windows”, so
> that the register in which a function sees an arguments is not
> necessarily the same as the one in which the caller passed the
> argument.
>
> For such machines, `FUNCTION_ARG` computes the register in which
> the caller passes the value, and `FUNCTION_INCOMING_ARG` should
> be defined in a similar fashion to tell the function being called
> where the arguments will arrive.
>
> If `FUNCTION_INCOMING_ARG` is not defined, `FUNCTION_ARG`
> serves both purposes.

— Target Hook: int __TARGET_ARG_PARTIAL_BYTES__ (CUMULATIVE_ARGS \*cum, enum machine_mode mode, tree type, bool named)
> This target hook returns the number of bytes at the beginning of an
> argument that must be put in registers. The value must be zero for
> arguments that are passed entirely in registers or that are entirely
> pushed on the stack.
>
> On some machines, certain arguments must be passed partially in
> registers and partially in memory. On these machines, typically the
> first few words of arguments are passed in registers, and the rest
> on the stack. If a multi-word argument (a `double` or a
> structure) crosses that boundary, its first few words must be passed
> in registers and the rest must be pushed. This macro tells the
> compiler when this occurs, and how many bytes should go in registers.
>
> `FUNCTION_ARG` for these arguments should return the first
> register to be used by the caller for this argument; likewise
> `FUNCTION_INCOMING_ARG`, for the called function.

— Target Hook: bool __TARGET_PASS_BY_REFERENCE__ (CUMULATIVE_ARGS \*cum, enum machine_mode mode, tree type, bool named)
> This target hook should return `true` if an argument at the
> position indicated by cum should be passed by reference. This
> predicate is queried after target independent reasons for being
> passed by reference, such as `TREE_ADDRESSABLE (type)`.
>
> If the hook returns true, a copy of that argument is made in memory and a
> pointer to the argument is passed instead of the argument itself.
> The pointer is passed in whatever way is appropriate for passing a pointer
> to that type.

— Target Hook: bool __TARGET_CALLEE_COPIES__ (CUMULATIVE_ARGS \*cum, enum machine_mode mode, tree type, bool named)
> The function argument described by the parameters to this hook is
> known to be passed by reference. The hook should return true if the
> function argument should be copied by the callee instead of copied
> by the caller.
>
> For any argument for which the hook returns true, if it can be
> determined that the argument is not modified, then a copy need
> not be generated.
>
> The default version of this hook always returns false.

— Macro: __CUMULATIVE_ARGS__
> A C type for declaring a variable that is used as the first argument of
> `FUNCTION_ARG` and other related values. For some target machines,
> the type `int` suffices and can hold the number of bytes of
> argument so far.
>
> There is no need to record in `CUMULATIVE_ARGS` anything about the
> arguments that have been passed on the stack. The compiler has other
> variables to keep track of that. For target machines on which all
> arguments are passed on the stack, there is no need to store anything in
> `CUMULATIVE_ARGS`; however, the data structure must exist and
> should not be empty, so use `int`.

— Macro: __INIT_CUMULATIVE_ARGS__ (cum, fntype, libname, fndecl, n_named_args)
> A C statement (sans semicolon) for initializing the variable
> cum for the state at the beginning of the argument list. The
> variable has type `CUMULATIVE_ARGS`. The value of fntype
> is the tree node for the data type of the function which will receive
> the args, or 0 if the args are to a compiler support library function.
> For direct calls that are not libcalls, fndecl contain the
> declaration node of the function. fndecl is also set when
> `INIT_CUMULATIVE_ARGS` is used to find arguments for the function
> being compiled. n_named_args is set to the number of named
> arguments, including a structure return address if it is passed as a
> parameter, when making a call. When processing incoming arguments,
> n_named_args is set to −1.
>
> When processing a call to a compiler support library function,
> libname identifies which one. It is a `symbol_ref` rtx which
> contains the name of the function, as a string. libname is 0 when
> an ordinary C function call is being processed. Thus, each time this
> macro is called, either libname or fntype is nonzero, but
> never both of them at once.

— Macro: __INIT_CUMULATIVE_LIBCALL_ARGS__ (cum, mode, libname)
> Like `INIT_CUMULATIVE_ARGS` but only used for outgoing libcalls,
> it gets a `MODE` argument instead of fntype, that would be
> `NULL`. indirect would always be zero, too. If this macro
> is not defined, `INIT_CUMULATIVE_ARGS (cum, NULL_RTX, libname,
> 0)` is used instead.

— Macro: __INIT_CUMULATIVE_INCOMING_ARGS__ (cum, fntype, libname)
> Like `INIT_CUMULATIVE_ARGS` but overrides it for the purposes of
> finding the arguments for the function being compiled. If this macro is
> undefined, `INIT_CUMULATIVE_ARGS` is used instead.
>
> The value passed for libname is always 0, since library routines
> with special calling conventions are never compiled with GCC. The
> argument libname exists for symmetry with
> `INIT_CUMULATIVE_ARGS`.

— Macro: __FUNCTION_ARG_ADVANCE__ (cum, mode, type, named)
> A C statement (sans semicolon) to update the summarizer variable
> cum to advance past an argument in the argument list. The
> values mode, type and named describe that argument.
> Once this is done, the variable cum is suitable for analyzing
> the _following_ argument with `FUNCTION_ARG`, etc.
>
> This macro need not do anything if the argument in question was passed
> on the stack. The compiler knows how to track the amount of stack space
> used for arguments without any special help.

— Macro: __FUNCTION_ARG_PADDING__ (mode, type)
> If defined, a C expression which determines whether, and in which direction,
> to pad out an argument with extra space. The value should be of type
> `enum direction`: either `upward` to pad above the argument,
> `downward` to pad below, or `none` to inhibit padding.
>
> The _amount_ of padding is always just enough to reach the next
> multiple of `FUNCTION_ARG_BOUNDARY`; this macro does not control
> it.
>
> This macro has a default definition which is right for most systems.
> For little-endian machines, the default is to pad upward. For
> big-endian machines, the default is to pad downward for an argument of
> constant size shorter than an `int`, and upward otherwise.

— Macro: __PAD_VARARGS_DOWN__
> If defined, a C expression which determines whether the default
> implementation of va_arg will attempt to pad down before reading the
> next argument, if that argument is smaller than its aligned space as
> controlled by `PARM_BOUNDARY`. If this macro is not defined, all such
> arguments are padded down if `BYTES_BIG_ENDIAN` is true.

— Macro: __BLOCK_REG_PADDING__ (mode, type, first)
> Specify padding for the last element of a block move between registers and
> memory. first is nonzero if this is the only element. Defining this
> macro allows better control of register function parameters on big-endian
> machines, without using `PARALLEL` rtl. In particular,
> `MUST_PASS_IN_STACK` need not test padding and mode of types in
> registers, as there is no longer a "wrong" part of a register; For example,
> a three byte aggregate may be passed in the high part of a register if so
> required.

— Macro: __FUNCTION_ARG_BOUNDARY__ (mode, type)
> If defined, a C expression that gives the alignment boundary, in bits,
> of an argument with the specified mode and type. If it is not defined,
> `PARM_BOUNDARY` is used for all arguments.

— Macro: __FUNCTION_ARG_REGNO_P__ (regno)
> A C expression that is nonzero if regno is the number of a hard
> register in which function arguments are sometimes passed. This does
> _not_ include implicit arguments such as the static chain and
> the structure-value address. On many machines, no registers can be
> used for this purpose since all function arguments are pushed on the
> stack.

— Target Hook: bool __TARGET_SPLIT_COMPLEX_ARG__ (tree type)
> This hook should return true if parameter of type type are passed
> as two scalar parameters. By default, GCC will attempt to pack complex
> arguments into the target's word size. Some ABIs require complex arguments
> to be split and treated as their individual components. For example, on
> AIX64, complex floats should be passed in a pair of floating point
> registers, even though a complex float would fit in one 64-bit floating
> point register.
>
> The default value of this hook is `NULL`, which is treated as always
> false.

— Target Hook: tree __TARGET_BUILD_BUILTIN_VA_LIST__ (void)
> This hook returns a type node for `va_list` for the target.
> The default version of the hook returns `void*`.

— Target Hook: tree __TARGET_GIMPLIFY_VA_ARG_EXPR__ (tree valist, tree type, tree \*pre_p, tree \*post_p)
> This hook performs target-specific gimplification of
> `VA_ARG_EXPR`. The first two parameters correspond to the
> arguments to `va_arg`; the latter two are as in
> `gimplify.c:gimplify_expr`.

— Target Hook: bool __TARGET_VALID_POINTER_MODE__ (enum machine_mode mode)
> Define this to return nonzero if the port can handle pointers
> with machine mode mode. The default version of this
> hook returns true for both `ptr_mode` and `Pmode`.

— Target Hook: bool __TARGET_SCALAR_MODE_SUPPORTED_P__ (enum machine_mode mode)
> Define this to return nonzero if the port is prepared to handle
> insns involving scalar mode mode. For a scalar mode to be
> considered supported, all the basic arithmetic and comparisons
> must work.
>
> The default version of this hook returns true for any mode
> required to handle the basic C types (as defined by the port).
> Included here are the double-word arithmetic supported by the
> code in `optabs.c`.

— Target Hook: bool __TARGET_VECTOR_MODE_SUPPORTED_P__ (enum machine_mode mode)
> Define this to return nonzero if the port is prepared to handle
> insns involving vector mode mode. At the very least, it
> must have move patterns for this mode.
