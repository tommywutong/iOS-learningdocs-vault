---
title: CreateMovie
apple_id: DTS10001035
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CreateMovie/Listings/Clippings_QTSound_c_NewTrackMedia_txt.html
archived_at: '2026-07-18T03:05:08.316826Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CreateMovie](CreateMovie.md)


[Next](Clippings-QTSound.c-SoundDescriptionVar.txt.md)[Previous](Clippings-QTSound.c-NewMovieTrack.txt.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html](https://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html)

# Clippings/QTSound.c/NewTrackMedia.txt

```
        theMedia = NewTrackMedia (theTrack,             /* track specifier */
                                  SoundMediaType,       /* type of media */
                                  FixRound((**sndDesc).sampleRate), /* time coordinate system */
                                  nil,                  /* data reference - use the file that is associated with the movie */
                                  0);                   /* data reference type */
```

[Next](Clippings-QTSound.c-SoundDescriptionVar.txt.md)[Previous](Clippings-QTSound.c-NewMovieTrack.txt.md)

