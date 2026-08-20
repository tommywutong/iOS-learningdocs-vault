---
title: WorldRayPickSample
apple_id: DTS10000140
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/WorldRayPickSample/Listings/Headers_WRay_Menu_h.html
archived_at: '2026-07-18T03:28:25.529089Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WorldRayPickSample](WorldRayPickSample.md)


[Next](Headers-WRayMessage.h.md)[Previous](Headers-WRayMemory.h.md)

# Headers/WRay_Menu.h

```c
/*  
 *  WRay_Menu.h
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   07/28/98   RDD     Created.
 */

#ifndef _HWRay_Menu
#define _HWRay_Menu

#include "WRay_Document.h"


/*------------------*/
/*    Constants     */
/*------------------*/
enum {
    mApple = 128,
    mFile,
    mEdit,
    mRay
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


/* mRay Menu */
enum {
    iRayBegin   = 1,
    iRayEnd,
    iRaySeparator,
    iRayRotate,
    iRaySound
};


/*--------------*/
/*  Prototypes  */
/*--------------*/
TQ3Boolean  Menu_Initialize (
            void);

TQ3Boolean  Menu_InitializeItems (
            TDocumentPtr    pDocument);

TQ3Boolean  Menu_Command (
            long            menuResult,
            TDocumentPtr    pDocument);

#endif /* _HWRay_Menu */
```

[Next](Headers-WRayMessage.h.md)[Previous](Headers-WRayMemory.h.md)

