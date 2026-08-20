---
title: Desktop Sprites
apple_id: DTS10001036
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Desktop_Sprites/Listings/Clippings_dispsprite_c_DisposeSprites_txt.html
archived_at: '2026-07-18T03:06:46.532431Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Desktop Sprites](Desktop%20Sprites.md)


[Next](Clippings-main.c-SpriteWorldIdle.txt.md)[Previous](Clippings-createsprites.c-NewSprite.txt.md)

# Clippings/dispsprite.c/DisposeSprites.txt

```
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
```

[Next](Clippings-main.c-SpriteWorldIdle.txt.md)[Previous](Clippings-createsprites.c-NewSprite.txt.md)

