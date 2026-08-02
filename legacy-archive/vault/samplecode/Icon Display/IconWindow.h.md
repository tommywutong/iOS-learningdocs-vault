---
title: Icon Display
apple_id: DTS10000085
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/Icon_Display/Listings/IconWindow_h.html
archived_at: '2026-07-18T03:12:15.975035Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Icon Display](Icon%20Display.md)


[Next](Document%20Revision%20History.md)[Previous](IconWindow.c.md)

# IconWindow.h

```c
/*
    File:       IconWindow.h

    Contains:   

    Written by:     

    Copyright:  Copyright © 1984-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/9/1999    Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#pragma once
#include <MacTypes.h>
#include <Windows.h>
void SetUpWindow();
Boolean RectNotInGrayRgn(Rect *r);
void FindNewDevice(WindowPtr    wind);
void MakeANewGWorld(Rect *r);
void DrawIcResources();
void DrawBullseye(short active);
```

[Next](Document%20Revision%20History.md)[Previous](IconWindow.c.md)

