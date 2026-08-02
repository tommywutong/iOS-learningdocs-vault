---
title: ViewerCallbackSample
apple_id: DTS10000137
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ViewerCallbackSample/Listings/Headers_Viewer_Main_h.html
archived_at: '2026-07-18T03:27:58.317541Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ViewerCallbackSample](ViewerCallbackSample.md)


[Next](Headers-ViewerMenu.h.md)[Previous](Headers-ViewerEvents.h.md)

# Headers/Viewer_Main.h

```
/*  
 *  Viewer_Main.h
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   12/22/98   RDD     Created.
 */

#ifndef _HViewer_Main
#define _HViewer_Main


enum {
    kWindowRsrcID       = 128,
    kStringRsrcID       = 128
};

/* STR# Indices */
enum {
    kQuickDraw3DNotInstalledStr = 1,
    kQuickDraw3DNotCurrentStr,
    kQuickDraw3DViewerNotInstalledStr,
    kQuickDraw3DViewerNotCurrentStr
};

#define kWindowOnTop        ((WindowPtr) -1)


#endif /* _HViewer_Main */
```

[Next](Headers-ViewerMenu.h.md)[Previous](Headers-ViewerEvents.h.md)

