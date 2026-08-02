---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAEGetDataSize_h.html
archived_at: '2026-07-18T03:14:37.554263Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAEMenuUtils.c.md)[Previous](Sources-MSAEGetDataSize.c.md)

# Sources/MSAEGetDataSize.h

```c
// MSGetDataSize.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAEGETDATASIZE__
#define __MSAEGETDATASIZE__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>

#include "MSToken.h"

pascal OSErr    DoGetDataSize(const AppleEvent *theAppleEvent, AppleEvent *reply, long refcon);

OSErr           GetDataSizeTextToken(TextToken* theToken, AEDesc* result);
OSErr           GetDataSizeTextDesc(AEDesc* textDesc, AEDesc* result);
OSErr           GetDataSizeDesc(AEDesc* aDesc, DescType reqType, AEDesc* result);

#endif
```

[Next](Sources-MSAEMenuUtils.c.md)[Previous](Sources-MSAEGetDataSize.c.md)

