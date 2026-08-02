---
title: WiredSprites
apple_id: DTS10001044
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/WiredSprites/Listings/Clippings_AddOverrideSamples_txt.html
archived_at: '2026-07-18T03:28:21.432520Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WiredSprites](WiredSprites.md)


[Next](Clippings-AddSpriteActions.txt.md)[Previous](Clippings-AddMovieResource.txt.md)

# Clippings/AddOverrideSamples.txt

```
    //////////
    //
    // add a few override samples to move penguin one and change its image index
    //
    //////////

    // original penguin one location
    myLocation.h    = (3 * kSpriteTrackWidth / 8) - (kPenguinWidth / 2);
    myLocation.v    = (kSpriteTrackHeight / 4) - (kPenguinHeight / 2);

    myDelta = (kSpriteTrackHeight / 2) / kNumOverrideSamples;
    myIndex = kPenguinDownRightCycleStartIndex;

    for (i = 1; i <= kNumOverrideSamples; i++) {
        QTRemoveChildren(mySample, kParentAtomIsContainer);
        QTNewAtomContainer(&myPenguinOneOverride);

        myLocation.h += myDelta;
        myLocation.v += myDelta;
        myIndex++;
        if (myIndex > kPenguinDownRightCycleEndIndex)
            myIndex = kPenguinDownRightCycleStartIndex;

        SetSpriteData(myPenguinOneOverride, &myLocation, NULL, NULL, &myIndex, NULL, NULL, NULL);
        AddSpriteToSample(mySample, myPenguinOneOverride, kPenguinOneSpriteID);
        AddSpriteSampleToMedia(myMedia, mySample, kSpriteMediaFrameDuration, false, NULL);  
        QTDisposeAtomContainer(myPenguinOneOverride);
    }

    EndMediaEdits(myMedia);
```

[Next](Clippings-AddSpriteActions.txt.md)[Previous](Clippings-AddMovieResource.txt.md)

