---
title: WorldRayPickSample
apple_id: DTS10000140
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/WorldRayPickSample/Listings/Headers_WRay_Memory_h.html
archived_at: '2026-07-18T03:28:25.484772Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WorldRayPickSample](WorldRayPickSample.md)


[Next](Headers-WRayMenu.h.md)[Previous](Headers-WRayMain.h.md)

# Headers/WRay_Memory.h

```
/*  
 *  Txtr_Memory.h
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   07/28/98   RDD     Created.
 */

#ifndef _HTxtr_Memory
#define _HTxtr_Memory


#ifdef __cplusplus
extern "C" {
#endif

unsigned char *Memory_Sys_New(
    unsigned long   size);

unsigned char *Memory_App_New(
    unsigned long   size);

void Memory_Dispose(
    void            *memory);

void Memory_Copy(
    void            *source,
    void            *destination,
    unsigned long   size);

TQ3Status Object_Dispose_NULL(
    TQ3Object       *pObject);


#ifdef __cplusplus
}
#endif


#endif /* _HTxtr_Memory */
```

[Next](Headers-WRayMenu.h.md)[Previous](Headers-WRayMain.h.md)

