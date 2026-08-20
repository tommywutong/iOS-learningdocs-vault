---
title: soundconverter.win
apple_id: DTS10000921
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/soundconverter.win/Listings/SoundConverter_h.html
archived_at: '2026-07-26T19:52:53.338864Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [soundconverter.win](soundconverter.win.md)


[Next](Document%20Revision%20History.md)[Previous](SoundConverter.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# SoundConverter.h

```c
//////////
//
//  File:       SoundConverter.h
//
//  Contains:   Sound format conversion sample code.
//
//  Written by: Bob Aron
//  Revised by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      07/01/99    rtm     first file from Bob Aron; conversion to personal coding style; updated to latest headers
//
//////////

//////////
//
// header files
//
//////////

#ifndef __MACERRORS__
#include <MacErrors.h>
#endif

#ifndef __COMPONENTS__
#include <Components.h>
#endif

#ifndef __FIXMATH__
#include <FixMath.h>
#endif

#ifndef __MOVIES__
#include <Movies.h>
#endif

#ifndef __MOVIESFORMAT__
#include <MoviesFormat.h>
#endif

#ifndef __QUICKTIMECOMPONENTS__
#include <QuickTimeComponents.h>
#endif

#ifndef __SOUND__
#include <Sound.h>
#endif

#ifndef __STRINGS__
#include <Strings.h>
#endif

#ifndef _STRING_H
#include <string.h>
#endif

#ifndef __QTUtilities__
#include "QTUtilities.h"
#endif

#if TARGET_OS_MAC
#include "MacFramework.h"
#endif

#if TARGET_OS_WIN32
#include "WinFramework.h"
#endif

#if TARGET_OS_WIN32
#include <math.h>
#define double_t        double
#endif

#if TARGET_OS_MAC
    #ifndef __FP__
    #include <fp.h>
    #endif
#endif

//////////
//
// compiler macros
//
//////////

#define FailIf(cond, handler)                               \
    if (cond) {                                             \
        goto handler;                                       \
    }

#define FailWithAction(cond, action, handler)               \
    if (cond) {                                             \
        { action; }                                         \
        goto handler;                                       \
    }

//////////
//
// constants
//
//////////

#define kMaxBufferSize              (20*1024)                                   // the upper limit for the in and out conversion buffers
#define kSaveSoundPrompt            "Save sound movie file as:"
#define kSaveSoundFileName          "Sound.mov"
#define kConcertA                   440

//////////
//
// function prototypes
//
//////////

void                                SndConv_DriveAudioConversion (void);

OSErr                               SndConv_ConvertSomeUncompressedAudio (
                                                Handle theSourceHandle,
                                                SoundComponentData theSourceInfo,
                                                unsigned long theSourceTotalFrames,
                                                Handle theDestHandle,
                                                SoundComponentData theDestInfo,
                                                unsigned long *theDestFramesMoved,
                                                CompressionInfo *theDestCompInfo,
                                                Handle *theDestCompParams);

OSErr                               SndConv_CreateSoundMovie (
                                                Handle theDestAudioData,
                                                short theMovieRefNum,
                                                Movie theMovie,
                                                SoundComponentData theDestInfo,
                                                Handle *theDestCompParams,
                                                CompressionInfo theDestCompInfo,
                                                unsigned long theDestFrameCount);

OSErr                               SndConv_UncompressedSineWaveToHandle (
                                                Handle theData,
                                                SoundComponentData *theCompInfo,
                                                unsigned long *theTotalFrames);
```

[Next](Document%20Revision%20History.md)[Previous](SoundConverter.c.md)

