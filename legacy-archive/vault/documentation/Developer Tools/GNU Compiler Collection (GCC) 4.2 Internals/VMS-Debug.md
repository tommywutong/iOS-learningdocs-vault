---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/VMS-Debug.html
archived_at: '2026-07-15T07:31:03.076425Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Previous: [SDB and DWARF](SDB-and-DWARF.md#apple-knceellbnzsc2rcxifjem),
Up: [Debugging Info](Debugging-Info.md#apple-irswe5lhm5uw4zznjfxgm3y)

---

#### 15.22.6 Macros for VMS Debug Format

Here are macros for VMS debug format.

— Macro: __VMS_DEBUGGING_INFO__
> Define this macro if GCC should produce debugging output for VMS
> in response to the `-g` option. The default behavior for VMS
> is to generate minimal debug info for a traceback in the absence of
> `-g` unless explicitly overridden with `-g0`. This
> behavior is controlled by `OPTIMIZATION_OPTIONS` and
> `OVERRIDE_OPTIONS`.
