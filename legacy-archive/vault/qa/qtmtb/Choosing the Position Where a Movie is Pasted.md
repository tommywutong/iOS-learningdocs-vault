---
title: Choosing the Position Where a Movie is Pasted
apple_id: DTS10001996
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb26.html
archived_at: '2026-07-18T02:38:47.951528Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB26Choosing the Position Where a Movie is Pasted |

|  |
| --- |
| Q When a user pastes a movie into a movie controller movie, the added movie is inserted in the top left corner of the movie. Is there a way for the user to choose the position where the movie is pasted? If not, how can I give the movie controller or Movie Toolbox an offset to use rather than have the editing operations use the top left corner?   A When you paste a movie into a movie-controller movie, the movie controller calls `PasteMovieSelection` to insert the source movie. Since all the characteristics of the movie are inserted, the pasted movie is inserted in the top left corner of the movie-controller movie. There's no easy way to specify an offset directly to the movie controller. If you need to change the offset of the pasted movie, you have to modify the movie yourself after the paste using Movie Toolbox commands. Once you're done changing the movie, be sure to call `MCMovieChanged` so that the movie controller updates correctly. The actual modification is simple: call `GetTrackMatrix`, add your offset to the matrix, and call `SetTrackMatrix`. The only difficulty is in determining which tracks to modify, since the paste may either create a new track or use an existing one. We recommend doing this by gathering all track IDs before the paste, and then comparing them with the track IDs after the paste. Since most movies these days have just a few tracks, this shouldn't require much overhead, but be warned -- some movies do have a lot of tracks! To get the track information, call `GetMovieTrackCount` and `GetMovieIndTrack`.  Here's one last idea: If you don't mind changing the source movie, offset the source movie before the paste as an alternative method. [May 01 1995] |

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
