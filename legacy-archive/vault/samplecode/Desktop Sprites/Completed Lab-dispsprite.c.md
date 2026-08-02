---
title: Desktop Sprites
apple_id: DTS10001036
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Desktop_Sprites/Listings/Completed_Lab_dispsprite_c.html
archived_at: '2026-07-18T03:06:47.009938Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Desktop Sprites](Desktop%20Sprites.md)


[Next](Completed%20Lab-dispsprite.h.md)[Previous](Completed%20Lab-createsprites.h.md)

# Completed Lab/dispsprite.c

```c

#ifndef _MAININCLUDES_
#include "main.h"
#endif


void MyDisposeEverything (void)
{
    short               nIndex;

    // dispose of each spriteÕs image data
    for (nIndex = 0; nIndex < kNumSprites; nIndex++)
    {
        if (gSprites[nIndex])
            DisposeSprite(gSprites[nIndex]);

        if (gCompressedPictures[nIndex])
            DisposeHandle(gCompressedPictures[nIndex]);

        if (gImageDescriptions[nIndex])
            DisposeHandle((Handle)gImageDescriptions[nIndex]);
    }

    // dispose of the sprite plane world
    if (gSpritePlane)
        DisposeGWorld(gSpritePlane);

    // dispose of the sprite world and associated graphics world
    if (gSpriteWorld)
        DisposeSpriteWorld(gSpriteWorld);
}
```

[Next](Completed%20Lab-dispsprite.h.md)[Previous](Completed%20Lab-createsprites.h.md)

