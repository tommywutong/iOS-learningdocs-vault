---
title: Empty Engine
apple_id: DTS10000152
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Empty_Engine/Listings/Empty_Engine_Code_TtTextureStore_c.html
archived_at: '2026-07-18T03:07:47.435183Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Empty Engine](Empty%20Engine.md)


[Next](Empty%20Engine%20Code-TtTinselTown.c.md)[Previous](Empty%20Engine%20Code-TtTexture.c.md)

# Empty Engine Code/TtTextureStore.c

```c
/******************************************************************************
 **                                                                          **
 **     Module:     TtTextureStore.c                                         **
 **                                                                          **
 **     Purpose:    Empty rasterizer drawing engine.                         **
 **                 Methods for texture New, Detach and Delete.              **
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
 * Allocate a texture.
 *************************************************************************************/

TQAError TtTextureNew (
    unsigned long       flags,              /* Mask of kQATexture_xxx flags */
    TQAImagePixelType   pixelType,          /* Depth, color space, etc. */
    const TQAImage      images[],           /* Image(s) for texture */
    TQATexture          **newTexture)       /* (Out) Newly created TQATexture, or NULL on error */ 
{
    /*
     * Allocate new texture memory, and assign new texture pointer to 'newTexture'.
     * For now we assign NULL and return an error (as this function isn't
     * yet implemented).
     */

    *newTexture = NULL;
    return (kQANotSupported);
}

/**************************************************************************************
 * Detach a texture (by copying the image data).
 *************************************************************************************/

TQAError TtTextureDetach (
    TQATexture          *texture)           /* Previously allocated by QATextureNew() */
{
    TTtTexture          *myTexture;

    myTexture = (TTtTexture *) texture;

    /*
     * Copy the image data. Not implemented, so for now we return an error.
     */

    return (kQANotSupported);
}

/**************************************************************************************
 * Delete a texture.
 *************************************************************************************/

void TtTextureDelete (
    TQATexture          *texture)           /* Previously allocated by QATextureNew() */
{
    TTtTexture          *myTexture;

    myTexture = (TTtTexture *) texture;

    /*
     * Delete the texture. Not yet implemented.
     */
}
```

[Next](Empty%20Engine%20Code-TtTinselTown.c.md)[Previous](Empty%20Engine%20Code-TtTexture.c.md)

