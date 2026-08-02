---
title: Accessing Decompressed Images
apple_id: DTS10001997
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb27.html
archived_at: '2026-07-18T02:38:48.009085Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB27Accessing Decompressed Images |

|  |
| --- |
| Q Is there a mechanism that would allow us to access each decompressed image prior to display during playback so that we can manipulate the image data and then hand it back for display?   A QuickTime 1.6.1 provides a function called `SetTrackGWorld`. `SetTrackGWorld` lets you force a track to draw into a particular `GWorld`, which can be different from that of the entire movie. After the track is drawn, it calls your transfer procedure to copy the track to the actual movie `GWorld`. When your transfer procedure is set, the current `GWorld` is set to the correct destination. You could also install a transfer procedure, and set the `GWorld` to nil. When you do this, your transfer procedure is called only as a notification that the track has drawn and that no transfer is taking place. You can also manipulate the image inside your transfer procedure. Note that calling resource-intensive or time-consuming routines in your transfer procedure may have an adverse effect on playback performance.  Here's an example of a transfer procedure that keeps a counter of the number of times it has been called and displays this number in the top-left corner of the movie:   ``` pascal OSErr myTrackTransferProc(Track t, long refCon) {      TransferDataHandle        myTDH = (TransferDataHandle)refCon ;     GrafPtr            theNewWorld ;     GrafPtr            movieGWorld ;     PixMapHandle            offPixMap ;     Rect                movieBox ;     static    long            index = 1 ;     CGrafPtr            savedWorld ;     GDHandle            savedDevice ;     Str255                theString ;        movieGWorld = (GrafPtr)((**myTDH).movieGWorld) ;     theNewWorld = (GrafPtr)((**myTDH).trackGWorld) ;     movieBox    = (**myTDH).movieRect ;      offPixMap = GetGWorldPixMap( (GWorldPtr)theNewWorld ) ;     (void) LockPixels( offPixMap ) ;      GetGWorld( &savedWorld, &savedDevice );     SetGWorld( (CGrafPtr)theNewWorld, nil ) ;      MoveTo ( 15, 15 );     NumToString ( index++, theString );     DrawString ( theString );      // copy the image from the offscreen port     // into the movies port      SetGWorld( savedWorld, savedDevice ) ;      CopyBits(     &theNewWorld->portBits,                 &movieGWorld->portBits,                 &theNewWorld->portRect,                 &movieBox,                 srcCopy,                 nil ) ;      (void) UnlockPixels( offPixMap ) ; }   //--------------------------------------------------------------------- // define a structure to hold all the information we need in the transfer // proc.  typedef struct {     GWorldPtr    movieGWorld ;     GWorldPtr    trackGWorld ;     Rect        movieRect ; } TransferData, *TransferDataPtr, **TransferDataHandle ;  //This has the original movie gWorld, the one we created for the track and a rect // describing the movie.  You can set a movie up to use this in the following way:      TransferDataHandle     myTDH = (TransferDataHandle)NewHandle( sizeof( TransferData )) ;     Track        aTrack = GetFirstTrackOfType( aMovie, VideoMediaType ) ;     short        trackDepth = GetFirstVideoTrackPixelDepth( aMovie ) ;      if( myTDH == nil || aTrack == nil || trackDepth < 0)         return ;      GetTrackDimensions( aTrack, &width, &height ) ;      trackDimensions.right = Fix2Long( width );     trackDimensions.bottom = Fix2Long( height );      // create the movie gWorld     theErr = NewGWorld( &theNewWorld, trackDepth, &trackDimensions, nil,     theNewWorldDevice, 0L ) ;     CheckError( theErr, "\pCall to NewGWorld failed" );      GetMovieGWorld( aMovie, &movieGWorld, nil ) ;      (**myTDH).movieGWorld = movieGWorld ;     (**myTDH).trackGWorld = theNewWorld ;      GetMovieBox( aMovie, &movieBox ) ;     (**myTDH).movieRect = movieBox ;      SetTrackGWorld( aTrack, (CGrafPtr)theNewWorld, nil, myTrackTransferProc,      (long)myTDH ) ; ```  [May 01 1995] |

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
