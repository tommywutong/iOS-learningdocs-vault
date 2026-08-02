---
title: WorldRayPickSample
apple_id: DTS10000140
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/WorldRayPickSample/Listings/Headers_WRay_Events_h.html
archived_at: '2026-07-18T03:28:25.415708Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WorldRayPickSample](WorldRayPickSample.md)


[Next](Headers-WRayMain.h.md)[Previous](Headers-WRayError.h.md)

# Headers/WRay_Events.h

```c
/*  
 *  WRay_Events.h
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   07/28/98   RDD     Created.
 */

#ifndef _HWRay_Events
#define _HWRay_Events

#include <Events.h>


Boolean Events_Initialize(
            void);

void    Events_Process (
            void);

Boolean Events_Update (
            EventRecord         *pEvent);


#endif /* _HWRay_Events */
```

[Next](Headers-WRayMain.h.md)[Previous](Headers-WRayError.h.md)

