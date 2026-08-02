---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/GameHeaders_MissileSprite_h.html
archived_at: '2026-07-18T03:28:32.605976Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](GameHeaders-Sprite.h.md)[Previous](GameHeaders-GameSounds.h.md)

# GameHeaders/MissileSprite.h

```
#pragma once
Boolean HaltMissileFrameTask(spritePtr spr);
Boolean MissileMoveFilter(spritePtr spr);
void LoadMissileSprites(gamePtr game);
spritePtr GetMissileSprite(Boolean network);
void FireMissileVelocity(fixPt *vel, Fixed h, Fixed v, Boolean network, short missileNum);
void FireMissile( short dir, Fixed h, Fixed v, Boolean network, short missileNum);
void NetworkFireMissile(gamePtr game, short dir, Fixed h, Fixed v, short missileNum);
void NetworkMoveMissile(short missileIndex);

/*---------- Apple Event Handlers ----------*/
pascal OSErr AEFireMissile (AppleEvent *theAE, AppleEvent *reply, long rfCon);
pascal OSErr AEMoveRemoteMissile (AppleEvent *theAE, AppleEvent *reply, long rfCon);

enum {
        kNumMSets = 3,
        kMaxMissiles = 5,
        kMissileID = 128,
        kMissileAnimFrames = 10,
        kMissileBaseID = 1100,
        kMissileSetOffset = 100,
        kMissileLife = 20
    };

extern frameSetPtr  MissileFrameSetList;
extern spritePtr    MissileSpriteList[kMaxMissiles];
extern spritePtr    RemoteMissileSpriteList[kMaxMissiles];
```

[Next](GameHeaders-Sprite.h.md)[Previous](GameHeaders-GameSounds.h.md)

