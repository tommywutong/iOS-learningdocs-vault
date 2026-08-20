---
title: Plug-in  -DistanceProxyGroup
apple_id: DTS10000121
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-DistanceProxyGroup/Listings/header_dpgIO_h.html
archived_at: '2026-07-18T03:19:15.201513Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  -DistanceProxyGroup](Plug-in%20-DistanceProxyGroup.md)


[Next](header-dpgMemory.h.md)[Previous](header-DPGGroup.h.md)

# header/dpgIO.h

```c
/******************************************************************************
 **                                                                          **
 **     Module:     dpgIO.h                                                  **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1995-1996 Apple Computer, Inc.  All rights reserved.   **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/

#ifndef dpgIO_h
#define dpgIO_h

#if PRAGMA_ONCE
    #pragma once
#endif

#include "QD3D.h"
#include "QD3DIO.h"
#include "QD3DGroup.h"
#include "QD3DExtension.h"

#ifdef __cplusplus
extern "C" {
#endif /*  __cplusplus  */

TQ3GroupObject exDistanceProxyGroup_Read(
    TQ3FileObject       file);

TQ3Status exDistanceProxyGroup_Traverse(
    TQ3GroupObject      group,
    void                *unused,
    TQ3ViewObject       view);

TQ3Status exDistanceProxyGroup_Write(
    TQ3GroupObject      group,
    TQ3FileObject       file);

#ifdef __cplusplus
}
#endif /*  __cplusplus  */

#endif
```

[Next](header-dpgMemory.h.md)[Previous](header-DPGGroup.h.md)

