---
title: vrflattenmovie
apple_id: DTS10001023
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrflattenmovie/Listings/VRFlatten_h.html
archived_at: '2026-07-26T19:52:57.126844Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrflattenmovie](vrflattenmovie.md)


[Next](Document%20Revision%20History.md)[Previous](VRFlatten.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# VRFlatten.h

```c
//////////
//
//  File:       VRFlatten.h
//
//  Contains:   Code showing how to call the QTVR file flattener.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 2000 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      05/11/00    rtm     first file
//
//////////

#pragma once

//////////
//
// header files
//
//////////

#ifndef __FILETYPESANDCREATORS__
#include <FileTypesAndCreators.h>
#endif

#ifndef __MOVIES__
#include <Movies.h>
#endif

#ifndef __QUICKTIMECOMPONENTS__
#include <QuickTimeComponents.h>
#endif

#ifndef __SCRIPT__
#include <Script.h>
#endif

//////////
//
// function prototypes
//
//////////

OSErr                       QTVRUtils_FlattenMovieForStreaming (Movie theMovie, FSSpecPtr theFSSpecPtr);
```

[Next](Document%20Revision%20History.md)[Previous](VRFlatten.c.md)

