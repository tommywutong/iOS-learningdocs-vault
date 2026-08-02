---
title: vrmovies
apple_id: DTS10001030
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrmovies/Listings/VRMovies_h.html
archived_at: '2026-07-26T19:53:00.834504Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrmovies](vrmovies.md)


[Next](Document%20Revision%20History.md)[Previous](VRMovies.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# VRMovies.h

```c
//////////
//
//  File:       VRMovies.h
//
//  Contains:   Support for QuickTime movie playback in VR nodes.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1997 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <2>      10/21/02    era     building Mach-O
//     <1>      12/11/96    rtm     first file
//
//////////

#pragma once

//////////
//
// header files
//
//////////

#ifdef __MACH__
    #include <Carbon/Carbon.h>
    #include <QuickTime/QuickTime.h>
#else
    #ifndef __MOVIES__
    #include <Movies.h>
    #endif

    #ifndef __MEDIAHANDLERS__
    #include <MediaHandlers.h>
    #endif

    #ifndef __QDOFFSCREEN__
    #include <QDOffscreen.h>
    #endif

    #ifndef __COLORPICKER__
    #include <ColorPicker.h>
    #endif

    #ifndef __FIXMATH__
    #include <FixMath.h>
    #endif

    #ifndef __QUICKTIMEVR__
    #include <QuickTimeVR.h>
    #endif
#endif

#ifndef __QTVRUtilities__
#include "QTVRUtilities.h"
#endif

#ifndef __QTUtilities__
#include "QTUtilities.h"
#endif

#if TARGET_OS_WIN32
    #ifndef _INC_COMMDLG
    #include <commdlg.h>
    #endif
#endif

#include "ComApplication.h"
#include "ComFramework.h"

//////////
//
// compiler macros
//
//////////

#define RECT_WIDTH(rect)            ((rect).right-(rect).left)
#define RECT_HEIGHT(rect)           ((rect).bottom-(rect).top)

//////////
//
// constants
//
//////////

#define kDefaultEmbMovieWidth       QTVRUtils_DegreesToRadians(20.0)
#define kColorPickerTextStringID    128

//////////
//
// function prototypes
//
//////////

ApplicationDataHdl                  VRMoov_InitWindowData (WindowObject theWindowObject);
void                                VRMoov_DumpWindowData (WindowObject theWindowObject);
Boolean                             VRMoov_GetEmbeddedMovie (WindowObject theWindowObject);
Boolean                             VRMoov_LoadEmbeddedMovie (FSSpec *theMovieFile, WindowObject theWindowObject);
void                                VRMoov_LoopEmbeddedMovie (Movie theMovie);
void                                VRMoov_DumpEmbeddedMovie (WindowObject theWindowObject);
OSErr                               VRMoov_InstallBackBufferImagingProc (QTVRInstance theInstance, WindowObject theWindowObject);
OSErr                               VRMoov_CalcImagingMatrix (WindowObject theWindowObject, Rect *theBBufRect);
OSErr                               VRMoov_SetupDecompSeq (WindowObject theWindowObject, GWorldPtr theDestGWorld);
OSErr                               VRMoov_RemoveDecompSeq (WindowObject theWindowObject);
PASCAL_RTN OSErr                    VRMoov_BackBufferImagingProc (QTVRInstance theInstance, Rect *theRect, UInt16 theAreaIndex, UInt32 theFlagsIn, UInt32 *theFlagsOut, long theRefCon);
float                               VRMoov_GetEmbeddedMovieWidth (WindowObject theWindowObject);
void                                VRMoov_SetEmbeddedMovieWidth (WindowObject theWindowObject, float theWidth);
void                                VRMoov_GetEmbeddedMovieCenter (WindowObject theWindowObject, QTVRFloatPoint *theCenter);
void                                VRMoov_SetEmbeddedMovieCenter (WindowObject theWindowObject, const QTVRFloatPoint *theCenter);
float                               VRMoov_GetEmbeddedMovieScale (WindowObject theWindowObject);
void                                VRMoov_SetEmbeddedMovieScale (WindowObject theWindowObject, float theScale);
void                                VRMoov_SetChromaColor (WindowObject theWindowObject);
PASCAL_RTN OSErr                    VRMoov_UncoverProc (Movie theMovie, RgnHandle theRegion, long theRefCon);
PASCAL_RTN Boolean                  VRMoov_ColorDialogEventFilter (EventRecord *theEvent);
void                                VRMoov_SetVideoGraphicsMode (Movie theMovie, ApplicationDataHdl theAppData, Boolean theSetVGM);
short                               VRMoov_GetVideoGraphicsPixelDepth (Movie theMovie);
#if TARGET_OS_WIN32
void                                VRMoov_MacRGBToWinRGB (RGBColorPtr theRGBColor, COLORREF *theColorRef);
void                                VRMoov_WinRGBToMacRGB (RGBColorPtr theRGBColor, COLORREF theColorRef);
#endif
```

[Next](Document%20Revision%20History.md)[Previous](VRMovies.c.md)

