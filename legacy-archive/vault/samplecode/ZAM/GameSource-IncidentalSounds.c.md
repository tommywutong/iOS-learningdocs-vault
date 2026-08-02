---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/GameSource_IncidentalSounds_c.html
archived_at: '2026-07-18T03:28:33.346166Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](GameSource-InitGame.c.md)[Previous](GameSource-GameSounds.c.md)

# GameSource/IncidentalSounds.c

```c
/*

    This file contains just a little code that uses the xthing timer
    to play sounds every once in a while.
*/
#include "ZAM.h"
#include "GameSounds.h"
#include "TankSprite.h"
#include <Math.h>
#include "ZAMProtos.h"


xthing gIncidentalSoundTask;
static gLastSound;

Boolean IncidentalSoundTask(xthing *xtp, long ignore)
{
    short   x;
    short   soundID = 0;

    x = abs(Random() % 7);

    if(x == 1)
        if(gLastSound == kIncidental1)
            soundID = kIncidental3;
        else
            soundID = kIncidental1;
    else if (x == 2)
        if(gLastSound == kIncidental2)
            soundID = kIncidental1;
        else
            soundID = kIncidental2;
    else if (x == 3)
        if(gLastSound == kIncidental3)
            soundID = kIncidental4;
        else
            soundID = kIncidental3;
    else if (x == 4)
        if(gLastSound == kIncidental4)
            soundID = kIncidental5;
        else
            soundID = kIncidental4;
    else if (x == 5)
        if(gLastSound == kIncidental5)
            soundID = kIncidental2;
        else
            soundID = kIncidental5;

    if(soundID != 0) {
        gLastSound = soundID;
        (void)PlaySndAsynchChannel(gLastSound, kMusicChan, kStdPriority);
    }

    /* play next sound in a random amount of time, from 5 to 30 seconds from now */
    xtp->interval = ( (Random() & 0x7FFFF) % 25000) + 5000;

    return true;
}

void StartIncidentalSounds(void)
{
    gLastSound = 0;
    (void)StartXThing(&gIncidentalSoundTask, 30000, 
            (updateProc)IncidentalSoundTask, 0L);
}
```

[Next](GameSource-InitGame.c.md)[Previous](GameSource-GameSounds.c.md)

