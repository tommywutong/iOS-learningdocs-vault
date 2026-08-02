---
title: vrscript.win
apple_id: DTS10001033
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrscript.win/Listings/Feature_Files_VRPicture_h.html
archived_at: '2026-07-26T19:53:04.139376Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrscript.win](vrscript.win.md)


[Next](Feature%20Files-VRPreferences.c.md)[Previous](Feature%20Files-VRPicture.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# Feature Files/VRPicture.h

```c
//////////
//
//  File:       VRPicture.h
//
//  Contains:   Headers for drawing pictures into the prescreen buffer.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1994-1997 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      01/28/97    rtm     first file
//
//////////

#pragma once

// header files
#include <QuickTimeVR.h>

#include "ComApplication.h"

#if TARGET_OS_MAC
#include "MacFramework.h"
#endif

#if TARGET_OS_WIN32
#include "WinFramework.h"
#endif

// function prototypes
void                                VRPicture_ShowPicture (WindowObject theWindowObject, UInt32 theResID, UInt32 theEntryID, UInt32 theHeight, UInt32 theWidth, UInt32 thePegSides, UInt32 theOffset, UInt32 theOptions);
void                                VRPicture_DrawNodePictures (WindowObject theWindowObject);
void                                VRPicture_DumpNodePictures (WindowObject theWindowObject);
void                                VRPicture_DumpEntryMem (VRScriptPicturePtr theEntry);
```

[Next](Feature%20Files-VRPreferences.c.md)[Previous](Feature%20Files-VRPicture.c.md)

