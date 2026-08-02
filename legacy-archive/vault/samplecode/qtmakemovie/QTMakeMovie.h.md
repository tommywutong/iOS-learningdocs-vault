---
title: qtmakemovie
apple_id: DTS10000784
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtmakemovie/Listings/QTMakeMovie_h.html
archived_at: '2026-07-26T19:52:33.926079Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtmakemovie](qtmakemovie.md)


[Next](Document%20Revision%20History.md)[Previous](QTMakeMovie.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTMakeMovie.h

```c
//////////
//
//  File:       QTMakeMovie.c
//
//  Contains:   QuickTime movie making sample code.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 2000 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      03/09/00    rtm     first file
//
//////////

//////////
//
// header files
//
//////////

#include "ComApplication.h"

#if TARGET_OS_MAC
#include "MacFramework.h"
#endif

#if TARGET_OS_WIN32
#include "WinFramework.h"
#endif

//////////
//
// constants
//
//////////

#define kVideoTimeScale         600                         // 600 units per second
#define kVideoFrameDuration     kVideoTimeScale/10          // each frame is 1/10 second
#define kVideoTrackHeight       202
#define kVideoTrackWidth        152

#define kNewMoviePrompt         "Save New Movie as:"
#define kNewMovieFileName       "untitled.mov"

#define kPixelDepth             32                          // 32 bits per pixel
#define kNumVideoFrames         100

#define kPictureID              128
#define kPICTFileHeaderSize     512

//////////
//
// function prototypes
//
//////////

OSErr                       QTMM_CreateVideoMovie (void);
static OSErr                QTMM_AddVideoSamplesToMedia (Media theMedia, short theTrackWidth, short theTrackHeight);
static void                 QTMM_DrawFrame (short theTrackWidth, short theTrackHeight, long theNumSample, GWorldPtr theGWorld);
```

[Next](Document%20Revision%20History.md)[Previous](QTMakeMovie.c.md)

