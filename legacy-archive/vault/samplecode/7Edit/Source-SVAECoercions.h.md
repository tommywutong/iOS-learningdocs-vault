---
title: 7Edit
apple_id: DTS10000200
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/7Edit/Listings/Source_SVAECoercions_h.html
archived_at: '2026-07-18T02:59:16.641104Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [7Edit](7Edit.md)


[Next](Source-SVAECompare.c.md)[Previous](Source-SVAECoercions.c.md)

# Source/SVAECoercions.h

```c
/*
    File:       SVAECoercions.h

    Contains:   

    Written by: Original version by Jon Lansdell and Nigel Humphreys.
                3.1 updates by Greg Sutton.

    Copyright:  Copyright © 1995-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/20/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/

#ifndef __SVAECOERCIONS__
#define __SVAECOERCIONS__

#include <AppleEvents.h>
#include <AEObjects.h>
#include <AERegistry.h>

OSErr           InstallCoercions(void);

pascal OSErr    CoerceObjToAnything(const AEDesc    *theAEDesc,
                                    DescType        toType,
                                    long            handlerRefCon,
                                    AEDesc          *result);

pascal OSErr    CoerceWindowToText(AEDesc   *theAEDesc,
                                    DescType        toType,
                                    long            handlerRefCon,
                                    AEDesc          *result);

pascal OSErr    CoerceWindowPropertyToText(AEDesc       *theAEDesc,
                                            DescType    toType,
                                            long        handlerRefCon,
                                            AEDesc      *result);

pascal OSErr    CoerceListToAnything(AEDesc     *theAEDesc,
                                     DescType   toType,
                                     long       handlerRefCon,
                                     AEDesc     *result);

OSErr           CoerceAnythingToType(AEDesc* theDesc, DescType toType, AEDesc* result);
#endif
```

[Next](Source-SVAECompare.c.md)[Previous](Source-SVAECoercions.c.md)

