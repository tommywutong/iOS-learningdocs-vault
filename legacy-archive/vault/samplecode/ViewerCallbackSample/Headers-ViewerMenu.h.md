---
title: ViewerCallbackSample
apple_id: DTS10000137
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ViewerCallbackSample/Listings/Headers_Viewer_Menu_h.html
archived_at: '2026-07-18T03:27:58.344580Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ViewerCallbackSample](ViewerCallbackSample.md)


[Next](Headers-ViewerMessage.h.md)[Previous](Headers-ViewerMain.h.md)

# Headers/Viewer_Menu.h

```
/*  
 *  Viewer_Menu.h
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   12/22/98   RDD     Created.
 */

#ifndef _HViewer_Menu
#define _HViewer_Menu


/*------------------*/
/*    Constants     */
/*------------------*/
enum {
    mApple = 128,
    mFile,
    mEdit
};


/* mApple Menu */
enum {
    iAbout = 1
};


/* mFile Menu */
enum {
    iNew = 1,
    iOpen,
    iClose,
        iFileSeparator1,
    iSave,
    iSaveAs,
        iFileSeparator2,
    iQuit
};


/* mEdit Menu */
enum {
    iUndo = 1,
        iEditSeparator1,
    iCut,
    iCopy,
    iPaste,
    iClear
};


/* mViewer Menu */
enum {
    iViewerWindowResize = 1,
    iViewerPaneResize,
    iViewerDrawAfter
};


/*--------------*/
/*  Prototypes  */
/*--------------*/
TQ3Boolean  Menu_Initialize (
            void);

OSErr       Menu_Command (
            long            menuResult);

#endif /* _HViewer_Menu */
```

[Next](Headers-ViewerMessage.h.md)[Previous](Headers-ViewerMain.h.md)

