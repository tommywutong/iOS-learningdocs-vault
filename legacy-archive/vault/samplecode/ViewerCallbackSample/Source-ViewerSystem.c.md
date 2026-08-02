---
title: ViewerCallbackSample
apple_id: DTS10000137
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ViewerCallbackSample/Listings/Source_Viewer_System_c.html
archived_at: '2026-07-18T03:27:59.105244Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ViewerCallbackSample](ViewerCallbackSample.md)


[Next](Source-ViewerWindow.c.md)[Previous](Source-ViewerMessage.c.md)

# Source/Viewer_System.c

```c
/* 
 *  Viewer_System.c
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   12/22/98   RDD     Created.
 */

/*------------------*/
/*  Include Files   */
/*------------------*/
#include "QD3D.h"

#if defined(OS_MACINTOSH) && OS_MACINTOSH
#include "QD3DViewer.h"

#include <CodeFragments.h>  /* kUnresolvedCFragSymbolAddress */
#include <Gestalt.h>
#include <Resources.h>
#include <Sound.h>
#endif

#include "Viewer_Main.h"
#include "Viewer_System.h"
#include "Viewer_Error.h"


/*----------------------*/
/*  Global Declarations */
/*----------------------*/


/*
 *  QuickDraw3D_Initialize
 */
TQ3Boolean QuickDraw3D_Initialize(
            void)
{
    TQ3Status       status = kQ3Failure;
    OSErr           error;
    long            response;
    unsigned long   viewerRelRev;

    error = Gestalt(gestaltQD3D, &response);

    if ((error != noErr)  ||
        (! (response & (1 << gestaltQD3DPresent)))) {

        Error_ShowMessage(kQuickDraw3DNotInstalledStr);
        return kQ3False;
    }

    /*
     * Test for specific symbol as recommended in develop, March 1995
     * NOTE: QuickDraw3DLib must be weak linked for this comparison to work.
     */
    if (((void *) Q3Initialize) == (void *) kUnresolvedCFragSymbolAddress) {
        Error_ShowMessage(kQuickDraw3DNotInstalledStr);
        return kQ3False;
    }

    status = Q3Initialize();
    if (status == kQ3Failure) {
        ERROR_DEBUG_STR ("QuickDraw3D_Initialize: Q3Initialize returned failure.");
        return kQ3False;
    }

    /* Get QuickDraw 3D version */
    error = Gestalt(gestaltQD3DVersion, &response);

    if ((error != noErr)  ||
        (response < kQD3DGestaltVersion_1_6_0)) {

        Error_ShowMessage(kQuickDraw3DNotCurrentStr);
        return kQ3False;
    }

    /* Get Viewer version */
    error = Q3ViewerGetReleaseVersion(&viewerRelRev);

    if ((error != noErr)  ||
        (response < kQD3DGestaltVersion_1_6_0)) {

        Error_ShowMessage(kQuickDraw3DViewerNotCurrentStr);
        return kQ3False;
    }

    return kQ3True;
}


/*
 *  QuickDraw3D_Exit
 */
TQ3Boolean QuickDraw3D_Exit(
            void)
{
    if (Q3Exit() == kQ3Failure) {
        ERROR_DEBUG_STR ("QuickDraw3D_Exit: Q3Exit returned failure.");
        return kQ3False;
    }

    return kQ3True;
}


#pragma mark -

/*
 *  System_Beep
 */
void System_Beep(
    void)
{
#if defined(OS_MACINTOSH) && OS_MACINTOSH
    SysBeep(1);
#endif
}
```

[Next](Source-ViewerWindow.c.md)[Previous](Source-ViewerMessage.c.md)

