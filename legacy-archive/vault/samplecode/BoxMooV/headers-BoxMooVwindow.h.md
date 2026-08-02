---
title: BoxMooV
apple_id: DTS10000099
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BoxMooV/Listings/headers_BoxMooV_window_h.html
archived_at: '2026-07-18T03:02:13.945654Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BoxMooV](BoxMooV.md)


[Next](headers-BoxPaintmain.h.md)[Previous](headers-BoxMooVTexture.h.md)

# headers/BoxMooV_window.h

```c
/*  window.h                                                                            

    Michael Bishop - August 21 1996                                                 
    Nick Thompson
    (c)1994-96 Apple Computer Inc., All Rights Reserved                             

*/
#ifndef _WINDOW_H_
#define _WINDOW_H_

#include <QuickDraw.h>

enum {
    kWindowResID = 6347
} ; 

WindowPtr   Window_New(void) ;
void        Window_Delete(WindowPtr theWindow) ;
void        Window_Update( WindowPtr window );
void        Window_Activate(WindowPtr theWindow, short activate);
void        Window_DoContent (WindowPtr theWindow, EventRecord *event);
WindowPtr   Window_GetNextWindow(WindowPtr theWindow);
void        Window_DestroyAll(void);

#endif
```

[Next](headers-BoxPaintmain.h.md)[Previous](headers-BoxMooVTexture.h.md)

