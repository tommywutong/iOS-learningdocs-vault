---
title: Problems with Panning and Zooming
apple_id: DTS10002053
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/qtvr/qtvr09.html
archived_at: '2026-07-18T02:38:50.779174Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Virtual Reality](https://developer.apple.com/referencelibrary/QuickTime/idxVirtualReality-date.html)

|  |
| --- |
| Technical Q&A QTVR09Problems with Panning and Zooming |

|  |
| --- |
| Q We are having a problem with panning and zooming. We defined a quality level of 0, which is defined as: pan/zoom interactively at low quality, and do a high-quality update when the user stops panning or zooming. When we use quality 0, all updates happen at quality 4. All interactive activity is at quality 1, except for the final "high-quality update". However, if we use quality 1, everything is at quality 1, and there is no "high-quality update" when we've finished panning or zooming. What's causing this?   A The default value for quality is 0, so at the beginning, the speed is relatively quick. If you change the quality level when you move between nodes (to 4, for example), all panning and zooming that takes place after that is at quality 4, and is quite slow.   Q I am creating objects in StrataStudio Pro, and I'm having problems turning them into navigable movies. I make the movies at 12fps, and each camera shot is three seconds long, so there are 36 shots per camera shot. I use Adobe Premier to compile all the shots into one QuickTime movie to be opened in the navigator. When I view the movie, some of the frames are duplicated.   A Adobe Premiere may be forcing the individual movies to a different time base (30fps, for example), thus adding duplicated frames.   [Jun 01 1995] |

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
