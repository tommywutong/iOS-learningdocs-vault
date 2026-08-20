---
title: Empty Engine
apple_id: DTS10000152
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Empty_Engine/Listings/Empty_Engine_Code_TtBitmapStore_c.html
archived_at: '2026-07-18T03:07:46.875504Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Empty Engine](Empty%20Engine.md)


[Next](Empty%20Engine%20Code-TtGouraud.c.md)[Previous](Empty%20Engine%20Code-TtBitmap.c.md)

# Empty Engine Code/TtBitmapStore.c

```c
/******************************************************************************
 **                                                                          **
 **     Module:     TtBitmapStore.c                                          **
 **                                                                          **
 **     Purpose:    Empty rasterizer drawing engine.                         **
 **                 Methods for bitmap New, Detach and Delete.               **
 **                                                                          **
 **     Author:     Mike W. Kelley                                           **
 **                                                                          **
 **                 2/3/95  Revised for 0.9 SDK release                      **
 **                                                                          **
 **     Copyright (C) 1994-95 Apple Computer, Inc.  All rights reserved.     **
 **     Apple Computer Confidential                                          **
 **                                                                          **
 *****************************************************************************/

/* System */
#include <stdlib.h>
#include <math.h>

#include "RAVE.h"
#include "RAVE_system.h"
#include "TtTinselTown.h"

/**************************************************************************************
 * Allocate a bitmap.
 *************************************************************************************/

TQAError TtBitmapNew (
    unsigned long       flags,              /* Mask of kQABitmap_xxx flags */
    TQAImagePixelType   pixelType,          /* Depth, color space, etc. */
    const TQAImage      *image,             /* Image */
    TQABitmap           **newBitmap)        /* (Out) Newly created TQABitmap, or NULL on error */ 
{
    /*
     * Allocate new bitmap memory, and assign new bitmap pointer to 'newBitmap'.
     * For now we assign NULL and return an error (as this function isn't
     * yet implemented).
     */

    *newBitmap = NULL;
    return (kQANotSupported);
}

/**************************************************************************************
 * Detach a bitmap (by copying the image data).
 *************************************************************************************/

TQAError TtBitmapDetach (
    TQABitmap           *bitmap)            /* Previously allocated by QABitmapNew() */
{
    TTtBitmap           *myBitmap;

    myBitmap = (TTtBitmap *) bitmap;

    /*
     * Copy the image data. Not implemented, so for now we return an error.
     */

    return (kQANotSupported);
}

/**************************************************************************************
 * Delete a bitmap.
 *************************************************************************************/

void TtBitmapDelete (
    TQABitmap           *bitmap)            /* Previously allocated by QABitmapNew() */
{
    TTtBitmap           *myBitmap;

    myBitmap = (TTtBitmap *) bitmap;

    /*
     * Delete the bitmap. Not yet implemented.
     */
}
```

[Next](Empty%20Engine%20Code-TtGouraud.c.md)[Previous](Empty%20Engine%20Code-TtBitmap.c.md)

