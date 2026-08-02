---
title: ViewerCallbackSample
apple_id: DTS10000137
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ViewerCallbackSample/Listings/Headers_Viewer_Window_h.html
archived_at: '2026-07-18T03:27:58.468081Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ViewerCallbackSample](ViewerCallbackSample.md)


[Next](Source-ViewerCallbacks.c.md)[Previous](Headers-ViewerSystem.h.md)

# Headers/Viewer_Window.h

```c
/*  
 *  Viewer_Window.h
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   12/22/98   RDD     Created.
 */

#ifndef _HViewer_Window
#define _HViewer_Window


#if defined(OS_MACINTOSH) && OS_MACINTOSH
#include <MacWindows.h>
#endif


#define kMaxWindowCount     6
extern WindowPtr    gWindows[];


TQ3Status Window_Initialize(
    void);

TQ3Status Window_Exit(
    void);

TQ3ViewerObject Window_GetViewer(
    WindowPtr   pWindow);

OSErr Window_CloseViewer(
    WindowPtr       *hWindow);


#endif /* _HViewer_Window */
```

[Next](Source-ViewerCallbacks.c.md)[Previous](Headers-ViewerSystem.h.md)

