---
title: addvractions.win
apple_id: DTS10001018
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/addvractions.win/Listings/AddVRActions_h.html
archived_at: '2026-07-18T03:28:47.781358Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [addvractions.win](addvractions.win.md)


[Next](Document%20Revision%20History.md)[Previous](AddVRActions.c.md)

# AddVRActions.h

```c
//////////
//
//  File:       AddVRActions.h
//
//  Contains:   Sample code for adding wired actions to a QuickTime VR movie.
//
//  Written by: Tim Monroe
//              Based on existing code by Bill Wright
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      07/14/99    rtm     first file from bw
//     
//////////

#if !TARGET_OS_WIN32
#define TARGET_API_MAC_CARBON           1
#endif


//////////
//
// header files
//
//////////

#ifndef __MACTYPES__
#include <MacTypes.h>
#endif

#ifndef __ENDIAN__
#include <Endian.h>
#endif

#ifndef __MOVIES__
#include <Movies.h>
#endif

#ifndef __MACMEMORY__
#include <MacMemory.h>
#endif

#ifndef _STRING_H
#include <string.h>
#endif

#ifndef __FONTS__
#include <Fonts.h>
#endif

#ifndef __MOVIES__
#include <Movies.h>
#endif

#ifndef __FIXMATH__
#include <FixMath.h>
#endif

#ifndef __QUICKTIMEVRFORMAT__
#include <QuickTimeVRFormat.h>
#endif

#ifndef __QUICKTIMEVR__
#include <QuickTimeVR.h>
#endif

// Mac-specific header files
#if TARGET_OS_MAC

    #ifndef __NAVIGATION__
    #include <Navigation.h>
    #endif

#endif

// Windows-specific header files
#if TARGET_OS_WIN32

    #ifndef __QTML__
    #include <QTML.h>
    #endif

    #include <windows.h>

#endif


//////////
//
// constants
//
//////////

#define kIndexZero                      0
#define kIndexOne                       1
#define kZeroDataLength                 0

// resource ID for string resource containing application's name
#define kAppNameResID                   1000
#define kAppNameResIndex                1


//////////
//
// data types
//
//////////

typedef const OSType *      QTFrameTypeListPtr;


//////////
//
// function prototypes
//
//////////

static OSErr                            AddVRAct_GetFirstHotSpot (Handle theSample, long *theHotSpotID);
static OSErr                            AddVRAct_CreateHotSpotActionContainer (QTAtomContainer *theActions);
static OSErr                            AddVRAct_CreateFrameLoadedActionContainer (QTAtomContainer *theActions);
static OSErr                            AddVRAct_CreateIdleActionContainer (QTAtomContainer *theActions);
static OSErr                            AddVRAct_SetWiredActionsToNode (Handle theSample, QTAtomContainer theActions, UInt32 theActionType);
static OSErr                            AddVRAct_SetWiredActionsToHotSpot (Handle theSample, long theHotSpotID, QTAtomContainer theActions);
static OSErr                            AddVRAct_WriteMediaPropertyAtom (Media theMedia, long thePropertyID, long thePropertySize, void *theProperty);
static void                             AddVRAct_AddWiredActionsToQTVRMovie (FSSpec *theFSSpec);
static void                             AddVRAct_ConvertFloatToBigEndian (float *theFloat);
static OSErr                            AddVRAct_GetOneFileWithPreview (short theNumTypes, QTFrameTypeListPtr theTypeList, FSSpecPtr theFSSpecPtr, void *theFilterProc);
static Handle                           AddVRAct_CreateOpenHandle (OSType theApplicationSignature, short theNumTypes, QTFrameTypeListPtr theTypeList);
```

[Next](Document%20Revision%20History.md)[Previous](AddVRActions.c.md)

