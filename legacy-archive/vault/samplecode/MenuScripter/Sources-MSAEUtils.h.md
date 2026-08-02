---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAEUtils_h.html
archived_at: '2026-07-18T03:14:39.805974Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAEWindowUtils.c.md)[Previous](Sources-MSAEUtils.c.md)

# Sources/MSAEUtils.h

```c
// MSAEUtils.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#include <Types.h>
#include <Quickdraw.h>
#include <Packages.h>
#include <GestaltEqu.h>
#include <Editions.h>
#include <Printing.h>
#include <AppleEvents.h>
#include <ToolUtils.h>

#ifndef __MSAEUTILS__
#define __MSAEUTILS__

#include "MSToken.h"

    // Utility Routines for getting data from AEDesc's

void    GetRawDataFromDescriptor(const AEDesc *theDesc, Ptr destPtr,
                                            Size destMaxSize, Size *actSize);

OSErr   GetPStringFromDescriptor(const AEDesc *aDesc, StringPtr resultStr);
OSErr   PutPStringToDescriptor(AEDesc* aDesc, StringPtr pStr);
OSErr   GetIntegerFromDescriptor(const AEDesc *sourceDesc, short *result);
OSErr   GetBooleanFromDescriptor(const AEDesc *sourceDesc, Boolean *result);
OSErr   GetLongIntFromDescriptor(const AEDesc *sourceDesc, long   *result);
OSErr   GetRectFromDescriptor(const AEDesc *sourceDesc, Rect *result);
OSErr   GetPointFromDescriptor(const AEDesc *sourceDesc, Point  *result);
OSErr   GetEnumeratedFromDescriptor(const AEDesc *sourceDesc, DescType  *result);

    // Parameter routines

OSErr       GotRequiredParams(const AppleEvent *theAppleEvent);
OSErr       AddResultToReply(AEDesc* result, AEDesc* reply, OSErr error);

    // Routine so events can be sent to self

OSErr       MakeSelfAddress(AEAddressDesc *selfAddress);


#endif
```

[Next](Sources-MSAEWindowUtils.c.md)[Previous](Sources-MSAEUtils.c.md)

