---
title: Plug-in  -DistanceProxyGroup
apple_id: DTS10000121
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-DistanceProxyGroup/Listings/src_dpgStubs_c.html
archived_at: '2026-07-18T03:19:15.566866Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  -DistanceProxyGroup](Plug-in%20-DistanceProxyGroup.md)


[Next](Document%20Revision%20History.md)[Previous](src-dpgSortedArray.c.md)

# src/dpgStubs.c

```c
/******************************************************************************
 **                                                                          **
 **     Module:     dpgStubs.c                                               **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1995-1996 Apple Computer, Inc.  All rights reserved.   **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/

#include "DPGGroup.h"
#include "dpg.h"

/*===========================================================================*\
 *
 *  Routine:    Q3DistanceProxyGroup_New()
 *
 *  Comments:   
 *
\*===========================================================================*/

TQ3GroupObject Q3DistanceProxyGroup_New(
    TQ3Point3D      *refPt,
    unsigned long   flags)
{
    TQ3GroupObject returnVal;

    returnVal = exDistanceProxyGroup_New(refPt, flags);

    return (returnVal);
}   


/*===========================================================================*\
 *
 *  Routine:    Q3DistanceProxyGroup_AddObject()
 *
 *  Comments:
 *
\*===========================================================================*/

TQ3GroupPosition Q3DistanceProxyGroup_AddObject(
    TQ3GroupObject      group,
    TQ3Object           object,
    float               distance)
{
    TQ3GroupPosition returnVal;

    returnVal = exDistanceProxyGroup_AddObjectDistance(group, object, distance);

    return (returnVal);
}


/*===========================================================================*\
 *
 *  Routine:    Q3DistanceProxyGroup_SetFlag()
 *
 *  Comments:
 *
\*===========================================================================*/

TQ3Status Q3DistanceProxyGroup_SetFlag(
    TQ3GroupObject      group,
    TQ3DPGFlag          flag)
{
    TQ3Status returnVal;

    returnVal = exDistanceProxyGroup_SetFlag(group, flag);

    return (returnVal);
}


/*===========================================================================*\
 *
 *  Routine:    Q3DistanceProxyGroup_GetFlag()
 *
 *  Comments:
 *
\*===========================================================================*/

TQ3Status Q3DistanceProxyGroup_GetFlag(
    TQ3GroupObject      group,
    TQ3DPGFlag          *flag)
{
    TQ3Status returnVal;

    returnVal = exDistanceProxyGroup_GetFlag(group, flag);

    return (returnVal);
}

/*===========================================================================*\
 *
 *  Routine:    Q3DistanceProxyGroup_SetReferencePoint()
 *
 *  Comments:
 *
\*===========================================================================*/

TQ3Status Q3DistanceProxyGroup_SetReferencePoint(
    TQ3GroupObject      group,
    TQ3Point3D          *refPt)
{
    TQ3Status returnVal;

    returnVal = exDistanceProxyGroup_SetReferencePoint(group, refPt);

    return (returnVal);
}


/*===========================================================================*\
 *
 *  Routine:    Q3DistanceProxyGroup_GetReferencePoint()
 *
 *  Comments:
 *
\*===========================================================================*/

TQ3Status Q3DistanceProxyGroup_GetReferencePoint(
    TQ3GroupObject      group,
    TQ3Point3D          *refPt)
{
    TQ3Status returnVal;

    returnVal = exDistanceProxyGroup_GetReferencePoint(group, refPt);


    return (returnVal);
}


/*===========================================================================*\
 *
 *  Routine:    Q3DistanceProxyGroup_SetDistanceAtPosition()
 *
 *  Comments:
 *
\*===========================================================================*/

TQ3Boolean Q3DistanceProxyGroup_SetDistanceAtPosition(
    TQ3GroupObject      group,
    TQ3GroupPosition    position,
    float               distance)
{
    TQ3Boolean returnVal;

    returnVal = exDistanceProxyGroup_SetDistanceAtPosition(
                    group, 
                    position, 
                    distance);

    return (returnVal);
}

/*===========================================================================*\
 *
 *  Routine:    Q3DistanceProxyGroup_GetDistanceAtPosition()
 *
 *  Comments:
 *
\*===========================================================================*/

TQ3Boolean Q3DistanceProxyGroup_GetDistanceAtPosition(
    TQ3GroupObject      group,
    TQ3GroupPosition    position,
    float               *distance)
{
    TQ3Boolean returnVal;

    returnVal = exDistanceProxyGroup_GetDistanceAtPosition(
                    group, 
                    position, 
                    distance);

    return (returnVal);

}
```

[Next](Document%20Revision%20History.md)[Previous](src-dpgSortedArray.c.md)

