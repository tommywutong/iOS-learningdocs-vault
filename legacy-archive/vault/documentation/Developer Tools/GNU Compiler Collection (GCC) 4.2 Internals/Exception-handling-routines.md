---
title: GNU Compiler Collection (GCC) 4.2 Internals
apple_id: TP40007093
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/gcc-4.2.1/gccint/Exception-handling-routines.html
archived_at: '2026-07-15T07:31:01.804008Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GNU Compiler Collection (GCC) 4.2 Internals](index.md)



Next: [Miscellaneous routines](Miscellaneous-routines.md#apple-jvuxgy3fnrwgc3tfn52xgllsn52xi2lomvzq),
Previous: [Decimal float library routines](Decimal-float-library-routines.md#apple-irswg2lnmfwc2ztmn5qxillmnfrheylspewxe33voruw4zlt),
Up: [Libgcc](Libgcc.md#apple-jruwez3dmm)

---

### 4.4 Language-independent routines for exception handling

document me!

```
       _Unwind_DeleteException
       _Unwind_Find_FDE
       _Unwind_ForcedUnwind
       _Unwind_GetGR
       _Unwind_GetIP
       _Unwind_GetLanguageSpecificData
       _Unwind_GetRegionStart
       _Unwind_GetTextRelBase
       _Unwind_GetDataRelBase
       _Unwind_RaiseException
       _Unwind_Resume
       _Unwind_SetGR
       _Unwind_SetIP
       _Unwind_FindEnclosingFunction
       _Unwind_SjLj_Register
       _Unwind_SjLj_Unregister
       _Unwind_SjLj_RaiseException
       _Unwind_SjLj_ForcedUnwind
       _Unwind_SjLj_Resume
       __deregister_frame
       __deregister_frame_info
       __deregister_frame_info_bases
       __register_frame
       __register_frame_info
       __register_frame_info_bases
       __register_frame_info_table
       __register_frame_info_table_bases
       __register_frame_table
```
