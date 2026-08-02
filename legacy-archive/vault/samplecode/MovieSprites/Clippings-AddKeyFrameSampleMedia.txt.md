---
title: MovieSprites
apple_id: DTS10001040
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MovieSprites/Listings/Clippings_AddKeyFrameSampleMedia_txt.html
archived_at: '2026-07-18T03:16:09.291928Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MovieSprites](MovieSprites.md)


[Next](Clippings-AddMovieResource.txt.md)[Previous](Application%20Files-ComResource.h.md)

# Clippings/AddKeyFrameSampleMedia.txt

```
    // add the key frame sample to the sprite track media
    //
    // to add the sample data in a compressed form, you would use a QuickTime DataCodec to perform the
    // compression; replace the call to the utility AddSpriteSampleToMedia with a call to the utility
    // AddCompressedSpriteSampleToMedia to do this

    AddSpriteSampleToMedia(myMedia, mySample, kSpriteMediaFrameDuration, true, NULL);   
    //AddCompressedSpriteSampleToMedia(myMedia, mySample, kSpriteMediaFrameDuration, true, zlibDataCompressorSubType, NULL);
```

[Next](Clippings-AddMovieResource.txt.md)[Previous](Application%20Files-ComResource.h.md)

