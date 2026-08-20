---
title: CreateMovie
apple_id: DTS10001035
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CreateMovie/Listings/Clippings_QTVideo_c_AddMediaSample_txt.html
archived_at: '2026-07-18T03:05:08.492067Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CreateMovie](CreateMovie.md)


[Next](Clippings-QTVideo.c-BeginMediaEdits.txt.md)[Previous](Clippings-QTSound.c-TrackMediaVars.txt.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html](https://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html)

# Clippings/QTVideo.c/AddMediaSample.txt

```
            err = AddMediaSample(theMedia,               /* media specifier */ 
                                 compressedData,         /* handle to sample data - dataIn */
                                 kNoOffset,              /* specifies offset into data reffered to by dataIn handle */
                                 (**imageDesc).dataSize, /* number of bytes of sample data to be added */ 
                                 kSampleDuration,        /* frame duration = 1/10 sec */
                                 (SampleDescriptionHandle)imageDesc,    /* sample description handle */ 
                                 kAddOneVideoSample,    /* number of samples */
                                 kSyncSample,           /* control flag indicating self-contained samples */
                                 nil);                  /* returns a time value where sample was insterted */
```

[Next](Clippings-QTVideo.c-BeginMediaEdits.txt.md)[Previous](Clippings-QTSound.c-TrackMediaVars.txt.md)

