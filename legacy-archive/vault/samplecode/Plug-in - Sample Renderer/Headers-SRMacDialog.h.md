---
title: Plug-in  - Sample Renderer
apple_id: DTS10000120
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-_Sample_Renderer/Listings/Headers_SR_MacDialog_h.html
archived_at: '2026-07-18T03:19:17.274144Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  - Sample Renderer](Plug-in%20-%20Sample%20Renderer.md)


[Next](Headers-SRMarker.h.md)[Previous](Headers-SRConfigData.h.md)

# Headers/SR_MacDialog.h

```c
/******************************************************************************
 **                                                                          **
 **     Module:     SR_MacDialog.h                                           **
 **                                                                          **
 **                                                                          **
 **     Purpose:    Modal dialog routines, and other Macintosh specific      **
 **                 routines                                                 **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1996 Apple Computer, Inc.  All rights reserved.        **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/

#ifndef SR_MacDialog_h
#define SR_MacDialog_h

#include "QD3D.h"

#define SR_NAME_RESOURCE    16211   /* the ID of the resource string for
                                     * this renderer's name
                                     */

TQ3Status SR_GetNameString(
    unsigned char               *dataBuffer, 
    unsigned long               bufferSize,
    unsigned long               *actualDataSize);

TQ3Status SR_MacModalDialog(
    TQ3RendererObject           renderer,
    TQ3DialogAnchor             dialogAnchor, 
    TQ3Boolean                  *canceled,  
    void                        *rendererPrivate);


#endif  /*  SR_MacDialog_h  */
```

[Next](Headers-SRMarker.h.md)[Previous](Headers-SRConfigData.h.md)

