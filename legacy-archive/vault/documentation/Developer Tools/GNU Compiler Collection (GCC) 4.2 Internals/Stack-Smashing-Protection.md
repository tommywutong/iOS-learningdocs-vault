---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Stack-Smashing-Protection.html
archived_at: '2026-07-15T07:31:02.853259Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [Tail Calls](Tail-Calls.md#apple-krqws3bninqwy3dt),
Up: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq)

---

#### 15.10.14 Stack smashing protection

— Target Hook: tree __TARGET_STACK_PROTECT_GUARD__ (void)
> This hook returns a `DECL` node for the external variable to use
> for the stack protection guard. This variable is initialized by the
> runtime to some random value and is used to initialize the guard value
> that is placed at the top of the local stack frame. The type of this
> variable must be `ptr_type_node`.
>
> The default version of this hook creates a variable called
> ``__stack_chk_guard`', which is normally defined in `libgcc2.c`.

— Target Hook: tree __TARGET_STACK_PROTECT_FAIL__ (void)
> This hook returns a tree expression that alerts the runtime that the
> stack protect guard variable has been modified. This expression should
> involve a call to a `noreturn` function.
>
> The default version of this hook invokes a function called
> ``__stack_chk_fail`', taking no arguments. This function is
> normally defined in `libgcc2.c`.
