---
title: What depth should I put in an Image Description?
apple_id: DTS10001712
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2006-11-27'
source_url: https://developer.apple.com/library/archive/qa/qa1183/_index.html
archived_at: '2026-07-18T02:30:12.239683Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1183

# What depth should I put in an Image Description?

## Q:  Are there any guidelines for the value of the depth field when creating Image Descriptions?

A: Are there any guidelines for the value of the depth field when creating Image Descriptions?

The Image Compression Manager uses Image Descriptions to describe compressed and uncompressed image data. Sometimes these are created for you by an API like `MakeImageDescriptionForPixMap` or `GraphicsImportGetImageDescription`. However, sometimes you need to create an image description yourself.

The `depth` field of an image description does not always contain a literal number of bits per pixel. Instead, it should be the QuickDraw pixel size that most closely describes the image data. This enables applications to broadly understand properties of a compressed image without needing to know specific details. Information about where the true depth gets stored is covered in 'Section 2' of this document.

When filling in the `depth` field directly, use the following guide:

- If the image has an alpha channel, always use 32.
- If the image is grayscale, use a grayscale depth:

  - 40 for 8-bit or deeper samples
  - 36 for 4-bit samples
  - 34 for 2-bit samples
  - 33 for 1-bit samples
- If the image is indexed color (ie, each sample is interpreted through a color look-up table), use the appropriate color depth; In these cases, the color table must be attached to the image description. You can do this by calling `SetImageDescriptionCTable`.

  - 8 for 256 color
  - 4 for 16 color
  - 2 for 4 color
  - 1 for Monochrome
- If the image is a 16-bit RGB pixel format, use 16.

Otherwise use 24 if the image doesn't match any of the above criteria. This is the generic "color with no alpha channel" depth.

For YUV pixel formats without alpha, use 24. Although YUV9 is 9 bits per pixel, YUV 4:2:0 is 12 bits per pixel, and YUV 4:2:2 is 16 bits per pixel, you should still use 24.

Follow the above guidelines even for pixel formats with samples deeper than 8-bit. For example, 48-bit RGB should use depth 24 and 64-bit ARGB should use depth 32.

__Table 1__  Quick Summary Guide

| Image type | Depth value to use |
| Has an alpha channel | 32 |
| 256 indexed color - requires CTable | 8 |
| 16 indexed color - requires CTable | 4 |
| 4 indexed color - requires CTable | 2 |
| 2 indexed color - requires CTable | 1 |
| 8-bit or deeper grayscale | 40 |
| 4-bit or grayscale | 36 |
| 2-bit or grayscale | 34 |
| 1-bit or grayscale | 33 |
| 16-bit RGB pixel format - any flavour | 16 |
| YUV pixel formats without alpha | 24 |
| Color with no alpha channel - generic depth | 24 |
| 48-bit RGB | 24 |
| 64-bit ARGB | 32 |
| 32-bit grayscale with alpha | 32 |
| 16-bit grayscale | 40 |

`QTGetPixelFormatDepthForImageDescription` (available in QuickTime 6.0 and greater) returns the appropriate depth code for any registered pixel format.

When the image data in question is an __uncompressed__ pixel array of a big-endian pixel format that QuickDraw supports (specifically, 1, 2, 4, 8, 16, 24, 32, 33, 34, 36, or 40), the `cType` field of the image description should be `kRawCodecType` and the `depth` field (as discussed above) should be the pixel format. For example, for 8-bit grayscale, the `cType` field should contain `kRawCodecType` and the `depth` field should contain 40.

When the image data in question is an __uncompressed__ pixel array of a non-QuickDraw pixel format, the `cType` field of the image description should be the pixel format code. For example, `k2vuyPixelFormat` ('2vuy'). In this case the `depth` field (as discussed above) should contain 24. For 16-bit grayscale, the `cType` field should contain `k16GrayCodecType` and the `depth` field should contain 40.

When the image data in question is __compressed__, but has a special native pixel format that it can be decompressed directly into, the pixel format should be stored as a big-endian OSType in an image description extension of type `kImageDescriptionColorSpace` ('cspc'). The value of the `cType` field should reflect the way the image data was compressed.

For example, a PNG file containing a 48-bit-per-pixel RGB image would be described by an image description with a `cType` of `kPNGCodecType` ('png '), a big-endian `kImageDescriptionColorSpace` ('cspc') image description extension containing the OSType `k48RGBCodecType` ('b48r') and a `depth` field (as discussed above) containing the value 24.

If your application needs more detailed information about registered pixel formats, use `ICMGetPixelFormatInfo`.

- [The Image Description Structure](https://developer.apple.com/documentation/QuickTime/RM/CompressDecompress/ImageComprMgr/F-Chapter/chapter_1000_section_15.html)
- [QTGetPixelFormatDepthForImageDescription - What's new in QuickTime 6](https://developer.apple.com/documentation/QuickTime/QT6WhatsNew/Chap1/chapter_1_section_45.html)
- [SetImageDescriptionCTable](https://developer.apple.com/documentation/QuickTime/Reference/QTRef_CompDecomp/Reference/reference.html#//apple_ref/c/func/SetImageDescriptionCTable)
- [ICMGetPixelFormatInfo](https://developer.apple.com/documentation/QuickTime/Reference/QTRef_CompDecomp/Reference/reference.html#//apple_ref/c/func/ICMGetPixelFormatInfo)
- [Technical Note TN2057, 'Fill in the size field before calling ICMGetPixelFormatInfo'](https://developer.apple.com/technotes/tn2002/tn2057.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-11-27 | editorial |
| 2002-08-15 | New document that describes how to select the correct value for the depth field of an image description. |

