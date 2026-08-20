---
title: QuickDraw GX 'ptyp' Page Size Calc
apple_id: DTS10001229
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd14.html
archived_at: '2026-07-18T02:29:32.775461Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD14QuickDraw GX 'ptyp' Page Size Calc |

|  |  |  |  |
| --- | --- | --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: The following code is from one of the sample GX drivers for a `'ptyp'` resource. How are the hex numbers derived from the inch numbers for page and paper sizes? For example, what does 8.10667 inches have to do with the number 0x0247AE18?   |  | | --- | | ``` resource gxPaperTypeType ( gxPrintingDriverBaseID + 1, "US Letter", kResAttributes ) {     "US Letter",     /* page rectangle */    0x00000000, /* 0.0 */    0x00000000, /* 0.0 */    0x0247AE18, /* 8.10667 */    0x0308A3DC, /* 10.7867 */     /* paper rectangle */    0xFFF1D70C, /* -0.196666 */    0xFFF870A8, /* -0.104999 */    0x0255D70C, /* 8.30333 */    0x031070A8, /* 10.895 */     usLetterBase,    kCreatorType,     inch,    etc. ``` |   A: The hex numbers represent pixels, and the values within the comments are in inches. Let's take a look at a piece of the `gxPaperTypeType` you sent:   |  | | --- | | ```    0x0247AE18, /* 8.10667 */ ``` |   0x0247AE18 translates to 583.68005 pixels. When you divide 583.68005 by 72, you get 8.1066674 -- the same value as the comment. |

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
