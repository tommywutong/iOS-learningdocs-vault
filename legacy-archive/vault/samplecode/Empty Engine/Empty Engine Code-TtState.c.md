---
title: Empty Engine
apple_id: DTS10000152
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Empty_Engine/Listings/Empty_Engine_Code_TtState_c.html
archived_at: '2026-07-18T03:07:47.343095Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Empty Engine](Empty%20Engine.md)


[Next](Empty%20Engine%20Code-TtTexture.c.md)[Previous](Empty%20Engine%20Code-TtRender.c.md)

# Empty Engine Code/TtState.c

```c
/******************************************************************************
 **                                                                          **
 **     Module:     TtState.c                                                **
 **                                                                          **
 **     Purpose:    Empty rasterizer drawing engine.                         **
 **                 Methods for state variable maintenance.                  **
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
 *  TtSetFloat.
 ***********************************************************************************************/

void TtSetFloat (
    TQADrawContext      *drawContext,       /* Draw context */
    TQATagFloat         tag,                /* Tag of variable to set */
    float               newValue)           /* New value for variable */
{
    TTtDrawPrivate      *myPrivate;

    if (tag > kTtMaxTag)
    {
        /*
         * Tag value is out of range; no-op.
         */

        return;
    }
    myPrivate = (TTtDrawPrivate *) drawContext->drawPrivate;
    myPrivate->state [tag].f = newValue;

    /*
     * Note that this function received a TQADrawContext pointer which is _not_ const.
     * This means you can change the methods based on the set operation.
     */
}

/************************************************************************************************
 *  TtSetInt
 ***********************************************************************************************/

void TtSetInt (
    TQADrawContext      *drawContext,       /* Draw context */
    TQATagInt           tag,                /* Tag of variable to set */
    unsigned long       newValue)           /* New value for variable */
{
    TTtDrawPrivate      *myPrivate;

    myPrivate = (TTtDrawPrivate *) drawContext->drawPrivate;
    if (tag > kTtMaxTag)
    {
        /*
         * Tag value is out of range; no-op.
         */

        return;
    }
    myPrivate->state [tag].i = newValue;

    /*
     * Note that this function received a TQADrawContext pointer which is _not_ const.
     * This means you can change the methods based on the set operation (e.g., if
     * the texture op is changed)
     */
}

/************************************************************************************************
 *  TtSetPtr
 ***********************************************************************************************/

void TtSetPtr (
    TQADrawContext      *drawContext,       /* Draw context */
    TQATagPtr           tag,                /* Tag of variable to set */
    const void          *newValue)          /* New value for variable */
{
    TTtDrawPrivate      *myPrivate;

    myPrivate = (TTtDrawPrivate *) drawContext->drawPrivate;
    if (tag > kTtMaxTag)
    {
        /*
         * Tag value is out of range; no-op.
         */

        return;
    }
    myPrivate->state [tag].p = newValue;

    /*
     * Note that this function received a TQADrawContext pointer which is _not_ const.
     * This means you can change the methods based on the set operation (e.g., if
     * the texture op is changed)
     */
}

/************************************************************************************************
 *  TtGetFloat
 ***********************************************************************************************/

float TtGetFloat (
    const TQADrawContext    *drawContext,       /* Draw context */
    TQATagFloat             tag)                /* Tag of variable to get */
{
    TTtDrawPrivate      *myPrivate;

    if (tag > kTtMaxTag)
    {
        /*
         * Tag value is out of range; return 0.
         */

        return (0);
    }
    myPrivate = (TTtDrawPrivate *) drawContext->drawPrivate;
    return (myPrivate->state [tag].f);
}

/************************************************************************************************
 *  TtGetInt
 ***********************************************************************************************/

unsigned long TtGetInt (
    const TQADrawContext    *drawContext,       /* Draw context */
    TQATagInt               tag)                /* Tag of variable to get */
{
    TTtDrawPrivate      *myPrivate;

    if (tag > kTtMaxTag)
    {
        /*
         * Tag value is out of range; return 0.
         */

        return (0);
    }
    myPrivate = (TTtDrawPrivate *) drawContext->drawPrivate;
    return (myPrivate->state [tag].i);
}

/************************************************************************************************
 *  TtGetPtr
 ***********************************************************************************************/

void *TtGetPtr (
    const TQADrawContext    *drawContext,       /* Draw context */
    TQATagPtr               tag)                /* Tag of variable to get */
{
    TTtDrawPrivate      *myPrivate;

    if (tag > kTtMaxTag)
    {
        /*
         * Tag value is out of range; return 0.
         */

        return (0);
    }
    myPrivate = (TTtDrawPrivate *) drawContext->drawPrivate;
    return ((void *) myPrivate->state [tag].p);
}
```

[Next](Empty%20Engine%20Code-TtTexture.c.md)[Previous](Empty%20Engine%20Code-TtRender.c.md)

