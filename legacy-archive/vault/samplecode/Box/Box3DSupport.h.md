---
title: Box
apple_id: DTS10000098
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Box/Listings/Box3DSupport_h.html
archived_at: '2026-07-18T03:02:13.553338Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Box](Box.md)


[Next](BoxShell.c.md)[Previous](Box3DSupport.c.md)

# Box3DSupport.h

```c
// My3dSupport.c - QuickDraw 3d routines - interface
//
// This file contains
//
// Created 27th Dec 1994, Nick Thompson, DEVSUPPORT
//
// Modification History:
//
//  12/27/94        nick        initial version

#ifndef _BOX3DSUPPORT_H_
#define _BOX3DSUPPORT_H_

// Macintosh System Stuff
#include <Types.h>
#include <Windows.h>

// QuickDraw 3D stuff
#include "QD3D.h"
#include "QD3DErrors.h"
#include "QD3DView.h"

//---------------------------------------------------------------------------------------

OSErr MyQD3DInitialize( void ) ;
OSErr MyQD3DExit() ;

TQ3ViewObject       MyNewView(WindowPtr theWindow) ;
TQ3DrawContextObject MyNewDrawContext( WindowPtr theWindow) ;
TQ3CameraObject         MyNewCamera(WindowPtr theWindow) ;
TQ3GroupObject      MyNewLights(void) ;
TQ3GroupObject      MyNewModel(void) ;

TQ3GroupObject InputHelloWorldModel() ;
TQ3GroupObject InputFactModel() ;

TQ3Point3D AdjustCamera(
    TQ3ViewObject       theView,
    TQ3GroupObject      mainGroup,
    short               winWidth,
    short               winHeight) ;


#endif
```

[Next](BoxShell.c.md)[Previous](Box3DSupport.c.md)

