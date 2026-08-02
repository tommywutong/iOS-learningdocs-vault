---
title: Tray Mismatch Dialog in QuickDraw GX 1.1.1b1
apple_id: DTS10001234
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd19.html
archived_at: '2026-07-18T02:29:33.047103Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD19Tray Mismatch Dialog in QuickDraw GX 1.1.1b1 |

|  |  |
| --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: I installed QuickDraw GX 1.1.1b1 and tried some of our printer drivers with it. The first print job after a DTP is created displays a 'Paper Mismatch Alert' alert, stating that the wrong paper is loaded in the printer. Selecting the 'Load Tray' option with 'Make paper change permanent' checked keeps the alert from showing again. Looking in the DTP file, I noticed a 'binp' resource, but I couldn't find a definition for this resource in the new header files.  What is the `'binp'` resource type definition? How do I prevent the 'Paper Mismatch Alert' from always appearing in the first print job? A: Starting with 1.1b1, QuickDraw GX presents a tray-mismatch dialog whenever a printer tray contains an "unknown" paper type. Although this is the correct behavior, users are presented with the tray-mismatch dialog the first time they print, unless they first define the paper types in the printer via the "Input Trays..." dialog.  Since users may be mystified or miffed by the increased frequency of seeing the paper-mismatch dialog, we put a change in place to reduce that frequency quite a bit. Now, when you create a desktop printer, the DTP's default tray is configured with the driver's default paper type (only if `gxDoesPaperFit` succeeds, of course). For most US drivers, this means that US Letter is stored in the DTP, and you don't get alerted unless you print with a paper type other than US Letter.  The `'binp'` resource is an undocumented, private resource used by GX to store the current tray setting of a DTP. Because this is a private resource type, it is subject to change in future versions of GX, so don't access it directly -- use `GXSetTrayPaperType` instead. |

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
