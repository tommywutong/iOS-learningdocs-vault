---
title: Plug-in  -DistanceProxyGroup
apple_id: DTS10000121
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-DistanceProxyGroup/Listings/header_dpgSortedArray_h.html
archived_at: '2026-07-18T03:19:15.280531Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  -DistanceProxyGroup](Plug-in%20-DistanceProxyGroup.md)


[Next](src-dpg.c.md)[Previous](header-dpgMemory.h.md)

# header/dpgSortedArray.h

```c
/******************************************************************************
 **                                                                          **
 **     Module:     dpgSortedArray.h                                         **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1996-1996 Apple Computer, Inc.  All rights reserved.   **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/

#ifndef dpgSortedArray_h
#define dpgSortedArray_h

#if PRAGMA_ONCE
    #pragma once
#endif

#include "QD3D.h"

#ifdef __cplusplus
extern "C" {
#endif /*  __cplusplus  */

typedef long (*dpgCompareFunction)(
    void        *key,
    void        *arrayElement);

TQ3Boolean dpgSortedArray_Search(
    void                *key,
    void                *array,
    unsigned long       nElems,
    unsigned long       elemSize,
    dpgCompareFunction  compare,
    unsigned long       *position);

TQ3Status dpgSortedArray_Resize(
    void                **array,
    unsigned long       nElems,
    unsigned long       elemSize);

void dpgSortedArray_InsertElement(
    void                *array,
    unsigned long       nElems,
    unsigned long       elemSize,
    void                *newElem,
    unsigned long       position);

void dpgSortedArray_DeleteElement(
    void                *array,
    unsigned long       nElems,
    unsigned long       elemSize,
    void                *oldElement,    /* Can be NULL */
    unsigned long       position);

#ifdef __cplusplus
}
#endif /*  __cplusplus  */

#endif
```

[Next](src-dpg.c.md)[Previous](header-dpgMemory.h.md)

