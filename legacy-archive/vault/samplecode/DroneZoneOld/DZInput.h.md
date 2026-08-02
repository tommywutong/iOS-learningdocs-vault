---
title: DroneZoneOld
apple_id: DTS10000051
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/DroneZoneOld/Listings/DZInput_h.html
archived_at: '2026-07-18T03:07:19.341519Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DroneZoneOld](DroneZoneOld.md)


[Next](DZISpPresets.r.md)[Previous](DZInput.c.md)

# DZInput.h

```c
/*
 *  File:       DZInput.h
 *
 *  Copyright © 1996 Apple Computer, Inc.
 */

#ifndef __DZInput__
#define __DZInput__

#include <Types.h>


typedef enum TInputEvent {
    kInputEvent_None,

    // it's IMPORTANT that end be begin+1
    kInputEvent_Fire_On,
    kInputEvent_Fire_Off,

    // it's IMPORTANT that off be on+1
    kInputEvent_InertialDampers_On,
    kInputEvent_InertialDampers_Off,

    kInputEvent_InstantStop,

    kInputEvent_ShowHUD,
    kInputEvent_ShowFPS,
    kInputEvent_ShowThrottle,
    kInputEvent_ShowVelocity,

    kInputEvent_Pause

} TInputEvent;


void Input_Init(
    void);

void Input_Exit(
    void);

void Input_Configure(
    void);

float Input_GetRoll     (void);
float Input_GetPitch    (void);
float Input_GetYaw      (void);
float Input_GetThrottle (void);

TInputEvent Input_GetEvent(
    void);

void Input_Activate(
    Boolean             inActivate);

#endif /* __DZInput__ */
```

[Next](DZISpPresets.r.md)[Previous](DZInput.c.md)

