---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/GameHeaders_GameSounds_h.html
archived_at: '2026-07-18T03:28:32.562748Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](GameHeaders-MissileSprite.h.md)[Previous](GameHeaders-GameDef.h.md)

# GameHeaders/GameSounds.h

```c
#pragma once
#include <Sound.h>

#define kNumChan 4
enum {
    kWakeUpSnd  = 128,
    kFireSnd    = 129,
    kRiffSnd    = 130,
    kBadFireSnd = 131,
    kExplode    = 132,
    kYouLose   = 133,
    kYouWin     = 134,
    kIncidental1 = 135,
    kEngineStart = 136,
    kIncidental2 = 137,
    kEngineLoop  = 138,
    kIncidental3 = 139,
    kIncidental4 = 140,
    kIncidental5 = 141
};

enum {
    kStdPriority = 0x01,
    kMedPriority = 0x05,
    kHighPriority = 0x0A
};

enum {
    kMusicChan,
    kShotChan,
    kExplosionChan,
    kFlightChan
};

typedef struct {
    SndChannelPtr   channel;
    short           priority;
    Handle          sndHandle;
} SndChanInfo;


/* call this when your program starts */
void InitSounds(Str255  sndFileName);

/* call this from your main loop */
void SoundKeeper();

/* use this to play sounds */
OSErr PlaySndAsynchChannel(short sndID, short chanNum, short priority);

/* call this when your program quits */
void FreeSounds(void);

/* misc routines used internally */
pascal void SndDoneProc(SndChannelPtr channel, SndCommand *cmd);
Handle  GetSound(short  sndID);

/* private global variables */
extern SndChanInfo  gChan[kNumChan];
```

[Next](GameHeaders-MissileSprite.h.md)[Previous](GameHeaders-GameDef.h.md)

