---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Per_002dFunction-Data.html
archived_at: '2026-07-15T07:31:00.532397Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [Storage Layout](Storage-Layout.md#apple-kn2g64tbm5ss2tdbpfxxk5a),
Previous: [Run-time Target](Run_002dtime-Target.md#apple-kj2w4xzqgazgi5djnvss2vdbojtwk5a),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 13.4 Defining data structures for per-function information.

If the target needs to store information on a per-function basis, GCC
provides a macro and a couple of variables to allow this. Note, just
using statics to store the information is a bad idea, since GCC supports
nested functions, so you can be halfway through encoding one function
when another one comes along.

GCC defines a data structure called `struct function` which
contains all of the data specific to an individual function. This
structure contains a field called `machine` whose type is
`struct machine_function *`, which can be used by targets to point
to their own specific data.

If a target needs per-function specific data it should define the type
`struct machine_function` and also the macro `INIT_EXPANDERS`.
This macro should be used to initialize the function pointer
`init_machine_status`. This pointer is explained below.

One typical use of per-function, target specific data is to create an
RTX to hold the register containing the function's return address. This
RTX can then be used to implement the `__builtin_return_address`
function, for level 0.

Note—earlier implementations of GCC used a single data area to hold
all of the per-function information. Thus when processing of a nested
function began the old per-function data had to be pushed onto a
stack, and when the processing was finished, it had to be popped off the
stack. GCC used to provide function pointers called
`save_machine_status` and `restore_machine_status` to handle
the saving and restoring of the target specific information. Since the
single data area approach is no longer used, these pointers are no
longer supported.

— Macro: __INIT_EXPANDERS__
> Macro called to initialize any target specific information. This macro
> is called once per function, before generation of any RTL has begun.
> The intention of this macro is to allow the initialization of the
> function pointer `init_machine_status`.

— Variable: void (\*)(struct function \*) __init_machine_status__
> If this function pointer is non-`NULL` it will be called once per
> function, before function compilation starts, in order to allow the
> target to perform any target specific initialization of the
> `struct function` structure. It is intended that this would be
> used to initialize the `machine` of that structure.
>
> `struct machine_function` structures are expected to be freed by GC.
> Generally, any memory that they reference must be allocated by using
> `ggc_alloc`, including the structure itself.
