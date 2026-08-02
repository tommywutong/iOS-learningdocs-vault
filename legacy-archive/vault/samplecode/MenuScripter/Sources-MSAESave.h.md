---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAESave_h.html
archived_at: '2026-07-18T03:14:38.820246Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAESelect.c.md)[Previous](Sources-MSAESave.c.md)

# Sources/MSAESave.h

```c
// MSAESave.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAESAVE__
#define __MSAESAVE__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>

#include "MSToken.h"

pascal OSErr    DoSaveWindow(const AppleEvent *theAppleEvent, AppleEvent *reply, long refcon);

OSErr           SaveDocumentToken(WindowToken* theToken, FSSpec* destFSSpec);
OSErr           SaveDocumentDesc(AEDesc* windowDesc, FSSpec* destFSSpec);
OSErr           SaveDesc(AEDesc* aDesc, FSSpec* destFSSpec);

#endif
```

[Next](Sources-MSAESelect.c.md)[Previous](Sources-MSAESave.c.md)

