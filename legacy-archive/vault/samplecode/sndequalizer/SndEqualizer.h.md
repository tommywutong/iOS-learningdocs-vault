---
title: sndequalizer
apple_id: DTS10000918
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/sndequalizer/Listings/SndEqualizer_h.html
archived_at: '2026-07-26T19:52:52.293218Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [sndequalizer](sndequalizer.md)


[Next](Document%20Revision%20History.md)[Previous](SndEqualizer.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# SndEqualizer.h

```c
//////////
//
//  File:       SndEqualizer.c
//
//  Contains:   Sample code for displaying a graphic equalizer (a la QuickTime Player).
//
//  Written by: Tim Monroe
//
//  Copyright:  © 2000 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      09/28/99    rtm     first file
//
//////////

#pragma once

//////////
//
// header files
//
//////////

#ifndef __MOVIES__
#include <Movies.h>
#endif

#ifndef _STRING_H
#include <string.h>
#endif

#ifndef __MEDIAHANDLERS__
#include <MediaHandlers.h>
#endif

#ifndef __MACWINDOWS__
#include <MacWindows.h>
#endif

#if TARGET_OS_MAC
#include "MacFramework.h"
#endif

#if TARGET_OS_WIN32
#include "WinFramework.h"
#endif

#include "ComApplication.h"

//////////
//
// constants
//
//////////

#define kSndEqResID             1000    // resource ID of DLOG resource to contain the equalizer
#define kSndEqUserItemIndex     1       // index of user item we draw the equalizer into
#define kSndEqTickThreshold     5       // the number of ticks we wait before updating display

// the band frequencies (these are the same bands used by QuickTime Player)
#define kBandFreq0              0x00C80000;         // 00200 Hz
#define kBandFreq1              0x01900000;         // 00400 Hz
#define kBandFreq2              0x03200000;         // 00800 Hz
#define kBandFreq3              0x06400000;         // 01600 Hz
#define kBandFreq4              0x0C800000;         // 03200 Hz
#define kBandFreq5              0x19000000;         // 06400 Hz
#define kBandFreq6              0x32000000;         // 12800 Hz
#define kBandFreq7              0x52080000;         // 21000 Hz

#define kSndEqNumCmdsInQueue    4                   // number of commands in a sound channel queue

//////////
//
// function prototypes
//
//////////

OSErr                           SndEq_Init (void);
OSErr                           SndEq_Stop (void);
Handle                          SndEq_InitWindowData (WindowObject theWindowObject);
OSErr                           SndEq_DumpWindowData (WindowObject theWindowObject);
OSErr                           SndEq_ShowDialog (void);
OSErr                           SndEq_HideDialog (void);
OSErr                           SndEq_ToggleDialog (void);
OSErr                           SndEq_UpdateMovieLevels (WindowObject theWindowObject);
PASCAL_RTN void                 SndEq_UserItemProcedure (DialogPtr theDialog, short theItem);

OSErr                           SndEq_InitSoundResource (void);
OSErr                           SndEq_StopSoundResource (void);
SndListHandle                   SndEq_OpenSoundFile (void);
void                            SndEq_CloseSoundFile (void);
void                            SndEq_PlaySoundResource (SndListHandle theSndResource);
OSErr                           SndEq_UpdateResourceLevels (void);
PASCAL_RTN void                 SndEq_CallbackProc (SndChannelPtr theChannel, SndCommand *theCommand);
```

[Next](Document%20Revision%20History.md)[Previous](SndEqualizer.c.md)

