---
title: CreateMovie
apple_id: DTS10001035
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CreateMovie/Listings/Clippings_QTSound_c_AddMediaSample_txt.html
archived_at: '2026-07-18T03:05:08.163888Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CreateMovie](CreateMovie.md)


[Next](Clippings-QTSound.c-InsertMediaIntoTrack.txt.md)[Previous](Clippings-QTFlatten.c-FlattenMovieData.txt.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html](https://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html)

# Clippings/QTSound.c/AddMediaSample.txt

```
        err = AddMediaSample (theMedia,             /* media specifier */       
                              sndHandle,            /* handle to sample data - dataIn */
                              sndDataOffset,        /* specifies offset into data reffered to by dataIn handle */
                              sndDataSize,          /* number of bytes of sample data to be added */
                              kSoundSampleDuration, /* duration of each sound sample */
                              (SampleDescriptionHandle)sndDesc, /* sample description handle */
                              numSamples,           /* number of samples */
                              kSyncSample,          /* control flag indicating self-contained samples */
                              nil);                 /* returns a time value where sample was insterted */
```

[Next](Clippings-QTSound.c-InsertMediaIntoTrack.txt.md)[Previous](Clippings-QTFlatten.c-FlattenMovieData.txt.md)

