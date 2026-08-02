---
title: Spooling in or out of CompressPicture or CompressImage
apple_id: DTS10001776
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/qd/qd17.html
archived_at: '2026-07-18T02:38:36.215643Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/Carbon/idxGraphicsImaging-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Graphics & Imaging](https://developer.apple.com/referencelibrary/Carbon/idxGraphicsImaging-date.html)

|  |
| --- |
| Technical Q&A QD17Spooling in or out of CompressPicture or CompressImage |

|  |
| --- |
| ---   Q: Can I use the `CompressPicture` routine to spool in a source picture from disk by overriding the QuickDraw proc `getPicProc` as documented in _Inside Macintosh Volume V_, pages 88-89? I'm trying to save the contents of an off-screen `GWorld` as a compressed PICT resource. Unfortunately there's no direct way to compress the `GWorld`'s pixel map to a resource.  A: We definitely don't recommend trying to spool in or out the results of `CompressPicture` or `CompressImage`. We recommend doing one of the following instead:   1. You can compress the `GWorld` using `CompressImage` and then call `OpenPicture`,    `DecompressImage`, and `ClosePicture` using a data-unloading picture proc. The    drawback here is that you need to have a copy of the compressed image in    memory. 2. If it's unacceptable to have an entire compressed image in memory, you can    consider banding along with data unloading: Call `OpenPicture`, then    `CompressImage` and `DecompressImage` on a band, `CompressImage` and `DecompressImage`    on another band, and so on. When all bands are done, call `ClosePicture`. The    drawback for this is that the compressed picture will have bands of image data    that won't display well dithered. This could be an issue, but the best way to    find out is to try it.   The second suggestion is probably the best idea if you want to keep your memory footprint small. But much of the decision depends on your application. |

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
