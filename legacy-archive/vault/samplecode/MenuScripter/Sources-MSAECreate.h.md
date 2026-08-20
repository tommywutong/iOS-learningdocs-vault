---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAECreate_h.html
archived_at: '2026-07-18T03:14:37.279852Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAECut.c.md)[Previous](Sources-MSAECreate.c.md)

# Sources/MSAECreate.h

```c
// MSAECreate.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAECREATE__
#define __MSAECREATE__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>

#include "MSToken.h"

pascal OSErr    DoNewElement(const AppleEvent   *theAppleEvent,
                                    AppleEvent  *reply, 
                                    long        handlerRefCon);

OSErr           CreateDocument(AEDesc* dataDesc, AEDesc* insertHereDesc,
                                        AEDesc* propertyDesc, AEDesc* result);

OSErr           GetBehindWindow(AEDesc* insertDesc, DescType insertType, WindowPtr* behindWindow);
OSErr           SetDocumentPropertyRecord(WindowPtr theWindow, AEDesc* propertyRecord);
OSErr           SetDocumentData(WindowPtr theWindow, AEDesc* dataDesc);

OSErr           CreateText(DescType textType, AEDesc* dataDesc, AEDesc* insertHereDesc,
                                                    AEDesc* propertyDesc, AEDesc* result);
OSErr           GetInsertToken(AEDesc* insertDesc, DescType insertType, TextToken* resultToken);
OSErr           CreateAtTextToken(DescType textType, const AEDesc* dataDesc, TextToken* theToken,
                                                        AEDesc* propertyDesc, AEDesc* result);
OSErr           SetTextPropertyRecord(TextToken* aTextToken, AEDesc* propertyRecord);

#endif
```

[Next](Sources-MSAECut.c.md)[Previous](Sources-MSAECreate.c.md)

