---
title: QuickDraw GX Raster and Blank Lines
apple_id: DTS10001231
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd16.html
archived_at: '2026-07-18T02:29:32.881264Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD16QuickDraw GX Raster and Blank Lines |

|  |  |
| --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: What does the `gxRasterTargetTranslation` option do if it's set in the `'cust'` resource for a raster driver? Does it make imaging quicker (by stripping out Postscript comments from the spool file)? If it's set, does it affect the ability of a spool file to be moved to another type of printer (e.g., PostScript or vector)?  A: You can use the query menu option in Apple DocViewer as a quick guide for these types of questions. For QuickDraw GX-related issues, it is helpful to open the QuickDraw GX collection document on recent issues of the Developer CD: Reference library edition.  The `gxRasterTargetTranslation` option causes PostScript picture comments to be discarded. The bitmap proxies sent along with such comments are preserved.  Yes, it does help make imaging quicker by stripping out PostScript comments from the spool file.  If the `gxRasterTargetTranslation` flag is set, the output is only "good" for raster printers. Bear in mind that this flag is effectively an option for the translator, so you may be able to print properly on a PostScript device, but if the app that generated the data puts in `PicComments` to improve imaging, and this flag is set, the output may not be as-expected. Use this option only if you are certain that the output is going to a raster device. |

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
