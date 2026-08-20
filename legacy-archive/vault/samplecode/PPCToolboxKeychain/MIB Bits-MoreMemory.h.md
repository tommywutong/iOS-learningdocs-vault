---
title: PPCToolboxKeychain
apple_id: DTS10000210
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/PPCToolboxKeychain/Listings/MIB_Bits_MoreMemory_h.html
archived_at: '2026-07-18T03:18:37.076855Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PPCToolboxKeychain](PPCToolboxKeychain.md)


[Next](MIB%20Bits-MoreProcesses.cp.md)[Previous](MIB%20Bits-MoreMemory.c.md)

# MIB Bits/MoreMemory.h

```c
/*
    File:       MoreMemory.h

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

         <4>     11/4/00    Quinn   Added some flags that should be Universal Interfaces.
         <3>     20/3/00    Quinn   Added MoreBlockCompare.
         <2>      6/3/00    Quinn   Added MoreMemError and temporarily removed SafeHoldMemory from
                                    Carbon builds.
         <1>      1/3/99    Quinn   First checked in.
*/

#pragma once

/////////////////////////////////////////////////////////////////
// MoreIsBetter Setup

#include "MoreSetup.h"

/////////////////////////////////////////////////////////////////
// Mac OS Interfaces

#ifdef __cplusplus
extern "C" {
#endif

// Constants for testing and modifying bits in the results of HGetState.
// These belong in Universal Interfaces but arenÕt there yet [2212458.]

enum {
    kHandleLockedBit      = 7,
    kHandlePurgeableBit   = 6,
    kHandleIsResourceBit  = 5,

    kHandleLockedMask     = 0x80,
    kHandlePurgeableMask  = 0x40,
    kHandleIsResourceMask = 0x20
};

// HoldMemory is not available to Carbon clients, even though SCSIAction
// on traditional Mac OS requires you to use it.  For the moment IÕve
// just made these routines CALL_NOT_IN_CARBON.  I probably should
// reimplement these routines so that they call use CFM to load
// the InterfaceLib versions of HoldMemory and UnholdMemory, but 
// thatÕs not high on my priority list right now.

#if CALL_NOT_IN_CARBON

extern pascal OSErr SafeHoldMemory(void *start, ByteCount length);
    // A safe version of the HoldMemory call, that does the right
    // thing regardless of whether the HoldMemory trap is actually
    // implemented.
    //
    // Note that if the system can't hold the memory because there's
    // not enough physical memory, this routine will return
    // notEnoughMemoryErr.

extern pascal OSErr SafeUnholdMemory(void *start, ByteCount length);
    // A safe version of the HoldMemory call, that does the right
    // thing regardless of whether the HoldMemory trap is actually
    // implemented.

#endif

extern pascal OSErr MoreMemError(void *p);
    // Returns MemError() or, if itÕs noErr and p is nil,
    // asserts and returns memFullErr.  The rationale for this routine
    // is that some folks (interrupt-time code or patches) can clear
    // MemErr unexpectedly.

extern pascal Boolean MoreBlockCompare(const void *p1, const void *p2, ByteCount numBytes);
    // Compares two blocks of memory, byte for byte, return true if they are equal.
    // Nice for places where you donÕt want to depend on StdCLib.

#ifdef __cplusplus
}
#endif
```

[Next](MIB%20Bits-MoreProcesses.cp.md)[Previous](MIB%20Bits-MoreMemory.c.md)

