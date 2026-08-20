---
title: Desktop Sprites
apple_id: DTS10001036
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Desktop_Sprites/Listings/Clippings_createsprites_c_CreateSpriteWorld_txt.html
archived_at: '2026-07-18T03:06:46.447685Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Desktop Sprites](Desktop%20Sprites.md)


[Next](Clippings-createsprites.c-NewSprite.txt.md)[Previous](Clippings-createsprites.c-CreateSpriteLayerGWorld.txt.md)

# Clippings/createsprites.c/CreateSpriteWorld.txt

```
        // create a sprite world
        err = NewSpriteWorld (&gSpriteWorld,        /* on return, a new sprite world */
                                windowPtr,          /* destination */
                                gSpritePlane,       /* sprite layer graphics world */
                                &gBackgroundColor,  /* background color */
                                nil);               /* graphics world to be used as the background. */
```

[Next](Clippings-createsprites.c-NewSprite.txt.md)[Previous](Clippings-createsprites.c-CreateSpriteLayerGWorld.txt.md)

