---
title: CGBitmapContextCreate Supported Color Spaces
apple_id: DTS10001589
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2007-07-18'
source_url: https://developer.apple.com/library/archive/qa/qa1037/_index.html
archived_at: '2026-07-18T02:29:54.830142Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1037

# CGBitmapContextCreate Supported Color Spaces

## Q:  What color spaces does `CGBitmapContextCreate` support?

A: `CGBitmapContextCreate` supports the following combinations for the `colorspace` (CS), `bitsPerComponent` (BPC), and `alphaInfo` parameters:

__Table 1__  Supported Combinations

| CS | BPC | alphaInfo | Resulting Bits and Description |
| NULL | 8 | kCGImageAlphaOnly | AAAAAAAA 8 bits per pixel alpha-only destination. Color data is thrown away. Useful for generating alpha-only bitmaps and masks. Available in Mac OS X 10.3 and later. |
| Gray | 8 | kCGImageAlphaNone | WWWWWWWW 8 bits per pixel grayscale channel. |
| RGB | 5 | kCGImageAlphaNoneSkipFirst | -RRRRRGGGGGBBBBB 16 bits per pixel, 5 bits per RGB component. |
| RGB | 8 | kCGImageAlphaNoneSkipFirst | --------RRRRRRRRRGGGGGGGGBBBBBBBB 32 bits per pixel, 8 bits per RGB component where first 8 bits are ignored. |
| RGB | 8 | kCGImageAlphaNoneSkipLast | RRRRRRRRRGGGGGGGGBBBBBBBB-------- 32 bits per pixel, 8 bits per RGB component where last 8 bits are ignored. |
| RGB | 8 | kCGImageAlphaPremultipliedFirst | AAAAAAAARRRRRRRRRGGGGGGGGBBBBBBBB 32 bits per pixel, 8 bits per ARGB component with premultiplied alpha. |
| RGB | 8 | kCGImageAlphaPremultipliedLast | RRRRRRRRRGGGGGGGGBBBBBBBBAAAAAAAA 32 bits per pixel, 8 bits per RGBA component with premultiplied alpha. |
| CMYK | 8 | kCGImageAlphaNone | CCCCCCCCMMMMMMMMYYYYYYYYKKKKKKKK 32 bits per pixel, 8 bits per CMYK component without alpha. Available in Mac OS X 10.3 and later. |

__Table 2__  and the resulting bits are designated as follows:

| Bit | Description |
| W | White |
| A | Alpha |
| R | Red |
| G | Green |
| B | Blue |
| C | Cyan |
| M | Magenta |
| Y | Yellow |
| K | Black |
| - | Skip |

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-06 | Updated to point to the Quartz 2D Programming Guide, minor text changes. |
| 2007-07-18 | Updated to point to the Quartz 2D Programming Guide, minor text changes. |
| 2005-10-04 | Updated to point to the Q&A describing how to properly create color spaces. Added a note that this Q&A is only valid for formats introduced in 10.3 and earlier. |
| 2004-09-09 | Removed two combinations in the Gray color space that had been incorrectly documented as supported. |
| 2004-02-20 | New document that lists the color space and alpha info combinations currently supported by CGBitmapContextCreate. |

