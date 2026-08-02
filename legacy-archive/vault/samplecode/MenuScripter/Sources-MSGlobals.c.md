---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSGlobals_c.html
archived_at: '2026-07-18T03:14:41.772672Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSGlobals.h.md)[Previous](Sources-MSFile.h.md)

# Sources/MSGlobals.c

```c
// MSGlobals.c
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

/*
    Changes for 3.1:

        12-Oct-95   : CW : Added Metrowerks condition for "qd" definition.
                           Added gHasDragManager flag, gDragTrackingHandlerUPP and
                           gDragReceiveHandlerUPP Drag Manager UPPs (all globals).

    Changes for 4.0:

        29-Feb-96   : GS : Added gAppRec which holds the script and FSSpec
                            information for the application
*/


#define __COMPGLOBALS__

#include "MSGlobals.h"


#if !defined(THINK_C) && !defined(__MWERKS__) // These declares "qd" in their runtime
    QDGlobals       qd;
#endif

AppRec      gAppRec;

short       gNewDocCount;
MenuHandle  myMenus[kLastMenu+1];
short       gFontMItem;
Boolean     gQuitting;
Cursor      editCursor;
Cursor      waitCursor;
Boolean     gInBackground;

  // now for the environment variables set up by Gestalt

Boolean     gGestaltAvailable;
Boolean     gAppleEventsImplemented;
Boolean     gAliasManagerImplemented;
Boolean     gEditionManagerImplemented;
Boolean     gOutlineFontsImplemented;
Boolean     gRecordingImplemented;
Boolean     gHasDragManager;        // Is the Drag Manager available?
Boolean     gGXIsPresent;
Boolean     gHasProcessManager;


ControlActionUPP        gHScrollActionUPP;
ControlActionUPP        gVScrollActionUPP;
UserItemUPP             gDefaultButtonUPP;
DragTrackingHandlerUPP  gDragTrackingHandlerUPP;
DragReceiveHandlerUPP   gDragReceiveHandlerUPP;
```

[Next](Sources-MSGlobals.h.md)[Previous](Sources-MSFile.h.md)

