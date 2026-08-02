---
title: FetchTaggedData not Called Often
apple_id: DTS10001237
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd22.html
archived_at: '2026-07-18T02:29:33.215210Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD22FetchTaggedData not Called Often |

|  |  |
| --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: My `FetchTaggedData` override doesn't get called as often as I expected, and it doesn't get called for `'ptyp'` resources. Does GX get the paper types (e.g., for the Page Setup popup) directly from the driver? What other resources are fetched this way?  If `FetchTaggedData` isn't used that often, how do I modify such things on the fly? For instance, if the user specifies a PPD when the DTP is created, how do I notify GX of the new list of paper types? Do I have to change/add resources in the driver or DTP?  A: It's true that `FetchTaggedData` is not called as often as you would expect. The LaserWriter GX driver does get the paper types and other resources directly from the driver. The job collection is setup when the DTP is created.  There are three things that prevent you from telling GX which fonts the user downloads to the printer's disk file in the current version of GX:   1. The font name is stored in the resource name of the `'pfnt'` resource, so `FetchTaggedData` can't access the name. 2. The core GX printing code never looks in desktop printer files for `'pfnt'`s. 3. The core GX printing code doesn't use `FetchTaggedData` to load the other `'pfnt'`s, so there is no way to override the current behavior.   What you are trying to do is perfectly reasonable, and there's no reason why GX should have this limitation. A fix for these problems ought to be incorporated into a future version of GX. |

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
