---
title: qtbigscreen.win
apple_id: DTS10000852
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtbigscreen.win/Listings/QTBigScreen_h.html
archived_at: '2026-07-26T19:52:46.127319Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtbigscreen.win](qtbigscreen.win.md)


[Next](Document%20Revision%20History.md)[Previous](QTBigScreen.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTBigScreen.h

```c
//////////
//
//  File:       QTBigScreen.h
//
//  Contains:   Code for playing QuickTime movies fullscreen.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 2002 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      07/01/02    rtm     first file
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
// compiler defines
//
//////////

#define END_FULLSCREEN_AT_MOVIE_END         0

//////////
//
// constants
//
//////////

//////////
//
// function prototypes
//
//////////

ApplicationDataHdl              QTBig_InitWindowData (WindowObject theWindowObject);
void                            QTBig_DumpWindowData (WindowObject theWindowObject);

OSErr                           QTBig_StartFullscreen (WindowObject theWindowObject);
OSErr                           QTBig_StopFullscreen (WindowObject theWindowObject);

#if END_FULLSCREEN_AT_MOVIE_END
Boolean                         QTBig_MovieIsStoppable (MovieController theMC);
void                            QTBig_InstallCallBack (WindowObject theWindowObject);
PASCAL_RTN void                 QTBig_FullscreenCallBack (QTCallBack theCallBack, long theRefCon);
#endif

#if TARGET_OS_WIN32
LRESULT CALLBACK                QTBig_HandleMessages (HWND theWnd, UINT theMessage, UINT wParam, LONG lParam);
#endif

void                            QTFrame_SetWindowVisState (WindowObject theWindowObject, Boolean theState);
```

[Next](Document%20Revision%20History.md)[Previous](QTBigScreen.c.md)

