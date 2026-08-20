---
title: DroneZoneOld
apple_id: DTS10000051
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/DroneZoneOld/Listings/DZGame_h.html
archived_at: '2026-07-18T03:07:19.046543Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DroneZoneOld](DroneZoneOld.md)


[Next](DZInput.c.md)[Previous](DZGame.c.md)

# DZGame.h

```c
/*
 *  File:       DZGame.h
 *
 *  Copyright © 1996 Apple Computer, Inc.
 */

#ifndef __DZGame__
#define __DZGame__

#include <Types.h>

#include <QD3D.h>


typedef enum TGameState {
    kGameState_Playing,
    kGameState_Paused,
    kGameState_Stopped
} TGameState;


// These are maintained by Game_Process
extern float            gGameInterval;
extern float            gGameFramesPerSecond;
extern Boolean          gSoundOn;

void Game_Init(
    void);

void Game_Exit(
    void);

void Game_SetState(
    TGameState          inGameState);

TGameState Game_GetState(
    void);

void Game_Process(
    void);

void Game_Submit(
    TQ3ViewObject       inView);

void Game_Silence(
    void);

#endif /* __DZGame__ */
```

[Next](DZInput.c.md)[Previous](DZGame.c.md)

