---
title: Preroll Movies
apple_id: DTS10002012
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb42.html
archived_at: '2026-07-18T02:38:48.819897Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB42Preroll Movies |

|  |
| --- |
| It is of utmost importance that you preroll your movies using the PrerollMovie call. Failing to do so will introduce playback problems, especially when the movie starts. PrerollMovie will fill caches and buffers optimally to prevent initial playback stuttering.  Note that StartMovie will preroll the movie; also, the standard controller prerolls the movie whenever the user starts a movie using the keyboard or the mouse. In these situations, a possible second PrerollMovie call is redundant and will waste time and resources.  In all other cases, you should preroll the movie. For instance, it is your responsibility to call PrerollMovie if you are using SetMovieRate, or if you use McDoAction with mcActionPlay and a rate. Here's an example of how to use PrerollMovie:   ``` OSErr DoPrerollMovie(Movie    theMovie) {     TimeValue         aTimeValue;     TimeValue         aMovieDur;     Fixed             aPreferredRate;     OSErr            anErr = noErr;      aTimeValue     = GetMovieTime(theMovie, nil);     aMovieDur    = GetMovieDuration(theMovie);     aPreferredRate = GetMoviePreferredRate(theMovie);      anErr = PrerollMovie(theMovie, aTimeValue, aPreferredRate);      return anErr; } ```  [May 01 1995] |

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
