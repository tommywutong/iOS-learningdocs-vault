---
title: Plug-in  - Sample Renderer
apple_id: DTS10000120
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-_Sample_Renderer/Listings/Headers_SR_ClipUtilities_h.html
archived_at: '2026-07-18T03:19:17.194717Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  - Sample Renderer](Plug-in%20-%20Sample%20Renderer.md)


[Next](Headers-SRConfigData.h.md)[Previous](Headers-SR.h.md)

# Headers/SR_ClipUtilities.h

```c
/******************************************************************************
 **                                                                          **
 **     Module:     SR_ClipUtilities.h                                       **
 **                                                                          **
 **                                                                          **
 **     Purpose:                                                             **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1995 Apple Computer, Inc.  All rights reserved.        **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/
#ifndef SR_ClipUtilities_h
#define SR_ClipUtilities_h

#include "SR.h"


#ifdef __cplusplus
extern "C" {
#endif  /* __cplusplus */

/******************************************************************************
 **                                                                          **
 **                             Clip Utilities                               **
 **                                                                          **
 *****************************************************************************/

void SR_ClipPlanesInDC(
    TQ3Matrix4x4                *frustumToDC, 
    float                       *clipPlanesInDC);


/******************************************************************************
 **                                                                          **
 **                             Other Routines                               **
 **                                                                          **
 *****************************************************************************/

void SRPointList_WDivide(
    TQ3RationalPoint4D  *in, 
    unsigned long       numVertices, 
    unsigned long       sizeOfIn);

void SRPointList_ClipTestVertices(
    TQ3RationalPoint4D  *deviceVertices,  
    unsigned long       *clipFlags, 
    long                numVertices, 
    float               *clipPlanesInDC, 
    long                *clipFound, 
    long                *allOut, 
    unsigned long       sizeOfIn);

void SRPointList_ClipVertices(
    TQ3RationalPoint4D  *vertices, 
    long                sizeOfVertex,
    TQ3RationalPoint4D  *clipVertices, 
    long                sizeOfClippedVertex,
    unsigned long       *clipFlags, 
    long                *clippedVerticesFlags,
    long                numVertices, 
    long                *numClippedVertices,
    float               *clipPlanes,
    long                mode);


#ifdef __cplusplus
}
#endif  /* __cplusplus */

#endif  /*  SR_ClipUtilities_h  */
```

[Next](Headers-SRConfigData.h.md)[Previous](Headers-SR.h.md)

