---
title: grayishTextOr and Mac OS 8.5
apple_id: DTS10001912
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-12-07'
source_url: https://developer.apple.com/library/archive/qa/qd/qd59.html
archived_at: '2026-07-18T02:38:38.633493Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/Carbon/idxGraphicsImaging-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Graphics & Imaging](https://developer.apple.com/referencelibrary/Carbon/idxGraphicsImaging-date.html)

|  |
| --- |
| Technical Q&A QD59grayishTextOr and Mac OS 8.5 |

|  |
| --- |
| ---   Q: Under Mac OS 8.5, text that is drawn using `TextMode(grayishTextOr)` is never actually drawn. What's wrong and what can I do to fix it?  A: Mac OS 8.5 doesn't properly check to see if the current port is a `GrafPort` or a `CGrafPort`. Gray text will draw correctly to a `CGrafPort`, but does not appear when drawn to an old `GrafPort`.  The best solution to this problem is to migrate your code to always use color windows and `CGrafPorts`.  However, you can simulate the gray text by painting over the text's area with a gray pattern in `patBic` mode. |

#### [Dec 07 1998]

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
