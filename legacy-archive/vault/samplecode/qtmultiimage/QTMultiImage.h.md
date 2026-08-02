---
title: qtmultiimage
apple_id: DTS10000871
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtmultiimage/Listings/QTMultiImage_h.html
archived_at: '2026-07-26T19:52:46.730468Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtmultiimage](qtmultiimage.md)


[Next](Document%20Revision%20History.md)[Previous](QTMultiImage.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTMultiImage.h

```c
//////////
//
//  File:       QTMultiImage.h
//
//  Contains:   Code for displaying multiple images contained in a single image file.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      09/30/98    rtm     first file
//
//////////

//////////
//
// header files
//
//////////

#include <Movies.h>
#include <QuickTimeComponents.h>

//////////
//
// constants
//
//////////

#define kImageDisplayTime       120     // ticks

//////////
//
// function prototypes
//
//////////

OSErr                   QTMulti_ShowAllImagesInFile (FSSpecPtr theFSSpecPtr);
```

[Next](Document%20Revision%20History.md)[Previous](QTMultiImage.c.md)

