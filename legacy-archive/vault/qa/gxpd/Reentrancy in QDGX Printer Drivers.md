---
title: Reentrancy in QDGX Printer Drivers
apple_id: DTS10001252
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-02-09'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd37.html
archived_at: '2026-07-18T02:29:33.980826Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD37Reentrancy in QDGX Printer Drivers |

|  |  |
| --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: I am writing a QuickDraw GX printer driver that supports SCSI and Server connection types. I can connect multiple printers to one Mac on the SCSI bus, and I have seen that I can have active print jobs printing on all of them simultaneously.  Do I have to be concerned about reentrancy when coding my message overrides?  A: There are a few issues you'll need to keep in mind.  One is that each copy of your driver must store any data it needs in its own data space. You can do this by using the `GetMessageHandlerInstanceContext` and `SetMessageHandler`-`InstanceContext` functions. If there is common global data that all copies of your driver will need to access, you can use the `SetMessageHandlerClassContext` and `GetMessageHandlerClassContext` functions. These are documented in Chapter 6 of _Inside Macintosh: QuickDraw GX Environment and Utilities_.  For each instance of your driver, you'll also need to watch out for insufficient memory. You shouldn't need to add much code if you are already checking for error conditions when attempting to allocate memory within your driver, but if there are places where you're not checking to make sure that the allocation was actually successful, you'll need to add code (it's a good idea to always check anyhow).  You will also need to confirm that you don't have multiple instances of your driver trying to write to the same DTP at the same time. There are any number of ways you can implement this, including using a shared (`ClassContext`) data block with a semaphore to mark whether an instance of your driver was in the middle of a `GXWriteDTPData` call. Each instance could then first check that semaphore before attempting to read or write data from the DTP. Be sure to include file-locking while your driver is reading or writing other files.  Additionally, if you are writing a PostScript driver, be aware that the PostScript font downloading code is not reentrant.  In general, you should use these techniques to write any QuickDraw GX print driver, whether you expect it to need to worry about reentrancy or not. |

#### [Feb 09 1996]

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
