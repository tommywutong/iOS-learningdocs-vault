---
title: Functions that Modify Movie Properties, QuickTime Track, and Movie Sound Volume
apple_id: DTS10002009
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb39.html
archived_at: '2026-07-18T02:38:48.643204Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB39Functions that Modify Movie Properties, QuickTime Track, and Movie Sound Volume |

|  |
| --- |
| Q What do the values of a movie's or track's volume represent? Is there any way to make a track louder?   A The volume is described as a small fract 8:8 and its values go from -1 to 1,with negative values as placeholders. The maximum volume you can get is `0x0100` with the minimum being 0 (or any negative value). The advantage of using negative volumes is that you can turn off sound while maintaining the level of volume. For example, -1 and 0 both equate to no volume, but the -1 implies that 1 should be the volume when sound is turned back on, whereas the 0 does not. The volume for a track is scaled to the movie's volume, and the movie's volume is scaled to the value the user specifies for the speaker volume using the Sound control panel. This means that the movie volume represents the maximum loudness of any track in the movie.  Note that starting with Sound Manager 3.0 you are able to increase the loudness above the maximum level using the Shift key. [May 01 1995] |

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
