---
title: ViewerCallbackSample
apple_id: DTS10000137
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ViewerCallbackSample/Listings/Headers_Viewer_Error_h.html
archived_at: '2026-07-18T03:27:58.234429Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ViewerCallbackSample](ViewerCallbackSample.md)


[Next](Headers-ViewerEvents.h.md)[Previous](Headers-ViewerCallbacks.h.md)

# Headers/Viewer_Error.h

```c
/*  
 *  Viewer_Error.h
 *
 *  QuickDraw 3D 1.6 Sample
 *  Robert Dierkes
 *
 *   12/22/98   RDD     Created.
 */

#ifndef _HViewer_Error
#define _HViewer_Error

#ifdef __cplusplus
extern "C" {
#endif

#include <Types.h>

void    Error_Alert(    short       iconType,
                        char        *pMessage);

Boolean Error_ShowMessage(
                        short       resStringIndex);


    #define USE_DEBUGGING   /* TODO */


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
        #include "Viewer_System.h"
    #else
        #define SYSTEM_BEEP()
    #endif

#ifdef __cplusplus
}
#endif


#endif /* _HViewer_Error */
```

[Next](Headers-ViewerEvents.h.md)[Previous](Headers-ViewerCallbacks.h.md)

