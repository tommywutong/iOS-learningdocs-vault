---
title: Plug-in  - Sample Renderer
apple_id: DTS10000120
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-_Sample_Renderer/Listings/Headers_SR_ConfigData_h.html
archived_at: '2026-07-18T03:19:17.230673Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  - Sample Renderer](Plug-in%20-%20Sample%20Renderer.md)


[Next](Headers-SRMacDialog.h.md)[Previous](Headers-SRClipUtilities.h.md)

# Headers/SR_ConfigData.h

```c
/******************************************************************************
 **                                                                          **
 **     Module:     SR_ConfigData.h                                          **
 **                                                                          **
 **                                                                          **
 **     Purpose:    Generic sample renderer routines                         **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1996 Apple Computer, Inc.  All rights reserved.        **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/
#ifndef SR_ConfigData_h
#define SR_ConfigData_h

#include "QD3D.h"

TQ3Status SR_GetConfigurationData(
    TQ3RendererObject           renderer, 
    unsigned char               *dataBuffer, 
    unsigned long               bufferSize,
    unsigned long               *actualDataSize,    
    void                        *rendererPrivate);

TQ3Status SR_SetConfigurationData(
    TQ3RendererObject           renderer, 
    unsigned char               *dataBuffer, 
    unsigned long               bufferSize, 
    void                        *rendererPrivate);

#endif  /*  SR_ConfigData_h  */
```

[Next](Headers-SRMacDialog.h.md)[Previous](Headers-SRClipUtilities.h.md)

