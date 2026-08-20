---
title: MCSetClip and Clipping with the Movie Controller
apple_id: DTS10001988
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb18.html
archived_at: '2026-07-18T02:38:47.788899Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB18MCSetClip and Clipping with the Movie Controller |

|  |
| --- |
| Q I use SetMovieDisplayClipRgn to set my movie clip, but the movie doesn't obey my clipping. Does the movie controller component ignore this clipping?   A The controller uses the display clip for its own purposes, such as for badges. If you want to do clipping with the movie controller you must use MCSetClip. MCSetClip takes two regions. The first clips both the movie and the controller. The second clips just the movie, and is equivalent to the movie display clip. If both clips are set, the controller does the right thing and merges them as appropriate. If you don't want one or the other of the clips, set them to zero. In general, if you are going to do something to a movie that is attached to a controller you must either do it through the controller, using the action calls, or you must call MCMovieChanged. Otherwise, the controller would need to constantly poll the movie to see if its state changed. Clearly this would be slow. [May 01 1995] |

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
