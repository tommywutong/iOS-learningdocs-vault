---
title: Setting the movie background color
apple_id: DTS10002023
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-12'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb53.html
archived_at: '2026-07-18T02:38:49.413643Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Movie Basics](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxMovieBasics-date.html) >

|  |
| --- |
| Technical Q&A QTMTB53Setting the movie background color |

|  |
| --- |
| ---   Q: I am creating a movie with multiple video tracks of different sizes and aspect ratios. Currently, QuickTime is displaying the parts of the movie outside of the current track's display region in white. Is there a way of giving the entire movie a background color (e.g, black)?  A: Yes. You can simply create another track with a duration equal to the movie duration, and set the track layer value for this track higher than any of the other movie tracks. Then, when the movie is played, the other movie tracks will draw over the top of the background track (because the background track has a higher layer value) and any uncovered areas will show the black background track.  Note that this background track could be a video track consisting of a single background image whose duration is the same as the movie. You need not create a video track consisting of a number of identical frames whose durations sum to the entire movie duration. [Aug 16 1999] |

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
