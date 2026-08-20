---
title: DroneZoneOld
apple_id: DTS10000051
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/DroneZoneOld/Listings/DZSound_h.html
archived_at: '2026-07-18T03:07:19.876545Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DroneZoneOld](DroneZoneOld.md)


[Next](DZSpace.c.md)[Previous](DZSound.c.md)

# DZSound.h

```c
/*
 *  File:       DZSound.h
 *
 *  Copyright © 1996 Apple Computer, Inc.
 */

#ifndef __DZSound__
#define __DZSound__

#include "SoundSprocket.h"


void Sound_Init(
    void);

void Sound_Exit(
    void);

SSpListenerReference Sound_GetListener(
    void);

void Sound_Configure(
    void);

#endif /* __DZSound__ */
```

[Next](DZSpace.c.md)[Previous](DZSound.c.md)

