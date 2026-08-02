---
title: WiredSprites
apple_id: DTS10001044
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/WiredSprites/Listings/Common_Files_EndianUtilities_h.html
archived_at: '2026-07-18T03:28:22.446733Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WiredSprites](WiredSprites.md)


[Next](Common%20Files-ImageCompressionUtilities.c.md)[Previous](Common%20Files-EndianUtilities.c.md)

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

void                        EndianUtils_ImageDescription_NtoB (ImageDescriptionHandle theIDH);
void                        EndianUtils_ImageDescription_BtoN (ImageDescriptionHandle theIDH);
void                        EndianUtils_MatrixRecord_NtoB (MatrixRecord *theMatrix);
void                        EndianUtils_RgnHandle_NtoB (RgnHandle theRgn);
void                        EndianUtils_Float_NtoB (float *theFloat);

#endif  // ifndef __ENDIANUTILITIES__
```

[Next](Common%20Files-ImageCompressionUtilities.c.md)[Previous](Common%20Files-EndianUtilities.c.md)

