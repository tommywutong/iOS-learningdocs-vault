---
title: GX 'comm' Resource Type
apple_id: DTS10001216
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd01.html
archived_at: '2026-07-18T02:29:32.117341Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD01GX 'comm' Resource Type |

|  |  |
| --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: We have a printer that can be connected through a serial or a parallel interface. We provide an entry in our `'look'` resource which references a special "parallel" `'comm'` resource to provide the "parallel" option in the Chooser menu. The communication type we specify in the `'comm'` resource is `'PARA'`. How can we create a `'PARA'` comm resource to be stored in our desktop printer?  A: There are two ways you can accomplish this:   1. Redefine the `'comm'` resource type to include your special connection type in addition to the standard ones (SPTL, PPTL, etc.). It is necessary to redefine the type, because otherwise, you won't be able to successfully Rez your code, since you're specifying a comm type that the interfaces don't describe. When the corresponding menu item is selected, QuickDraw GX automatically copies your `'look'` into the desktop printer that's created. If you need to tweak the data being written to the desktop printer, override `GXDefaultDesktopPrinter` and modify the resource (see number 2). 2. Create your `'comm'` resource as a `'nops comm'` resource. While nops comm resources are intended for non-connected printers, you can modify the resource as it's being written out, since the comm resource is only used after copying it to the desktop printer. To do this, override `GXDefaultDesktopPrinter`, forward the message, call `GXFetchDTPData` to load the comm resource, modify the data (change it to a `'PARA'` comm resource), and write it back out by calling `GXWriteDTPData`.   Your `'look'` and `'iobm'` resources don't require any changes, except to have the look resource reference the appropriate comm resources. You'll have to override `GXOpenConnection`, `GXCloseConnection`, `GXDumpBuffer`, and so on, since you're specifying an unknown communication protocol (you need to implement that communication mechanism). |

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
