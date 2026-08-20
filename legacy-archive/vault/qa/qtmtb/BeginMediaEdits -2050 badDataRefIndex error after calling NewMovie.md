---
title: BeginMediaEdits -2050 badDataRefIndex error after calling NewMovie
apple_id: DTS10002028
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-10'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb58.html
archived_at: '2026-07-18T02:38:49.569125Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Movie Basics](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxMovieBasics-date.html) >

|  |
| --- |
| Technical Q&A QTMTB58BeginMediaEdits -2050 badDataRefIndex error after calling NewMovie |

|  |  |  |
| --- | --- | --- |
| ---   Q: I have created a movie with the `NewMovie` function. After adding the tracks and the media using the `NewMovieTrack` and `NewTrackMedia` functions, I'm calling `BeginMediaEdits` to start a media editing session. However, `BeginMediaEdits` returns the `-2050 badDataRefIndex` error code. I have checked the movie, track and media, and all are valid. What am I doing wrong?  A: What's happening is when you create a movie from "nothing," as with `NewMovie`, the movie does not have a containing data reference (for example, if you call `NewMovieFromFile`, the containing data reference is an alias to the movie file on disk). Therefore, when you attempt to add sample data to the media with `BeginMediaEdits`, QuickTime can't do this because there's no data reference. You can solve this problem by specifying a data reference when you create your media with the `NewTrackMedia` function. In the sample below, we show how to create a handle data reference (you can get away with specifying a 0-length handle for the reference). Now, when `BeginMediaEdits` is called to begin the media editing session, QuickTime will have a data reference to write data to:   |  |  | | --- | --- | | __Listing 1__. Creating a handle data reference to pass to the `NewTrackMedia` function.    |  | | --- | | ``` OSType    dataRefType; Handle    dataRef = nil; Handle    hMovieData = NewHandle(0);  // Construct the Handle data reference err = PtrToHand( &hMovieData, &dataRef, sizeof(Handle));  theMedia = NewTrackMedia (theTrack,                           VideoMediaType,                           600, // pass an appropriate time scale                                // for your media here                           dataRef,                           HandleDataHandlerSubType); . . . // clean up when we are done with the // media editing session DisposeHandle(hMovieData); DisposeHandle(dataRef); ``` | |  [Sep 05 2000] |

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
