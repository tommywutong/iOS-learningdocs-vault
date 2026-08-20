---
title: Plug-in  - Sample Renderer
apple_id: DTS10000120
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-_Sample_Renderer/Listings/Headers_SR_Marker_h.html
archived_at: '2026-07-18T03:19:17.415148Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  - Sample Renderer](Plug-in%20-%20Sample%20Renderer.md)


[Next](Headers-SRMarkerRenderer.h.md)[Previous](Headers-SRMacDialog.h.md)

# Headers/SR_Marker.h

```c
/******************************************************************************
 **                                                                          **
 **     Module:     SR_Marker.h                                              **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Purpose:    Private data types for markers                           **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1996 Apple Computer, Inc. All rights reserved.         ** 
 **                                                                          **
 **                                                                          **
 *****************************************************************************/
#ifndef SR_Marker_h
#define SR_Marker_h

#include "QD3D.h"

#ifdef __cplusplus
extern "C" {
#endif  /* __cplusplus */

typedef struct TSRMarkerRasterData {
    long                startRowSkip;
    long                endRowSkip; 
    long                startLineSkip;
    long                endLineSkip;
    TQ3Bitmap           *bitmap;
} TSRMarkerRasterData;

typedef struct TSRPixmapMarkerRasterData {
    long                startRowSkip;
    long                endRowSkip;
    long                startLineSkip;
    long                endLineSkip;
    TQ3StoragePixmap    *pixmap;
} TSRPixmapMarkerRasterData;

#ifdef __cplusplus
}
#endif  /* __cplusplus */

#endif  /*  SR_Marker_h  */
```

[Next](Headers-SRMarkerRenderer.h.md)[Previous](Headers-SRMacDialog.h.md)

