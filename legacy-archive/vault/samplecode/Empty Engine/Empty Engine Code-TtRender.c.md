---
title: Empty Engine
apple_id: DTS10000152
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Empty_Engine/Listings/Empty_Engine_Code_TtRender_c.html
archived_at: '2026-07-18T03:07:47.106154Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Empty Engine](Empty%20Engine.md)


[Next](Empty%20Engine%20Code-TtState.c.md)[Previous](Empty%20Engine%20Code-TtPoint.c.md)

# Empty Engine Code/TtRender.c

```c
/******************************************************************************
 **                                                                          **
 **     Module:     TtRender.c                                               **
 **                                                                          **
 **     Purpose:    Empty rasterizer drawing engine.                         **
 **                 Methods for starting and ending rendering, and for       **
 **                 flush and sync.                                          **
 **                                                                          **
 **     Author:     Mike W. Kelley                                           **
 **                                                                          **
 **                 2/3/95  Revised for 0.9 SDK release                      **
 **                                                                          **
 **     Copyright (C) 1994-95 Apple Computer, Inc.  All rights reserved.     **
 **     Apple Computer Confidential                                          **
 **                                                                          **
 *****************************************************************************/

/* Private */
#include "RAVE.h"
#include "RAVE_system.h"
#include "TtTinselTown.h"

/************************************************************************************************
 *  TtRenderStart
 ***********************************************************************************************/

void TtRenderStart (
    const TQADrawContext    *drawContext,       /* Draw context */
    const TQARect       *dirtyRect,         /* Minimum area to clear; NULL means whole buffer */
    const TQADrawContext    *initialContext)    /* Initial background image (or NULL) */
{
    TTtDrawPrivate      *myPrivate;

    myPrivate = (TTtDrawPrivate *) drawContext->drawPrivate;

    /*
     * Initialize the ARGB and Z buffers for rendering.
     *
     * If this is a single-buffered context, and we're drawing directly to the screen,
     * and we don't have a hardware cursor, this is a good time to do a ShieldCursor().
     */
}

/************************************************************************************************
 *  TtRenderEnd
 ***********************************************************************************************/

TQAError TtRenderEnd (
    const TQADrawContext    *drawContext,       /* Draw context */
    const TQARect       *modifiedRect)      /* Minimum area to swap; NULL means whole buffer */
{
    TTtDrawPrivate      *myPrivate;

    myPrivate = (TTtDrawPrivate *) drawContext->drawPrivate;

    /*
     * If this is double-buffered, display the back buffer. If we called ShieldCursor()
     * in TtRenderStart(), now's the time to call ShowCursor(). Note that this call
     * isn't blocking -- for example, we could start a back-to-front buffer blit and
     * then return. (If the app wants blocking behavior, TtSync() will be called.)
     *
     * RenderEnd returns an error value. If there were no errors on this frame,
     * kQANoErr should be returned.
     */

    return (kQANoErr);
}

/************************************************************************************************
 * Abort any current rendering in progress.
 ***********************************************************************************************/

TQAError TtRenderAbort (
    const TQADrawContext    *drawContext)       /* Draw context */
{
    TTtDrawPrivate      *myPrivate;

    myPrivate = (TTtDrawPrivate *) drawContext->drawPrivate;

    /*
     * Kill any rendering commands, free any resources, and recover.
     */

    return (kQANoErr);
}

/************************************************************************************************
 *  TtFlush
 ***********************************************************************************************/

TQAError TtFlush (
    const TQADrawContext    *drawContext)       /* Draw context */
{
    TTtDrawPrivate      *myPrivate;

    myPrivate = (TTtDrawPrivate *) drawContext->drawPrivate;

    /*
     * If rendering commands are queued, start running them.
     */

    return (kQANoErr);
}

/************************************************************************************************
 *  TtSync
 ***********************************************************************************************/

TQAError TtSync (
    const TQADrawContext    *drawContext)       /* Draw context */
{
    TTtDrawPrivate      *myPrivate;

    myPrivate = (TTtDrawPrivate *) drawContext->drawPrivate;

    /*
     * Don't return until all outstanding rendering is complete. Note that this may
     * be called after TtRenderEnd().
     */

    return (kQANoErr);
}
```

[Next](Empty%20Engine%20Code-TtState.c.md)[Previous](Empty%20Engine%20Code-TtPoint.c.md)

