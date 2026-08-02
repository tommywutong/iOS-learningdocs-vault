---
title: Plug-in  -DistanceProxyGroup
apple_id: DTS10000121
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-DistanceProxyGroup/Listings/header_dpg_h.html
archived_at: '2026-07-18T03:19:15.326211Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  -DistanceProxyGroup](Plug-in%20-DistanceProxyGroup.md)


[Next](header-DPGGroup.h.md)[Previous](DPGPre.h.md)

# header/dpg.h

```c
/******************************************************************************
 **                                                                          **
 **     Module:     dpg.h                                                    **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1995-1996 Apple Computer, Inc.  All rights reserved.   **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/

#ifndef DistanceProxyGroup_sys_h
#define DistanceProxyGroup_sys_h

#if PRAGMA_ONCE
    #pragma once
#endif

#include "QD3D.h"
#include "QD3DGroup.h"
#include "DPGGroup.h"

/******************************************************************************
 **                                                                          **
 **                 Distance Proxy Display Groups                            **
 **                                                                          **
 *****************************************************************************/

typedef struct TQ3DistanceData {
    float               distance;
    TQ3GroupPosition    position;
} TQ3DistanceData;

typedef struct TQ3DistanceIOData {
    float               distance;
    unsigned long       index;
} TQ3DistanceIOData;

typedef struct TQ3DistanceProxyDisplayGroupPrivate {
    TQ3Point3D              refPt;
    TQ3DPGFlag              flag;
    float                   d;
    TQ3GroupPosition        position;

    TQ3DistanceData         *distTbl;
    unsigned long           distTblCnt;

    TQ3DistanceIOData       *distIOTbl;
    unsigned long           distIOTblCnt;
} TQ3DistanceProxyDisplayGroupPrivate;


typedef struct TQ3DPGPositionPrivate {
    TQ3Boolean  flag;
    float       distance;
} TQ3DPGPositionPrivate;

extern void *EiGroup_GetPositionPrivate(
    TQ3XObjectClass         objectClass,
    TQ3GroupObject          group,
    TQ3GroupPosition        gPos);

extern TQ3XObjectClass EgDistanceProxyDisplayGroupClass;


#define DPG_GETPRIVATE(x)\
     (TQ3DistanceProxyDisplayGroupPrivate *)Q3XObjectClass_GetPrivate(EgDistanceProxyDisplayGroupClass, (x))

#define DPG_POSITION_GETPRIVATE(group, pos)\
     (TQ3DPGPositionPrivate *)Q3XGroup_GetPositionPrivate( (group), (pos))


#ifdef __cplusplus
extern "C" {
#endif /*  __cplusplus  */


TQ3Status exDistanceProxyGroup_Register( 
    void);

TQ3GroupObject exDistanceProxyGroup_New(
    TQ3Point3D      *position,
    unsigned long   flags);

TQ3GroupPosition exDistanceProxyGroup_AddObjectDistance(
    TQ3GroupObject      group,
    TQ3Object           object,
    float               distance);

TQ3Status exDistanceProxyGroup_SetFlag(
    TQ3GroupObject      group,
    TQ3DPGFlag          flag);

TQ3Status exDistanceProxyGroup_GetFlag(
    TQ3GroupObject      group,
    TQ3DPGFlag          *flag);

TQ3Status exDistanceProxyGroup_SetReferencePoint(
    TQ3GroupObject      group,
    TQ3Point3D          *refPt);

TQ3Status exDistanceProxyGroup_GetReferencePoint(
    TQ3GroupObject      group,
    TQ3Point3D          *refPt);

TQ3Boolean exDistanceProxyGroup_SetDistanceAtPosition(
    TQ3GroupObject      group,
    TQ3GroupPosition    position,
    float               distance);

TQ3Boolean exDistanceProxyGroup_GetDistanceAtPosition(
    TQ3GroupObject      group,
    TQ3GroupPosition    position,
    float               *distance);

#ifdef __cplusplus
}
#endif /*  __cplusplus  */

#endif
```

[Next](header-DPGGroup.h.md)[Previous](DPGPre.h.md)

