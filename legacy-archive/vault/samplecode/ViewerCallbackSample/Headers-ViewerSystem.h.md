---
title: ViewerCallbackSample
apple_id: DTS10000137
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ViewerCallbackSample/Listings/Headers_Viewer_System_h.html
archived_at: '2026-07-18T03:27:58.429674Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ViewerCallbackSample](ViewerCallbackSample.md)


[Next](Headers-ViewerWindow.h.md)[Previous](Headers-ViewerMessage.h.md)

# Headers/Viewer_System.h

```
/*  
 *  Viewer_System.h
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   12/22/98   RDD     Created.
 */

#ifndef _HViewer_System
#define _HViewer_System


#ifdef __cplusplus
extern "C" {
#endif


/*------------------*/
/*    Constants     */
/*------------------*/


/*------------------*/
/*      Macros      */
/*------------------*/
#define kQD3DGestaltVersion_1_6_0   0x00010600


TQ3Boolean QuickDraw3D_Initialize(
    void);

TQ3Boolean QuickDraw3D_Exit(
    void);

void System_Beep (
    void);


#ifdef __cplusplus
}
#endif

#endif /* _HViewer_System */
```

[Next](Headers-ViewerWindow.h.md)[Previous](Headers-ViewerMessage.h.md)

