---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAEMove_h.html
archived_at: '2026-07-18T03:14:38.040486Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAEObjectsExist.c.md)[Previous](Sources-MSAEMove.c.md)

# Sources/MSAEMove.h

```c
// MSAEMove.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAEMOVE__
#define __MSAEMOVE__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>

#include "MSToken.h"


pascal OSErr    DoMove(const AppleEvent *theAppleEvent, AppleEvent *reply, long  handlerRefCon);

OSErr           MoveTextToken(TextToken* token, AEDesc* insertHereDesc, AEDesc* result);
OSErr           MoveTextDesc(AEDesc* textDesc, AEDesc* insertHereDesc, AEDesc* result);
OSErr           MoveDesc(AEDesc* aDesc, AEDesc* insertHereDesc, AEDesc* result);

#endif
```

[Next](Sources-MSAEObjectsExist.c.md)[Previous](Sources-MSAEMove.c.md)

