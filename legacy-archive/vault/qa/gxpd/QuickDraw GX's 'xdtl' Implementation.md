---
title: QuickDraw GX's 'xdtl' Implementation
apple_id: DTS10001232
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd17.html
archived_at: '2026-07-18T02:29:32.926353Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD17QuickDraw GX's 'xdtl' Implementation |

|  |  |  |
| --- | --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: I have a few questions about QuickDraw GX's 'xdtl' implementation. When using the `xdtlEditTextReal` element, what size/type of real number is stored in the collection (presumably a normal Extended type)?  A: When you use the `xdtlEditTextReal` element, it stores the user's real as a Fixed type (16.16 format). Although this may not be what you'd expect, Fixed does make sense. Floating point formats vary quite a bit from platform to platform, and with PowerPC (which makes a deliberate effort of being IEEE compliant), it's likely that the days of the SANE standard (and its Extended format) are numbered. As a rule, QuickDraw GX uses Fixed whenever possible.  Q: Does the offset into the collection (as specified in the xdtl) have to have any particular alignment for the real type (i.e., are odd byte offsets valid)?  A: There are no intrinsic alignment rules for xdtl's. However, since xdtl's are most often read into high level language structures, they are, in actual practice, subject to the alignment rules that your compiler enforces.  Q: Is it possible to have a panel which uses a combination of xdtl items and items handled by the driver (via an override of `HandlePanelEvent`)?  I've also noticed a possible fault in the LaserWriter GX's use of the xdtl in conjunction with the horizontal and vertical flipping items. The xdtl says that the offset into the collection items for horizontal and vertical flipping items is 1. However, the type definition for each item is just a struct with a single boolean. This boolean (according to MPW C) is the first byte of the structure (a pad byte is appended to the struct by the compiler to make its sizeof = 2). The xdtl should specify 0 as the offset, since with an offset of 1, you are accessing the pad byte. (Obviously this fault exists throughout the Postscript engine since flipping does actually work.) This means that any app that looks to see if flipping is enabled does not see it with the LaserWriter driver. In my raster driver, I access the boolean. Perhaps it would be better to redefine the single-boolean collection item structs so that they are consistent with the LaserWriter's implementation of them, as follows:   |  | | --- | | ``` struct     char padByte;     Boolean importantField } xxx ; ``` |   Can you provide any suggestions or clarifications?  A: It is possible to mix user items and xdtl items in a dialog (to rotate or flip Clarus, Dogcow, or some other indicator, for example). However, this was tried earlier, and a problem with the responsiveness of the indicator was observed. If the control is an xdtl item, then indicator user item does not respond immediately to the user's actions. To avoid this cosmetic problem, we decided to make the flip controls with ditl items instead of xdtl items.  _Inside Macintosh_ states that the collection is only filled in when the user accepts the dialog (i.e., not when the user interacts with the xdtl item), so you cannot have a panel which uses a combination of xdtl items and items handled by the driver.  Regarding the LaserWriter flipping bug, it isn't clear at the present time whether our LaserWriter driver will have the boolean in the 1st or 2nd byte. The fix for this problem is to change the type definition and the documentation, so that it conforms to the way that the current LaserWriter GX driver does things. |

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
