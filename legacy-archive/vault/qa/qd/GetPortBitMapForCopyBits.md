---
title: GetPortBitMapForCopyBits
apple_id: DTS10001914
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-11-08'
source_url: https://developer.apple.com/library/archive/qa/qd/qd61.html
archived_at: '2026-07-18T02:38:38.740076Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/Carbon/idxGraphicsImaging-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Graphics & Imaging](https://developer.apple.com/referencelibrary/Carbon/idxGraphicsImaging-date.html)

|  |
| --- |
| Technical Q&A QD61GetPortBitMapForCopyBits |

|  |
| --- |
| ---     Q: What is `GetPortBitMapForCopyBits` and is it only for use with `CopyBits`?  A: `GetPortBitMapForCopyBits` is designed to do the right thing when extracting a `BitMap/PixMap` out of a `GrafPort/CGrafPort/GWorld`. If you are given a port and need to pull out the `BitMap/PixMap` to pass to a QuickDraw function that takes a pointer to a `BitMap`, then you should use `GetPortBitMapForCopyBits`.  While the name `GetPortBitMapForCopyBits` suggests that the function can only be used with `CopyBits`, there are a number of other APIs in QuickDraw that have `BitMap` pointers for parameters but can take `PixMap` pointers as well. `CopyMask` and `CopyDeepMask` are two examples. |

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
