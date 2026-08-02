---
title: qtflattentohandle
apple_id: DTS10000895
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtflattentohandle/Listings/QTFlattenToHandle_h.html
archived_at: '2026-07-26T19:52:49.285263Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtflattentohandle](qtflattentohandle.md)


[Next](Document%20Revision%20History.md)[Previous](QTFlattenToHandle.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTFlattenToHandle.h

```c
//////////
//
//  File:       QTFlattenToHandle.h
//
//  Contains:   Handle data handler sample code.
//
//  Written by: Tim Monroe
//              Based on the existing code revised by Deeje Cooley.
//
//  Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      04/09/98    rtm     first file; integrated existing code with shell framework
//
//////////

//////////
//
// header files
//
//////////

#include <Movies.h>
#include <Resources.h>
#include <MacWindows.h>
#include <Script.h>

#include "QTUtilities.h"

//////////
//
// constants
//
//////////

#define kWindowTitle        "Movie Window"

//////////
//
// function prototypes
//
//////////

OSErr           QTHandle_OpenMovieFileAndFlattenToHandle (FSSpecPtr theFSSpecPtr);
OSErr           QTHandle_PlayMovieResource (Movie theMovie);
```

[Next](Document%20Revision%20History.md)[Previous](QTFlattenToHandle.c.md)

