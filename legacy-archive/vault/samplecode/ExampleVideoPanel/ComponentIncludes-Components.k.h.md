---
title: ExampleVideoPanel
apple_id: DTS10000800
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ExampleVideoPanel/Listings/ComponentIncludes_Components_k_h.html
archived_at: '2026-07-18T03:07:57.878915Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ExampleVideoPanel](ExampleVideoPanel.md)


[Next](Includes-DebugFlags.h.md)[Previous](README.txt.md)

# ComponentIncludes/Components.k.h

```c
/*
     File:       Components.k.h

     Contains:   Component Manager Interfaces.

     Version:    Technology: QuickTime 5.0
                 Release:    Universal Interfaces 3.4

     Copyright:  © 1991-2001 by Apple Computer, Inc., all rights reserved.

     Bugs?:      For bug reports, consult the following page on
                 the World Wide Web:

                     http://developer.apple.com/bugreporter/

*/
#ifndef __COMPONENTS_K__
#define __COMPONENTS_K__

#include <QuickTime/QuickTime.h>

/*
    Example usage:

        #define CALLCOMPONENT_BASENAME()    Fred
        #define CALLCOMPONENT_GLOBALS() FredGlobalsHandle
        #include <Components.k.h>

    To specify that your component implementation does not use globals, do not #define CALLCOMPONENT_GLOBALS
*/
#ifdef CALLCOMPONENT_BASENAME
    #ifndef CALLCOMPONENT_GLOBALS
        #define CALLCOMPONENT_GLOBALS() 
        #define ADD_CALLCOMPONENT_COMMA 
    #else
        #define ADD_CALLCOMPONENT_COMMA ,
    #endif
    #define CALLCOMPONENT_GLUE(a,b) a##b
    #define CALLCOMPONENT_STRCAT(a,b) CALLCOMPONENT_GLUE(a,b)
    #define ADD_CALLCOMPONENT_BASENAME(name) CALLCOMPONENT_STRCAT(CALLCOMPONENT_BASENAME(),name)

    EXTERN_API( ComponentResult  ) ADD_CALLCOMPONENT_BASENAME(Open) (CALLCOMPONENT_GLOBALS() ADD_CALLCOMPONENT_COMMA ComponentInstance  self);

    EXTERN_API( ComponentResult  ) ADD_CALLCOMPONENT_BASENAME(Close) (CALLCOMPONENT_GLOBALS() ADD_CALLCOMPONENT_COMMA ComponentInstance  self);

    EXTERN_API( ComponentResult  ) ADD_CALLCOMPONENT_BASENAME(CanDo) (CALLCOMPONENT_GLOBALS() ADD_CALLCOMPONENT_COMMA short  ftnNumber);

    EXTERN_API( ComponentResult  ) ADD_CALLCOMPONENT_BASENAME(Version) (CALLCOMPONENT_GLOBALS());

    EXTERN_API( ComponentResult  ) ADD_CALLCOMPONENT_BASENAME(Register) (CALLCOMPONENT_GLOBALS());

    EXTERN_API( ComponentResult  ) ADD_CALLCOMPONENT_BASENAME(Target) (CALLCOMPONENT_GLOBALS() ADD_CALLCOMPONENT_COMMA ComponentInstance  target);

    EXTERN_API( ComponentResult  ) ADD_CALLCOMPONENT_BASENAME(Unregister) (CALLCOMPONENT_GLOBALS());

    EXTERN_API( ComponentResult  ) ADD_CALLCOMPONENT_BASENAME(GetMPWorkFunction) (CALLCOMPONENT_GLOBALS() ADD_CALLCOMPONENT_COMMA ComponentMPWorkFunctionUPP * workFunction, void ** refCon);

    EXTERN_API( ComponentResult  ) ADD_CALLCOMPONENT_BASENAME(GetPublicResource) (CALLCOMPONENT_GLOBALS() ADD_CALLCOMPONENT_COMMA OSType  resourceType, short  resourceID, Handle * resource);

#endif  /* CALLCOMPONENT_BASENAME */


#endif /* __COMPONENTS_K__ */
```

[Next](Includes-DebugFlags.h.md)[Previous](README.txt.md)

