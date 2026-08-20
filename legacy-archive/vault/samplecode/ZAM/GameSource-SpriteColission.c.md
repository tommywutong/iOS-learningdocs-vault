---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/GameSource_SpriteColission_c.html
archived_at: '2026-07-18T03:28:33.737850Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](GameSource-SpriteFrameSet.c.md)[Previous](GameSource-Sprite.proto.h.md)

# GameSource/SpriteColission.c

```c
#include "ZAMProtos.h"


void CollideSpriteLayer(spriteLayerPtr sprLayer1, spriteLayerPtr sprLayer2)
/*
    VERY Simple colission detection.  A sprite is not checked unless it has
    a callback, so if you have things that can never be collided with,
    don't give them a colission callback.  Layers are collided against each other,
    so sprites in the same layer can never collide.
*/
{
    spritePtr   spr1, spr2;
    Rect        sectArea;

    for(spr1 = sprLayer1->sprites; spr1 != nil; spr1 = spr1->next)
        for(spr2 = sprLayer2->sprites; spr2 != nil; spr2 = spr2->next)
            if(spr1->collideHandler || spr2->collideHandler) {
                if( SectRect(&spr1->bounds, &spr2->bounds, &sectArea) ) {
                    /* we have a rectangle colission  - call the handlers if installed */
                    if(spr1->collideHandler)
                        (*spr1->collideHandler)(spr1, spr2, &sectArea);
                    if(spr2->collideHandler)
                        (*spr2->collideHandler)(spr2, spr1, &sectArea);
                }
            }

}
```

[Next](GameSource-SpriteFrameSet.c.md)[Previous](GameSource-Sprite.proto.h.md)

