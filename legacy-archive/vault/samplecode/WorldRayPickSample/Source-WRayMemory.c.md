---
title: WorldRayPickSample
apple_id: DTS10000140
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/WorldRayPickSample/Listings/Source_WRay_Memory_c.html
archived_at: '2026-07-18T03:28:26.094252Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WorldRayPickSample](WorldRayPickSample.md)


[Next](Source-WRayMenu.c.md)[Previous](Source-WRayMain.c.md)

# Source/WRay_Memory.c

```c
/* 
 *  WRay_Memory.c
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   07/28/98   RDD     Created.
 */

/*------------------*/
/*  Include Files   */
/*------------------*/
#include <Memory.h>

#include "QD3D.h"

#include "WRay_Error.h"
#include "WRay_Memory.h"


/*------------------*/
/*    Constants     */
/*------------------*/


/*----------------------*/
/*  Global Declarations */
/*----------------------*/



/*
 *  Memory_Sys_New
 */
unsigned char *Memory_Sys_New(
    unsigned long   size)
{
    return (unsigned char *) NewPtrSysClear(size);
}


/*
 *  Memory_App_New
 */
unsigned char *Memory_App_New(
    unsigned long   size)
{
    return (unsigned char *) NewPtrClear(size);
}


/*
 *  Memory_Dispose
 */
void Memory_Dispose(
    void    *memory)
{
    DisposePtr((Ptr) memory);
}


/*
 *  Memory_Copy
 */
void Memory_Copy(
    void            *source,
    void            *destination,
    unsigned long   size)
{
    BlockMove(source, destination,(Size) size);
}



/*
 *  Object_Dispose_NULL
 */
TQ3Status Object_Dispose_NULL(
    TQ3Object       *pObject)
{
    DEBUG_ASSERT(pObject != NULL, Object_Dispose_NULL);
    if (pObject == NULL) {
        return kQ3Failure;
    }

    if (*pObject != NULL) {
        Q3Object_Dispose(*pObject);
        *pObject = NULL;
    }

    return kQ3Success;
}
```

[Next](Source-WRayMenu.c.md)[Previous](Source-WRayMain.c.md)

