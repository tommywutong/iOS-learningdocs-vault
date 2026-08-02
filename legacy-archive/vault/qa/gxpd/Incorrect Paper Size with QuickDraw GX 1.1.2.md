---
title: Incorrect Paper Size with QuickDraw GX 1.1.2
apple_id: DTS10001250
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-08-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd35.html
archived_at: '2026-07-18T02:29:33.876874Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD35Incorrect Paper Size with QuickDraw GX 1.1.2 |

|  |  |
| --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: Documents formatted for US Letter that are created with non-QuickDraw GX drivers open as A4 in QuickDraw GX 1.1.2. This did not occur with QuickDraw GX 1.0. How we can avoid this problem?  A: In QuickDraw GX 1.0, there were no custom paper types. When we added custom paper types in QuickDraw GX 1.1.1, we created the problem that you are encountering. There are several possible workarounds that you can implement until this problem can be fixed (in QuickDraw GX 1.2):   1. Default the paper type to US Letter, and have the user make corrections in your page-setup dialog. 2. Force users to choose the paper type before printing. 3. When your application is set up on a system that has QuickDraw GX installed, warn the user of the paper-type problem. 4. When your application is set up on a system that has QuickDraw GX installed, inform the user that they should remove all custom paper types from the Extensions folder (3-hole punch, letterhead, and stationery), and re-save the documents. |

#### [Aug 01 1995]

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
