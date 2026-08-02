---
title: PBLockRange with a zero-length range
apple_id: DTS10001199
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-11-22'
source_url: https://developer.apple.com/library/archive/qa/fl/fl13.html
archived_at: '2026-07-18T02:29:29.138731Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [File Management](https://developer.apple.com/library/archive/technicalqas/Carbon/idxFileManagement-date.html) >

|  |
| --- |
| Technical Q&A FL13PBLockRange with a zero-length range |

|  |
| --- |
| ---   Q Why do I keep getting the `afpRangeOverlap` (-5021) error although the file is not ranged-locked?  A The most likely culprit might be that you are doing a range-lock/unlocked-wrapped `PBWrite()` with a length determined programmatically. If this computed length happens to be zero at a specific offset, then any further attempt to call `PBLockRange` which would include that offset will return the `afpRangeOverlap` error.  This is a known bug [2295724] which has yet to be fixed. A valid, now and in the future, workaround is to simply test the computed length against zero and to not call the sequence in that case. |

#### [Nov 22 1999]

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
