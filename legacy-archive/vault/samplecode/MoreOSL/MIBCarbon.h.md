---
title: MoreOSL
apple_id: DTS10000670
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: ApplicationServices
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MoreOSL/Listings/MIB_Carbon_h.html
archived_at: '2026-07-18T03:15:50.407026Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MoreOSL](MoreOSL.md)


[Next](MoreAppearance-MoreAppearance.cp.md)[Previous](MoreOSL.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html%23//apple_ref/doc/uid/TP40002164](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

# MIB_Carbon.h

```
/*
    File:       MIB_Carbon.h

    Contains:   prefix for Carbon target in MIB libraries project

    Written by: Pete Gontier

    Copyright:  Copyright © 1999 Apple Computer, Inc.

    Change History (most recent first):

         <2>     23/9/99    Quinn   Define TARGET_API_MAC_CARBON, which is the real name of the
                                    switch.  I'll remove TARGET_CARBON in some future release, once
                                    MIB has made the switch to UI 3.3.
         <1>     2/11/99    PCG     initial check-in
*/



#pragma once

    //
    //  This file is just here to tell the Carbon target in the
    //  library project to compile for Carbon. You don't need to
    //  include this file; all it will ever do is #define TARGET_CARBON.
    //  And, with that...
    //

#define TARGET_CARBON 1

    //  TARGET_CARBON was used by older versions of the Carbon
    //  interfaces.  Modern code should use TARGET_API_MAC_CARBON.
    //  I've added the definition here, but I haven't removed
    //  the TARGET_CARBON definition because it's used by lots
    //  of code within MIB and MIB isn't prepared to make the
    //  leap to Universal Interfaces 3.3 yet (because they're
    //  not final yet)

#define TARGET_API_MAC_CARBON 1
```

[Next](MoreAppearance-MoreAppearance.cp.md)[Previous](MoreOSL.md)

