---
title: MoreOSL
apple_id: DTS10000670
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: ApplicationServices
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MoreOSL/Listings/MoreAppearance_MoreAppearance_h.html
archived_at: '2026-07-18T03:15:50.556090Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MoreOSL](MoreOSL.md)


[Next](MoreAppleEvents-MoreAEObjects.c.md)[Previous](MoreAppearance-MoreAppearance.cp.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html%23//apple_ref/doc/uid/TP40002164](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

# MoreAppearance/MoreAppearance.h

```c
/*
    File:       MoreAppearance.h

    Contains:   

    Written by: Pete Gontier

    Copyright:  Copyright (c) 1998 Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):

         <3>     20/3/00    Quinn   Comment changes that I made in the implementation.
         <2>    11/11/98    PCG     fix headers
         <1>    11/10/98    PCG     first big re-org at behest of Quinn

    Old Change History (most recent first):

         <5>    10/11/98    Quinn   Convert "MorePrefix.h" to "MoreSetup.h".
         <4>      9/4/98    PCG     #pragma export on
         <3>      9/1/98    PCG     add theme drawing state functions
         <2>     7/24/98    PCG     coddle linker (C++, CFM-68K)
         <1>     6/16/98    PCG     initial checkin
*/

#pragma once

#include "MoreSetup.h"

#include <Appearance.h>

typedef struct MoreThemeDrawingStateTag *MoreThemeDrawingState;

#ifdef __cplusplus
    extern "C" {
#endif

#pragma import on // for clients
#pragma export on // for building a library

pascal OSStatus     InitMoreAppearance              (void);

pascal Boolean      HaveAppearance                  (void);
pascal Boolean      AppearanceInCompatibilityMode   (void);
pascal long         GetAppearanceVersion            (void);
    // The above routines now implicitly call InitMoreAppearance
    // if you havenÕt done so.

pascal OSStatus     MoreGetThemeDrawingState        (MoreThemeDrawingState *);
pascal OSStatus     MoreNormalizeThemeDrawingState  (void);
pascal OSStatus     MoreSetThemeDrawingState        (MoreThemeDrawingState, Boolean disposeNow);
pascal OSStatus     MoreDisposeThemeDrawingState    (MoreThemeDrawingState);

#pragma import reset // for clients
#pragma export reset // for building a library

#ifdef __cplusplus
    }
#endif
```

[Next](MoreAppleEvents-MoreAEObjects.c.md)[Previous](MoreAppearance-MoreAppearance.cp.md)

