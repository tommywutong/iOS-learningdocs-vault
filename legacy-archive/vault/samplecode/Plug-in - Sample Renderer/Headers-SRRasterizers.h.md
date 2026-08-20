---
title: Plug-in  - Sample Renderer
apple_id: DTS10000120
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-_Sample_Renderer/Listings/Headers_SR_Rasterizers_h.html
archived_at: '2026-07-18T03:19:17.678850Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  - Sample Renderer](Plug-in%20-%20Sample%20Renderer.md)


[Next](Headers-SRWinDialog.h.md)[Previous](Headers-SRPrefixFile.h.md)

# Headers/SR_Rasterizers.h

```c
/******************************************************************************
 **                                                                          **
 **     Module:     SR_Rasterizers.h                                         **
 **                                                                          **
 **                                                                          **
 **     Purpose:    Sample Renderer rasterizer function declarations         **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1996 Apple Computer, Inc.  All rights reserved.        **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/
#ifndef SR_Rasterizers_h
#define SR_Rasterizers_h

#include "SR.h"
#include "SR_Marker.h"

#ifdef __cplusplus
extern "C" {
#endif  /* __cplusplus */


/******************************************************************************
 **                                                                          **
 **                         Line Rasterization Functions                     **
 **                                                                          **
 *****************************************************************************/

TQ3Status SRLine_Rasterize_32(
    const struct TSRPrivate         *srPrivate, 
    const TQ3Point3D                *pt0, 
    const TQ3Point3D                *pt1, 
    const TQ3ColorRGB               *lineColorRGB);

TQ3Status SRLine_Rasterize_32_WClip(
    const struct TSRPrivate         *srPrivate, 
    const TQ3Point3D                *pt0, 
    const TQ3Point3D                *pt1, 
    const TQ3ColorRGB               *lineColorRGB);

TQ3Status SRLine_Rasterize_8(
    const struct TSRPrivate         *srPrivate, 
    const TQ3Point3D                *pt0, 
    const TQ3Point3D                *pt1, 
    const TQ3ColorRGB               *lineColorRGB);

TQ3Status SRLine_Rasterize_8_WClip(
    const struct TSRPrivate         *srPrivate, 
    const TQ3Point3D                *pt0, 
    const TQ3Point3D                *pt1, 
    const TQ3ColorRGB               *lineColorRGB);

TQ3Status SRLine_Rasterize_Null(
    const struct TSRPrivate         *srPrivate, 
    const TQ3Point3D                *pt0, 
    const TQ3Point3D                *pt1, 
    const TQ3ColorRGB               *lineColorRGB);


/******************************************************************************
 **                                                                          **
 **                         Point Rasterization Functions                    **
 **                                                                          **
 *****************************************************************************/

TQ3Status SRPoint_Rasterize_32(
    const struct TSRPrivate         *srPrivate, 
    const TQ3Point3D                *pt0, 
    const TQ3ColorRGB               *pointColorRGB);

TQ3Status SRPoint_Rasterize_32_WClip(
    const struct TSRPrivate         *srPrivate, 
    const TQ3Point3D                *pt0, 
    const TQ3ColorRGB               *pointColorRGB);

TQ3Status SRPoint_Rasterize_8(
    const struct TSRPrivate         *srPrivate, 
    const TQ3Point3D                *pt0, 
    const TQ3ColorRGB               *pointColorRGB);

TQ3Status SRPoint_Rasterize_8_WClip(
    const struct TSRPrivate         *srPrivate, 
    const TQ3Point3D                *pt0, 
    const TQ3ColorRGB               *pointColorRGB);

TQ3Status SRPoint_Rasterize_Null(
    const struct TSRPrivate         *srPrivate, 
    const TQ3Point3D                *pt0, 
    const TQ3ColorRGB               *pointColorRGB);    


/******************************************************************************
 **                                                                          **
 **                         Marker Rasterization Functions                   **
 **                                                                          **
 *****************************************************************************/

TQ3Status SRMarker_Rasterize_32(
    const struct TSRPrivate         *srPrivate,
    const TQ3Point3D                *pt0,
    const TSRMarkerRasterData       *bitmap,
    const TQ3ColorRGB               *pointColorRGB);

TQ3Status SRMarker_Rasterize_32_WClip(
    const struct TSRPrivate         *srPrivate,
    const TQ3Point3D                *pt0,
    const TSRMarkerRasterData       *bitmap,
    const TQ3ColorRGB               *pointColorRGB);

TQ3Status SRMarker_Rasterize_8( 
    const struct TSRPrivate         *srPrivate,
    const TQ3Point3D                *pt0,
    const TSRMarkerRasterData       *bitmap,
    const TQ3ColorRGB               *pointColorRGB);

TQ3Status SRMarker_Rasterize_8_WClip( 
    const struct TSRPrivate         *srPrivate,
    const TQ3Point3D                *pt0,
    const TSRMarkerRasterData       *bitmap,
    const TQ3ColorRGB               *pointColorRGB);

TQ3Status SRMarker_Rasterize_Null(
    const struct TSRPrivate         *srPrivate, 
    const TQ3Point3D                *pt0, 
    const TSRMarkerRasterData       *bitmap, 
    const TQ3ColorRGB               *pointColorRGB);


/******************************************************************************
 **                                                                          **
 **                 Pixmap Marker Rasterization Functions                    **
 **                                                                          **
 *****************************************************************************/

TQ3Status SRPixmapMarker_Rasterize_32(
    const struct TSRPrivate         *srPrivate,
    const TQ3Point3D                *pt0,
    const TSRPixmapMarkerRasterData *pixmap,
    const TQ3ColorRGB               *highlightColor);

TQ3Status SRPixmapMarker_Rasterize_32_WClip(
    const struct TSRPrivate         *srPrivate,
    const TQ3Point3D                *pt0,
    const TSRPixmapMarkerRasterData *pixmap,
    const TQ3ColorRGB               *highlightColor);

TQ3Status SRPixmapMarker_Rasterize_8( 
    const struct TSRPrivate         *srPrivate,
    const TQ3Point3D                *pt0,
    const TSRPixmapMarkerRasterData *pixmap,
    const TQ3ColorRGB               *highlightColor);

TQ3Status SRPixmapMarker_Rasterize_8_WClip( 
    const struct TSRPrivate         *srPrivate,
    const TQ3Point3D                *pt0,
    const TSRPixmapMarkerRasterData *pixmap,
    const TQ3ColorRGB               *highlightColor);

TQ3Status SRPixmapMarker_Rasterize_Null(
    const struct TSRPrivate         *srPrivate, 
    const TQ3Point3D                *pt0, 
    const TSRPixmapMarkerRasterData *pixmap,
    const TQ3ColorRGB               *highlightColor);


#ifdef __cplusplus
}
#endif  /* __cplusplus */

#endif  /*  SR_Rasterizers_h  */
```

[Next](Headers-SRWinDialog.h.md)[Previous](Headers-SRPrefixFile.h.md)

