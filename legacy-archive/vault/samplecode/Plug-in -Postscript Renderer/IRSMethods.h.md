---
title: Plug-in -Postscript Renderer
apple_id: DTS10000123
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in_-Postscript_Renderer/Listings/IRS_Methods_h.html
archived_at: '2026-07-18T03:19:14.869942Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in -Postscript Renderer](Plug-in%20-Postscript%20Renderer.md)


[Next](IRSRegister.c.md)[Previous](IRSMethods.c.md)

# IRS_Methods.h

```c
/******************************************************************************\

        Module:     IRS_Methods.h                                           

        Purpose:    top level meta handler function for QD3D plug-in renderer                               

        Author:     Sun-Inn Shih                                    

        Copyright (C) 1993-96 Apple Computer, Inc.  All rights reserved.    

\*****************************************************************************/
#ifndef PF_METHODS_H
#define PF_METHODS_H

#include <QD3D.h>
#include <QD3DView.h>

#include "IRShell.h"

TQ3Status IRSNew(
    TQ3RendererObject       pRenderer,
    irsData                 *irsdata,
    void                    *pInitData);

void IRSDelete(
    TQ3RendererObject       PerformRenderer,
    irsData                 *irsdata);

TQ3Status IRSStartFrame(
    TQ3ViewObject           pView,
    irsData                 *irsdata,
    TQ3DrawContextObject    pQD3DDrawContext);

TQ3Status IRSEndFrame(
    TQ3ViewObject           pView,
    irsData                 *irsdata,
    TQ3DrawContextObject    pQD3DDrawContext);

TQ3Status IRSStartPass(
    TQ3ViewObject           pView,
    irsData                 *irsdata,
    TQ3CameraObject         pCamera,
    TQ3GroupObject          pLightGroup);

TQ3ViewStatus IRSEndPass(
    TQ3ViewObject           pView,
    irsData                 *irsdata);

void IRSCancel(
    TQ3ViewObject            pView,
    irsData                 *irsdata);

#endif /* PF_METHODS_H */
```

[Next](IRSRegister.c.md)[Previous](IRSMethods.c.md)

