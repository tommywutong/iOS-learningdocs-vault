---
title: How do I decompress individual frames into an offscreen?
apple_id: DTS10002027
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-11'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb57.html
archived_at: '2026-07-18T02:38:49.521998Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Movie Basics](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxMovieBasics-date.html) >

|  |
| --- |
| Technical Q&A QTMTB57How do I decompress individual frames into an offscreen? |

|  |  |
| --- | --- |
| ---   Q: How can you scale and decompress individual frames of a video track into an offscreen RGB buffer so the pixels can be further manipulated?  A: The code snippets below show how a single frame can be drawn into a `GWorld`. Once the `GWorld` is created, use `SetMovieGWorld()` to specify the `GWorld` you would like the movie to draw into. Use `GetMovieNextInterestingTime()` to find the places where the movie will display a new video sample (frame), then set the movie position using `SetMovieTimeValue()`. The time value passed to `SetMovieTimeValue()` is returned by `GetMovieNextInterestingTime()`. Finally, task the movie using `MovieTask()`, which performs the actual drawing into your `GWorld`. You will end up with the `GWorld` containing the frame pixels ready for manipulation.  `GWorlds` are very flexible and can contain pixel formats other than RGB. For more information regarding `GWorlds` and drawing, refer to the following technical documentation:   - [http://developer.apple.com/documentation/quicktime/qtdevdocs/   INMAC/MACWIN/imOffGraphWorlds.1.htm](https://developer.apple.com/documentation/quicktime/qtdevdocs/INMAC/MACWIN/imOffGraphWorlds.1.htm) - [http://developer.apple.com/quicktime/icefloe/dispatch008.html](https://developer.apple.com/quicktime/icefloe/dispatch008.html) - [http://developer.apple.com/quicktime/icefloe/dispatch016.html](https://developer.apple.com/quicktime/icefloe/dispatch016.html) - [http://developer.apple.com/technotes/tn/tn1182.html](https://developer.apple.com/library/archive/technotes/tn/tn1182.html) - [http://developer.apple.com/documentation/mac/QuickDraw/QuickDraw-302.html](https://developer.apple.com/documentation/mac/QuickDraw/QuickDraw-302.html)   The full sample application called `VideoFrameToGWorld` can be found on the QuickTime Sample Code page:   - [http://www.developer.apple.com/samplecode/Sample_Code/QuickTime.htm](https://developer.apple.com/samplecode/Sample_Code/QuickTime.htm)      |  | | --- | | ```     /* Globals */  GWorldPtr gSrcGWorld = NULL; Movie gMovie = NULL;      /* set current time value to beginning of the movie */ TimeValue gMovieTime = 0; UInt32 gFrameCount = -1; UInt32 gFrameNumber = 0;        /* CountThemFrames     Count the number of video "frames" in the movie by stepping     through all of the video "interesting times", or in other words,     the places where the movie displays a new video sample. The time     between these interesting times is not necessarily constant. */  void CountThemFrames( void ) {     OSType whichMediaType = VIDEO_TYPE;     short flags = nextTimeMediaSample + nextTimeEdgeOK;     TimeValue duration;     TimeValue theTime = 0;      while (theTime >= 0) {         gFrameCount++;         GetMovieNextInterestingTime(gMovie,                             flags,                             1,                             &whichMediaType,                             theTime,                             0,                             &theTime,                             &duration);          /* after the first interesting time, don't include         the time we are currently at. */          flags = nextTimeMediaSample;     } }        /* MakeGWorld     Get the bounding rectangle of the movie and create a     32-bit gworld with those dimensions.  This GWorld will     be used for rendering movie frames into. */  void MakeGWorld( void ) {     Rect srcRect;     Rect portRect;     OSErr err = noErr;          /* get the movies dimensions */     GetMovieBox(gMovie,&srcRect);      err = NewGWorld(&gSrcGWorld,                 k32ARGBPixelFormat,                 &srcRect,                 NULL,                 NULL,                 0);     BailError(err);          /* make sure to lock the PixMap */     LockPixels(GetGWorldPixMap(gSrcGWorld));          /* erase */     SetGWorld(gSrcGWorld,NULL);     GetPortBounds(gSrcGWorld, &portRect);     EraseRect(&portRect);          /* tell the movie to draw into the GWorld */     SetMovieGWorld(gMovie, gSrcGWorld,  GetGWorldDevice(gSrcGWorld));  bail:     return; }         /* NextFrame     Get the next frame of the movie, set the movie time     for that frame, then task the movie which will draw     the frame to the GWorld.  Modify the movie matrix so     the next frame will be rotated just for fun, and     finally, draw the frame number on top of the image     and inval the window rect. */  void NextFrame( void ) {     if ( gFrameNumber < gFrameCount ) {          TimeValue duration;              /* get the next frame of the source movie */         short   flags = nextTimeMediaSample;         OSType  whichMediaType = VIDEO_TYPE;              /* if this is the first frame, include the             frame we are currently on */         if (gFrameNumber == 0)             flags |= nextTimeEdgeOK;              /* skip to the next interesting time and             get the duration for that frame */         GetMovieNextInterestingTime(gMovie,                             flags,                             1,                             &whichMediaType,                             gMovieTime,                             0,                             &gMovieTime,                             &duration);              /* set the time for the frame and give             time to the movie toolbox */         SetMovieTimeValue(gMovie,gMovieTime);              /* tasking the movie does the actual draw */         MoviesTask(gMovie,0);     }      /* You now have pixels you can     play with in the GWorld! */ } ``` |     [Apr 24 2000] |

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
