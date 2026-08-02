---
title: qtstreamsplicer.win
apple_id: DTS10001056
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtstreamsplicer.win/Listings/QTStreamSplicer_h.html
archived_at: '2026-07-26T19:53:08.403096Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtstreamsplicer.win](qtstreamsplicer.win.md)


[Next](Document%20Revision%20History.md)[Previous](QTStreamSplicer.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTStreamSplicer.h

```c
//////////
//
//  File:       QTStreamSplicer.c
//
//  Contains:   Code to splice a still frame onto a streamed movie.
//
//  Written by: Dan Crow
//  Revised by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      05/18/99    rtm     first file from Dan Crow
//
//
//
//////////

//////////
//
// header files
//
//////////

#include "ComApplication.h"

//////////
//
// constants
//
//////////

#define kSaveSplicePrompt           "Save spliced movie file as:"
#define kSaveSpliceFileName         "Spliced.mov"

#define kSpliceOntoDialogID         2000
#define kSpliceOverDialogID         2001

#define kSpliceButtonDone           1
#define kSelfContainedCheckbox      2
#define kSpliceScaleCheckbox        3
#define kSpliceDuration             4

#define kSpliceWidth                4
#define kSpliceHeight               5

#define kOneSecond                  600

//////////
//
// function prototypes
//
//////////

OSErr                       QTSplicer_SpliceImageOntoStream (void);
OSErr                       QTSplicer_SpliceImageOverStream (void);
OSErr                       QTSplicer_CreateSplicedOntoMovie (FSSpec theImageSpec, FSSpec theMovieSpec, Movie theSplicedMovie, Boolean isScaleImage, Boolean isSelfContained, long theImageDuration);
OSErr                       QTSplicer_CreateSplicedOverMovie (FSSpec theImageSpec, FSSpec theMovieSpec, Movie theSplicedMovie, Boolean isScaleImage, Boolean isSelfContained, long theImageHeight, long theImageWidth);
Boolean                     QTSplicer_FileContainsStream (FSSpec theMovieFile);
OSErr                       QTSplicer_SetSelectionTimes (MovieController theController, TimeValue theTime1, TimeValue theTime2);
OSErr                       QTSplicer_SetCurrentTime (MovieController theController, TimeValue theTime);
OSErr                       QTSplicer_AddVideoTrackFromGWorld (Movie *theMovie, GWorldPtr theGW, short theWidth, short theHeight, long theImageDuration);
```

[Next](Document%20Revision%20History.md)[Previous](QTStreamSplicer.c.md)

