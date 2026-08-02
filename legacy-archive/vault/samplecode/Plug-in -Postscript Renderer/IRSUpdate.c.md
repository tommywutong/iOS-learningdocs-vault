---
title: Plug-in -Postscript Renderer
apple_id: DTS10000123
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in_-Postscript_Renderer/Listings/IRS_Update_c.html
archived_at: '2026-07-18T03:19:14.945502Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in -Postscript Renderer](Plug-in%20-Postscript%20Renderer.md)


[Next](IRSUpdate.h.md)[Previous](IRSRegister.c.md)

# IRS_Update.c

```c
/******************************************************************************\

        Module:     IRS_Update.c                                            

        Purpose:    update metahandler functions                                

        Author:     Sun-Inn Shih                                        

        Copyright (C) 1993-96 Apple Computer, Inc.  All rights reserved.    

\*****************************************************************************/

#include <QD3D.h>
#include "IRS_Update.h"

/*
 *  IRS_Update_Matrix_localToFrustum
 */
TQ3Status IRS_Update_Matrix_localToFrustum(
    TQ3ViewObject           pView,
    irsData                 *irsdata,
    TQ3Matrix4x4            *pData)
{
    irsdata->localToFrustum = *pData;

    return kQ3Success;
}
```

[Next](IRSUpdate.h.md)[Previous](IRSRegister.c.md)

