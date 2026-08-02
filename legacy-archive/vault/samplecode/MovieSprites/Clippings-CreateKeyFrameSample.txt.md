---
title: MovieSprites
apple_id: DTS10001040
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MovieSprites/Listings/Clippings_CreateKeyFrameSample_txt.html
archived_at: '2026-07-18T03:16:09.424403Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MovieSprites](MovieSprites.md)


[Next](Clippings-CreateSpriteMovie.txt.md)[Previous](Clippings-AddSpritesToKeyFrameSample.txt.md)

# Clippings/CreateKeyFrameSample.txt

```
    //////////
    //
    // create a key frame sample containing the sprites and all of their shared images
    //
    //////////


    // create a new, empty key frame sample
    myErr = QTNewAtomContainer(&mySample);
    if (myErr != noErr)
        goto bail;

    // specify transparency color for recompression
    myKeyColor.red = myKeyColor.green = myKeyColor.blue = 0xffff;       // white

    // add images to the key frame sample - AddPICTImageToKeyFrameSample
    // will add the following atom data to the key frame atom container:
    //
    // kSpriteShareDataAtomType
    // kSpriteImagesContainerAtomType
    // kSpriteImageAtomType
    // kSpriteImageDataAtomType
    //
    // and optionally:
    //
    // kSpriteImageRegistrationAtomType
    // kSpriteImageNameAtomType

    AddPICTImageToKeyFrameSample(mySample, kIconPictID, &myKeyColor, kIconImageIndex, NULL, NULL);
    AddPICTImageToKeyFrameSample(mySample, kWorldPictID, &myKeyColor, kWorldImageIndex, NULL, NULL);
    AddPICTImageToKeyFrameSample(mySample, kBackgroundPictID, &myKeyColor, kBackgroundImageIndex, NULL, NULL);
    for (myIndex = 1; myIndex <= kNumSpaceShipImages; myIndex++)
        AddPICTImageToKeyFrameSample(mySample, kFirstSpaceShipPictID + myIndex - 1, &myKeyColor, myIndex + 3, NULL, NULL);
```

[Next](Clippings-CreateSpriteMovie.txt.md)[Previous](Clippings-AddSpritesToKeyFrameSample.txt.md)

