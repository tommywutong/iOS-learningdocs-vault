---
title: Picking Mesh ShapeParts
apple_id: DTS10000116
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Picking_Mesh_ShapeParts/Listings/Includes_PickMeshShapePartShell_h.html
archived_at: '2026-07-18T03:18:59.382021Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Picking Mesh ShapeParts](Picking%20Mesh%20ShapeParts.md)


[Next](Includes-PickMeshShapePartSupport.h.md)[Previous](Includes-PickMeshShapePartPrefix.h.md)

# Includes/PickMeshShapePartShell.h

```c
// PickMeshShapePartShell.h
//
// Modification History:
//
//  01/01/95    nick    created this file from other stuff
//  11/09/95    robert  removed unused things and added _documentRecord from
//                      MeshShapePartPickShell.c. Added fPickPartStyle, fPickParts,
//                      and support for shape part menu.
//
//

#ifndef _MESHSHAPEPARTPICKSHELL_H_
#define _MESHSHAPEPARTPICKSHELL_H_


// for QuickDraw 3D
#include "QD3D.h"
#include "QD3DGroup.h"
#include "QD3DStyle.h"
#include "QD3DView.h"

extern WindowPtr    gMainWindow;

//-------------------------------------------------------------------------------------------

struct _documentRecord {
    TQ3ViewObject   fView;              // the view for the scene
    TQ3GroupObject  fModel;             // object in the scene being modelled
    TQ3StyleObject  fInterpolation;     // interpolation style used when rendering
    TQ3StyleObject  fBackFacing;        // whether to draw shapes that face away from the camera
    TQ3StyleObject  fFillStyle;         // whether drawn as solid filled object or decomposed to components
    TQ3StyleObject  fPickPartStyle;     // indicates which shape parts can be picked

    TQ3PickParts    fPickParts;         // pick parts selected in shape part menu
};

typedef struct _documentRecord DocumentRec, *DocumentPtr, **DocumentHdl;


//-------------------------------------------------------------------------------------------
//
enum {
    mApple = 128,
    mFile,
    mParts
};

enum {
    iAbout = 1
};

enum {
    iQuit = 1
};

enum {
    iObject = 1,
    iFace,
    iEdge,
    iVertex
};

//-------------------------------------------------------------------------------------------
//

TQ3Status DrawDocumentData(
    DocumentPtr theDocument);

#endif
```

[Next](Includes-PickMeshShapePartSupport.h.md)[Previous](Includes-PickMeshShapePartPrefix.h.md)

