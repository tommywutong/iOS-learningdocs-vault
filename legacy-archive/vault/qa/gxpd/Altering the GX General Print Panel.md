---
title: Altering the GX General Print Panel
apple_id: DTS10001256
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-10-25'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd41.html
archived_at: '2026-07-18T02:29:34.235336Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD41Altering the GX General Print Panel |

|  |  |
| --- | --- |
| ---     |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: I am writing a printer driver that will create an EPS file for each page of a document. To do this, I need to customize the General print panel. I basically need to eliminate the dialog items displayed when the More Choices button is clicked (paper feed, destination, etc.). I also need to change the Print button to a Save button, so the user can choose a destination for the EPS file(s) created. Can I eliminate the controls I don't want by modifying the job collection from a printer driver? If so, how do I modify the collection items to hide the unwanted controls, and what message do I override to modify them? If this approach won't work, is there another way (such as substituting my own General panel for the default?)  A: Currently, there is no mechanism in GX to remove most panel items from the standard print panels. The reasoning behind this is that from a user interface standpoint, the panels need to remain the same across various drivers so every user gets the same user experience. You can, however, grey out/disable certain items in the print panel as well as customize the destination pop-up/OK button to suit your needs.  In order to disable items in the print panel, you need to get the collection item of what you want to disable and set the locked attribute by calling `SetCollectionItemInfo()`. This will dim the item in the panel. (NOTE: Not all items are able to be dimmed.) Collection items are documented in [Inside Macintosh: QuickDraw GX Environments and Utilities.](https://developer.apple.com/documentation/mac/GXEnvironment/GXEnvironment-2.html) FYI, the Quality item is an exception to the dimming/elimination rule... The Quality collection item (`gxQualityTag` = `'qual'`) whose structure is defined in GXPrinting.h, has a Boolean field called `disableQuality`. If your driver specifies this field as true, then the quality item will not appear at all.  In order to change the destination pop-up and modify the 'OK' button (you need to do both together) you need to override the `GXHandleAltDestination` message and add an Alternate Destination (`'dsta'`) resource to your driver. The specific details of these items are documented in [Technote 1028](https://developer.apple.com/library/archive/technotes/tn/tn1028.html).  If none of this suits your needs, you can override the panel entirely (via `GXJobPrintDialog`) and create your own. This is really not a good idea from the user interface standpoint, but it will get the job done. |

#### [Oct 25 1996]

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
