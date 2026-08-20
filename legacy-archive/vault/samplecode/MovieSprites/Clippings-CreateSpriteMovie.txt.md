---
title: MovieSprites
apple_id: DTS10001040
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MovieSprites/Listings/Clippings_CreateSpriteMovie_txt.html
archived_at: '2026-07-18T03:16:09.449163Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MovieSprites](MovieSprites.md)


[Next](Clippings-CreateSpriteTrackAndMedia.txt.md)[Previous](Clippings-CreateKeyFrameSample.txt.md)

# Clippings/CreateSpriteMovie.txt

```
    // create a movie file for the destination movie
    myErr = CreateMovieFile(&myFile, FOUR_CHAR_CODE('TVOD'), smSystemScript, myFlags, &myResRefNum, &myMovie);
    if (myErr != noErr)
        goto bail;
```

[Next](Clippings-CreateSpriteTrackAndMedia.txt.md)[Previous](Clippings-CreateKeyFrameSample.txt.md)

