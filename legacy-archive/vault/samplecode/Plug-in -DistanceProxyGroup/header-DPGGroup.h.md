---
title: Plug-in  -DistanceProxyGroup
apple_id: DTS10000121
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-DistanceProxyGroup/Listings/header_DPGGroup_h.html
archived_at: '2026-07-18T03:19:15.137144Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  -DistanceProxyGroup](Plug-in%20-DistanceProxyGroup.md)


[Next](header-dpgIO.h.md)[Previous](header-dpg.h.md)

# header/DPGGroup.h

```c

/******************************************************************************
 **                                                                          **
 **     Distance Proxy Display Group                                         **
 **                                                                          **
 **     Copyright (C) 1995-1996 Apple Computer, Inc.  All rights reserved.   **
 **                                                                          **
 *****************************************************************************/

#ifndef DPGGroup_h
#define DPGGroup_h

#if PRAGMA_ONCE
    #pragma once
#endif

#include "QD3D.h"

#define kQ3DisplayGroupTypeDistanceProxy    Q3_OBJECT_TYPE('d','p','x','g')

typedef enum TQ3DPGFlag {
    kQ3DPG_AlwaysVisible = 0,
    kQ3DPG_HideWhenNear,
    kQ3DPG_ClipWhenFar
} TQ3DPGFlag;


#ifdef __cplusplus
extern "C" {
#endif /*  __cplusplus  */

QD3D_EXPORT TQ3GroupObject Q3DistanceProxyGroup_New(
    TQ3Point3D      *refPt,
    unsigned long   flag);

QD3D_EXPORT TQ3GroupPosition Q3DistanceProxyGroup_AddObject(
    TQ3GroupObject      group,
    TQ3Object           object,
    float               distance);

QD3D_EXPORT TQ3Status Q3DistanceProxyGroup_SetFlag(
    TQ3GroupObject      group,
    TQ3DPGFlag          flag);

QD3D_EXPORT TQ3Status Q3DistanceProxyGroup_GetFlag(
    TQ3GroupObject      group,
    TQ3DPGFlag          *flag);

QD3D_EXPORT TQ3Status Q3DistanceProxyGroup_SetReferencePoint(
    TQ3GroupObject      group,
    TQ3Point3D          *refPt);

QD3D_EXPORT TQ3Status Q3DistanceProxyGroup_GetReferencePoint(
    TQ3GroupObject      group,
    TQ3Point3D          *refPt);

QD3D_EXPORT TQ3Boolean Q3DistanceProxyGroup_SetDistanceAtPosition(
    TQ3GroupObject      group,
    TQ3GroupPosition    position,
    float               distance);

QD3D_EXPORT TQ3Boolean Q3DistanceProxyGroup_GetDistanceAtPosition(
    TQ3GroupObject      group,
    TQ3GroupPosition    position,
    float               *distance);


#ifdef __cplusplus
}
#endif /*  __cplusplus  */

#endif
```

[Next](header-dpgIO.h.md)[Previous](header-dpg.h.md)

