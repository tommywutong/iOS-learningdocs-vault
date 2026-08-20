---
title: Creating track references when editing movies
apple_id: DTS10002031
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-11'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb61.html
archived_at: '2026-07-18T02:38:49.813609Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Movie Basics](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxMovieBasics-date.html) >

|  |
| --- |
| Technical Q&A QTMTB61Creating track references when editing movies |

|  |
| --- |
| ---   Q: I'm using the `InsertTrackSegment` function to copy a track from one movie to another. However, I don't want to actually copy the track media data itself - I want to simply create a reference to the track media in the original movie. Is this possible?  A: If you explicitly do \*not\* bracket the `InsertTrackSegment` call with calls to `BeginMediaEdits/EndMediaEdits`, the track media data is not copied. Instead, a reference to the track media is made. [Sep 05 2000] |

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
