---
title: DroneZoneOld
apple_id: DTS10000051
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/DroneZoneOld/Listings/DZSpace_h.html
archived_at: '2026-07-18T03:07:20.024518Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DroneZoneOld](DroneZoneOld.md)


[Next](DZThumbprint.h.md)[Previous](DZSpace.c.md)

# DZSpace.h

```c
/*
 *  File:       DZSpace.h
 *
 *  Copyright © 1996 Apple Computer, Inc.
 */

#ifndef __DZSpace__
#define __DZSpace__

#include <QD3D.h>

void Space_Init(
    void);

void Space_Exit(
    void);

void Space_Submit(
    TQ3ViewObject       inView,
    const TQ3Point3D*   inPosition,
    const TQ3Vector3D*  inDirection);

#endif /* __DZSpace__ */
```

[Next](DZThumbprint.h.md)[Previous](DZSpace.c.md)

