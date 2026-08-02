---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAEObjectsExist_h.html
archived_at: '2026-07-18T03:14:38.117062Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAEPaste.c.md)[Previous](Sources-MSAEObjectsExist.c.md)

# Sources/MSAEObjectsExist.h

```c
// MSAEObjectsExist.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAEOBJECTSEXIST__
#define __MSAEOBJECTSEXIST__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>

pascal OSErr DoObjectsExist(const AppleEvent    *theAppleEvent,
                                    AppleEvent  *reply, 
                                    long        handlerRefCon);

#endif
```

[Next](Sources-MSAEPaste.c.md)[Previous](Sources-MSAEObjectsExist.c.md)

