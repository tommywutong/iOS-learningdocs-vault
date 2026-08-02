---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAESelect_h.html
archived_at: '2026-07-18T03:14:38.957286Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAESetData.c.md)[Previous](Sources-MSAESelect.c.md)

# Sources/MSAESelect.h

```c
// MSAESelect.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAESELECT__
#define __MSAESELECT__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>

#include "MSToken.h"

pascal OSErr    DoSelect(const AppleEvent *theAppleEvent, AppleEvent *reply, long refcon);

OSErr           SelectWindowToken(WindowToken* theToken);
OSErr           SelectWindowDesc(AEDesc* windowDesc);

OSErr           SelectTextToken(TextToken* theToken);
OSErr           SelectTextDesc(AEDesc* textDesc);

OSErr           SelectMenuItemToken( MenuItemToken* theToken );
OSErr           SelectMenuItemDesc( AEDesc* theDesc );

OSErr           SelectDesc(const AEDesc* aDesc, AEDesc* result);

OSErr           GetWindowSelection(WindowPtr aWindow, TextToken* resultToken,
                                                                short* resultLength);
OSErr           UpdateSelectionToken(TextToken* anInsertToken, TextToken* aSelectionToken,
                                                        short oldLength, short* insertLength);

#endif
```

[Next](Sources-MSAESetData.c.md)[Previous](Sources-MSAESelect.c.md)

