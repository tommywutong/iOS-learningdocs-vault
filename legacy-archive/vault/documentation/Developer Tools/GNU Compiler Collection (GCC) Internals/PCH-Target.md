---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/PCH-Target.html
archived_at: '2026-07-15T07:31:00.461721Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Next: [C++ ABI](C_002b_002b-ABI.md#apple-inptambsmjptambsmiwucqsj),
Previous: [MIPS Coprocessors](MIPS-Coprocessors.md#apple-jvevauzninxxa4tpmnsxg43pojzq),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 13.25 Parameters for Precompiled Header Validity Checking

— Target Hook: void __\*__ TARGET_GET_PCH_VALIDITY (size_t \* sz)
> Define this hook if your target needs to check a different collection
> of flags than the default, which is every flag defined by
> `TARGET_SWITCHES` and `TARGET_OPTIONS`. It should return
> some data which will be saved in the PCH file and presented to
> `TARGET_PCH_VALID_P` later; it should set `SZ` to the size
> of the data.

— Target Hook: const __char__ \* TARGET_PCH_VALID_P (const void \* data, size_t sz)
> Define this hook if your target needs to check a different collection of
> flags than the default, which is every flag defined by `TARGET_SWITCHES`
> and `TARGET_OPTIONS`. It is given data which came from
> `TARGET_GET_PCH_VALIDITY` (in this version of this compiler, so there
> is no need for extensive validity checking). It returns `NULL` if
> it is safe to load a PCH file with this data, or a suitable error message
> if not. The error message will be presented to the user, so it should
> be localized.
