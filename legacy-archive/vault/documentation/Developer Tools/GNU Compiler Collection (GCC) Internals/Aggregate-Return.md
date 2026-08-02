---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Aggregate-Return.html
archived_at: '2026-07-15T07:30:59.227391Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Caller Saves](Caller-Saves.md#apple-inqwy3dfoiwvgylwmvzq),
Previous: [Scalar Return](Scalar-Return.md#apple-knrwc3dboiwvezluovzg4),
Up: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq)

---

#### 13.9.9 How Large Values Are Returned

When a function value's mode is `BLKmode` (and in some other
cases), the value is not returned according to `FUNCTION_VALUE`
(see [Scalar Return](Scalar-Return.md#apple-knrwc3dboiwvezluovzg4)). Instead, the caller passes the address of a
block of memory in which the value should be stored. This address
is called the structure value address.

This section describes how to control returning structure values in
memory.

— Target Hook: bool __TARGET_RETURN_IN_MEMORY__ (tree type, tree fntype)
> This target hook should return a nonzero value to say to return the
> function value in memory, just as large structures are always returned.
> Here type will be the data type of the value, and fntype
> will be the type of the function doing the returning, or `NULL` for
> libcalls.
>
> Note that values of mode `BLKmode` must be explicitly handled
> by this function. Also, the option `-fpcc-struct-return`
> takes effect regardless of this macro. On most systems, it is
> possible to leave the hook undefined; this causes a default
> definition to be used, whose value is the constant 1 for `BLKmode`
> values, and 0 otherwise.
>
> Do not use this hook to indicate that structures and unions should always
> be returned in memory. You should instead use `DEFAULT_PCC_STRUCT_RETURN`
> to indicate this.

— Macro: __DEFAULT_PCC_STRUCT_RETURN__
> Define this macro to be 1 if all structure and union return values must be
> in memory. Since this results in slower code, this should be defined
> only if needed for compatibility with other compilers or with an ABI.
> If you define this macro to be 0, then the conventions used for structure
> and union return values are decided by the `TARGET_RETURN_IN_MEMORY`
> target hook.
>
> If not defined, this defaults to the value 1.

— Target Hook: rtx __TARGET_STRUCT_VALUE_RTX__ (tree fndecl, int incoming)
> This target hook should return the location of the structure value
> address (normally a `mem` or `reg`), or 0 if the address is
> passed as an “invisible” first argument. Note that fndecl may
> be `NULL`, for libcalls. You do not need to define this target
> hook if the address is always passed as an “invisible” first
> argument.
>
> On some architectures the place where the structure value address
> is found by the called function is not the same place that the
> caller put it. This can be due to register windows, or it could
> be because the function prologue moves it to a different place.
> incoming is `true` when the location is needed in
> the context of the called function, and `false` in the context of
> the caller.
>
> If incoming is `true` and the address is to be found on the
> stack, return a `mem` which refers to the frame pointer.

— Macro: __PCC_STATIC_STRUCT_RETURN__
> Define this macro if the usual system convention on the target machine
> for returning structures and unions is for the called function to return
> the address of a static variable containing the value.
>
> Do not define this if the usual system convention is for the caller to
> pass an address to the subroutine.
>
> This macro has effect in `-fpcc-struct-return` mode, but it does
> nothing when you use `-freg-struct-return` mode.
