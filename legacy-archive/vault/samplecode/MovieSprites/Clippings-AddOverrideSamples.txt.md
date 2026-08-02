---
title: MovieSprites
apple_id: DTS10001040
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MovieSprites/Listings/Clippings_AddOverrideSamples_txt.html
archived_at: '2026-07-18T03:16:09.345541Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MovieSprites](MovieSprites.md)


[Next](Clippings-AddSpritesToKeyFrameSample.txt.md)[Previous](Clippings-AddMovieResource.txt.md)

# Clippings/AddOverrideSamples.txt

```
    //////////
    //
    // add a few override samples to move the space ship and icon, and to change the icon's layer
    //
    //////////

    // original space ship location
    myIndex         = kFirstSpaceShipImageIndex;
    myLocation.h    = 0;
    myLocation.v    = 80;
    isVisible       = true;

    for (i = 1; i <= kNumOverrideSamples; i++) {

        // remove existing atoms (which we used above
        // to create our key frame sample) from our key
        // frame sample atom container so we can re-use
        // the atom containers for our override samples
        QTRemoveChildren(mySample, kParentAtomIsContainer);
        QTRemoveChildren(mySpriteData, kParentAtomIsContainer);

        // every third frame, bump the space ship's image index (so that it spins as it moves)
        if ((i % 3) == 0) {
            myIndex++;
            if (myIndex > kLastSpaceShipImageIndex)
                myIndex = kFirstSpaceShipImageIndex;
        }

        // every frame, bump the space ship's location (so that it moves as it spins)
        myLocation.h += 2;
        myLocation.v += 1;

        if (isVisible)
            SetSpriteData(mySpriteData, &myLocation, NULL, NULL, &myIndex, NULL, NULL, NULL);
        else {
            isVisible = true;
            SetSpriteData(mySpriteData, &myLocation, &isVisible, NULL, &myIndex, NULL, NULL, NULL);
        }

        AddSpriteToSample(mySample, mySpriteData, 2);

        // make the icon move and change layer

        // first remove previous children from our container
        // so we can re-add the new sprite property atoms
        QTRemoveChildren(mySpriteData, kParentAtomIsContainer);

        // change the icon location
        myIconLocation.h += myDelta;

        if (myIconLocation.h >= myIconMaxH ) {
            myIconLocation.h = myIconMaxH;
            myDelta = -myDelta;
        }

        if (myIconLocation.h <= myIconMinH ) {
            myIconLocation.h = myIconMinH;
            myDelta = -myDelta;
        }

        // change the sprite layer
        if (myDelta > 0)
            myLayer = 0;
        else
            myLayer = 3;

        // set the data for the sprite
        SetSpriteData(mySpriteData, &myIconLocation, NULL, &myLayer, NULL, NULL, NULL, NULL);

        AddSpriteToSample(mySample, mySpriteData, 4);

        AddSpriteSampleToMedia(myMedia, mySample, kSpriteMediaFrameDuration, false, NULL);  
    }

    EndMediaEdits(myMedia);

    // add the media to the track
    InsertMediaIntoTrack(myTrack, 0, 0, GetMediaDuration(myMedia), fixed1);
```

[Next](Clippings-AddSpritesToKeyFrameSample.txt.md)[Previous](Clippings-AddMovieResource.txt.md)

