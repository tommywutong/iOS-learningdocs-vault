---
title: ColorSync Color Matching on Intel-based Macs
apple_id: DTS10003888
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2006-03-16'
source_url: https://developer.apple.com/library/archive/qa/qa1464/_index.html
archived_at: '2026-07-18T02:30:52.760841Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1464

# ColorSync Color Matching on Intel-based Macs

## Q:  Do I need to byte-swap my bitmap before performing color matching with the ColorSync APIs on an Intel-based Macintosh?

A: Do I need to byte-swap my bitmap before performing color matching with the ColorSync APIs on an Intel-based Macintosh?

If you are using `CWMatchColors` then make sure the values in the array of `CMColors` are in host endian order.

If you are using `CWMatchBitmap`, the `CMBitmapColorSpace` field of the source and destination `CMBitmap` structs can be flagged with `cmLittleEndianPacking`.

The ColorSync APIs only accept data in canonical component order (RGB is R,G,B, CMYK is C,M,Y,K, and so on).

For example, if you have a "Green" CMYK pixel seen as 0x00FF00FF on an Intel-based Mac you will need to swap it before (and possibly after) calling ColorSync. Specifying `cmLittleEndianPacking` in the `CMBitmapColorSpace` field of the source and destination `CMBitmap` structs will not help in this case because the pixel is represented by 8 bits per component.

Should you need to swap the component order within a pixel we recommend you use the `CMFloatBitmap` structure which is very flexible with regard to component ordering and even allows for planar bitmaps. See [Technical Note 2035 ColorSync on Mac OS X](https://developer.apple.com/technotes/tn/tn2035.html) for more information.

ICC Profiles need not and should not be changed to swap pixel data. The ICC specification (see [International Color Consortium](http://www.color.org/)) provides for big-endian data in profiles and for component data to be in canonical order.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-03-16 | New document that describes special considerations for byte ordering when performing ColorSync color matching on Intel-based Macs |

