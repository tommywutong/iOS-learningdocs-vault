---
title: Plug-in  -QuickDraw Renderer
apple_id: DTS10000122
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-QuickDraw_Renderer/Listings/IRShell_h.html
archived_at: '2026-07-18T03:19:16.538541Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  -QuickDraw Renderer](Plug-in%20-QuickDraw%20Renderer.md)


[Next](Document%20Revision%20History.md)[Previous](IRSUpdate.h.md)

# IRShell.h

```c
/******************************************************************************\

        Module:     IRShell.h                                           

        Purpose:    Interactive rendering plug-in shell for QD3D                            

        Author:     Sun-Inn Shih                                    

        Copyright (C) 1993-96 Apple Computer, Inc.  All rights reserved.    

\*****************************************************************************/
#ifndef _IRSHELL_H_
#define _IRSHELL_H_
#include <stdio.h>

struct irsData
    {
    TQ3Matrix4x4 localToFrustum ;
    float XScale ;
    float YScale ;
    float XOffset ;
    float YOffset ;
    } ;

extern irsData* gdata;

#endif
```

[Next](Document%20Revision%20History.md)[Previous](IRSUpdate.h.md)

