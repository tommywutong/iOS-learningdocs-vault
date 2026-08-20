---
title: Empty Engine
apple_id: DTS10000152
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Empty_Engine/Listings/Empty_Engine_Code_TtLine_c.html
archived_at: '2026-07-18T03:07:47.011105Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Empty Engine](Empty%20Engine.md)


[Next](Empty%20Engine%20Code-TtPoint.c.md)[Previous](Empty%20Engine%20Code-TtGouraud.c.md)

# Empty Engine Code/TtLine.c

```c
/******************************************************************************
 **                                                                          **
 **     Module:     TtLine.c                                                 **
 **                                                                          **
 **     Purpose:    Empty rasterizer drawing engine.                         **
 **                 Methods for drawing lines.                               **
 **                                                                          **
 **     Author:     Mike Kelley                                              **
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

/************************************************************************************************
 * Draw a line.
 ***********************************************************************************************/

void TtDrawLine (
    const TQADrawContext    *drawContext,       /* Draw context */
    const TQAVGouraud   *v0,                /* Vertex 0 */
    const TQAVGouraud   *v1)                /* Vertex 1 */
{
    TTtDrawPrivate      *myPrivate;

    myPrivate = (TTtDrawPrivate *) drawContext->drawPrivate;
}
```

[Next](Empty%20Engine%20Code-TtPoint.c.md)[Previous](Empty%20Engine%20Code-TtGouraud.c.md)

