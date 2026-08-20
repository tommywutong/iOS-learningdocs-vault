---
title: Allocate and Disk Full Error
apple_id: DTS10001198
resource_type: QA
platform: macOS
topic: Data Management
technology: CoreServices
published: '2011-07-10'
source_url: https://developer.apple.com/library/archive/qa/fl/fl12.html
archived_at: '2026-07-18T02:29:29.097050Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [File Management](https://developer.apple.com/library/archive/technicalqas/Carbon/idxFileManagement-date.html) >

|  |
| --- |
| Technical Q&A FL12Allocate and Disk Full Error |

|  |
| --- |
| ---   Q: When my application attempts to save a document onto some AFP volumes, it reports that the document could not be saved because the disk was full, even though there's plenty of free space. (In fact, Finder displays a size for the volume that is much larger than it should be, but I've seen servers play this kind of trick before, and it hasn't caused any problems like this.) Further investigation shows that my app's call to `Allocate` is failing. Why?  A: AFP servers do not implement `Allocate`; the AppleShare client does. It decides whether the `Allocate` call should succeed or fail based on the space available on the disk. Some versions of some third-party AFP servers erroneously report the space available in such a way as to confuse AppleShare client into failing the request. Many calls to `Allocate` are done for the sake of optimization only. If this is the case for your code, simply ignore the return value of `Allocate` and continue saving the document. If not, the best action for you to take may be to recommend to your users that they upgrade their AFP server to a later version which does not have this bug. |

#### [Jul 21 1999]

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
