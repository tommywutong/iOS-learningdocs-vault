---
title: QuickDraw GX and Adobe Type Reunion
apple_id: DTS10001224
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd09.html
archived_at: '2026-07-18T02:29:32.509632Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Text & Fonts](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTextFonts-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Text & Fonts](https://developer.apple.com/referencelibrary/TextFonts/index.html)

|  |
| --- |
| Technical Q&A GXPD09QuickDraw GX and Adobe Type Reunion |

|  |  |
| --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: I have a question relating to QuickDraw GX:  I'm using the `HierFontMenu` function in the font-menu library that came with GX to build my font menu. However, it seems that Adobe Type Reunion (which is trying to perform a similar function) affects this menu, causing some fonts to be omitted. Is there a simple way that I can tell Type Reunion and other font-menu extensions like it to leave my `GXHierFontMenu` alone?  A: Unfortunately, there is no method to tell Type Reunion and other font-menu extensions like it, to leave your menus alone. They were designed to affect all applications, and they don't have options. You'll have to remove or turn off Type Reunion and other font-menu extensions to prevent the types of problems you're experiencing with your `GXHierFontMenu`.  There are no notes or other documentation for the QuickDraw GX library code. This code is provided as "sample code" to help your development and learning processes. Notes relating to the GX libraries are on our list of things to do. However, we can point you towards some documentation on the SDK that may be of some help. There is a document called "QD GX Font HI Guidelines" in the "Documents" folder on the SDK that contains guidelines and ideas for creating GX font menus. |

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
