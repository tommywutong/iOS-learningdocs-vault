---
title: PPCToolboxKeychain
apple_id: DTS10000210
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/PPCToolboxKeychain/Listings/MIB_Bits_MoreMemory_c.html
archived_at: '2026-07-18T03:18:37.018044Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PPCToolboxKeychain](PPCToolboxKeychain.md)


[Next](MIB%20Bits-MoreMemory.h.md)[Previous](MIB%20Bits-MoreAppleEvents.h.md)

# MIB Bits/MoreMemory.c

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

         <3>     20/3/00    Quinn   Added MoreBlockCompare.
         <2>      6/3/00    Quinn   Added MoreMemError and temporarily removed SafeHoldMemory from
                                    Carbon builds.
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

#if CALL_NOT_IN_CARBON

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

#endif

extern pascal OSErr MoreMemError(void *p)
    // See comment in interface part.
{
    OSErr err;

    err = MemError();
    if ((err == noErr) && (p == nil)) {
        MoreAssertQ(false);
        err = memFullErr;
    }
    return err;
}

extern pascal Boolean MoreBlockCompare(const void *p1, const void *p2, ByteCount numBytes)
    // See comment in interface part.
{
    const UInt8 *cursor1;
    const UInt8 *cursor2;

    cursor1 = p1;   
    cursor2 = p2;
    while (numBytes > 0 && (*cursor1 == *cursor2)) {
        cursor1 += 1;
        cursor2 += 1;
        numBytes -= 1;
    }
    return (numBytes == 0);
}
```

[Next](MIB%20Bits-MoreMemory.h.md)[Previous](MIB%20Bits-MoreAppleEvents.h.md)

