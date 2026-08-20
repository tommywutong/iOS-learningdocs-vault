---
title: Desktop Sprites
apple_id: DTS10001036
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Desktop_Sprites/Listings/Clippings_createsprites_c_NewSprite_txt.html
archived_at: '2026-07-18T03:06:46.501013Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Desktop Sprites](Desktop%20Sprites.md)


[Next](Clippings-dispsprite.c-DisposeSprites.txt.md)[Previous](Clippings-createsprites.c-CreateSpriteWorld.txt.md)

# Clippings/createsprites.c/NewSprite.txt

```
        nErr = NewSprite(&(gSprites[lIndex]),           /* on return, the ID of the new sprite */
                        gSpriteWorld,                   /* the sprite world for this sprite */
                        gImageDescriptions[lIndex],     /* image description of the spriteÕs image. */
                        *gCompressedPictures[lIndex],   /* sprite image data */
                        &matrix,                        /* sprite matrix */
                        true,                           /* is sprite visible? */
                        lIndex);                        /* sprite layer */
```

[Next](Clippings-dispsprite.c-DisposeSprites.txt.md)[Previous](Clippings-createsprites.c-CreateSpriteWorld.txt.md)

