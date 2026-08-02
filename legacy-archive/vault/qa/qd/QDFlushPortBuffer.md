---
title: QDFlushPortBuffer
apple_id: DTS10001918
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-11-08'
source_url: https://developer.apple.com/library/archive/qa/qd/qd65.html
archived_at: '2026-07-18T02:38:39.025838Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Porting](https://developer.apple.com/library/archive/technicalqas/Porting/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Porting/idxCarbon-date.html) >

|  |
| --- |
| Technical Q&A QD65QDFlushPortBuffer |

|  |
| --- |
| ---     Q: I ported my application to Carbon on Mac OS X and my windows don't always update properly. My drawing code hasn't changed but my windows won't display their new contents until I call `WaitNextEvent`. How can I get my windows to update outside of the normal event loop?  A: Mac OS X windows are double-buffered by default. See Technote 2003, [Moving your code to Mac OS X](https://developer.apple.com/technotes/tn/tn2003.html) for more details. If you draw into a window and want those changes to appear on the screen immediately (before the next call to `WaitNextEvent`) then you need to call `QDFlushPortBuffer` to flush the updated portion to the screen. |

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
