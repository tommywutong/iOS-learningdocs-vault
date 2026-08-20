---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAECoercions_h.html
archived_at: '2026-07-18T03:14:36.666398Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAECompare.c.md)[Previous](Sources-MSAECoercions.c.md)

# Sources/MSAECoercions.h

```c
// MSAECoercions.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.

// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSAECOERCIONS__
#define __MSAECOERCIONS__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>

OSErr           InstallCoercions(void);

pascal OSErr    CoerceObjToAnything(const AEDesc    *theAEDesc,
                                    DescType        toType,
                                    long            handlerRefCon,
                                    AEDesc          *result);

pascal OSErr    CoerceDocumentToText(AEDesc *theAEDesc,
                                    DescType        toType,
                                    long            handlerRefCon,
                                    AEDesc          *result);

pascal OSErr    CoerceDocumentPropertyToText(AEDesc     *theAEDesc,
                                            DescType    toType,
                                            long        handlerRefCon,
                                            AEDesc      *result);

pascal OSErr    CoerceDocumentToWindow( DescType    typeCode,
                                        Ptr         dataPtr,
                                        Size        dataSize,
                                        DescType    toType,
                                        long        handlerRefcon,
                                        AEDesc*     result );

#endif
```

[Next](Sources-MSAECompare.c.md)[Previous](Sources-MSAECoercions.c.md)

