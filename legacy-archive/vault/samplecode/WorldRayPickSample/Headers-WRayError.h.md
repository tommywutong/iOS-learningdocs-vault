---
title: WorldRayPickSample
apple_id: DTS10000140
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/WorldRayPickSample/Listings/Headers_WRay_Error_h.html
archived_at: '2026-07-18T03:28:25.378271Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WorldRayPickSample](WorldRayPickSample.md)


[Next](Headers-WRayEvents.h.md)[Previous](Headers-WRayDocument.h.md)

# Headers/WRay_Error.h

```c
/*  
 *  WRay_Error.h
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   07/28/98   RDD     Created.
 */

#ifndef _HWRay_Error
#define _HWRay_Error

#ifdef __cplusplus
extern "C" {
#endif

#include <Types.h>

void    Error_Alert(    short       iconType,
                        char        *pMessage);

Boolean Error_ShowMessage(
                        short       resStringIndex);

    #if defined(USE_DEBUGGING)
        #define     DEBUGGING   1
    #else
        #define     DEBUGGING   0
    #endif

    #if defined(USE_DEBUGGING)  || defined(ERROR_DEBUG_STR)
        #undef  ERROR_DEBUG_STR
        #define ERROR_DEBUG_STR(s)  debugstr(s)
    #else
        #define ERROR_DEBUG_STR(s)
    #endif

    #if defined(USE_DEBUGGING)
        #define DEBUG_ASSERT(x,f)   \
            if ((x) == 0) { \
                char    msg[256];   \
                sprintf(msg, "%s %s (%d): (%s)", __FILE__, #f, __LINE__, #x);   \
                debugstr(msg);      \
            }
    #else
        #define DEBUG_ASSERT(x,f)
    #endif

    #if defined(SYSTEM_BEEP)
        #undef  SYSTEM_BEEP
        #define SYSTEM_BEEP()   System_Beep()
        #include "WRay_System.h"
    #else
        #define SYSTEM_BEEP()
    #endif

#ifdef __cplusplus
}
#endif


#endif /* _HWRay_Error */
```

[Next](Headers-WRayEvents.h.md)[Previous](Headers-WRayDocument.h.md)

