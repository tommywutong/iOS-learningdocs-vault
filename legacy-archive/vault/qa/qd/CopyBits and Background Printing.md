---
title: CopyBits and Background Printing
apple_id: DTS10001775
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/qd/qd16.html
archived_at: '2026-07-18T02:38:36.141895Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A QD16CopyBits and Background Printing |

|  |  |
| --- | --- |
| ---   Q: When I use `CopyBits` to move a `cGrafPort`'s `portPixMap` to another `cGrafPort` (my printing port), it works like a charm when background printing is turned on, but when `CopyBits` gets called with background printing turned off, the image that prints isn't the image at all. Why is this happening?  A: You should be aware that since you're copying the pixels directly from the screen, the `baseAddr` pointer for the screen's `pixMap` may be 32-bit addressed. In fact, with 32-Bit QuickDraw, this is the case. This in itself isn't a problem, since `CopyBits` knows enough to access the `baseAddr` of the port's pixMap in 32-bit mode, as follows:   |  | | --- | | ``` mode = true32b;             // Make sure we're in 32-bit addressing mode.                              // Access pixels directly; make no other system calls.  SwapMMUMode(&mode);         // Restore the current mode. ``` |   That's how you'd normally handle things if you were accessing the pixels directly yourself. Unfortunately, the LaserWriter driver doesn't know enough to do the `SwapMMUMode` and instead ends up copying garbage (from a 32-bit pointer stripped to a 24-bit pointer).  So why does background printing work? Because when you print in the background, everything is rolled into a PICT, which the driver saves off for PrintMonitor. Since the driver is using the standard QuickDraw picture bottlenecks to do this, and `CopyBits` knows to swap the MMU mode before copying the data into the picture, everything works great. Later, at PrintMonitor time, the picture is played back. Since the data is no longer 32-bit addressed, the LaserWriter driver doesn't have to call `SwapMMUMode` to do the right thing; it can just play the picture back.  The solution we propose for you is something similar. At print time (before your `PrOpenPage` call), call `OpenPicture`, copy the data from the screen with `CopyBits`, call `ClosePicture`, and then call `DrawPicture` within your `PrOpenPage/PrClosePage` loop. That should do the trick.  Note that copying bits directly from the screen is not something we recommend. Unless you have no alternative, you should always copy from the original source of the data instead. |

#### [Sep 15 1995]

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
