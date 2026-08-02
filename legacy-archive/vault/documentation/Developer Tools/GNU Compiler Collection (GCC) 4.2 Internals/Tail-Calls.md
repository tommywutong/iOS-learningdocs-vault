---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Tail-Calls.html
archived_at: '2026-07-15T07:31:02.944315Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Stack Smashing Protection](Stack-Smashing-Protection.md#apple-kn2gcy3lfvjw2yltnbuw4zznkbzg65dfmn2gs33o),
Previous: [Profiling](Profiling.md#apple-kbzg6ztjnruw4zy),
Up: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq)

---

#### 15.10.13 Permitting tail calls

— Target Hook: bool __TARGET_FUNCTION_OK_FOR_SIBCALL__ (tree decl, tree exp)
> True if it is ok to do sibling call optimization for the specified
> call expression exp. decl will be the called function,
> or `NULL` if this is an indirect call.
>
> It is not uncommon for limitations of calling conventions to prevent
> tail calls to functions outside the current unit of translation, or
> during PIC compilation. The hook is used to enforce these restrictions,
> as the `sibcall` md pattern can not fail, or fall over to a
> “normal” call. The criteria for successful sibling call optimization
> may vary greatly between different architectures.

— Target Hook: void __TARGET_EXTRA_LIVE_ON_ENTRY__ (bitmap \*regs)
> Add any hard registers to regs that are live on entry to the
> function. This hook only needs to be defined to provide registers that
> cannot be found by examination of FUNCTION_ARG_REGNO_P, the callee saved
> registers, STATIC_CHAIN_INCOMING_REGNUM, STATIC_CHAIN_REGNUM,
> TARGET_STRUCT_VALUE_RTX, FRAME_POINTER_REGNUM, EH_USES,
> FRAME_POINTER_REGNUM, ARG_POINTER_REGNUM, and the PIC_OFFSET_TABLE_REGNUM.
