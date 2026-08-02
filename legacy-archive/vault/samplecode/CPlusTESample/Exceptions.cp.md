---
title: CPlusTESample
apple_id: DTS10000730
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CPlusTESample/Listings/Exceptions_cp.html
archived_at: '2026-07-18T03:02:43.518472Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CPlusTESample](CPlusTESample.md)


[Next](Exceptions.h.md)[Previous](Document.h.md)

# Exceptions.cp

```c
/*------------------------------------------------------------------------------------------

    Program:    CPlusTESample 2.0
    File:       Exceptions.cp
    Uses:       Exceptions.h

    by Andrew Shebanow
    of Apple Macintosh Developer Technical Support

    Copyright © 1989-1990 Apple Computer, Inc.
    All rights reserved.

------------------------------------------------------------------------------------------*/

#include "Exceptions.h"

extern "C" {
    long gFailMessage;      // Current failure message
    short gFailError;       // Current failure error
};

pascal void StandardHandler(short e, long m, void* Handler_StaticLink)
{
    gFailError = e;
    gFailMessage = m;
    longjmp((jmp_buf) Handler_StaticLink, 1);
}
```

[Next](Exceptions.h.md)[Previous](Document.h.md)

