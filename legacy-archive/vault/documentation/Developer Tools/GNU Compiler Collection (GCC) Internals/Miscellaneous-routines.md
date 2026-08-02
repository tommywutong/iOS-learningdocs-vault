---
title: GNU Compiler Collection (GCC) Internals
apple_id: TP40006804
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.0.1/gccint/Miscellaneous-routines.html
archived_at: '2026-07-15T07:31:00.395724Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) Internals](index.md)



Previous: [Exception handling routines](Exception-handling-routines.md#apple-iv4ggzlqoruw63rnnbqw4zdmnfxgollsn52xi2lomvzq),
Up: [Libgcc](Libgcc.md#apple-jruwez3dmm)

---

### 4.4 Miscellaneous runtime library routines

#### 4.4.1 Cache control functions

— Runtime Function: void ____clear_cache__ (char \*beg, char \*end)
> This function clears the instruction cache between beg and end.
