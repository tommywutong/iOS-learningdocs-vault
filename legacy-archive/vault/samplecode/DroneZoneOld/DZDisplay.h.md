---
title: DroneZoneOld
apple_id: DTS10000051
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/DroneZoneOld/Listings/DZDisplay_h.html
archived_at: '2026-07-18T03:07:17.538637Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DroneZoneOld](DroneZoneOld.md)


[Next](DZDrone.c.md)[Previous](DZDisplay.c.md)

# DZDisplay.h

```c
/*
 *  File:       DZDisplay.h
 *
 *  Copyright © 1996 Apple Computer, Inc.
 */

#ifndef __DZDisplay__
#define __DZDisplay__

#include <Windows.h>

#include <QD3D.h>

void Display_Init(
    void);

void Display_Exit(
    void);

void Display_Activate(
    Boolean                 inActivate);

Boolean Display_IsActive(
    void);

void Display_DrawGrow(
    void);

void Display_DrawContents(
    void);

void Display_Resize(
    void);

WindowPtr Display_GetWindow(
    void);

void Display_SetViewerPosition(
    const TQ3Point3D*       inPosition,
    const TQ3Vector3D*      inDirection,
    const TQ3Vector3D*      inUp);

void Display_GetViewerPosition(
    TQ3Point3D*             outPosition,
    TQ3Vector3D*            outDirection,
    TQ3Vector3D*            outUp);

#endif /* __DZDisplay__ */
```

[Next](DZDrone.c.md)[Previous](DZDisplay.c.md)

