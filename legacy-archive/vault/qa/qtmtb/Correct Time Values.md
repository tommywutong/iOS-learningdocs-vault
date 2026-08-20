---
title: Correct Time Values
apple_id: DTS10002002
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb32.html
archived_at: '2026-07-18T02:38:48.269336Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB32Correct Time Values |

|  |
| --- |
| Q How do I determine the correct time values to pass to `GetMoviePict` to get all the sequential frames of a QuickTime movie?   A The best way to determine the correct time to pass to get movie frames is to call the `GetMovieNextInterestingTime` routine repeatedly. Note that the first time you call `GetMovieNextInterestingTime`, its `flags` parameter should have a value of `nextTimeMediaSample`+`nextTimeEdgeOK` to get the first frame. For subsequent calls, the value of `flags` should be `nextTimeMediaSample`, and the `whichMediaTypes` parameter should include only tracks with visual information, `VisualMediaCharacteristic`, or "eyes." Check the Movie Toolbox chapter of the QuickTime documentation for details about the `GetMovieNextInterestingTime` call. [May 01 1995] |

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
