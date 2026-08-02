---
title: Plug-in  -DistanceProxyGroup
apple_id: DTS10000121
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-DistanceProxyGroup/Listings/src_dpgMemory_c.html
archived_at: '2026-07-18T03:19:15.445609Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  -DistanceProxyGroup](Plug-in%20-DistanceProxyGroup.md)


[Next](src-dpgSortedArray.c.md)[Previous](src-dpgIO.c.md)

# src/dpgMemory.c

```c
/******************************************************************************
 **                                                                          **
 **     Module:     dpgMemory.c                                              **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1995-1996 Apple Computer, Inc.  All rights reserved.   **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/

#include "QD3D.h"
#include "dpgMemory.h"
#include "stdlib.h"

#include <Memory.h>

void *dpgAlloc(unsigned long size)
{
    return malloc(size);
}

void dpgFree(void *ptr)
{
    free(ptr);
}

void *dpgRealloc(void *ptr, unsigned long size)
{
    return realloc(ptr, size);
}

void dpgCopy(const void *src, void *dst, unsigned long size)
{
#if defined(OS_MACINTOSH) && OS_MACINTOSH
    BlockMove (src, dst, size);
#else
    memcpy (dst, src, size);
#endif

}
```

[Next](src-dpgSortedArray.c.md)[Previous](src-dpgIO.c.md)

