---
title: Quickdraw GX Raster Printer Drivers
apple_id: DTS10001220
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/gxpd/gxpd05.html
archived_at: '2026-07-18T02:29:32.324126Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A GXPD05Quickdraw GX Raster Printer Drivers |

|  |  |
| --- | --- |
| ---  |  | | --- | | __Important for all Apple Printing and Graphics Developers:__   The information in this Technical Q & A is still relevant up to and including [Mac OS 7.6](https://developer.apple.com/library/archive/technotes/tn/tn1090.html) with QuickDraw GX 1.1.5. Beginning with the release of Mac OS 8.0, however, Apple plans to deliver a system which incorporates QuickDraw GX graphics and typography __only__. QuickDraw GX printer drivers and GX printing extensions will __not__ be supported in Mac OS 8.0 or in future Mac OS releases. Apple's goal is to simplify the user experience of printing by unifying the Macintosh graphic and printing architectures and standardizing on the classic Printing Manager. For details on Apple's official announcement, refer to [</dev/technotes/gxchange.html>](https://developer.apple.com/library/archive/technotes/gxchange.html) |     Q: I'm having a problem with my GX raster driver (for a monochrome plotter): I need to call my `RasterPackageBitmap` override for all the lines in a print, regardless of whether the lines are dirty or not. It seems that `RasterDataIn` is checking for clean lines, but not bothering to call `RasterPackageBitmap` for these lines, and is just calling `RasterLineFeed` on its own. Is there a way for me to use the default `RasterDataIn` to accomplish this task, or do I have to override it myself?  It seems that there are plenty of options available in the resources to send all bands, regardless of whether they are dirty, but this doesn't seem to help individual blank lines to get through to `PackageBitmap`. I've tried setting `dirtyRectangle` to `bandRectangle`, but this doesn't work for individual blank lines within bands.  A: There are two possible causes for your problem. The first is the `'rdip'` resource of your driver. The `gxSendAllBands` flag of the `'rdip'` should be set to force the default implementation of `RasterDataIn` to call `RasterPackageBitmap`, even if a line isn't dirty. You should also override `RasterLineFeed`. In this override, you should package up blank lines in the same way that you package up dirty lines in `RasterPackageBitmap`. You have to override both these messages if you use the default implementation of `RasterDataIn`.  There is also a bug in QuickDraw GX 1.0.x, where the `gxOnePlaneAtATime` bit is wrongly used to invoke this behavior. To quickly find out if this is the cause of your problem, try setting the `gxOnePlaneAtATime` bit instead. This bug was fixed in the GX 1.1.1.  If you need a workaround that works with GX 1.0.x, you should have your `RasterDataIn` override pad the output with the appropriate number of empty lines before and after forwarding the message. Pad the output again after `Forward_RenderPage` for any empty bands at the tail end of the page.  It is also possible that the problem is caused, at least in part, by the approach that your driver is taking. We've found that most raster drivers completely override the `RasterDataIn` message (which circumvents `RasterPackageBitmap` altogether) in order to have total control of the banding and the buffering (i.e., `SendBufferData`) process. This is a much easier way to implement your driver. |

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
