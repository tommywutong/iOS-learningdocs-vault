---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAEPaste_h.html
archived_at: '2026-07-18T03:14:38.214203Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAERecording.c.md)[Previous](Sources-MSAEPaste.c.md)

# Sources/MSAEPaste.h

```c
// MSAEPaste.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAEPASTE__
#define __MSAEPASTE__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>

#include "MSToken.h"

pascal OSErr    DoPaste(const AppleEvent *theAppleEvent, AppleEvent *reply, long refcon);

OSErr           PasteTextToken(TextToken* theToken);
OSErr           PasteTextDesc(AEDesc* textDesc);
OSErr           PasteDesc(AEDesc* aDesc);

#endif
```

[Next](Sources-MSAERecording.c.md)[Previous](Sources-MSAEPaste.c.md)

