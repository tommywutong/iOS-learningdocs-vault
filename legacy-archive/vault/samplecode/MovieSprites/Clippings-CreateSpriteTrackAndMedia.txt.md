---
title: MovieSprites
apple_id: DTS10001040
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MovieSprites/Listings/Clippings_CreateSpriteTrackAndMedia_txt.html
archived_at: '2026-07-18T03:16:09.474624Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MovieSprites](MovieSprites.md)


[Next](Common%20Files-ComFramework.c.md)[Previous](Clippings-CreateSpriteMovie.txt.md)

# Clippings/CreateSpriteTrackAndMedia.txt

```
    //////////
    //
    // create the sprite track and media
    //
    //////////

    myTrack = NewMovieTrack(myMovie, ((long)kSpriteTrackWidth << 16), ((long)kSpriteTrackHeight << 16), kNoVolume);
    myMedia = NewTrackMedia(myTrack, SpriteMediaType, kSpriteMediaTimeScale, NULL, 0);
```

[Next](Common%20Files-ComFramework.c.md)[Previous](Clippings-CreateSpriteMovie.txt.md)

