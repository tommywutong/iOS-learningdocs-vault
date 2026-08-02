---
title: BoxMooV
apple_id: DTS10000099
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BoxMooV/Listings/headers_BoxPaint_Support_h.html
archived_at: '2026-07-18T03:02:13.988202Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BoxMooV](BoxMooV.md)


[Next](headers-BoxPaintutility.h.md)[Previous](headers-BoxPaintmenu.h.md)

# headers/BoxPaint_Support.h

```c
/*  BoxPaint_Support.h

    Quickdraw 3D sample code

    This file contains utility routines for QuickDraw 3d sample code. This
    app shows how to apply a texture shader to an object.  Bear in mind
    that any object that you wish to texture map needs to have UV parameters
    applied.

    Nick Thompson
    (c)1994-96 Apple computer Inc., All Rights Reserved                             

*/

#ifndef _BOXPAINTSUPPORT_H_
#define _BOXPAINTSUPPORT_H_

#include    "BoxMooV_document.h"

/*  Macintosh System Stuff */
#include <Windows.h>

/*  QuickDraw 3D stuff */
#include "QD3D.h"
#include "QD3DErrors.h"
#include "QD3DView.h"

/* --------------------------------------------------------------------------------------- */

TQ3GroupObject      MyNewModel(void) ;
TQ3ViewObject       MyNewView(WindowPtr theWindow) ;


TQ3Point3D AdjustCamera(DocumentPtr theDocument) ;

#endif
```

[Next](headers-BoxPaintutility.h.md)[Previous](headers-BoxPaintmenu.h.md)

