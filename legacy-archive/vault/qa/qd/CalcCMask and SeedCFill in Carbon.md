---
title: CalcCMask and SeedCFill in Carbon
apple_id: DTS10001915
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-11-08'
source_url: https://developer.apple.com/library/archive/qa/qd/qd62.html
archived_at: '2026-07-18T02:38:38.813441Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/GraphicsImaging/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/GraphicsImaging/idxCarbon-date.html) >

|  |
| --- |
| Technical Q&A QD62CalcCMask and SeedCFill in Carbon |

|  |
| --- |
| ---     Q: My pre-Carbon code makes extensive use of `CalcCMask` and `SeedCFill`, which produce 1-bit deep masks. I currently call `OpenPort` and pass the port's `BitMap` to `CalcCMask` and `SeedCFill`, but `OpenPort` isn't supported in Carbon and its replacement, `CreateNewPort`, creates a `CGrafPort` with a `PixMap`. What should I pass as the `dstBits` parameter?  A: Create a 1-bit deep `GWorld` and pass in its `PixMap` using `GetPortBitMapForCopyBits`. QuickDraw calls that used to expect a `GrafPort` (or `BitMap`) have been modified to accept a 1-bit deep `GWorld` (or `PixMap`).   --- |

#### [Nov 08 2000]

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
