---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAECountElements_h.html
archived_at: '2026-07-18T03:14:37.050183Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAECreate.c.md)[Previous](Sources-MSAECountElements.c.md)

# Sources/MSAECountElements.h

```c
// MSAECountElements.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAECOUNTELEMENTS__
#define __MSAECOUNTELEMENTS__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>

pascal OSErr    DoCountElements(const AppleEvent    *theAppleEvent,
                                      AppleEvent    *reply,
                                      long          handlerRefCon);

pascal OSErr    MyCountProc(DescType desiredType, DescType containerClass,
                                        const AEDesc *container, long* result);

OSErr           GetDescForNumberOfElements(DescType desiredType,
                                            AEDesc* container, AEDesc* result);

#endif
```

[Next](Sources-MSAECreate.c.md)[Previous](Sources-MSAECountElements.c.md)

