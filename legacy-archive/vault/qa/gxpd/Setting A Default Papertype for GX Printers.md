---
title: Setting A Default Papertype for GX Printers
apple_id: DTS10001253
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-04-08'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd38.html
archived_at: '2026-07-18T02:29:34.043963Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD38Setting A Default Papertype for GX Printers |

|  |  |
| --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: My driver has a `'ptyp'` of "A4 portrait" as the default paper type (via the `isDefaultpapertype` flag). When a user chooses my driver from Page Setup dialog, "A4" is selected as the default paper type in the desktop printer, though my driver has no `'ptyp'` named "A4".  How can I set my own paper type ("A4 portrait") as the default?  A: Unfortunately, this is a bug in QuickDraw GX.  GX internally adds the standard paper types (e.g., A4, US Letter, etc,) to your driver. The bug is that GX thinks it is finding a better fit for the current page dimensions than the assigned A4 portrait paper type. It then defaults to GX's internal A4 paper type. In other words, the paper matching code is working incorrectly.  If you are defaulting to a non-standard paper type, such as Letterhead, Stationery or Three-hole Punch, the best workaround is to remove that paper type from the Extensions folder.  If you are defaulting to another paper type, then the easiest thing you can do is to open your driver with ResEdit and remove or edit the `'ptyp'` resource for the paper type that is incorrectly matching (open up the resource in ResEdit, and you'll see the paper type name embedded in the data).  This is the only way to correct the problem at this time. It is not very user-friendly, but it will force the driver to default to the correct paper type. |

#### [Apr 08 1996]

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
