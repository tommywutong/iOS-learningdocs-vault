---
title: Plug-in  -QuickDraw Renderer
apple_id: DTS10000122
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-QuickDraw_Renderer/Listings/IRS_Register_c.html
archived_at: '2026-07-18T03:19:16.434606Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  -QuickDraw Renderer](Plug-in%20-QuickDraw%20Renderer.md)


[Next](IRSUpdate.c.md)[Previous](IRSMethods.h.md)

# IRS_Register.c

```c
/******************************************************************************\

        Module:     IRS_Register.c                                          

        Purpose:    plug-in renderer's registration methods                             

        Author:     Sun-Inn Shih                                        

        Copyright (C) 1993-96 Apple Computer, Inc.  All rights reserved.    

\*****************************************************************************/

#include <QD3D.h>
#include <QD3DRenderer.h>
#include <QD3DExtension.h>
#include "IRS_MetaHandler.h"
#include "IRShell.h"

TQ3XObjectClass RendererClass;

#include <CodeFragments.h>

extern "C" {
OSErr IRSRegister(
    void);

long IRSExit(
    void);
}
/*===========================================================================*\
 *
 *  Routine:    IRSRegister()
 *
 *  Purpose: Register an object class in the QuickDraw 3D hierarchy.
 *
 *  QD3D calls: Q3XObjectHierarchy_RegisterClass() in QD3DExtentionl.h
 *
\*===========================================================================*/
OSErr IRSRegister(
    void)
{
    TQ3ObjectType   classType;                      /* This is returned from QD3D */

    RendererClass =
            Q3XObjectHierarchy_RegisterClass(       /* register into QD3D hierarchy */
                kQ3SharedTypeRenderer,              /* parent type - a existing type */
                &classType,                         /* the new object class type */
                "IR Shell",                         /* name, used in the text metafile */
                IRSMetaHandler,                     /* metahandler */               
                NULL,                               /* virtual meta handler*/   
                0,                                  /* methods Size */
                sizeof(struct irsData));            /* size of the object instandce data */

    if(RendererClass == NULL)
    {
        return kQ3Failure;
    }

    return noErr;
}

/*===========================================================================*\
 *
 *  Routine:    IRSExit()
 *
 *  Comments:   exit share library
 *
\*===========================================================================*/

long IRSExit(
    void)
{
    return 0;
}
```

[Next](IRSUpdate.c.md)[Previous](IRSMethods.h.md)

