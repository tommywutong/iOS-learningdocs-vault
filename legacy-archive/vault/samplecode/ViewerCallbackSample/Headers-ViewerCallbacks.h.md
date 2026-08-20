---
title: ViewerCallbackSample
apple_id: DTS10000137
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ViewerCallbackSample/Listings/Headers_Viewer_Callbacks_h.html
archived_at: '2026-07-18T03:27:58.198256Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ViewerCallbackSample](ViewerCallbackSample.md)


[Next](Headers-ViewerError.h.md)[Previous](ViewerCallbackSample.md)

# Headers/Viewer_Callbacks.h

```
/*  
 *  Viewer_Callbacks.h
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   12/22/98   RDD     Created.
 */

#ifndef _HViewer_Callbacks
#define _HViewer_Callbacks


TQ3Status Callbacks_InitWindowResizeCallback(
    TQ3ViewerObject viewer,
    WindowPtr       window);

TQ3Status Callbacks_InitPaneResizeCallback(
    TQ3ViewerObject viewer,
    WindowPtr       window,
    unsigned long   example);

TQ3Status Callbacks_InitDrawingCallback(
    TQ3ViewerObject viewer,
    WindowPtr       window);


#endif /* _HViewer_Callbacks */
```

[Next](Headers-ViewerError.h.md)[Previous](ViewerCallbackSample.md)

