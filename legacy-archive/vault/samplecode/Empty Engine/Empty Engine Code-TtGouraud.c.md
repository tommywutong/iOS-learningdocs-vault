---
title: Empty Engine
apple_id: DTS10000152
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Empty_Engine/Listings/Empty_Engine_Code_TtGouraud_c.html
archived_at: '2026-07-18T03:07:46.964727Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Empty Engine](Empty%20Engine.md)


[Next](Empty%20Engine%20Code-TtLine.c.md)[Previous](Empty%20Engine%20Code-TtBitmapStore.c.md)

# Empty Engine Code/TtGouraud.c

```c
/******************************************************************************
 **                                                                          **
 **     Module:     TtGouraud.c                                              **
 **                                                                          **
 **     Purpose:    Empty rasterizer drawing engine.                         **
 **                 Methods for drawing Gouraud-shaded triangles.            **
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
 * Draw a Gouraud-shaded triangle.
 ***********************************************************************************************/

void TtDrawTriGouraud (
    const TQADrawContext    *drawContext,       /* Draw context */
    const TQAVGouraud   *v0,                /* Vertex 0 */
    const TQAVGouraud   *v1,                /* Vertex 1 */
    const TQAVGouraud   *v2,                /* Vertex 2 */
    unsigned long       flags)              /* Flags */
{
    TTtDrawPrivate      *myPrivate;

    myPrivate = (TTtDrawPrivate *) drawContext->drawPrivate;
}
```

[Next](Empty%20Engine%20Code-TtLine.c.md)[Previous](Empty%20Engine%20Code-TtBitmapStore.c.md)

