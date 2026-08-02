---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Scalar-Return.html
archived_at: '2026-07-15T07:31:02.741995Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Aggregate Return](Aggregate-Return.md#apple-iftwo4tfm5qxizjnkjsxi5lsny),
Previous: [Register Arguments](Register-Arguments.md#apple-kjswo2ltorsxelkbojtxk3lfnz2hg),
Up: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq)

---

#### 15.10.8 How Scalar Function Values Are Returned

This section discusses the macros that control returning scalars as
values—values that can fit in registers.

— Target Hook: rtx __TARGET_FUNCTION_VALUE__ (tree ret_type, tree fn_decl_or_type, bool outgoing)
> Define this to return an RTX representing the place where a function
> returns or receives a value of data type ret_type, a tree node
> node representing a data type. fn_decl_or_type is a tree node
> representing `FUNCTION_DECL` or `FUNCTION_TYPE` of a
> function being called. If outgoing is false, the hook should
> compute the register in which the caller will see the return value.
> Otherwise, the hook should return an RTX representing the place where
> a function returns a value.
>
> On many machines, only `TYPE_MODE (`ret_type`)` is relevant.
> (Actually, on most machines, scalar values are returned in the same
> place regardless of mode.) The value of the expression is usually a
> `reg` RTX for the hard register where the return value is stored.
> The value can also be a `parallel` RTX, if the return value is in
> multiple places. See `FUNCTION_ARG` for an explanation of the
> `parallel` form.
>
> If `TARGET_PROMOTE_FUNCTION_RETURN` returns true, you must apply
> the same promotion rules specified in `PROMOTE_MODE` if
> valtype is a scalar type.
>
> If the precise function being called is known, func is a tree
> node (`FUNCTION_DECL`) for it; otherwise, func is a null
> pointer. This makes it possible to use a different value-returning
> convention for specific functions when all their calls are
> known.
>
> Some target machines have “register windows” so that the register in
> which a function returns its value is not the same as the one in which
> the caller sees the value. For such machines, you should return
> different RTX depending on outgoing.
>
> `TARGET_FUNCTION_VALUE` is not used for return values with
> aggregate data types, because these are returned in another way. See
> `TARGET_STRUCT_VALUE_RTX` and related macros, below.

— Macro: __FUNCTION_VALUE__ (valtype, func)
> This macro has been deprecated. Use `TARGET_FUNCTION_VALUE` for
> a new target instead.

— Macro: __FUNCTION_OUTGOING_VALUE__ (valtype, func)
> This macro has been deprecated. Use `TARGET_FUNCTION_VALUE` for
> a new target instead.

— Macro: __LIBCALL_VALUE__ (mode)
> A C expression to create an RTX representing the place where a library
> function returns a value of mode mode. If the precise function
> being called is known, func is a tree node
> (`FUNCTION_DECL`) for it; otherwise, func is a null
> pointer. This makes it possible to use a different value-returning
> convention for specific functions when all their calls are
> known.
>
> Note that “library function” in this context means a compiler
> support routine, used to perform arithmetic, whose name is known
> specially by the compiler and was not mentioned in the C code being
> compiled.
>
> The definition of `LIBRARY_VALUE` need not be concerned aggregate
> data types, because none of the library functions returns such types.

— Macro: __FUNCTION_VALUE_REGNO_P__ (regno)
> A C expression that is nonzero if regno is the number of a hard
> register in which the values of called function may come back.
>
> A register whose use for returning values is limited to serving as the
> second of a pair (for a value of type `double`, say) need not be
> recognized by this macro. So for most machines, this definition
> suffices:
>
> ```
>           #define FUNCTION_VALUE_REGNO_P(N) ((N) == 0)
>
> ```
>
> If the machine has register windows, so that the caller and the called
> function use different registers for the return value, this macro
> should recognize only the caller's register numbers.

— Macro: __APPLY_RESULT_SIZE__
> Define this macro if ``untyped_call`' and ``untyped_return`'
> need more space than is implied by `FUNCTION_VALUE_REGNO_P` for
> saving and restoring an arbitrary return value.

— Target Hook: bool __TARGET_RETURN_IN_MSB__ (tree type)
> This hook should return true if values of type type are returned
> at the most significant end of a register (in other words, if they are
> padded at the least significant end). You can assume that type
> is returned in a register; the caller is required to check this.
>
> Note that the register provided by `TARGET_FUNCTION_VALUE` must
> be able to hold the complete return value. For example, if a 1-, 2-
> or 3-byte structure is returned at the most significant end of a
> 4-byte register, `TARGET_FUNCTION_VALUE` should provide an
> `SImode` rtx.
