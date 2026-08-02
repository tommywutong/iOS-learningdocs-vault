---
title: BoxTex
apple_id: DTS10000101
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BoxTex/Listings/BoxTex3DSupport_h.html
archived_at: '2026-07-18T03:02:15.784160Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BoxTex](BoxTex.md)


[Next](BoxTexShell.c.md)[Previous](BoxTex3DSupport.c.md)

# BoxTex3DSupport.h

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

//-------------------------------------------------------------------------------------------

struct _documentRecord {
    TQ3ViewObject   fView ;                 // the view for the scene
    TQ3GroupObject  fModel ;                // object in the scene being modelled
    TQ3StyleObject  fInterpolation ;        // interpolation style used when rendering
    TQ3StyleObject  fBackFacing ;           // whether to draw shapes that face away from the camera
    TQ3StyleObject  fFillStyle ;            // whether drawn as solid filled object or decomposed to components
    TQ3Matrix4x4        fRotation;          // the transform for the model
    TQ3Point3D      fGroupCenter ;          // the center of the group (for rotation) 
    float           fGroupScale ;           // scaling factor to apply before drawing
};

typedef struct _documentRecord DocumentRec, *DocumentPtr, **DocumentHdl ;

//---------------------------------------------------------------------------------------

OSErr MyQD3DInitialize( void ) ;
OSErr MyQD3DExit() ;

TQ3ViewObject       MyNewView(WindowPtr theWindow) ;
TQ3DrawContextObject MyNewDrawContext( WindowPtr theWindow) ;
TQ3CameraObject         MyNewCamera(WindowPtr theWindow) ;
TQ3GroupObject      MyNewLights(void) ;
TQ3GroupObject      MyNewModel(void) ;
TQ3Status SubmitScene( DocumentPtr theDocument ) ;


TQ3Point3D AdjustCamera(
    DocumentPtr         theDocument,
    short               winWidth,
    short               winHeight) ;

#endif
```

[Next](BoxTexShell.c.md)[Previous](BoxTex3DSupport.c.md)

