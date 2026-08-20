---
title: vrmovies
apple_id: DTS10001030
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrmovies/Listings/Application_Files_ComApplication_h.html
archived_at: '2026-07-26T19:53:00.218098Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrmovies](vrmovies.md)


[Next](Application%20Files-ComResource.h.md)[Previous](Application%20Files-ComApplication.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# Application Files/ComApplication.h

```c
//////////
//
//  File:       ComApplication.h
//
//  Contains:   Functions that could be overridden in a specific application.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <2>      10/21/02    era     building Mach-O
//     <1>      11/05/99    rtm     first file; based on earlier sample code
//
//////////

#pragma once

#ifndef __ComApplication__
#define __ComApplication__

//////////
//
// header files
//
//////////

#ifdef __MACH__
    #include <Carbon/Carbon.h>
    #include <QuickTime/QuickTime.h>
#else
    #ifndef __QUICKTIMEVR__
    #include <QuickTimeVR.h>
    #endif

    #ifndef __TEXTUTILS__
    #include <TextUtils.h>
    #endif

    #ifndef __SCRIPT__
    #include <Script.h>
    #endif

    #if TARGET_OS_MAC
    #ifndef __APPLEEVENTS__
    #include <AppleEvents.h>
    #endif
    #endif
#endif

#if TARGET_OS_MAC
#include "MacFramework.h"
#endif

#if TARGET_OS_WIN32
#include "WinFramework.h"
#endif

#ifndef __QTUtilities__
#include "QTUtilities.h"
#endif

#include "ComResource.h"

//////////
//
// constants
//
//////////

//////////
//
// structures
//
//////////

// application-specific data
typedef struct ApplicationDataRecord {
    Movie                       fMovie;             // the embedded movie to play
    GWorldPtr                   fOffscreenGWorld;   // the offscreen graphics world used for imaging embedded movies
    PixMapHandle                fOffscreenPixMap;   // the pixmap of the offscreen graphics world
    GWorldPtr                   fPrevBBufGWorld;    // the previous offscreen graphics world used for the back buffer
    Rect                        fPrevBBufRect;      // the previous rectangle of the area of interest
    QTVRFloatPoint              fMovieCenter;       // the center in the panorama of the movie screen (in angles: x = pan; y = tilt)
    Rect                        fMovieBox;          // the movie box
    float                       fMovieScale;        // a scale factor for the movie rectangle
    float                       fMovieWidth;        // the width (in radians) of the embedded movie
    Boolean                     fUseOffscreenGWorld;// use an offscreen GWorld?
    Boolean                     fUseMovieCenter;    // use the specified movie center?
    Boolean                     fQTMovieHasSound;   // does the embedded movie have a sound track?
    Boolean                     fCompositeMovie;    // does the embedded movie need to be composited?
    Boolean                     fUseHideRegion;     // use the specified movie hide region?
    QTVRBackBufferImagingUPP    fBackBufferProc;    // a routine descriptor for our back buffer routine
    RGBColor                    fChromaColor;       // the color for chroma key compositing
    RgnHandle                   fHideRegion;        // the region that obscures the embedded movie
    MatrixRecord                fMovieMatrix;       // the matrix we use to (optionally) rotate the movie
    MatrixRecord                fOrigMovieMatrix;   // the movie's original matrix
    Boolean                     fBackBufferIsHoriz; // is the backbuffer oriented horizontally?
    ImageDescriptionHandle      fImageDesc;         // image description for DecompressSequenceFrameS
    ImageSequence               fImageSequence;     // image sequence for DecompressSequenceFrameS
} ApplicationDataRecord, *ApplicationDataPtr, **ApplicationDataHdl;

//////////
//
// function prototypes
//
//////////

#if TARGET_OS_MAC
void                    QTApp_InstallAppleEventHandlers (void);
PASCAL_RTN OSErr        QTApp_HandleOpenApplicationAppleEvent (const AppleEvent *theMessage, AppleEvent *theReply, long theRefcon);
PASCAL_RTN OSErr        QTApp_HandleOpenDocumentAppleEvent (const AppleEvent *theMessage, AppleEvent *theReply, long theRefcon);
PASCAL_RTN OSErr        QTApp_HandlePrintDocumentAppleEvent (const AppleEvent *theMessage, AppleEvent *theReply, long theRefcon);
PASCAL_RTN OSErr        QTApp_HandleQuitApplicationAppleEvent (const AppleEvent *theMessage, AppleEvent *theReply, long theRefcon);
#endif  // TARGET_OS_MAC

// the other function prototypes are in the file MacFramework.h or WinFramework.h

#endif // __ComApplication__
```

[Next](Application%20Files-ComResource.h.md)[Previous](Application%20Files-ComApplication.c.md)

