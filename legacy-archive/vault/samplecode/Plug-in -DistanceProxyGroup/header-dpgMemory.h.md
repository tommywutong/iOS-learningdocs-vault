---
title: Plug-in  -DistanceProxyGroup
apple_id: DTS10000121
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-DistanceProxyGroup/Listings/header_dpgMemory_h.html
archived_at: '2026-07-18T03:19:15.239281Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  -DistanceProxyGroup](Plug-in%20-DistanceProxyGroup.md)


[Next](header-dpgSortedArray.h.md)[Previous](header-dpgIO.h.md)

# header/dpgMemory.h

```
/******************************************************************************
 **                                                                          **
 **     Module:     dpgMemory.h                                              **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1995-1996 Apple Computer, Inc.  All rights reserved.   **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/

#ifndef dpgMemory_h
#define dpgMemory_h

#if PRAGMA_ONCE
    #pragma once
#endif

#ifdef __cplusplus
extern "C" {
#endif /*  __cplusplus  */

void *dpgAlloc(unsigned long size);
void dpgFree(void *ptr);
void *dpgRealloc(void *ptr, unsigned long size);
void dpgCopy(const void *src, void *dst, unsigned long cnt);

#ifdef __cplusplus
}
#endif /*  __cplusplus  */

#endif
```

[Next](header-dpgSortedArray.h.md)[Previous](header-dpgIO.h.md)

