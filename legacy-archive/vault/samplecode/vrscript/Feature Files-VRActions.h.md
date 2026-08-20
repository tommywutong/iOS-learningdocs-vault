---
title: vrscript
apple_id: DTS10001032
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrscript/Listings/Feature_Files_VRActions_h.html
archived_at: '2026-07-26T19:53:02.401548Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrscript](vrscript.md)


[Next](Feature%20Files-VREffects.c.md)[Previous](Feature%20Files-VRActions.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# Feature Files/VRActions.h

```c
//////////
//
//  File:       VRActions.h
//
//  Contains:   Support for reacting to QuickTime wired actions in VR nodes.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      08/05/99    rtm     first file
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

// special value for fEventType field of wired action commands
#define kVRAnyEvent         (OSType)-1

// special value for fID field of wired action commands
#define kVRAnyItemID        (UInt32)-1

//////////
//
// function prototypes
//
//////////

void                        VRActions_InitWindowData (WindowObject theWindowObject);
void                        VRActions_DumpWindowData (WindowObject theWindowObject);
```

[Next](Feature%20Files-VREffects.c.md)[Previous](Feature%20Files-VRActions.c.md)

