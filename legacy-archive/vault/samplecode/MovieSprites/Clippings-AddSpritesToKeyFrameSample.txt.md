---
title: MovieSprites
apple_id: DTS10001040
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MovieSprites/Listings/Clippings_AddSpritesToKeyFrameSample_txt.html
archived_at: '2026-07-18T03:16:09.384474Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MovieSprites](MovieSprites.md)


[Next](Clippings-CreateKeyFrameSample.txt.md)[Previous](Clippings-AddOverrideSamples.txt.md)

# Clippings/AddSpritesToKeyFrameSample.txt

```
    //////////
    //
    // add samples to the sprite track's media
    //
    //////////

    // the code below will add to each kSpriteAtomType 
    // sprite atom the following sprite property atoms:
    //
    // kSpritePropertyImageIndex
    // kSpritePropertyLayer
    // kSpritePropertyGraphicsMode
    // kSpritePropertyMatrix
    // kSpritePropertyVisible
    // kSpriteNameAtomType
    // kSpriteURLLinkAtomtype

    BeginMediaEdits(myMedia);

    // create 
    myErr = QTNewAtomContainer(&mySpriteData);
    if (myErr != noErr)
        goto bail;

    // the background image
    if (gUseBackgroundPicture) {
        myLocation.h    = 0;
        myLocation.v    = 0;
        isVisible       = true;
        myLayer         = kBackgroundSpriteLayerNum;            // this makes the sprite a background sprite
        myIndex         = kBackgroundImageIndex;
        myErr = SetSpriteData(mySpriteData, &myLocation, &isVisible, &myLayer, &myIndex, NULL, NULL, NULL);
        if (myErr != noErr)
            goto bail;
        AddSpriteToSample(mySample, mySpriteData, kBackgroundSpriteAtomID);
    }

    // the space ship sprite
    myLocation.h    = 0;
    myLocation.v    = 60;
    isVisible       = true;
    myLayer         = -1;
    myIndex         = kFirstSpaceShipImageIndex;
    myErr = SetSpriteData(mySpriteData, &myLocation, &isVisible, &myLayer, &myIndex, NULL, NULL, NULL);
    if (myErr != noErr)
        goto bail;
    AddSpriteToSample(mySample, mySpriteData, kSpaceShipSpriteAtomID);

    // the world sprite
    myLocation.h    = (kSpriteTrackWidth / 2) - 24;
    myLocation.v    = (kSpriteTrackHeight / 2) - 24;
    isVisible       = true;
    myLayer         = 1;
    myIndex         = kWorldImageIndex;
    myErr = SetSpriteData(mySpriteData, &myLocation, &isVisible, &myLayer, &myIndex, NULL, NULL, NULL);
    if (myErr != noErr)
        goto bail;
    AddSpriteToSample(mySample, mySpriteData, kWorldSpriteAtomID);

    // the icon sprite
    myIconMinH          = (kSpriteTrackWidth / 2) - 116;
    myIconMaxH          = myIconMinH + 200;
    myDelta             = 2;
    myIconLocation.h    = myIconMinH;
    myIconLocation.v    = (kSpriteTrackHeight / 2) - (24 + 12);
    isVisible           = true;
    myLayer             = 0;
    myIndex             = kIconImageIndex;
    myErr = SetSpriteData(mySpriteData, &myIconLocation, &isVisible, &myLayer, &myIndex, NULL, NULL, NULL);
    if (myErr != noErr)
        goto bail;
    AddSpriteToSample(mySample, mySpriteData, kIconSpriteAtomID);
```

[Next](Clippings-CreateKeyFrameSample.txt.md)[Previous](Clippings-AddOverrideSamples.txt.md)

