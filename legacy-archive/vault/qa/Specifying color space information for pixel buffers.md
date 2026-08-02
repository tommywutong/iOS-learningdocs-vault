---
title: Specifying color space information for pixel buffers
apple_id: DTS40014645
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2014-06-05'
source_url: https://developer.apple.com/library/archive/qa/qa1839/_index.html
archived_at: '2026-07-18T02:35:09.313381Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1839

# Specifying color space information for pixel buffers

## Q:  Why does the `AVAssetWriterInputPixelBufferAdaptor` `appendPixelBuffer`:`withPresentationTime`: method fail with the `AVAssetWriter` error property set to -12917 (`kVTInsufficientSourceColorDataErr`) when I try to write pixel buffers not allocated from the provided `CVPixelBufferPool` to an output file?

A: The -12917 (`kVTInsufficientSourceColorDataErr`) error indicates a color space has not been specified for the source pixel buffers. If you are not using pixel buffers allocated from the provided `CVPixelBufferPool` for `AVAssetWriterInputPixelBufferAdaptor` instances you must specify color space information for the buffers.

For `RGB` source buffers, set the `kCVImageBufferICCProfileKey` or `kCVImageBufferCGColorSpaceKey` attachment on the buffer. Here’s an example of how to set a color space attachment for `RGB` pixel buffers on OS X:

__Listing 1__  Specifying a color space attachment for `RGB` pixel buffers on OS X.

```
CGColorSpaceRef sRGBColorSpace = CGColorSpaceCreateWithName(kCGColorSpaceSRGB);
if (sRGBColorSpace != NULL)
{
    CFDataRef sRGBProfileData = CGColorSpaceCopyICCProfile(sRGBColorSpace);
    if (sRGBProfileData != NULL)
    {
        NSDictionary *pbAttachements =
                    @{(id)kCVImageBufferICCProfileKey : (id)sRGBProfileData};

        CFRelease(sRGBProfileData);

        CVBufferRef pixelBuffer = <#Your pixel buffer#>;

        /* set the color space attachment on the buffer */
        CVBufferSetAttachments(pixelBuffer,
                    (CFDictionaryRef)pbAttachements, kCVAttachmentMode_ShouldPropagate);
    }
    else
    {
        NSLog(@"CGColorSpaceCopyICCProfile returned NULL");

        /* handle the error */
    }

    CFRelease(sRGBColorSpace);
}
else
{
    NSLog(@"CGColorSpaceCreateWithName returned NULL");

    /* handle the error */
}
```

Set the `kCVImageBufferYCbCrMatrixKey`, `kCVImageBufferColorPrimariesKey`, and `kCVImageBufferTransferFunctionKey` attachments to describe `YUV` buffers. Here's an example:

__Listing 2__  Specifying a color space attachment for `YUV` pixel buffers.

```
NSDictionary *pbAttachments =
    @{(id)kCVImageBufferYCbCrMatrixKey:(id)kCVImageBufferYCbCrMatrix_ITU_R_709_2,
     (id)kCVImageBufferColorPrimariesKey:(id)kCVImageBufferColorPrimaries_ITU_R_709_2,
     (id)kCVImageBufferTransferFunctionKey:(id)kCVImageBufferTransferFunction_ITU_R_709_2};
CVBufferRef pixelBuffer = <#Your pixel buffer#>;
CVBufferSetAttachments(pixelBuffer,
    (CFDictionaryRef)pbAttachments, kCVAttachmentMode_ShouldPropagate);
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-06-05 | New document that describes how to specify color space information for pixel buffers |

