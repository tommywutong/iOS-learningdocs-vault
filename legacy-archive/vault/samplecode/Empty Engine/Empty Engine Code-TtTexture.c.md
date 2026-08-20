---
title: Empty Engine
apple_id: DTS10000152
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Empty_Engine/Listings/Empty_Engine_Code_TtTexture_c.html
archived_at: '2026-07-18T03:07:47.474298Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Empty Engine](Empty%20Engine.md)


[Next](Empty%20Engine%20Code-TtTextureStore.c.md)[Previous](Empty%20Engine%20Code-TtState.c.md)

# Empty Engine Code/TtTexture.c

```c
/******************************************************************************
 **                                                                          **
 **     Module:     TtTexture.c                                              **
 **                                                                          **
 **     Purpose:    Empty rasterizer drawing engine.                         **
 **                 Methods for texture-mapped triangles.                    **
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

/************************************************************************************************
 * Draw a Texture-mapped triangle.
 ***********************************************************************************************/

void TtDrawTriTexture (
    const TQADrawContext    *drawContext,       /* Draw context */
    const TQAVTexture   *v0,                /* Vertex 0 */
    const TQAVTexture   *v1,                /* Vertex 1 */
    const TQAVTexture   *v2,                /* Vertex 2 */
    unsigned long       flags)              /* Flags */
{
    TTtDrawPrivate      *myPrivate;
    TTtTexture          *texture;

    myPrivate = (TTtDrawPrivate *) drawContext->drawPrivate;
    texture = (TTtTexture *) myPrivate->state [kQATag_Texture].i;
}
```

[Next](Empty%20Engine%20Code-TtTextureStore.c.md)[Previous](Empty%20Engine%20Code-TtState.c.md)

