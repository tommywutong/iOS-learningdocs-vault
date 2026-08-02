---
title: addflashactions
apple_id: DTS10001062
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/addflashactions/Listings/AddFlashActions_h.html
archived_at: '2026-07-18T03:28:46.559211Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [addflashactions](addflashactions.md)


[Next](FlashParser.c.md)[Previous](AddFlashActions.c.md)

# AddFlashActions.h

```c
//////////
//
//  File:       AddFlashActions.h
//
//  Contains:   Sample code for adding actions to a Flash track in a movie.
//
//  Written by: 
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     
//////////

//////////
//
// header files
//     
//////////

#ifndef __MACMEMORY__
#include <MacMemory.h>
#endif

#ifndef __NUMBERFORMATTING__
#include <NumberFormatting.h>
#endif

#ifndef __FONTS__
#include <Fonts.h>
#endif

#ifndef __ENDIAN__
#include <Endian.h>
#endif

#ifndef __RESOURCES__
#include <Resources.h>
#endif

#ifndef __STRINGCOMPARE__
#include <StringCompare.h>
#endif

#ifndef __MOVIES__
#include <Movies.h>
#endif

#ifndef __FIXMATH__
#include <FixMath.h>
#endif

#ifndef _STRING_H
#include <string.h>
#endif

// Windows-specific header files
#if TARGET_OS_WIN32

    #ifndef __QTML__
    #include <QTML.h>
    #endif

    #include <windows.h>

#endif

#include "FlashParser.h"


//////////
//
// constants
//     
//////////

#define kNilPointer         NULL
#define kIndexZero          0
#define kIndexOne           1

#define kZeroDataLength     0


//////////
//
// function prototypes
//     
//////////

static void                             AddFLAct_SetWiredActionToButton (Handle theSample, long theButtonID, U16 theCondition, QTAtomContainer theAction);
static OSErr                            AddFLAct_SetWiredActionsToButton (Handle theSample, long theButtonID, QTAtomContainer theActions);
static OSErr                            AddFLAct_CreateButtonActionContainer (QTAtomContainer *theActions);
static OSErr                            AddFLAct_CreateFrameLoadedActionContainer (QTAtomContainer *theActions);
static OSErr                            AddFLAct_SetFrameLoadedWiredActions (Handle theSample, long theFrameID, QTAtomContainer theActions);
static void                             AddFLAct_AddWiredActionsToFlashMovie (FSSpec *theFSSpec);
static OSErr                            AddFLAct_CopyAtomAndChildren (QTAtomContainer theSrcContainer, QTAtom theSrcAtom, QTAtomContainer theDstContainer, QTAtom theDstAtom);
static OSErr                            AddFLAct_CopyChildren (QTAtomContainer theSrcContainer, QTAtom theSrcAtom, QTAtomContainer theDstContainer, QTAtom theDstAtom);
```

[Next](FlashParser.c.md)[Previous](AddFlashActions.c.md)

