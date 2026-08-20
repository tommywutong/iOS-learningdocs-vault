---
title: ViewerCallbackSample
apple_id: DTS10000137
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ViewerCallbackSample/Listings/Source_Viewer_Window_c.html
archived_at: '2026-07-18T03:27:59.163657Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ViewerCallbackSample](ViewerCallbackSample.md)


[Next](Document%20Revision%20History.md)[Previous](Source-ViewerSystem.c.md)

# Source/Viewer_Window.c

```c
/* 
 *  Viewer_Window.c
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   12/22/98   RDD     Created.
 */

/*------------------*/
/*  Include Files   */
/*------------------*/
#include "QD3DViewer.h"

#if defined(OS_MACINTOSH) && OS_MACINTOSH
#include <MacWindows.h>
#endif

#include "Viewer_Error.h"
#include "Viewer_Window.h"


/*----------------------*/
/*  Global Declarations */
/*----------------------*/
WindowPtr   gWindows[kMaxWindowCount];


/*----------------------*/
/*  Local Prototypes    */
/*----------------------*/



/*
 *  Window_Initialize
 */
TQ3Status Window_Initialize(
    void)
{
    unsigned long   i;

    for (i = 0; i < kMaxWindowCount; i++) {
        gWindows[i] = NULL;
    }

    return kQ3Success;
}


/*
 *  Window_Exit
 */
TQ3Status Window_Exit(
    void)
{
    unsigned long   i;

    for (i = 0; i < kMaxWindowCount; i++) {
        if (gWindows[i] != NULL) {
            (void) Window_CloseViewer(&gWindows[i]);
        }
    }

    return kQ3Success;
}


#pragma mark -

/*
 *  Window_GetViewer
 */
TQ3ViewerObject Window_GetViewer(
    WindowPtr   pWindow)
{
    if (pWindow != NULL) {
        return ((TQ3ViewerObject) GetWRefCon(pWindow));
    }

    return NULL;
}


/*
 * Window_CloseViewer
 */
OSErr Window_CloseViewer(
    WindowPtr       *hWindow)
{
    OSErr           theErr = noErr;
    TQ3ViewerObject viewer = NULL;
    WindowPtr       window;
    unsigned long   i;

    if ((hWindow == NULL) ||
        (*hWindow == NULL)) {
        ERROR_DEBUG_STR("Window_CloseViewer: hWindow == NULL");
        return paramErr;
    }
    window = *hWindow;

    if ((viewer = Window_GetViewer(window)) == NULL) {
        ERROR_DEBUG_STR("Window_CloseViewer: viewer == NULL");
        return paramErr;
    }

    /* Dispose the Viewer */
    if ((theErr = Q3ViewerDispose(viewer)) != noErr) {
        ERROR_DEBUG_STR("Window_CloseViewer: Q3ViewerDispose failed");
        return paramErr;
    }

    /* Remove window from list */
    for (i = 0; i < kMaxWindowCount; i++) {
        if (window == gWindows[i]) {
            gWindows[i] = NULL;
            break;
        }
    }

    /* Dispose the window */
    DisposeWindow(window);
    *hWindow = NULL;

    return theErr;
}
```

[Next](Document%20Revision%20History.md)[Previous](Source-ViewerSystem.c.md)

