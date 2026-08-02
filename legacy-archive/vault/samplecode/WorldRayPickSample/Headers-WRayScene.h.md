---
title: WorldRayPickSample
apple_id: DTS10000140
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/WorldRayPickSample/Listings/Headers_WRay_Scene_h.html
archived_at: '2026-07-18T03:28:25.632073Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WorldRayPickSample](WorldRayPickSample.md)


[Next](Headers-WRaySystem.h.md)[Previous](Headers-WRayPick.h.md)

# Headers/WRay_Scene.h

```c
/*  
 *  WRay_Scene.h
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   07/28/98   RDD     Created.
 */

#ifndef _HWRay_Scene
#define _HWRay_Scene


#ifdef __cplusplus
extern "C" {
#endif

#include <Windows.h>
#include "QD3D.h"


/*------------------*/
/*    Constants     */
/*------------------*/
#define kDefaultHither          0.001
#define kDefaultYon             1000.0
#define kDefaultFieldOfView     0.45

#define kCylRadius              1.5f


/*--------------*/
/*  Prototypes  */
/*--------------*/
TQ3ViewObject Scene_NewView(
    WindowPtr       pWindow);

TQ3GroupObject Scene_NewModel(
    void);

TQ3Boolean Scene_IsRotating(
    void);

TQ3Boolean Scene_SetIsRotating(
    TQ3Boolean      newIsRotating);

TQ3Status Scene_Rotate(
    void);


#ifdef __cplusplus
}
#endif

#endif /* _HWRay_Scene */
```

[Next](Headers-WRaySystem.h.md)[Previous](Headers-WRayPick.h.md)

