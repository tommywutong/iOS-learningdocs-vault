---
title: Picking Mesh ShapeParts
apple_id: DTS10000116
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Picking_Mesh_ShapeParts/Listings/Includes_PickMeshShapePart_h.html
archived_at: '2026-07-18T03:18:59.478984Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Picking Mesh ShapeParts](Picking%20Mesh%20ShapeParts.md)


[Next](Includes-PickMeshShapePartPrefix.h.md)[Previous](Picking%20Mesh%20ShapeParts.md)

# Includes/PickMeshShapePart.h

```c
// PickMeshShapePart.h
//
// Modification History:
//
//  11/09/95    robert  created


#ifndef _PICKMESHSHAPEPART_H_
#define _PICKMESHSHAPEPART_H_

#include "PickMeshShapePartShell.h"


/*
 *  TQ3HitData validMask Macros
 */

#if defined(QD3D_OBSOLETE) && QD3D_OBSOLETE
    #define HitData_Has_PickID(hitData)             ((hitData.validMask & kQ3PickDetailMaskPickID)!=0)
    #define HitData_Has_Path(hitData)               ((hitData.validMask & kQ3PickDetailMaskPath)!=0  && (hitData.path.depth != 0) && (hitData.path.positions != NULL))
    #define HitData_Has_Object(hitData)             (((hitData.validMask & kQ3PickDetailMaskObject)!=0)  && (hitData.object != NULL))
    #define HitData_Has_LocalToWorldMatrix(hitData) ((hitData.validMask & kQ3PickDetailMaskLocalToWorldMatrix)!=0)
    #define HitData_Has_XYZ(hitData)                ((hitData.validMask & kQ3PickDetailMaskXYZ)!=0)
    #define HitData_Has_Distance(hitData)           ((hitData.validMask & kQ3PickDetailMaskDistance)!=0)
    #define HitData_Has_Normal(hitData)             ((hitData.validMask & kQ3PickDetailMaskNormal)!=0)
    #define HitData_Has_ShapePart(hitData)          (((hitData.validMask & kQ3PickDetailMaskShapePart)!=0)  && (hitData.shapePart != NULL))
#endif  /* QD3D_OBSOLETE */

TQ3Status InitPicking(
    void);

TQ3Status ExitPicking(
    void);

TQ3Status DoPicking(
    Point               *pWhere,
    DocumentPtr         theDocument);

#endif
```

[Next](Includes-PickMeshShapePartPrefix.h.md)[Previous](Picking%20Mesh%20ShapeParts.md)

