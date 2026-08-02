---
title: Plug-in  -QuickDraw Renderer
apple_id: DTS10000122
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-QuickDraw_Renderer/Listings/IRS_Geometry_h.html
archived_at: '2026-07-18T03:19:16.184657Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  -QuickDraw Renderer](Plug-in%20-QuickDraw%20Renderer.md)


[Next](IRSMetaHandler.c.md)[Previous](IRSGeometry.c.md)

# IRS_Geometry.h

```c
/******************************************************************************\

        Module:     IRS_Geometry.h                                          

        Purpose:    plug-in renderer for QD3D: geometry rendering                               

        Author:     Sun-Inn Shih                                        

        Copyright (C) 1993-96 Apple Computer, Inc.  All rights reserved.    

\*****************************************************************************/
#ifndef IRS_GEOMETRY_H
#define IRS_GEOMETRY_H

#include <QD3D.h>
#include <QD3DGeometry.h>
#include "IRShell.h"

/*
 *  IRS_Geometry_Triangle 
 */
TQ3Status IRS_Geometry_Triangle(
    TQ3ViewObject       pView,
    irsData             *irsdata,
    TQ3GeometryObject   pGeom, 
    TQ3TriangleData     *pTriangleData);

/*
 *  IRS_Geometry_Line 
 */
TQ3Status IRS_Geometry_Line(
    TQ3ViewObject       pView,
    irsData             *irsdata,
    TQ3GeometryObject   pGeom, 
    TQ3LineData         *pLineData);

/*
 *  IRS_Geometry_Point 
 */
TQ3Status IRS_Geometry_Point(
    TQ3ViewObject       pView,
    irsData             *irsdata,
    TQ3GeometryObject   pGeom, 
    TQ3PointData        *pPointData);
/*
 *  IRS_Geometry_Marker 
 */
TQ3Status IRS_Geometry_Marker(
    TQ3ViewObject       pView,
    irsData             *irsdata,
    TQ3GeometryObject   pGeom, 
    TQ3MarkerData       *pMarkerData);
/*
 *  IRS_Geometry_PixmapMarker 
 */
TQ3Status IRS_Geometry_PixmapMarker(
    TQ3ViewObject       pView,
    irsData                 *irsdata,
    TQ3GeometryObject   pGeom, 
    TQ3PixmapMarkerData *pPixmapMarkerData);

TQ3Status IRS_Geometry_TM (
                                TQ3ViewObject       pView,
                                irsData             *irsdata,
                                TQ3GeometryObject   pGeom, 
                                TQ3TriMeshData      *pTriMeshData ) ;

#endif
```

[Next](IRSMetaHandler.c.md)[Previous](IRSGeometry.c.md)

