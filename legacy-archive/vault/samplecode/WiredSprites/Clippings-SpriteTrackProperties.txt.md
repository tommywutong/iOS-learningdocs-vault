---
title: WiredSprites
apple_id: DTS10001044
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/WiredSprites/Listings/Clippings_SpriteTrackProperties_txt.html
archived_at: '2026-07-18T03:28:21.724583Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WiredSprites](WiredSprites.md)


[Next](Common%20Files-ComFramework.c.md)[Previous](Clippings-SetSpriteProperties.txt.md)

# Clippings/SpriteTrackProperties.txt

```
    //////////
    //
    // set the sprite track properties
    //
    //////////
    {
        QTAtomContainer     myTrackProperties;
        RGBColor            myBackgroundColor;

        // add a background color to the sprite track
        myBackgroundColor.red = EndianU16_NtoB(0x8000);
        myBackgroundColor.green = EndianU16_NtoB(0);
        myBackgroundColor.blue = EndianU16_NtoB(0xffff);

        QTNewAtomContainer(&myTrackProperties);
        QTInsertChild(myTrackProperties, 0, kSpriteTrackPropertyBackgroundColor, 1, 1, sizeof(RGBColor), &myBackgroundColor, NULL);

        // tell the movie controller that this sprite track has actions, Jackson
        hasActions = true;
        QTInsertChild(myTrackProperties, 0, kSpriteTrackPropertyHasActions, 1, 1, sizeof(hasActions), &hasActions, NULL);

        // tell the sprite track to generate QTIdleEvents
        myFrequency = EndianU32_NtoB(60);
        QTInsertChild(myTrackProperties, 0, kSpriteTrackPropertyQTIdleEventsFrequency, 1, 1, sizeof(myFrequency), &myFrequency, NULL);
        myErr = SetMediaPropertyAtom(myMedia, myTrackProperties);
        if (myErr != noErr)
            goto bail;

        QTDisposeAtomContainer(myTrackProperties);
    }
```

[Next](Common%20Files-ComFramework.c.md)[Previous](Clippings-SetSpriteProperties.txt.md)

