---
title: DroneZoneOld
apple_id: DTS10000051
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/DroneZoneOld/Listings/DZUtils_h.html
archived_at: '2026-07-18T03:07:20.193685Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DroneZoneOld](DroneZoneOld.md)


[Next](DZVersion.r.md)[Previous](DZUtils.c.md)

# DZUtils.h

```c
/*
 *  File:       DZUtils.h
 *
 *  Copyright © 1996 Apple Computer, Inc.
 */

#ifndef __DZUtils__
#define __DZUtils__

#include <QD3D.h>

Boolean CheckVersionNumber(
    const NumVersion*       inVersion,
    UInt8                   inMajor,
    UInt8                   inMinor,
    UInt8                   inBug);

TQ3Object Get3DMFResource(
    short               inResourceID);

#endif /* __DZUtils__ */
```

[Next](DZVersion.r.md)[Previous](DZUtils.c.md)

