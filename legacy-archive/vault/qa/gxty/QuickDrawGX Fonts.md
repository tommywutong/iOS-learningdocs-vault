---
title: QuickDrawGX Fonts
apple_id: DTS10001267
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gxty/gxty08.html
archived_at: '2026-07-18T02:29:34.831871Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXTY08QuickDrawGX Fonts |

|  |
| --- |
| ---   Q: I have certain fonts which cause the driver to fail when they are installed in the system while my spool file is being processed. If I remove these fonts from the system, the problem disappears. It isn't clear whether all of the necessary font information is contained in the spool file once it is generated. If it is, why does it appear that QuickDrawGX looks for the fonts when processing the spool file? Where can I learn about how the QuickDrawGX font mechanism works during page generation and printing?  A: PDDs (page description documents) are transportable and include all the information necessary to image a document. Spool files are not intended to be transportable and assume that the fonts designated in the file continue to be available. For efficiency's sake, they don't spool the fonts, which explains why the fonts are being accessed.  You can learn more about printing from _Inside Macintosh: QuickDraw GX Printing Extensions and Drivers_ , both on the December 94 Dev CD and in print from Addison Wesley. You may also find a number of articles in _develop_ which could help you to learn more about the QuickDraw GX font mechanism. |

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
