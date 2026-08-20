---
title: CreateMovie
apple_id: DTS10001035
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CreateMovie/Listings/Clippings_QTVideo_c_GetMaxCompressionSize_txt.html
archived_at: '2026-07-18T03:05:08.896571Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CreateMovie](CreateMovie.md)


[Next](Clippings-QTVideo.c-ImageDescriptorVar.txt.md)[Previous](Clippings-QTVideo.c-EndMediaEdits.txt.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html](https://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html)

# Clippings/QTVideo.c/GetMaxCompressionSize.txt

```
        err = GetMaxCompressionSize(GetPortPixMap(theGWorld),       /* Handle to the source image */
                                    trackFrame,                     /* bounds */
                                    kMgrChoose,                     /* let ICM choose depth */
                                    codecNormalQuality,             /* desired image quality */ 
                                    kAnimationCodecType,            /* compressor type */ 
                                    (CompressorComponent)anyCodec,  /* compressor identifier */
                                    &maxCompressedSize);            /* returned size */
```

[Next](Clippings-QTVideo.c-ImageDescriptorVar.txt.md)[Previous](Clippings-QTVideo.c-EndMediaEdits.txt.md)

