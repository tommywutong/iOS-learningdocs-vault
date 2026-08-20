---
title: WiredSprites
apple_id: DTS10001044
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/WiredSprites/Listings/Clippings_SetSpriteProperties_txt.html
archived_at: '2026-07-18T03:28:21.675500Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WiredSprites](WiredSprites.md)


[Next](Clippings-SpriteTrackProperties.txt.md)[Previous](Clippings-InsertMediaIntoTrack.txt.md)

# Clippings/SetSpriteProperties.txt

```
    //////////
    //
    // add samples to the sprite track's media
    //
    //////////

    BeginMediaEdits(myMedia);

    // go to beginning button with no actions
    myErr = QTNewAtomContainer(&myBeginButton);
    if (myErr != noErr)
        goto bail;
    myLocation.h    = (1 * kSpriteTrackWidth / 8) - (kStartEndButtonWidth / 2);
    myLocation.v    = (4 * kSpriteTrackHeight / 5) - (kStartEndButtonHeight / 2);
    isVisible       = false;
    myLayer         = 1;
    myIndex         = kGoToBeginningButtonUpIndex;
    myErr = SetSpriteData(myBeginButton,
                        &myLocation,    /* sprite location */
                        &isVisible,     /* sprite visible property */
                        &myLayer,       /* sprite layer (smaller #'s are further forward) */
                        &myIndex,       /* sprite index property */
                        NULL,
                        NULL,
                        myActions);
    if (myErr != noErr)
        goto bail;

    // go to previous button with no actions
    myErr = QTNewAtomContainer(&myPrevButton);
    if (myErr != noErr)
        goto bail;
    myLocation.h    = (3 * kSpriteTrackWidth / 8) - (kNextPrevButtonWidth / 2);
    myLocation.v    = (4 * kSpriteTrackHeight / 5) - (kStartEndButtonHeight / 2);
    isVisible       = false;
    myLayer         = 1;
    myIndex         = kGoToPrevButtonUpIndex;
    myErr = SetSpriteData(myPrevButton, &myLocation, &isVisible, &myLayer, &myIndex, NULL, NULL, myActions);
    if (myErr != noErr)
        goto bail;

    // go to next button with no actions
    myErr = QTNewAtomContainer(&myNextButton);
    if (myErr != noErr)
        goto bail;
    myLocation.h    = (5 * kSpriteTrackWidth / 8) - (kNextPrevButtonWidth / 2);
    myLocation.v    = (4 * kSpriteTrackHeight / 5) - (kStartEndButtonHeight / 2);
    isVisible       = false;
    myLayer         = 1;
    myIndex         = kGoToNextButtonUpIndex;
    myErr = SetSpriteData(myNextButton, &myLocation, &isVisible, &myLayer, &myIndex, NULL, NULL, myActions);
    if (myErr != noErr)
        goto bail;

    // go to end button with no actions
    myErr = QTNewAtomContainer(&myEndButton);
    if (myErr != noErr)
        goto bail;
    myLocation.h    = (7 * kSpriteTrackWidth / 8) - (kStartEndButtonWidth / 2);
    myLocation.v    = (4 * kSpriteTrackHeight / 5) - (kStartEndButtonHeight / 2);
    isVisible       = false;
    myLayer         = 1;
    myIndex         = kGoToEndButtonUpIndex;
    myErr = SetSpriteData(myEndButton, &myLocation, &isVisible, &myLayer, &myIndex, NULL, NULL, myActions);
    if (myErr != noErr)
        goto bail;

    // first penguin sprite with no actions
    myErr = QTNewAtomContainer(&myPenguinOne);
    if (myErr != noErr)
        goto bail;
    myLocation.h    = (3 * kSpriteTrackWidth / 8) - (kPenguinWidth / 2);
    myLocation.v    = (kSpriteTrackHeight / 4) - (kPenguinHeight / 2);
    isVisible       = true;
    myLayer         = 2;
    myIndex         = kPenguinDownRightCycleStartIndex;
    myGraphicsMode.graphicsMode = blend;
    myGraphicsMode.opColor.red = myGraphicsMode.opColor.green = myGraphicsMode.opColor.blue = 0x8FFF;   // grey
    myErr = SetSpriteData(myPenguinOne, &myLocation, &isVisible, &myLayer, &myIndex, &myGraphicsMode, NULL, myActions);
    if (myErr != noErr)
        goto bail;

    // second penguin sprite with no actions
    myErr = QTNewAtomContainer(&myPenguinTwo);
    if (myErr != noErr)
        goto bail;
    myLocation.h    = (5 * kSpriteTrackWidth / 8) - (kPenguinWidth / 2);
    myLocation.v    = (kSpriteTrackHeight / 4) - (kPenguinHeight / 2);
    isVisible       = true;
    myLayer         = 3;
    myIndex         = kPenguinForwardIndex;
    myErr = SetSpriteData(myPenguinTwo, &myLocation, &isVisible, &myLayer, &myIndex, NULL, NULL, myActions);
    if (myErr != noErr)
        goto bail;
```

[Next](Clippings-SpriteTrackProperties.txt.md)[Previous](Clippings-InsertMediaIntoTrack.txt.md)

