---
title: CallMachOFramework
apple_id: DTS10001082
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-17'
source_url: https://developer.apple.com/library/archive/samplecode/CallMachOFramework/Listings/MIB_Carbon_h.html
archived_at: '2026-07-18T03:02:50.372470Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CallMachOFramework](CallMachOFramework.md)


[Next](MoreCodeFragments-CFMLateImport-CallMachOFramework-CallMachOFramework.c.md)[Previous](CallMachOFramework.md)

# MIB_Carbon.h

```
/*
    File:       MIB_Carbon.h

    Contains:   prefix for Carbon target in MIB libraries project

    Written by: Pete Gontier

    Copyright:  Copyright © 1999 Apple Computer, Inc.

    Change History (most recent first):

         <3>     21/9/01    Quinn   Changes for CWPro7 Mach-O build.
         <2>     23/9/99    Quinn   Define TARGET_API_MAC_CARBON, which is the real name of the
                                    switch.  I'll remove TARGET_CARBON in some future release, once
                                    MIB has made the switch to UI 3.3.
         <1>     2/11/99    PCG     initial check-in
*/



#pragma once

    //
    //  This file is just here to tell the Carbon target in the
    //  library project to compile for Carbon. You don't need to
    //  include this file; all it will ever do is #define TARGET_API_MAC_CARBON.
    //  And, with that...
    //

#define TARGET_API_MAC_CARBON 1
```

[Next](MoreCodeFragments-CFMLateImport-CallMachOFramework-CallMachOFramework.c.md)[Previous](CallMachOFramework.md)

