---
title: Plug-in  -QuickDraw Renderer
apple_id: DTS10000122
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-QuickDraw_Renderer/Listings/IRS_Update_c.html
archived_at: '2026-07-18T03:19:16.466819Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  -QuickDraw Renderer](Plug-in%20-QuickDraw%20Renderer.md)


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
#include <QD3DDrawContext.h>
#include <QD3DView.h>
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

    irsdata->XScale = 1.0f ;
    irsdata->YScale = 1.0f ;

    irsdata->XOffset = 0 ;
    irsdata->YOffset = 0 ;

    TQ3DrawContextObject DrawContext ;
    if ( Q3View_GetDrawContext ( pView , &DrawContext ) != kQ3Failure )
        {
        TQ3DrawContextData Data ;
        if ( Q3DrawContext_GetData ( DrawContext , &Data ) != kQ3Failure )
            {
            irsdata->XScale = ( Data.pane.max.x - Data.pane.min.x ) / 2.0f ;
            irsdata->YScale = ( Data.pane.max.y - Data.pane.min.y ) / 2.0f ;

            irsdata->XOffset = Data.pane.min.x + irsdata->XScale ;
            irsdata->YOffset = Data.pane.max.y - irsdata->YScale ;
            }
        }
    return kQ3Success;
    }
```

[Next](IRSUpdate.h.md)[Previous](IRSRegister.c.md)

