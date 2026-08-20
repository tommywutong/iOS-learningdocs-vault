---
title: INIT - CDEV
apple_id: DTS10000187
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/INIT_-_CDEV/Listings/SAGlobals_c.html
archived_at: '2026-07-18T03:12:04.857776Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [INIT - CDEV](INIT%20-%20CDEV.md)


[Next](SAGlobals.h.md)[Previous](INITInstall.a.md)

# SAGlobals.c

```c
/*------------------------------------------------------------------------------
#
#   Macintosh Developer Technical Support
#
#   Sample Control Panel Device and INIT Combination
#
#   Program:    INIT - CDEV
#   File:       SAGlobals.c -   C Source
#
#   Copyright © 1990 Apple Computer, Inc.
#   All rights reserved.
#
------------------------------------------------------------------------------*/

#include <Memory.h>
#include <OSUtils.h>
#include <SAGlobals.h>

#define kAppParmsSize 32

/*
    !!! NOTE !!!

    These routines are used to implement global variables in standalone code,
    as per Technote #256. However, they have been modified here to allocate
    the buffer space from a non-relocatable pointer rather than a relocatable
    handle. The reason for this is because our globals will be used in our
    INIT to hold a PPC parameter block. Our INIT will prime a PPCInform call,
    and then exit. While the INIT is not executing and while the PPCInform
    call is outstanding, we don't want our globals to move. Since our INIT
    will be spending 99.9999999% of its time in this state, it doesn't made
    sense to allocate our memory from a handle. And since the best place for a
    block of memory that isn't going to be moving is low in the heap, we
    allocate the block with NewPtr. 
*/

long A5Size (void);
/* prototype for routine in Runtime.o */

void A5Init (Ptr myA5);
/* prototype for routine in Runtime.o */

pascal void MakeA5World (A5RefType *A5Ref) {
    *A5Ref = NewPtr(A5Size());
    if ((long)*A5Ref) {
        A5Init((Ptr)( (long)*A5Ref + A5Size() - kAppParmsSize));
    }
}

pascal long SetA5World (A5RefType A5Ref) {
    return SetA5( (long)A5Ref + A5Size() - kAppParmsSize);
}

pascal void DisposeA5World (A5RefType A5Ref) {
    DisposePtr((Ptr)A5Ref);
}
```

[Next](SAGlobals.h.md)[Previous](INITInstall.a.md)

