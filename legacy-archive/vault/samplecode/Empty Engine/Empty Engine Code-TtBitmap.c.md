---
title: Empty Engine
apple_id: DTS10000152
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Empty_Engine/Listings/Empty_Engine_Code_TtBitmap_c.html
archived_at: '2026-07-18T03:07:46.925686Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Empty Engine](Empty%20Engine.md)


[Next](Empty%20Engine%20Code-TtBitmapStore.c.md)[Previous](Empty%20Engine.md)

# Empty Engine Code/TtBitmap.c

```c
/******************************************************************************
 **                                                                          **
 **     Module:     TtBitmap.c                                               **
 **                                                                          **
 **     Purpose:    Empty rasterizer drawing engine.                         **
 **                 Methods for drawing bitmaps.                             **
 **                                                                          **
 **     Author:     Mike W. Kelley                                           **
 **                                                                          **
 **                 2/3/95  Revised for 0.9 SDK release                      **
 **                                                                          **
 **     Copyright (C) 1994-95 Apple Computer, Inc.  All rights reserved.     **
 **     Apple Computer Confidential                                          **
 **                                                                          **
 *****************************************************************************/

#include "RAVE.h"
#include "RAVE_system.h"
#include "TtTinselTown.h"

/************************************************************************************************
 * Draw a bitmap.
 ***********************************************************************************************/

void TtDrawBitmap (
    const TQADrawContext    *drawContext,       /* Draw context */
    const TQAVGouraud   *v,                 /* xyz, and (if a 1 bit/pixel bitmap) argb */
    TQABitmap           *bitmap)            /* Previously allocated by QABitmapNew() */
{
    TTtDrawPrivate      *myPrivate;
    TTtBitmap           *myBitmap;

    myPrivate = (TTtDrawPrivate *) drawContext->drawPrivate;
    myBitmap = (TTtBitmap *) bitmap;
}
```

[Next](Empty%20Engine%20Code-TtBitmapStore.c.md)[Previous](Empty%20Engine.md)

