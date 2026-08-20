---
title: Plug-in  - Sample Renderer
apple_id: DTS10000120
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-_Sample_Renderer/Listings/Source_SR_MarkerRasterize_32_c.html
archived_at: '2026-07-18T03:19:18.619314Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  - Sample Renderer](Plug-in%20-%20Sample%20Renderer.md)


[Next](Source-SRMarkerRasterize8.c.md)[Previous](Source-SRMarker.c.md)

# Source/SR_MarkerRasterize_32.c

```c
/******************************************************************************
 **                                                                          **
 **     Module:     SR_MarkerRasterize_32.c                                  **
 **                                                                          **
 **                                                                          **
 **     Purpose:    Marker rasterization.                                    **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1996 Apple Computer, Inc.  All rights reserved.        **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/

#define SR_RASTERIZE_32BITS

    #undef SR_WIN_CLIP
        #include "SR_MarkerRenderer.h"

    #define SR_WIN_CLIP
        #include "SR_MarkerRenderer.h"
    #undef SR_WIN_CLIP

#undef SR_RASTERIZE_32BITS
```

[Next](Source-SRMarkerRasterize8.c.md)[Previous](Source-SRMarker.c.md)

