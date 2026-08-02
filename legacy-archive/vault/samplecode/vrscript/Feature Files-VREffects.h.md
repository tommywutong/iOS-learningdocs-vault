---
title: vrscript
apple_id: DTS10001032
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrscript/Listings/Feature_Files_VREffects_h.html
archived_at: '2026-07-26T19:53:02.447780Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrscript](vrscript.md)


[Next](Feature%20Files-VRHash.c.md)[Previous](Feature%20Files-VREffects.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# Feature Files/VREffects.h

```c
//////////
//
//  File:       VREffects.h
//
//  Contains:   QuickTime video effects support for QuickTime VR movies.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1997 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      12/13/96    rtm     first file
//
//////////

#pragma once

//////////
//
// header files
//
//////////

#include <ImageCompression.h>
#include <ImageCodec.h>

#include "ComApplication.h"

#if TARGET_OS_MAC
#include "MacFramework.h"
#endif

#if TARGET_OS_WIN32
#include "WinFramework.h"
#endif

#include "VRScript.h"

//////////
//
// compiler flags
//
//////////

#define USES_MAKE_IMAGE_DESC_FOR_EFFECT 1       // use MakeImageDescriptionForEffect (QT 4.0 and later)

//////////
//
// constants
//
//////////

#define kSourceOneName                  FOUR_CHAR_CODE('srcA')
#define kSourceTwoName                  FOUR_CHAR_CODE('srcB')
#define kSourceNoneName                 FOUR_CHAR_CODE('srcZ')

#define kDefaultNumSteps                50      // the number of steps in a transition
#define kDoIdleStep                     10      // the number of steps we take before giving scene-wide sound-only movies some idle time

//////////
//
// function prototypes
//
//////////

void                        VREffects_InitWindowData (WindowObject theWindowObject);
void                        VREffects_DumpWindowData (WindowObject theWindowObject);
Boolean                     VREffects_DoIdle (WindowObject theWindowObject);
VRScriptTransitionPtr       VREffects_GetTransitionEffect (WindowObject theWindowObject, UInt32 fromNodeID, UInt32 toNodeID);
QTAtomContainer             VREffects_MakeEffectDescription (OSType theEffectType, long theEffectNum, OSType theSourceName1, OSType theSourceName2);
ImageDescriptionHandle      VREffects_MakeSampleDescription (OSType theEffectType, short theWidth, short theHeight);
OSErr                       VREffects_SetupTransitionEffect (WindowObject theWindowObject, UInt32 fromNodeID, UInt32 toNodeID);
OSErr                       VREffects_RunTransitionEffect (WindowObject theWindowObject);
void                        VREffects_DumpEntryMem (VRScriptTransitionPtr theEntry);
```

[Next](Feature%20Files-VRHash.c.md)[Previous](Feature%20Files-VREffects.c.md)

