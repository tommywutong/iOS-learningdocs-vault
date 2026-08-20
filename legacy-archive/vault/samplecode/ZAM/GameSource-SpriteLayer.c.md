---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/GameSource_SpriteLayer_c.html
archived_at: '2026-07-18T03:28:33.870945Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](GameSource-TankSprite.c.md)[Previous](GameSource-SpriteFrameSet.c.md)

# GameSource/SpriteLayer.c

```c
#include "sprite.h"

#include "SpriteLayer.proto.h"

typedef struct spriteLayer {
    struct spriteLayer  *next;      // the layer in back of this one
    struct spriteLayer  *prev;      // the layer in front of this one
    spritePtr   *sprites;           // the sprites in this layer
    GWorldPtr   tween;              // the work GWorld for this layer
    GWorldPtr   backdrop;           // the background for this layer
    WindowPtr   window;             // the window this layer ends up in
    long        layerFlags;
    long        layerID;
    long        layerRefcon;
} spriteLayer, *spriteLayerPtr;


static spriteLayerPtr   MasterSpriteHead;
static spriteLayerPtr   MasterSpriteTail;

OSErr   CreateSpriteLayer(spriteLayerPtr *retSprite, 
                            GWorldPtr tween, 
                            GWorldPtr backdrop, 
                            WindowPtr spriteWin)
{

    OSErr           err;
    spriteLayerPtr  sl;

    sl = (spriteLayerPtr)NewPtrClear(sizeof(spriteLayer));
    if(!sl) {
        err = MemError();
        ErrMsgCode("\pCreateSpriteLayer NewPtrClear failed.",err);
    }

    if(err == noErr) {
        sl->tween = tween;
        sl->backdrop = backdrop;
        sl->window = spriteWin;
    }

    if(MasterSpriteTail) {
        sl->prev = MasterSpriteTail;
        MasterSpriteTail->next = sl;
        MasterSpriteTail = sl;
    } else {
        MasterSpriteHead = MasterSpriteTail = sl;
    }

    *retSprite = sl;

    return err;

}
```

[Next](GameSource-TankSprite.c.md)[Previous](GameSource-SpriteFrameSet.c.md)

