---
title: PickOne
apple_id: DTS10000117
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PickOne/Listings/headers_PickOne_window_h.html
archived_at: '2026-07-18T03:18:58.464739Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PickOne](PickOne.md)


[Next](headers-PictRead.h.md)[Previous](headers-PickOneutility.h.md)

# headers/PickOne_window.h

```c
/*  window.h                                                                            

    Michael Bishop - August 21 1996                                                 
    Nick Thompson
    (c)1994-96 Apple Computer Inc., All Rights Reserved                             

*/
#ifndef _BP_WINDOW_H_
#define _BP_WINDOW_H_

#include <QuickDraw.h>

#include    "PickOne_document.h"


enum {
    kWindowResID = 6347
} ; 

WindowPtr   Window_New(void) ;
void        Window_Dispose(WindowPtr theWindow) ;

DocumentHdl Window_GetDocument( WindowPtr theWindow);
int         Window_SetDocument( WindowPtr theWindow,  DocumentHdl theDocument);
WindowPtr   Window_GetNextWindow(WindowPtr theWindow);

void        Window_Update( WindowPtr window );
void        Window_Activate(WindowPtr theWindow, short activate);
void        Window_DoContent (WindowPtr theWindow, EventRecord *event);
void        Window_DestroyAll(void);

#endif
```

[Next](headers-PictRead.h.md)[Previous](headers-PickOneutility.h.md)

