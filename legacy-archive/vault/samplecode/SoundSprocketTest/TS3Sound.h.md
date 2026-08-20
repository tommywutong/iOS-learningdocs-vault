---
title: SoundSprocketTest
apple_id: DTS10000060
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SoundSprocketTest/Listings/TS3Sound_h.html
archived_at: '2026-07-18T03:25:10.017287Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SoundSprocketTest](SoundSprocketTest.md)


[Next](TS3TestAPI.c.md)[Previous](TS3Sound.c.md)

# TS3Sound.h

```c
/*
 *  File:       TS3Sound.h
 *
 *  Copyright © 1996 Apple Computer, Inc.
 */

#ifndef __TS3Sound__
#define __TS3Sound__

#include <Sound.h>
#include <Types.h>

#include "SoundSprocket.h"


void Sound_Init(
    void);

void Sound_Exit(
    void);

void Sound_Configure(
    void);

void Sound_PlaySilence(
    void);

Boolean Sound_PlayResource(
    Str255              inSndName);

void Sound_Set3DInfo(
    const SSpLocalizationData*  in3DInfo);

#endif /* __TS3Sound__ */
```

[Next](TS3TestAPI.c.md)[Previous](TS3Sound.c.md)

