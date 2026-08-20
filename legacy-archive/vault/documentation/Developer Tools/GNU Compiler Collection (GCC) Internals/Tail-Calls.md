---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Tail-Calls.html
archived_at: '2026-07-15T07:31:00.863366Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [Profiling](Profiling.md#apple-kbzg6ztjnruw4zy),
Up: [Stack and Calling](Stack-and-Calling.md#apple-kn2gcy3lfvqw4zbninqwy3djnztq)

---

#### 13.9.13 Permitting tail calls

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
