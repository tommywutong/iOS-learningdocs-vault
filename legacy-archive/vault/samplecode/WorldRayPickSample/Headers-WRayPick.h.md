---
title: WorldRayPickSample
apple_id: DTS10000140
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/WorldRayPickSample/Listings/Headers_WRay_Pick_h.html
archived_at: '2026-07-18T03:28:25.595429Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WorldRayPickSample](WorldRayPickSample.md)


[Next](Headers-WRayScene.h.md)[Previous](Headers-WRayMessage.h.md)

# Headers/WRay_Pick.h

```c
/*  
 *  WRay_Pick.h
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   07/28/98   RDD     Created.
 */

#ifndef _HWRay_Pick
#define _HWRay_Pick

#include "WRay_Document.h"


#ifdef __cplusplus
extern "C" {
#endif


/*----------------------*/
/*   Type Definitions   */
/*----------------------*/
TQ3Boolean Pick_Initialize(
    void);

TQ3Boolean Pick_Exit(
    void);

TQ3Boolean Pick_IsAnimating(
    void);

TQ3Status Pick_BeginAnimation(
    TDocumentPtr        pDocument);

TQ3Status Pick_Animate(
    TDocumentPtr        pDocument);

TQ3Status Pick_EndAnimation(
    TDocumentPtr        pDocument);


#ifdef __cplusplus
}
#endif


#endif /* _HWRay_Pick */
```

[Next](Headers-WRayScene.h.md)[Previous](Headers-WRayMessage.h.md)

