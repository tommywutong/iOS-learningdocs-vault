---
title: vrbackbuffer
apple_id: DTS10001019
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrbackbuffer/Listings/VRBackBuffer_h.html
archived_at: '2026-07-26T19:52:55.392278Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrbackbuffer](vrbackbuffer.md)


[Next](Document%20Revision%20History.md)[Previous](VRBackBuffer.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# VRBackBuffer.h

```c
//////////
//
//  File:       VRBackBuffer.h
//
//  Contains:   Sample code showing how to work with orientation of QuickTime VR back buffer.
//
//  Written by: Ken Doyle
//  Revised by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      06/26/99    rtm     first file
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

#ifndef __FIXMATH__
#include <FixMath.h>
#endif

#ifndef __QUICKTIMEVR__
#include <QuickTimeVR.h>
#endif

#ifndef __QUICKDRAW__
#include <QuickDraw.h>
#endif

#ifndef __QTVRUtilities__
#include "QTVRUtilities.h"
#endif

#ifndef __QTUtilities__
#include "QTUtilities.h"
#endif

#include "ComApplication.h"

//////////
//
// compiler macros
//
//////////

//////////
//
// constants
//
//////////

#define kDefaultEmbPictWidth        QTVRUtils_DegreesToRadians(30.0)
#define kQTVRNormalPictID           1010
#define kQTVRRotatedPictID          1011

//////////
//
// function prototypes
//
//////////

ApplicationDataHdl                  VRBB_InitWindowData (WindowObject theWindowObject);
void                                VRBB_DumpWindowData (WindowObject theWindowObject);
OSErr                               VRBB_InstallBackBufferImagingProc (QTVRInstance theInstance, WindowObject theWindowObject, short thePictResID, Boolean theIsHoriz);
OSErr                               VRBB_CleanUpBackBuffer (WindowObject theWindowObject);
PASCAL_RTN OSErr                    VRBB_BackBufferImagingProc (QTVRInstance theInstance, Rect *theRect, UInt16 theAreaIndex, UInt32 theFlagsIn, UInt32 *theFlagsOut, long theRefCon);
Boolean                             VRBB_IsBackBufferHorizontal (QTVRInstance theInstance);
```

[Next](Document%20Revision%20History.md)[Previous](VRBackBuffer.c.md)

