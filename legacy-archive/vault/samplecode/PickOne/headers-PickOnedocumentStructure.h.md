---
title: PickOne
apple_id: DTS10000117
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PickOne/Listings/headers_PickOne_documentStructure_h.html
archived_at: '2026-07-18T03:18:58.272498Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PickOne](PickOne.md)


[Next](headers-PickOneevent.h.md)[Previous](headers-PickOnedocument.h.md)

# headers/PickOne_documentStructure.h

```c
/*  PickOne_documentStructure.h                                                                         

    This contains all the document-specific code.

    Michael Bishop - August 21 1996                                                 
    (c)1994-96 Apple Computer Inc., All Rights Reserved                             

*/

#ifndef _BP_DOCUMENTSTRUCTURE_H_
#define _BP_DOCUMENTSTRUCTURE_H_

#include    <QuickDraw.h>

#include    "QD3D.h"


struct _documentRecord {

    WindowPtr       fWindow ;               /* the window associated with this document */

    TQ3ViewObject   fView ;                 /*  the view for the scene */
    TQ3GroupObject  fModel ;                /*  object in the scene being modelled */
    TQ3StyleObject  fInterpolation ;        /*  interpolation style used when rendering */
    TQ3StyleObject  fBackFacing ;           /*  whether to draw shapes that face away from the camera */
    TQ3StyleObject  fFillStyle ;            /*  whether drawn as solid filled object or decomposed to components */
    TQ3Matrix4x4    fRotation;              /*  the transform for the model */

} ;


#endif
```

[Next](headers-PickOneevent.h.md)[Previous](headers-PickOnedocument.h.md)

