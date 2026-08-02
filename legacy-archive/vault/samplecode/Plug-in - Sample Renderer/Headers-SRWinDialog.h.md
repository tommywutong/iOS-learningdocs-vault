---
title: Plug-in  - Sample Renderer
apple_id: DTS10000120
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-_Sample_Renderer/Listings/Headers_SR_WinDialog_h.html
archived_at: '2026-07-18T03:19:17.748723Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  - Sample Renderer](Plug-in%20-%20Sample%20Renderer.md)


[Next](Source-SR.c.md)[Previous](Headers-SRRasterizers.h.md)

# Headers/SR_WinDialog.h

```c
/******************************************************************************
 **                                                                          **
 **     Module:     SR_WinDialog.h                                           **
 **                                                                          **
 **                                                                          **
 **     Purpose:    Modal dialog routines                                    **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1996 Apple Computer, Inc.  All rights reserved.        **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/
#ifndef SR_WinDialog_h
#define SR_WinDialog_h

#include "QD3D.h"


TQ3Status SR_WinModalDialog(
    TQ3RendererObject           renderer,
    TQ3DialogAnchor             dialogAnchor, 
    TQ3Boolean                  *canceled,  
    void                        *rendererPrivate);


#endif  /*  SR_WinDialog_h  */
```

[Next](Source-SR.c.md)[Previous](Headers-SRRasterizers.h.md)

