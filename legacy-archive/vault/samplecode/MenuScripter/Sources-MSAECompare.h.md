---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAECompare_h.html
archived_at: '2026-07-18T03:14:36.818695Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAECopy.c.md)[Previous](Sources-MSAECompare.c.md)

# Sources/MSAECompare.h

```c
// MSAECompare.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.

// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAECOMPARE__
#define __MSAECOMPARE__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>

OSErr           InstallObjectCallbacks(void);

pascal OSErr    MyCompareProc(DescType oper, const AEDesc* obj1,
                                        const AEDesc* obj2, Boolean *result);

OSErr           ExtractData (const AEDesc *sourceDesc, AEDesc *theData);

OSErr           MyCompareText(DescType oper, const AEDesc *desc1,
                                        const AEDesc *desc2, Boolean *result);
OSErr           MyCompareInteger(DescType oper, const AEDesc *desc1,
                                        const AEDesc *desc2, Boolean *result);
OSErr           MyCompareBoolean (DescType oper, const AEDesc *desc1,
                                        const AEDesc *desc2, Boolean *result);

#endif
```

[Next](Sources-MSAECopy.c.md)[Previous](Sources-MSAECompare.c.md)

