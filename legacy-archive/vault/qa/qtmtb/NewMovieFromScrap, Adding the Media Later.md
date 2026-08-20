---
title: NewMovieFromScrap, Adding the Media Later
apple_id: DTS10001980
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb10.html
archived_at: '2026-07-18T02:38:47.679087Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB10NewMovieFromScrap, Adding the Media Later |

|  |
| --- |
| Q When my application creates a new media (of text type in this case) for a new track in a movie created with NewMovieFromScrap, the dataRef and dataRefType should be set to nil, according to the QuickTime documentation. The problem is that later I want to edit that media (adding a text sample to it, for example), but BeginMediaEdits returns the noDataHandler error (no data handler found). I assume I can get around that by first saving the movie to a file, but this seems slimy since the movie won't end up on disk in the end. Any suggestions for a better approach?   A You're correct -- BeginMediaEdits complains if the movie has been created with NewMovieFromScrap. Unfortunately, BeginMediaEdits doesn't think memory-based movies are on a media that will support editing. The workaround is to store the movie in a temporary file until you're finished editing it. When you call NewTrackMedia, pass an alias to a new file in the dataRef parameter instead of nil. Passing nil (the usual approach) indicates that the movie's default data reference should be used, but because your movie came from the scrap and not a file, it has no data reference -- hence the error you're getting. By the way, using the handle data handler in QuickTime 2.0 you can create a movie entirely in memory. [May 01 1995] |

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
