---
title: ISp SampleOld
apple_id: DTS10000056
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/ISp_SampleOld/Listings/Source_ToolboxUtils_c.html
archived_at: '2026-07-18T03:12:10.619445Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ISp SampleOld](ISp%20SampleOld.md)


[Next](Source-ToolboxUtils.h.md)[Previous](Source-ShellWindow.h.md)

# Source/ToolboxUtils.c

```c
/*
    File:       ToolboxUtils.c

    Contains:   xxx put contents here xxx

    Version:    xxx put version here xxx

    Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.

    File Ownership:

        DRI:                xxx put dri here xxx

        Other Contact:      xxx put other contact here xxx

        Technology:         xxx put technology here xxx

    Writers:

        (BWS)   Brent Schorsch

    Change History (most recent first):

       <SP1>      7/1/99    BWS     first checked in
*/

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Includes

#include <Quickdraw.h>

#include "ToolboxUtils.h"

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Definitions
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Types
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Variables
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Private Functions
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Variables

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    GlobalToLocalRect

void
GlobalToLocalRect(RectPtr ioRect)
{
    GlobalToLocal((Point *) &ioRect->top);
    GlobalToLocal((Point *) &ioRect->bottom);
}

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    LocalToGlobalRect

void
LocalToGlobalRect(RectPtr ioRect)
{
    LocalToGlobal((Point *) &ioRect->top);
    LocalToGlobal((Point *) &ioRect->bottom);
}
```

[Next](Source-ToolboxUtils.h.md)[Previous](Source-ShellWindow.h.md)

