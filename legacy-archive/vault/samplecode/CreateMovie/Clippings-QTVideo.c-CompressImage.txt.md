---
title: CreateMovie
apple_id: DTS10001035
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CreateMovie/Listings/Clippings_QTVideo_c_CompressImage_txt.html
archived_at: '2026-07-18T03:05:08.720343Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CreateMovie](CreateMovie.md)


[Next](Clippings-QTVideo.c-EndMediaEdits.txt.md)[Previous](Clippings-QTVideo.c-BeginMediaEdits.txt.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html](https://developer.apple.com/mac/library/samplecode/QTKitCreateMovie/index.html)

# Clippings/QTVideo.c/CompressImage.txt

```
            err = CompressImage(GetPortPixMap(theGWorld), /* source image to compress */
                                trackFrame,               /* bounds */
                                codecNormalQuality,       /* desired image quality */
                                kAnimationCodecType,      /* compressor identifier */
                                imageDesc,                /* handle to Image Description Structure; will be resized by call */
                                compressedDataPtr);       /* pointer to a location to recieve the compressed image data */
```

[Next](Clippings-QTVideo.c-EndMediaEdits.txt.md)[Previous](Clippings-QTVideo.c-BeginMediaEdits.txt.md)

