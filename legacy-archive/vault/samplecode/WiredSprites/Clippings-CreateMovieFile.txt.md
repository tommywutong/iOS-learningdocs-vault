---
title: WiredSprites
apple_id: DTS10001044
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/WiredSprites/Listings/Clippings_CreateMovieFile_txt.html
archived_at: '2026-07-18T03:28:21.609548Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WiredSprites](WiredSprites.md)


[Next](Clippings-InsertMediaIntoTrack.txt.md)[Previous](Clippings-CreateKeyFrameSample.txt.md)

# Clippings/CreateMovieFile.txt

```
    // create a movie file for the destination movie
    myErr = CreateMovieFile(&myFile,                /* fsspec for the movie to be created */
                            FOUR_CHAR_CODE('TVOD'), /* creator value for the new file */
                            smSystemScript,         /* script in which the movie file should be created */
                            myFlags,                /* movie creation flags */
                            &myResRefNum,           /* file reference for movie file return here */
                            &myMovie);              /* new movie identifier return here */
    if (myErr != noErr)
        goto bail;

    // select the "no controller" movie controller option
    myType = EndianU32_NtoB(myType);
    SetUserDataItem(GetMovieUserData(myMovie),
                    &myType,
                    sizeof(myType),
                    kUserDataMovieControllerType,
                    1);

    //////////
    //
    // create the sprite track and media
    //
    //////////

    myTrack = NewMovieTrack(myMovie,
                            ((long)kSpriteTrackWidth << 16),    /* display width in pixels */
                            ((long)kSpriteTrackHeight << 16),   /* display height in pixels */
                            kNoVolume);                         /* volume setting of the track */
    myMedia = NewTrackMedia(myTrack,
                            SpriteMediaType,        /* type of media to create */
                            kSpriteMediaTimeScale,  /* media time scale */
                            NULL,                   /* data ref, pass nil to use the file the movie was created in */
                            0);                     /* data ref type, pass nil to use the file the movie was created in */
```

[Next](Clippings-InsertMediaIntoTrack.txt.md)[Previous](Clippings-CreateKeyFrameSample.txt.md)

