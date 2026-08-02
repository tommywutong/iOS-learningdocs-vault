---
title: qtskins
apple_id: DTS10000877
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtskins/Listings/QTSkins_h.html
archived_at: '2026-07-26T19:52:47.528325Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtskins](qtskins.md)


[Next](Document%20Revision%20History.md)[Previous](QTSkins.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTSkins.h

```c
//////////
//
//  File:       QTSkins.h
//
//  Contains:   Sample code for using QuickTime's skins.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 2000 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      11/15/00    rtm     first file
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

#ifndef __QUICKTIMECOMPONENTS__
#include <QuickTimeComponents.h>
#endif

#ifndef __MEDIAHANDLERS__
#include <MediaHandlers.h>
#endif

#ifndef __FIXMATH__
#include <FixMath.h>
#endif

#include "ComApplication.h"

//////////
//
// compiler macros
//
//////////

#if TARGET_OS_WIN32
#define HiWord                      HIWORD
#define LoWord                      LOWORD
#define GetPortPixMap(port)         ((port)->portPixMap)
#endif

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

OSErr                               QTSkin_AddSkinTrack (Movie theMovie);
PicHandle                           QTSkin_GetPicHandleFromFile (void);
#if TARGET_OS_MAC
PASCAL_RTN Boolean                  QTSkin_FileFilterFunction (AEDesc *theItem, void *theInfo, void *theCallBackUD, NavFilterModes theFilterMode);
#endif
#if TARGET_OS_WIN32
PASCAL_RTN Boolean                  QTSkin_FileFilterFunction (CInfoPBPtr thePBPtr);
#endif

void                                QTSkin_Init (void);
void                                QTSkin_Stop (void);
static PASCAL_RTN long              QTSkin_SkinWindowDef (short theVarCode, WindowRef theWindow, short theMessage, long theParam);
WindowReference                     QTSkin_CreateSkinsWindow (Movie theMovie);
OSErr                               QTSkin_ConvertPictureToRegion (PicHandle thePicture, RgnHandle *theRegionPtr);
ApplicationDataHdl                  QTSkin_InitWindowData (WindowObject theWindowObject);
void                                QTSkin_DumpWindowData (WindowObject theWindowObject);
#if TARGET_OS_WIN32
Boolean                             QTSkin_IsDragClick (WindowObject theWindowObject, LONG lParam);
#endif
OSErr                               QTSkin_GetRegionsFromMovie (Movie theMovie);

Boolean                             QTSkin_IsSkinnedMovie (Movie theMovie) ;
```

[Next](Document%20Revision%20History.md)[Previous](QTSkins.c.md)

