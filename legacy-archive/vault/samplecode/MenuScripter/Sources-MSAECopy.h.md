---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAECopy_h.html
archived_at: '2026-07-18T03:14:36.915761Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAECountElements.c.md)[Previous](Sources-MSAECopy.c.md)

# Sources/MSAECopy.h

```c
// MSAECopy.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.

// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAECOPY__
#define __MSAECOPY__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>

#include "MSToken.h"

pascal OSErr    DoCopy(const AppleEvent *theAppleEvent, AppleEvent *reply, long refcon);

OSErr           CopyTextToken(TextToken* theToken);
OSErr           CopyTextDesc(AEDesc* textDesc);
OSErr           CopyDesc(AEDesc* aDesc);

#endif
```

[Next](Sources-MSAECountElements.c.md)[Previous](Sources-MSAECopy.c.md)

