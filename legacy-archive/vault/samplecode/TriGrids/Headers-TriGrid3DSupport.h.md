---
title: TriGrids
apple_id: DTS10000105
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/TriGrids/Listings/Headers_TriGrid3DSupport_h.html
archived_at: '2026-07-18T03:27:19.558464Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TriGrids](TriGrids.md)


[Next](Headers-TriGridShell.h.md)[Previous](Headers-Textures2.h.md)

# Headers/TriGrid3DSupport.h

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

TQ3Point3D AdjustCamera(
    TQ3ViewObject       theView,
    TQ3GroupObject      mainGroup,
    short               winWidth,
    short               winHeight) ;


#endif
```

[Next](Headers-TriGridShell.h.md)[Previous](Headers-Textures2.h.md)

