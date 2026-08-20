---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAEClose_h.html
archived_at: '2026-07-18T03:14:36.567253Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAECoercions.c.md)[Previous](Sources-MSAEClose.c.md)

# Sources/MSAEClose.h

```c
// MSAEClose.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAECLOSE__
#define __MSAECLOSE__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>

#include "MSToken.h"

pascal OSErr    DoCloseWindow(const AppleEvent *theAppleEvent, AppleEvent *reply, long refcon);

OSErr           CloseWindowToken(WindowToken* theToken, DescType saveOpt);
OSErr           CloseWindowDesc(AEDesc* windowDesc, DescType saveOpt);
OSErr           CloseDesc(AEDesc* aDesc, DescType saveOpt);

#endif
```

[Next](Sources-MSAECoercions.c.md)[Previous](Sources-MSAEClose.c.md)

