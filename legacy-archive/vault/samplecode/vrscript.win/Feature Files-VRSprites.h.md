---
title: vrscript.win
apple_id: DTS10001033
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrscript.win/Listings/Feature_Files_VRSprites_h.html
archived_at: '2026-07-26T19:53:04.281336Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrscript.win](vrscript.win.md)


[Next](VRScript.c.md)[Previous](Feature%20Files-VRSprites.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# Feature Files/VRSprites.h

```c
//////////
//
//  File:       VRSprites.h
//
//  Contains:   Support for QuickTime sprite tracks in VR nodes.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      06/19/98    rtm     first file
//
//////////

#pragma once

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

#include "VRScript.h"

//////////
//
// constants
//
//////////

// special value for Options field of sprite click commands
#define kVRAnySprite        (UInt32)-1

//////////
//
// function prototypes
//
//////////

void                        VRSprites_InitWindowData (WindowObject theWindowObject);
void                        VRSprites_DumpWindowData (WindowObject theWindowObject);
void                        VRSprites_SetVisibleState (WindowObject theWindowObject, QTAtomID theSpriteID, Boolean theState, UInt32 theOptions);
void                        VRSprites_SetLayer (WindowObject theWindowObject, QTAtomID theSpriteID, short theLayer, UInt32 theOptions);
void                        VRSprites_SetGraphicsMode (WindowObject theWindowObject, QTAtomID theSpriteID, long theMode, UInt32 theOptions);
void                        VRSprites_SetImageIndex (WindowObject theWindowObject, QTAtomID theSpriteID, short theIndex, UInt32 theOptions);
void                        VRSprites_SetMatrix (WindowObject theWindowObject, QTAtomID theSpriteID, MatrixRecord *theMatrix, UInt32 theOptions);
void                        VRSprites_SetLocation (WindowObject theWindowObject, QTAtomID theSpriteID, Point *thePoint, UInt32 theOptions);
```

[Next](VRScript.c.md)[Previous](Feature%20Files-VRSprites.c.md)

