---
title: QuickTime Toolbox GetMovieTime Call
apple_id: DTS10002008
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb38.html
archived_at: '2026-07-18T02:38:48.582453Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB38QuickTime Toolbox GetMovieTime Call |

|  |
| --- |
| Q If a movie returns a point other than the start time, is it corrupt, or must I seek the start (i.e., SetTimeValue()) to ensure that I'm at the very beginning of the movie?   A The current time is saved in the movie header atom (see _Inside Mac: QuickTime_, page 4- 11). There is a utility called Dumpster in QT 1.6 (and on the QT 2.0 beta CD) that you can use to verify this. The resource type is 'mdhd'. To change the current time, call SetMovieTime (_Inside Mac:QuickTime_, page 2- 186) or call GoToBeginningOfMovie (_Inside Mac:QuickTime_, page 2- 113) to reposition a movie to play from its start.   [May 01 1995] |

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
