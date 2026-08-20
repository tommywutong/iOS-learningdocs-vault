---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAEClone_h.html
archived_at: '2026-07-18T03:14:36.472613Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAEClose.c.md)[Previous](Sources-MSAEClone.c.md)

# Sources/MSAEClone.h

```c
// MSAEClone.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAECLONE__
#define __MSAECLONE__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>

pascal OSErr    DoClone(const AppleEvent *theAppleEvent, AppleEvent *reply, long refcon);

OSErr           CloneTextDesc(AEDesc* textDesc, AEDesc* insertHereDesc, AEDesc* result);
OSErr           CloneDesc(AEDesc* aDesc, AEDesc* insertHereDesc, AEDesc* result);

#endif
```

[Next](Sources-MSAEClose.c.md)[Previous](Sources-MSAEClone.c.md)

