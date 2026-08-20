---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/GameHeaders_ZAM_h.html
archived_at: '2026-07-18T03:28:32.777347Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](GameSource-DirectionTable.c.md)[Previous](GameHeaders-xthing.h.md)

# GameHeaders/ZAM.h

```c
#pragma once
#include "FixGraf.h"
#include "CoreAssertion.h"
#include "GrafUtils.h"
#include "GWorldUtils.h"
#include "Sprite.h"

#define kBaseID 128

typedef unsigned long ulong;

typedef enum {
    kNumDirections = 32,
    max_obstacle = 8,
    max_tank = 2,
    max_shot = 2,
    kNumShotFrames = 16,
    kMaxExp = 20,
    kMaxExpFrames = 6
} max_enums;

typedef enum {
    kWaitingForRequest, kWaitingForAccept, kGameInSetup, kGameInProgress
} stateFlags;

typedef enum {
    kLeftSide = 1, kRightSide = 2, kBottomMargin = 24
} sideFlags;

typedef  struct {
    stateFlags          gameState;                  // state of the game
    short               localTankIndex;                 // indicates left or right side of map
    short               remoteTankIndex;
    GWorldPtr           backdrop;                   // background image
    GWorldPtr           tween;
    Str255              playerName;                 // name of this player
    Str255              oppName;                    // name of opponent
    ulong               gameID;                     // transactionID
    AEAddressDesc       oppAddr;                    // address of remote mac
    WindowPtr           gameWind;                   // the main game window
    Rect                gameArea;                   // area where game takes place
    Rect                statusArea;                 // status area of map
    CTabHandle          gameCTab;
    short               gameCTSeed;
} gameRec, *gamePtr;

/*---- function prototypes --------*/
OSErr NewGame(void);
gamePtr MakeGameRecord(void);
OSErr SetUpPlayer(gamePtr game);

 // keyboard constants
enum
    {
    kUpArrowKey = 0x7E,
    kLeftArrowKey = 0x7B,
    kRightArrowKey = 0x7C,
    kSpaceBarKey = 0x31,
    kEscapeKey = 0x35
    };

#define KeyMapLoMem ((unsigned char *)0x174)
#define KeyIsDown(key) ((KeyMapLoMem[key >> 3] >> (key & 7)) & 1)


extern spritePtr    gDebugSprite;
extern gamePtr      gGame;

extern Boolean gDead;
extern long gDeadTime;
```

[Next](GameSource-DirectionTable.c.md)[Previous](GameHeaders-xthing.h.md)

