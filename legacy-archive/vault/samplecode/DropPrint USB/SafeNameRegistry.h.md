---
title: DropPrint USB
apple_id: DTS10000288
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/DropPrint_USB/Listings/SafeNameRegistry_h.html
archived_at: '2026-07-18T03:07:22.064650Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DropPrint USB](DropPrint%20USB.md)


[Next](TestPrinterClass.c.md)[Previous](SafeNameRegistry.c.md)

# SafeNameRegistry.h

```c
/*
    File:       SafeNameRegistry.h

    Contains:   Prototypes for stub routines for name registry calls

    Written by: G. Poon

    Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.

    Change History:

        25 Mar 98   gp      Added InitNameRegistryPtrs and RemoveNameRegistryPtrs prototypes
        18 Mar 98   gp      Created

    To Do:
*/


#ifndef __SafeNameRegistry__
#define __SafeNameRegistry__

#ifndef __NAMEREGISTRY__
#include "NameRegistry.h"
#endif

extern  Boolean NameRegistryInstalled( void );

// prototypes for name registry stub routines
extern  OSStatus SafeRegistryEntryIDInit(RegEntryID *id);
extern  OSStatus SafeRegistryCStrEntryLookup( RegEntryID *searchPointID, 
        RegCStrPathName *pathName, RegEntryID *foundEntry);
extern  OSStatus SafeRegistryEntryIterateCreate(RegEntryIter *cookie);
extern  OSStatus SafeRegistryEntryIterateDispose(RegEntryIter *cookie);
extern  OSStatus SafeRegistryEntryIterateSet(RegEntryIter *cookie, RegEntryID *startEntryID);
extern  OSStatus SafeRegistryEntryIterate(RegEntryIter *cookie, 
            RegEntryIterationOp relationship, RegEntryID *foundEntry, Boolean *done);
extern  OSStatus SafeRegistryEntryIDDispose(RegEntryID *id);
extern  OSStatus SafeRegistryPropertyGet( RegEntryID *entryID, 
            RegPropertyName *propertyName, void *propertyValue, RegPropertyValueSize *propertySize);
extern  void    InitNameRegistryPtrs( void );
extern  void    RemoveNameRegistryPtrs( void );

#endif
```

[Next](TestPrinterClass.c.md)[Previous](SafeNameRegistry.c.md)

