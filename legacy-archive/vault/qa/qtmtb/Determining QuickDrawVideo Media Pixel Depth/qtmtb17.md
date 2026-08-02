---
title: Determining QuickDrawVideo Media Pixel Depth
apple_id: DTS10001987
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb17.html
archived_at: '2026-07-26T19:53:35.185637Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Document[close button](javascript:closeWatermark())

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB17Determining QuickDrawVideo Media Pixel Depth |

|  |
| --- |
| Q How do I get the pixel depth of the QuickTime video media for a given track?   A To find the video media pixel depth, retrieve the media's image description handle. You can use GetMediaSampleDescription to get it, but this routine needs both the video media and the track's index number. It's not obvious, but a media's type is identified by its media handler's type. Thus, you can walk through a movie's tracks by using its indexes until you find video media, at which point you have both the track index and video media. The following sample code does the trick:   ```  Media GetFirstVideoMedia(Movie coolMovie, long *trackIndex) {   Track    coolTrack = nil;   Media    coolMedia = nil;   long    numTracks;   OSType  mediaType;   numTracks = GetMovieTrackCount(coolMovie);   for (*trackIndex=1; *trackIndex<=numTracks; (*trackIndex)++) {     coolTrack = GetMovieIndTrack(coolMovie, *trackIndex);     if (coolTrack) coolMedia = GetTrackMedia(coolTrack);     if (coolMedia) GetMediaHandlerDescription(coolMedia,       &mediaType, nil, nil);     if (mediaType = VideoMediaType) return coolMedia;   }   *trackIndex = 0;  // trackIndex can't be 0   return nil;      // went through all tracks and no video }  short GetFirstVideoTrackPixelDepth(Movie coolMovie) {   SampleDescriptionHandle imageDescH =     (SampleDescriptionHandle)NewHandle(sizeof(Handle));   long    trackIndex = 0;   Media    coolMedia = nil;   coolMedia = GetFirstVideoMedia(coolMovie, &trackIndex);   if (!trackIndex || !coolMedia) return -1;  // we need both   GetMediaSampleDescription(coolMedia, trackIndex, imageDescH);   return (*(ImageDescriptionHandle)imageDescH)->depth; }   ```   Note that QuickTime 2.0 has a new function called GetMovieIndTrackType that does most of the work described in the sample. GetMovieIndTrackType lets you search for all of a movie's tracks that share a given media type or media characteristic. See the QuickTime 2.0 SDK documentation for more details. [May 01 1995] |

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
