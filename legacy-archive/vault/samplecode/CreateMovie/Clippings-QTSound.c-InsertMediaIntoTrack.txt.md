---
title: CreateMovie
apple_id: DTS10001035
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CreateMovie/Listings/Clippings_QTSound_c_InsertMediaIntoTrack_txt.html
archived_at: '2026-07-18T03:05:08.213225Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CreateMovie](CreateMovie.md)


[Next](Clippings-QTSound.c-NewMovieTrack.txt.md)[Previous](Clippings-QTSound.c-AddMediaSample.txt.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html](https://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html)

# Clippings/QTSound.c/InsertMediaIntoTrack.txt

```
        err = InsertMediaIntoTrack (theTrack,       /* track specifier */ 
                                    kTrackStart,    /* track start time */
                                    kMediaStart,    /* media start time */
                                    GetMediaDuration (theMedia),     /* media duration */
                                    fixed1);        /* media rate ((Fixed) 0x00010000L) */
```

[Next](Clippings-QTSound.c-NewMovieTrack.txt.md)[Previous](Clippings-QTSound.c-AddMediaSample.txt.md)

