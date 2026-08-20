---
title: Picking Mesh ShapeParts
apple_id: DTS10000116
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Picking_Mesh_ShapeParts/Listings/Includes_PickMeshShapePartSupport_h.html
archived_at: '2026-07-18T03:18:59.421364Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Picking Mesh ShapeParts](Picking%20Mesh%20ShapeParts.md)


[Next](Sources-PickMeshShapePart.c.md)[Previous](Includes-PickMeshShapePartShell.h.md)

# Includes/PickMeshShapePartSupport.h

```c
// PickMeshShapePartSupport.h
//
// Modification History:
//
//  12/27/94        nick        initial version
//  11/09/95        robert      Removed unused prototypes

#ifndef _PICKMESHSHAPEPARTSUPPORT_H_
#define _PICKMESHSHAPEPARTSUPPORT_H_

// Macintosh System Stuff
#include <Windows.h>

// QuickDraw 3D stuff
#include "QD3D.h"

TQ3ViewObject MyNewView(
    WindowPtr   theWindow);

TQ3DrawContextObject MyNewDrawContext(
    WindowPtr   theWindow);

TQ3CameraObject MyNewCamera(
    WindowPtr   theWindow);

TQ3GroupObject MyNewCamera(
    WindowPtr   theWindow);

TQ3GroupObject MyNewLights(
    void);

TQ3GroupObject MyNewModel(
    void);

#endif
```

[Next](Sources-PickMeshShapePart.c.md)[Previous](Includes-PickMeshShapePartShell.h.md)

