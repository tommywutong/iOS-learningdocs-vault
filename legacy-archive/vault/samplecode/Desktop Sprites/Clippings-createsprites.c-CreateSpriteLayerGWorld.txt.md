---
title: Desktop Sprites
apple_id: DTS10001036
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Desktop_Sprites/Listings/Clippings_createsprites_c_CreateSpriteLayerGWorld_txt.html
archived_at: '2026-07-18T03:06:46.418404Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Desktop Sprites](Desktop%20Sprites.md)


[Next](Clippings-createsprites.c-CreateSpriteWorld.txt.md)[Previous](Clippings-animsprite.c-SetSpriteMatrix.txt.md)

# Clippings/createsprites.c/CreateSpriteLayerGWorld.txt

```
    // create a sprite layer graphics world with a bit depth of 32
    NewGWorld (&gSpritePlane, 32, &bounds, nil, nil, useTempMem);
    if (gSpritePlane == nil)
    {
        NewGWorld (&gSpritePlane, 32, &bounds, nil, nil, 0);
    }
```

[Next](Clippings-createsprites.c-CreateSpriteWorld.txt.md)[Previous](Clippings-animsprite.c-SetSpriteMatrix.txt.md)

