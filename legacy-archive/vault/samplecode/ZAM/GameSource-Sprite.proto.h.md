---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/GameSource_Sprite_proto_h.html
archived_at: '2026-07-18T03:28:34.155917Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](GameSource-SpriteColission.c.md)[Previous](GameSource-Sprite.c.md)

# GameSource/Sprite.proto.h

```

/* Sprite.c */
void AnimateSprites(void);
void SpriteUpdateEvent(void);
void InitSprites(void);
OSErr CreateSpriteLayer(spriteLayerPtr *retSprite, GWorldPtr tween, GWorldPtr backdrop, WindowPtr spriteWin);
void StopSpriteAction(spritePtr spr);
void StopSpriteLayerAction(spriteLayerPtr sprLayer);
void KillSprites(void);
void AddSpriteToLayer(spritePtr spr, spriteLayerPtr sprLayer);
void RemoveSpriteFromLayer(spritePtr spr, spriteLayerPtr sprLayer);
void MoveCellMaskRgnToRect(frameCellPtr curFrame, Rect *r);
OSErr CreateEmptySprite(spriteLayerPtr sprLayer, spritePtr *newSprite, long spriteFlags, long moveTimeInterval, long frameTimeInterval, long refCon);
OSErr CreateColorIconSprite(spriteLayerPtr sprLayer, spritePtr *newSprite, short startID, short numFrames, long spriteFlags, long moveTimeInterval, long frameTimeInterval, long refCon);
void SetSpriteLoc(spritePtr spr, Fixed h, Fixed v);
void ShowSprite(spritePtr spr);
void HideSprite(spritePtr spr);
void StartSpriteAction(spritePtr spr);
void StartRemoteSpriteAction(spritePtr spr);
Boolean SpriteFrameTask(xthing *xtp, spritePtr spr);
Boolean SpriteMoveTask(xthing *xtp, spritePtr spr);
```

[Next](GameSource-SpriteColission.c.md)[Previous](GameSource-Sprite.c.md)

