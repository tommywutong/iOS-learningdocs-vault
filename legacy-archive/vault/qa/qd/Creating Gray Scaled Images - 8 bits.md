---
title: Creating Gray Scaled Images > 8 bits
apple_id: DTS10001904
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-11-17'
source_url: https://developer.apple.com/library/archive/qa/qd/qd51.html
archived_at: '2026-07-18T02:38:38.174485Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/Carbon/idxGraphicsImaging-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Graphics & Imaging](https://developer.apple.com/referencelibrary/Carbon/idxGraphicsImaging-date.html)

|  |
| --- |
| Technical Q&A QD51Creating Gray Scaled Images > 8 bits |

|  |  |
| --- | --- |
| ---   Q: I want to create gray-scaled images at resolutions greater than 8 bits, and display them on the Mac. What is the best way to go about this?  A: Quickdraw doesn't have any inherent support for gray-scaled `PixMaps`, so you need to build a custom data structure to manipulate the gray-scale image, and copy this image to an offscreen `GWorld` when you want to draw it to the screen.  The Quickdraw color table for the offscreen should ramp from white at location 0 to black at location 255. Quickdraw always assumes that white and black will be in these locations, and does not perform correctly when this isn't the case. However, this is the opposite of the intensity value in a gray-scaled image, where black would be at 0, and white at 255.  The other thing that is required is a routine to convert from the custom data structure to the QuickDraw offscreen. This conversion can be accomplished by taking the top 8 bits of each gray pixel, inverting them and copying it into the offscreen `GWorld`. A good source of info would be "Drawing in GWorlds for Speed and Versatility" in [_Develop issue 10_](https://developer.apple.com/library/archive/dev/techsupport/develop/issue10toc.shtml). The following snippet of code accumulates four pixels worth of data, converting from a 16-bit gray pixel to an 8-bit color index.   |  | | --- | | ``` UInt16 *sourceGreyPtr; UInt32 *destPixelsPtr; UInt16 pixel1, pixel2, pixel3, pixel4; UInt32 pixelOutput; { 	pixel1 = sourceGreyPtr[0]; 	pixel2 = sourceGreyPtr[1]; 	pixel3 = sourceGreyPtr[2]; 	pixel4 = sourceGreyPtr[3]; 	// Shift each pixel to its location, take the complement, and mask out  the correct byte 	pixel1 = ~(pixel1 << 16) & 0xFF000000; 	pixel2 = ~(pixel2 << 8)  & 0x00FF0000; 	pixel3 = ~(pixel3)       & 0x0000FF00; 	pixel4 = ~(pixel4 >> 8)  & 0x000000FF; 	pixelOutput = (pixel1 << 24) | (pixel2 << 16) | (pixel3 << 8) | (pixel4); 	*destPixelsPtr = pixelOutput; 	sourceGreyPtr +=4;                           // Advances 8 bytes 	destPixelsPtr +=1;                           // Advances 4 bytes } ``` |   Quickdraw GX does include a luminance-based color model (`gxGraySpace`). |

#### [Nov 17 1997]

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
