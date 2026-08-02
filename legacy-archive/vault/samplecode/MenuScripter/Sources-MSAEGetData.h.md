---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAEGetData_h.html
archived_at: '2026-07-18T03:14:37.801630Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAEGetDataSize.c.md)[Previous](Sources-MSAEGetData.c.md)

# Sources/MSAEGetData.h

```c
// MSAEGetData.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAEGETDATA__
#define __MSAEGETDATA__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>


#include "MSToken.h"


pascal OSErr    DoGetData(const AppleEvent  *theAppleEvent,
                                AppleEvent  *reply,
                                long        handlerRefCon);

pascal OSErr    DoGetDataSize(const AppleEvent  *theAppleEvent,
                                    AppleEvent  *reply,
                                    long        handlerRefCon);

OSErr           HandleGetData( AEDesc *theObj, DescType theWantType, AEDesc *result );

OSErr           GetTextProperty(const AEDesc *theTokenDesc, AEDesc *result);
OSErr           GetWindowProperty(const AEDesc *theTokenDesc, AEDesc *result);
OSErr           GetWindowTokenProperty( WindowPropToken* thePropToken, AEDesc *result );
OSErr           GetDocumentProperty( const AEDesc *theTokenDesc,
                                            DescType theWantType, AEDesc *result );
OSErr           GetDocumentTokenProperty( WindowPropToken* theToken,
                                            DescType theWantType, AEDesc *result );
OSErr           GetApplicationProperty( const AEDesc *theTokenDesc,
                                            DescType theWantType, AEDesc *result );
OSErr           GetMenuProperty(const AEDesc *theTokenDesc,
                                            DescType theWantType, AEDesc *result);
OSErr           GetMenuItemProperty(const AEDesc *theTokenDesc,
                                            DescType theWantType, AEDesc *result);

OSErr           GetTextTextProperty(TextToken* theToken, AEDesc *result);
#endif
```

[Next](Sources-MSAEGetDataSize.c.md)[Previous](Sources-MSAEGetData.c.md)

