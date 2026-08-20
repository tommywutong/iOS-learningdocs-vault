---
title: Plug-in  - Sample Renderer
apple_id: DTS10000120
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-_Sample_Renderer/Listings/Headers_SR_Math_h.html
archived_at: '2026-07-18T03:19:17.442667Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  - Sample Renderer](Plug-in%20-%20Sample%20Renderer.md)


[Next](Headers-SRPixmapMarkerRenderer.h.md)[Previous](Headers-SRMarkerRenderer.h.md)

# Headers/SR_Math.h

```c
/******************************************************************************
 **                                                                          **
 **     Module:     SR_Math.h                                                **
 **                                                                          **
 **                                                                          **
 **     Purpose:    Sample renderer math routines                            **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1992-1996 Apple Computer, Inc.  All rights reserved.   **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/
#ifndef SR_Math_h
#define SR_Math_h

#include "QD3D.h"
#include "QD3DGeometry.h"

#ifdef __cplusplus
extern "C" {
#endif  /* __cplusplus */


typedef struct TSRVector4D {
    float       x;
    float       y;
    float       z;
    float       w;
} TSRVector4D;

TQ3Status SRTriangle_GetNormal(
    TQ3TriangleData     *triangleData,
    TQ3Vector3D         *normal);

void SRMatrix_LUDecomposeSingular3x3(
    float               matrix[3][3],
    long                indexPtr[3],
    float               *rowInterchanges,
    long                *rank);

TQ3Status SRMatrix_ComputeFlatLand(
    TQ3Matrix4x4        *matrix,
    TQ3Matrix3x3        *luDecomp,
    TQ3Boolean          parallelProjection,
    TSRVector4D         *eyeVectorWC,
    TQ3RationalPoint4D  *eyePointWC,
    TSRVector4D         *eyeVectorLC,
    TQ3PlaneEquation    *flatWorld);

TSRVector4D *SRVector4D_Set(
    TSRVector4D         *vector4D,
    float               x, 
    float               y,
    float               z, 
    float               w);

TSRVector4D *SRVector3D_To4D(
    const TQ3Vector3D   *vector3D,
    TSRVector4D         *result);

TQ3Vector3D *SRVector4D_To3D(
    const TSRVector4D   *vector4D,
    TQ3Vector3D         *result);

TSRVector4D *SRVector4D_Negate(
    const TSRVector4D   *vector4D,
    TSRVector4D         *result);

TSRVector4D *SRVector4D_Normalize(
    const TSRVector4D   *vector4D,
    TSRVector4D         *result);

TSRVector4D *SRVector4D_Transform(
    const TSRVector4D   *vector4D,
    const TQ3Matrix4x4  *matrix4x4,
    TSRVector4D         *result);

#ifdef __cplusplus
}
#endif  /* __cplusplus */

#endif  /*  SR_Math_h  */
```

[Next](Headers-SRPixmapMarkerRenderer.h.md)[Previous](Headers-SRMarkerRenderer.h.md)

