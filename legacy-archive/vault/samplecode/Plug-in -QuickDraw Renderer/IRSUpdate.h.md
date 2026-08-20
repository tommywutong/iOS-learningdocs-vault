---
title: Plug-in  -QuickDraw Renderer
apple_id: DTS10000122
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-QuickDraw_Renderer/Listings/IRS_Update_h.html
archived_at: '2026-07-18T03:19:16.500788Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  -QuickDraw Renderer](Plug-in%20-QuickDraw%20Renderer.md)


[Next](IRShell.h.md)[Previous](IRSUpdate.c.md)

# IRS_Update.h

```c
/******************************************************************************\

        Module:     IRS_Update.h                                            

        Purpose:    update metahandler functions for QD3D plug-in renderer                              

        Author:     Sun-Inn Shih                                        

        Copyright (C) 1993-96 Apple Computer, Inc.  All rights reserved.    

\*****************************************************************************/
#ifndef IRS_UPDATE_H
#define IRS_UPDATE_H

#include <QD3D.h>
#include "IRShell.h"

/*
    Matricies
*/
TQ3Status IRS_Update_Matrix_localToFrustum(
    TQ3ViewObject           pView,
    irsData                 *irsdata,
    TQ3Matrix4x4            *pData);

#endif /* IRS_UPDATE_H */
```

[Next](IRShell.h.md)[Previous](IRSUpdate.c.md)

