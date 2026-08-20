---
title: How to Compute Data Rate for QuickTime Movies
apple_id: DTS10002016
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb46.html
archived_at: '2026-07-18T02:38:49.043647Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB46How to Compute Data Rate for QuickTime Movies |

|  |
| --- |
| Q How do I compute the data rate for QuickTime movies? Is this rate stored somewhere in the QuickTime movie?   A QuickTime is a time-based sample media. In other words, various samples are organized on a track and are played using a uniform time clock. Typically, in the case of video, one sample equals one frame; in the case of sound and other media, this 1:1 relationship does not necessarily hold. Additionally, none of the video samples in a continuous stream are exactly the same size, even if in practical terms this is often assumed. QuickTime always tries to synchronize video and sound. If the CPU does not have enough cycles to play back samples, the video samples are sacrificed for a period, and, in the worst case, sound samples may also be skipped to the next anchor point (a key frame).  There are two aspects to measuring the rate of samples, one based on a static estimation of the duration of the movie and the amount of video samples (frames), and the other based on when the movie is played back.  In the first case, you can make a quick estimate by assuming that all video samples are of equal duration, then taking the duration of the movie and dividing it by the duration of the first sample, yielding the number of video samples present per one second unit.  Here's a code snippet showing this technique:   ``` framecount = GetMovieDuration(theMovie)/GetDurationofFirstMovieSample(theMovie, VideoMediaType);  pascal TimeValue GetDurationOfFirstMovieSample(Movie theMovie, OSType theMediaType) {     OSErr             anErr = noErr;     TimeValue        interestingDuration = 0;     short            timeFlags = nextTimeMediaSample+nextTimeEdgeOK;      GetMovieNextInterestingTime(theMovie, timeFlags, (TimeValue)1, &theMediaType,     0, fixed1, NULL, &interestingDuration);     anErr = GetMoviesError(); DebugAssert(anErr == noErr);      return interestingDuration; } ```   If you want the exact number of frames, you need to parse each one using GetMovieNextInterestingTime (or any of its variants), find out the duration of each sample and its starting point, and use this information to calculate the frame rate.  Note that when you digitize, and you specify the frame rate, you will most likely create similarly-sized video samples.  In the second case, to create a dynamic testing of frames displayed, install a MovieDrawingCompleteProc that is triggered every time a frame is drawn. In this way you can keep a counter of how many frames are drawn per time unit. Note that if end user information is drawn too often, the results will be skewed. Refer to [Technote QT 04](https://developer.apple.com/library/archive/technotes/qt/qt_04.html) for more information about how to install a MovieDrawingCompleteProc. [Sep 15 1995] |

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
