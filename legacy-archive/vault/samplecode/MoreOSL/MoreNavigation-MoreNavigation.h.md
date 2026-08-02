---
title: MoreOSL
apple_id: DTS10000670
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: ApplicationServices
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MoreOSL/Listings/MoreNavigation_MoreNavigation_h.html
archived_at: '2026-07-18T03:15:51.980501Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MoreOSL](MoreOSL.md)


[Next](MoreOSL-MoreOSL.c.md)[Previous](MoreNavigation-MoreNavigation.c.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html%23//apple_ref/doc/uid/TP40002164](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

# MoreNavigation/MoreNavigation.h

```c
/*
    File:       MoreNavigation.h

    Contains:   Basic Navigation services utilities functionality.

    Written by: Quinn

    Copyright:  Copyright © 2000 by Apple Computer, Inc., all rights reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):

         <1>     20/3/00    Quinn   First checked in.
*/

#pragma once

/////////////////////////////////////////////////////////////////

// MoreIsBetter Setup

#include "MoreSetup.h"

// Mac OS Interfaces

#include <Files.h>
#include <Navigation.h>

/////////////////////////////////////////////////////////////////

#ifdef __cplusplus
extern "C" {
#endif

extern pascal OSStatus MoreNavExtractSingleReply(const NavReplyRecord *reply, FSSpec *target);
    // This routine extracts a single FSSpec from the selection
    // in the reply record.  It also normalises that FSSpec
    // to avoid Nav's broken Ôname is emptyÕ FSSpec's.  This
    // is boilerplate code required by all Nav clients that use
    // the save dialog.

#ifdef __cplusplus
};
#endif
```

[Next](MoreOSL-MoreOSL.c.md)[Previous](MoreNavigation-MoreNavigation.c.md)

