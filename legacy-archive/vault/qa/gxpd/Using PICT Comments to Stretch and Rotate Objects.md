---
title: Using PICT Comments to Stretch and Rotate Objects
apple_id: DTS10001240
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd25.html
archived_at: '2026-07-18T02:29:33.366637Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD25Using PICT Comments to Stretch and Rotate Objects |

|  |  |  |
| --- | --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: We are trying to add full GX-printing support to our drawing program, which isn't a GX-aware application, and we're running into some problems with the translator. When we use PICT comments to stretch and rotate objects, the objects sometimes disappear completely. Using direct `GXRotateShape` routines to rotate a shape has the same result. However, direct rotation and concatenation of the mappings works properly.  A: This happens because support for flipping with picture comments was not included in the current implementation of GX. This will be fixed in a future release.  If you are using the translator, you're limited by the way it performs its translation. You would be better off providing your own replacement for the translator, because you understand your data structures better.  You can use the following code snippet as a starting point to create your own translator. It creates a GX Ink with a simple 8 x 8 black and white bit pattern, allows an arbitrary color for foreground and another for background, and can be added to a frame or fill:   |  | | --- | | ``` //Code for calling SetShapeQDPattern()             {                 char        pattern[] = {0xAA,0x55,0xAA,0x55,0xAA,0x55,0xAA,0x55};                 RGBColor    fore, back;                  fore.red = 0xFFFF;                 fore.green = 0;                 fore.blue = 0;                 back.red = 0;                 back.green = 0xFFFF;                 back.blue = 0;                  SetShapeQDPattern(tempShape, (PatPtr)&pattern, &fore, &back);             }  //SetShapeQDPattern() // ------------------------------------------------------------------------------------- static void SetShapeQDPattern(                 gxShape theShape,               // shape to set pattern on                 PatPtr pPattern,                // 1 bit QD pattern to use                 RGBColor *pForeColor,           // color of the 0 bits (or is this 1?)                 RGBColor *pBackColor)           // color of the 1 bits (or is this 0?) {     gxPatternRecord     pattern;     gxBitmap            bits;     gxSetColor          colors[2];      pattern.attributes  = 0;     pattern.u.x         = ff(8);     pattern.u.y         = ff(0);     pattern.v.x         = ff(0);     pattern.v.y         = ff(8);      colors[0].rgb.red = pForeColor->red;     colors[0].rgb.green = pForeColor->green;     colors[0].rgb.blue = pForeColor->blue;     colors[1].rgb.red = pBackColor->red;     colors[1].rgb.green = pBackColor->green;     colors[1].rgb.blue = pBackColor->blue;      bits.image      = (char*)pPattern;     bits.width      = 8;     bits.height     = 8;     bits.rowBytes   = 1;     bits.pixelSize  = 1;     bits.space      = gxIndexedSpace;     bits.set        = GXNewColorSet(gxRGBSpace, 2, &colors);     bits.profile    = nil;     pattern.pattern = GXNewBitmap(&bits, nil);     GXDisposeColorSet(bits.set);      GXSetShapePattern(theShape, &pattern);     GXDisposeShape(pattern.pattern);  } // SetShapeQDPattern  //-------------------------------------------------- ``` | |

#### [May 01 1995]

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
