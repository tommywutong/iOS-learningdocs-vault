---
title: BasicDiskImage
apple_id: DTS10000425
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BasicDiskImage/Listings/MoreIsBetterBits_MoreMemory_c.html
archived_at: '2026-07-18T03:01:45.400675Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BasicDiskImage](BasicDiskImage.md)


[Next](MoreIsBetterBits-MoreMemory.h.md)[Previous](MoreIsBetterBits-MoreInterfaceLib.h.md)

# MoreIsBetterBits/MoreMemory.c

```c
/*
    File:       MoreMemory.c

    Contains:   Memory utility routines.

    Written by: Quinn

    Copyright:  Copyright © 1999 by Apple Computer, Inc., all rights reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):

         <1>      1/3/99    Quinn   First checked in.
*/

/////////////////////////////////////////////////////////////////
// MoreIsBetter Setup

#include "MoreSetup.h"

/////////////////////////////////////////////////////////////////
// Mac OS Interfaces

#include <Traps.h>
#include <Patches.h>
#include <Memory.h>

/////////////////////////////////////////////////////////////////
// Our Prototypes

#include "MoreMemory.h"

/////////////////////////////////////////////////////////////////

extern pascal OSErr SafeHoldMemory(void *start, ByteCount length)
    // See comment in interface part.
{
    OSErr err;

    err = noErr;
    if ( GetOSTrapAddress(_HWPriv) != GetToolTrapAddress(_Unimplemented) ) {
        err = HoldMemory(start, length);
    }
    if (err == paramErr) {
        err = noErr;
    }
    return err;
}

extern pascal OSErr SafeUnholdMemory(void *start, ByteCount length)
    // See comment in interface part.
{
    OSErr err;

    err = noErr;
    if ( GetOSTrapAddress(_HWPriv) != GetToolTrapAddress(_Unimplemented) ) {
        err = UnholdMemory(start, length);
    }
    if (err == paramErr) {
        err = noErr;
    }
    return err;
}
```

[Next](MoreIsBetterBits-MoreMemory.h.md)[Previous](MoreIsBetterBits-MoreInterfaceLib.h.md)

