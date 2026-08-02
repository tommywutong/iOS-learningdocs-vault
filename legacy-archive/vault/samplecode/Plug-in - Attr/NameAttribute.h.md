---
title: Plug-in  - Attr
apple_id: DTS10000119
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-_Attr/Listings/NameAttribute_h.html
archived_at: '2026-07-18T03:19:16.990213Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  - Attr](Plug-in%20-%20Attr.md)


[Next](NameAttrTest.c.md)[Previous](NameAttribute.c.md)

# NameAttribute.h

```c
#ifndef _NAMEATTRIBUTE_
#define _NAMEATTRIBUTE_

#include <CodeFragments.h>
#include "QD3D.h"

/******************************************************************************
 **     
 **     Macros and constants
 **     
 *****************************************************************************/

/*
 * ESSENTIAL NOTE: With the QuickDraw 3D 1.5 release (and later) when you
 * register the element with QuickDraw 3D, for both elements and attributes
 * we change the type you pass in, and return a new dynamically determined
 * type.  You can save the type from Q3XElementClass_Register for later use,
 * get the type from the class using Q3XObjectClass_GetType, or get the type
 * from the same name string used when the element was registered by using
 * Q3ObjectHierarchy_GetTypeFromString.
 */
#define kElementTypeNameString  "ABC Company:NameAttributeSample"


/******************************************************************************
 **     
 **     Function prototypes for exported functions
 **     
 *****************************************************************************/

TQ3Status   NameAttribute_SetName(
                TQ3Object       object, 
                char            *name) ;


TQ3Status   NameAttribute_GetName(
                TQ3Object       object, 
                char            *name) ;

TQ3Status   NameAttribute_Unregister(
                void) ;

TQ3Status   NameAttribute_Register( 
                void ) ;

OSErr       NameAttribute_ConnectionInitializationRoutine(
                InitBlockPtr    initBlkPtr) ;

void        NameAttribute_ConnectionTerminationRoutine (
                void) ;


#endif
```

[Next](NameAttrTest.c.md)[Previous](NameAttribute.c.md)

