---
title: qtmissingcomp
apple_id: DTS10000867
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtmissingcomp/Listings/QTMissingComp_c.html
archived_at: '2026-07-26T19:52:46.635601Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtmissingcomp](qtmissingcomp.md)


[Next](QTMissingComp.h.md)[Previous](qtmissingcomp.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTMissingComp.c

```c
//////////
//
//  File:       QTMissingComp.c
//
//  Contains:   Sample code for detecting missing QuickTime components.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      03/24/99    rtm     first file
//
//////////

#include "QTMissingComp.h"

//////////
//
// QTMissing_IsComponentOfTypeAvailable
// Is the component with the specified type and subtype available?
//
//////////

Boolean QTMissing_IsComponentOfTypeAvailable (OSType theType, OSType theSubType)
{
    ComponentDescription        myCompDesc;
    Component                   myComponent = NULL;

    // look for the specified component
    myCompDesc.componentType = theType;
    myCompDesc.componentSubType = theSubType;
    myCompDesc.componentManufacturer = 0;
    myCompDesc.componentFlags = 0;
    myCompDesc.componentFlagsMask = cmpIsMissing;

    myComponent = FindNextComponent(NULL, &myCompDesc);

    return(myComponent != NULL);
}
```

[Next](QTMissingComp.h.md)[Previous](qtmissingcomp.md)

