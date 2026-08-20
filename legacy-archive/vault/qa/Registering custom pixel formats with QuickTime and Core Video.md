---
title: Registering custom pixel formats with QuickTime and Core Video
apple_id: DTS10003774
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2005-09-06'
source_url: https://developer.apple.com/library/archive/qa/qa1401/_index.html
archived_at: '2026-07-18T02:30:31.632850Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1401

# Registering custom pixel formats with QuickTime and Core Video

## Q:  How does a Codec register custom pixel formats in QuickTime 7.0?

A: With previous versions of QuickTime, a codec supporting custom pixel formats would need to register these formats by calling the Image Compression Manager API `ICMSetPixelFormatInfo`. The codec would also list the four-character codes for these pixel formats in it's `'cpix'` resource.

`ICMSetPixelFormatInfo` takes a pixel format code and a pointer to a `ICMPixelFormatInfo` structure providing information about the pixel format being registered.

The `'cpix'` resource is an array of four-character pixel format codes listing the codec's supported custom pixel formats.

With the release of QuickTime 7 codec writers additionally need to register custom pixel formats with Core Video. This is done by calling the Core Video API `CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType`.

`CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType` takes a `CFDictionary` containing the pixel format description in the form of a list of required and optional keys, along with the four-character code for the pixel format being registered.

Listing 1 demonstrates how to register a hypothetical pixel format we'll call 'R120'. For demonstration purposes this is an invented 120-bit-per-pixel format with 40-bit R, 40-bit G and 40-bit B. Each "block" contains a single pixel, so the description is minimal:

- `kCVPixelFormatConstant` `CFNumber` 'R120'
- `kCVPixelFormatBitsPerBlock` `CFNumber` 120

__Listing 1__  Registering a custom pixel format.

```
enum {
  kHypotheticalPixelFormat = FOUR_CHAR_CODE('R120')
};

OSStatus SetNumberValue(CFMutableDictionaryRef inDict, CFStringRef inKey, SInt32 inValue)
{
    CFNumberRef number;

    number = CFNumberCreate(kCFAllocatorDefault, kCFNumberSInt32Type, &inValue);
    if (NULL == number) return coreFoundationUnknownErr;

    CFDictionarySetValue(inDict, inKey, number);

    CFRelease(number);

    return noErr;
}

// Register information about a custom pixel format with the ICM and Core Video
OSStatus RegisterMyPixelFormat(void)
{
    ICMPixelFormatInfo pixelInfo;
    OSStatus status;

    CFDictionaryRef dict = CFDictionaryCreateMutable(kCFAllocatorDefault,
                                              0,
                                              &kCFTypeDictionaryKeyCallBacks,
                                              &kCFTypeDictionaryValueCallBacks);
    if (NULL == dict) return coreFoundationUnknownErr;

    BlockZero(&pixelInfo, sizeof(pixelInfo));
    pixelInfo.size  = sizeof(ICMPixelFormatInfo);
    pixelInfo.formatFlags    = 0;
    pixelInfo.bitsPerPixel[0] = 120;

    // Ignore any errors here as this could be a duplicate registration
    ICMSetPixelFormatInfo(kHypotheticalPixelFormat, &pixelInfo);

    status = SetNumberValue(dict, kCVPixelFormatConstant, kHypotheticalPixelFormat);
    if (noErr != status) goto bail;

    status = SetNumberValue(dict, kCVPixelFormatBitsPerBlock, 120);
    if (noErr != status) goto bail;

    CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType(dict,
                                                              kHypotheticalPixelFormat);
bail:
    CFRelease(dict);

    return status;
}
```

Some pixel formats cluster pixels together into blocks. In these "chunky block" cases, the pixel format description should describe the dimensions of the block (the default block width and block height are both 1).

For example, the 8-bit Y'CbCr 4:2:2 format, `'2vuy'`, clusters pairs of adjacent pixels into a 32-bit block with two Y samples but one shared Cb sample and one shared Cr sample.

The dictionary Apple builds to describe `'2vuy'` contains the following keys:

- `kCVPixelFormatConstant` `CFNumber` k422YpCbCr8PixelFormat
- `kCVPixelFormatBlockWidth` `CFNumber` 2
- `kCVPixelFormatBitsPerBlock` `CFNumber` 32
- `kCVPixelFormatFillExtendedPixelsCallback` `CFData` containing a `CVFillExtendedPixelsCallBackData` structure describing a custom extended pixel fill algorithm for `'2vuy'`

The 10-bit Y'CbCr 4:2:2 format, `'v210'`, clusters six pixels into each 128-bit block. `'v210'` imposes a further requirement that there be a multiple of 8 blocks in each line.

The dictionary Apple builds to describe `'v210'` contains the following keys:

- `kCVPixelFormatConstant` `CFNumber` k422YpCbCr10CodecType
- `kCVPixelFormatBlockWidth` `CFNumber` 6
- `kCVPixelFormatBitsPerBlock` `CFNumber` 128
- `kCVPixelFormatBlockHorizontalAlignment` `CFNumber` 8
- `kCVPixelFormatFillExtendedPixelsCallback` `CFData` containing a `CVFillExtendedPixelsCallBackData` structure describing a custom extended pixel fill algorithm for `'v210'`

- [Pixel Format Description Keys](https://developer.apple.com/documentation/GraphicsImaging/Reference/CoreVideoRef/Core_Video_Ref/chapter_2.3_section_13.html#//apple_ref/doc/uid/TP40001537-DontLinkChapterID_3-BABFJCJJ)
- [ICMSetPixelFormatInfo](https://developer.apple.com/documentation/QuickTime/APIREF/icmsetpixelformatinfo.htm)
- [CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType](https://developer.apple.com/documentation/GraphicsImaging/Reference/CoreVideoRef/Core_Video_Ref/chapter_2.1_section_12.html)
- ['cpix' Resource](https://developer.apple.com/documentation/QuickTime/APIREF/-cpix-.htm)
- [CVFillExtendedPixelsCallBack](https://developer.apple.com/documentation/GraphicsImaging/Reference/CoreVideoRef/Core_Video_Ref/chapter_2.2_section_3.html)
- [CVFillExtendedPixelsCallbackData](https://developer.apple.com/documentation/GraphicsImaging/Reference/CoreVideoRef/Core_Video_Ref/chapter_2.4_section_4.html#//apple_ref/doc/uid/TP40001537-DontLinkChapterID_4-BABHBJHJ)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-09-06 | editorial |
| 2005-08-30 | New document that discusses how to register custom pixel formats with QuickTime & Core Video with QuickTime 7. |

