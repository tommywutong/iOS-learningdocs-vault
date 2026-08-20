---
title: qtbroadcast
apple_id: DTS10001046
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-06'
source_url: https://developer.apple.com/library/archive/samplecode/qtbroadcast/Listings/Common_Files_EndianUtilities_h.html
archived_at: '2026-07-26T19:53:05.370605Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtbroadcast](qtbroadcast.md)


[Next](Common%20Files-MacFramework.c.md)[Previous](Common%20Files-EndianUtilities.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# Common Files/EndianUtilities.h

```c
//////////
//
//  File:       EndianUtilities.h
//
//  Contains:   Utilities for managing the endian differences between operating systems.
//
//  Written by: Tim Monroe
//              Based on existing endian functions by various QT engineers
//
//  Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      03/27/98    rtm     first file
//
//////////

#pragma once

// header files

#ifndef __ENDIANUTILITIES__
#define __ENDIANUTILITIES__

#ifndef __ENDIAN__
#include <Endian.h>
#endif

#ifndef __MOVIES__
#include <Movies.h>
#endif

// constants

enum {
    kBtoN                   = false,
    kNtoB                   = true
};

// data types

typedef struct {
    ImageDescription        id;
    ColorTable              ct;
} ImDesc;

// function prototypes

static void                 EndianUtils_FlipImageDescription (Boolean theNtoB, ImageDescriptionHandle theIDH);
void                        EndianUtils_ImageDescription_NtoB (ImageDescriptionHandle theIDH);
void                        EndianUtils_ImageDescription_BtoN (ImageDescriptionHandle theIDH);
void                        EndianUtils_MatrixRecord_NtoB (MatrixRecord *theMatrix);
void                        EndianUtils_RgnHandle_NtoB (RgnHandle theRgn);
void                        EndianUtils_Float_NtoB (float *theFloat);

#endif  // ifndef __ENDIANUTILITIES__
```

[Next](Common%20Files-MacFramework.c.md)[Previous](Common%20Files-EndianUtilities.c.md)

