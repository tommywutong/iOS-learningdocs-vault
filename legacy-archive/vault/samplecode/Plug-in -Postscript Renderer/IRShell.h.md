---
title: Plug-in -Postscript Renderer
apple_id: DTS10000123
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in_-Postscript_Renderer/Listings/IRShell_h.html
archived_at: '2026-07-18T03:19:15.026337Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in -Postscript Renderer](Plug-in%20-Postscript%20Renderer.md)


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

typedef struct irsData
{
    TQ3Matrix4x4 localToFrustum;
    FILE    *filePtr;
    float   center;
    float   scale;
} irsData;

extern irsData* gdata;

#endif
```

[Next](Document%20Revision%20History.md)[Previous](IRSUpdate.h.md)

