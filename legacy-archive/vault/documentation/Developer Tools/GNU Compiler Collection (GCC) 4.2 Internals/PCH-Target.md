---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/PCH-Target.html
archived_at: '2026-07-15T07:31:02.549560Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [C++ ABI](C_002b_002b-ABI.md#apple-inptambsmjptambsmiwucqsj),
Previous: [MIPS Coprocessors](MIPS-Coprocessors.md#apple-jvevauzninxxa4tpmnsxg43pojzq),
Up: [Target Macros](Target-Macros.md#apple-krqxez3foqwu2yldojxxg)

---

### 15.27 Parameters for Precompiled Header Validity Checking

— Target Hook: void __\*TARGET_GET_PCH_VALIDITY__ (size_t \*sz)
> This hook returns the data needed by `TARGET_PCH_VALID_P` and sets
> ``*sz`' to the size of the data in bytes.

— Target Hook: const __char__ \*TARGET_PCH_VALID_P (const void \*data, size_t sz)
> This hook checks whether the options used to create a PCH file are
> compatible with the current settings. It returns `NULL`
> if so and a suitable error message if not. Error messages will
> be presented to the user and must be localized using ``_(msg)`'.
>
> data is the data that was returned by `TARGET_GET_PCH_VALIDITY`
> when the PCH file was created and sz is the size of that data in bytes.
> It's safe to assume that the data was created by the same version of the
> compiler, so no format checking is needed.
>
> The default definition of `default_pch_valid_p` should be
> suitable for most targets.

— Target Hook: const __char__ \*TARGET_CHECK_PCH_TARGET_FLAGS (int pch_flags)
> If this hook is nonnull, the default implementation of
> `TARGET_PCH_VALID_P` will use it to check for compatible values
> of `target_flags`. pch_flags specifies the value that
> `target_flags` had when the PCH file was created. The return
> value is the same as for `TARGET_PCH_VALID_P`.
