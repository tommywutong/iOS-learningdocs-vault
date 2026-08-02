---
title: qtfullscreen
apple_id: DTS10000861
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtfullscreen/Listings/QTFullScreen_h.html
archived_at: '2026-07-26T19:52:46.415054Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtfullscreen](qtfullscreen.md)


[Next](Document%20Revision%20History.md)[Previous](QTFullScreen.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

Relevant replacement documents include:

- Sample Code Project _[FullScreenWindow](../FullScreenWindow/FullScreenWindow.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmjyha)_

# QTFullScreen.h

```c
//////////
//
//  File:       QTFullScreen.h
//
//  Contains:   Functions to display full-screen QuickTime movies.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1997 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      12/22/97    rtm     first file
//
//////////

//////////
//
// header files
//
//////////

#ifndef __MOVIES__
#include <Movies.h>
#endif

#ifndef __QTML__
#include <QTML.h>
#endif

//////////
//
// function prototypes
//
//////////

OSErr                       QTFullScreen_PlayOnFullScreen (FSSpecPtr theFSSpecPtr);
OSErr                       QTFullScreen_RestoreScreen (void);
OSErr                       QTFullScreen_EventLoopAction (EventRecord *theEvent);

#if TARGET_OS_WIN32
LRESULT CALLBACK            QTFullScreen_HandleMessages (HWND theWnd, UINT theMessage, UINT wParam, LONG lParam);
#endif

PASCAL_RTN void             QTFullScreen_MoviePrePrerollCompleteProc (Movie theMovie, OSErr thePrerollErr, void *theRefcon);
OSErr                       QTFullScreen_PlayMovieOnFullScreen (Movie theMovie);
```

[Next](Document%20Revision%20History.md)[Previous](QTFullScreen.c.md)

