---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAERevert_h.html
archived_at: '2026-07-18T03:14:38.705697Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAESave.c.md)[Previous](Sources-MSAERevert.c.md)

# Sources/MSAERevert.h

```c
// MSRevert.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAEREVERT__
#define __MSAEREVERT__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>

#include "MSToken.h"

pascal OSErr    DoRevert(const AppleEvent *theAppleEvent, AppleEvent *reply, long refcon);

OSErr           RevertDocumentToken(WindowToken* theToken);
OSErr           RevertDocumentDesc(AEDesc* textDesc);
OSErr           RevertDesc(AEDesc* aDesc);

#endif
```

[Next](Sources-MSAESave.c.md)[Previous](Sources-MSAERevert.c.md)

