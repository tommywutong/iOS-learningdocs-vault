---
title: Restore Screen Cluts
apple_id: DTS10000159
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-12'
source_url: https://developer.apple.com/library/archive/samplecode/Restore_Screen_Cluts/Listings/EmergMem_c.html
archived_at: '2026-07-18T03:22:10.815208Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Restore Screen Cluts](Restore%20Screen%20Cluts.md)


[Next](EmergMem.h.md)[Previous](ColorReset.h.md)

# EmergMem.c

```c
/*
    File:       EmergMem.c

    Contains:   Source code for the emergency memory routines

    Written by: Forrest Tanaka  

    Copyright:  Copyright © 1988-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/13/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/


/******************************************************************************\
* Header Files
\******************************************************************************/

#ifndef THINK_C
#include <OSUtils.h>
#endif

#include "EmergMem.h"


/******************************************************************************\
* Constants
\******************************************************************************/

#define kEmergMemSize 32768 /* Number of bytes of emergency mem to allocate */
#define kMemoryMargin 32768 /* Òsignificant amountÓ amount of free mem */


/******************************************************************************\
* Global Variables
\******************************************************************************/

Handle gEmergMem; /* Handle to block of emergency memory */


/******************************************************************************\
* Private: AppGrowZone - Custom grow-zone procedure
*
* This is a very basic grow zone procedure.  My application keeps a reserve
* handle of memory in case the Memory Manager gets a request for some memory
* that is not available in my heap.  If memory were to get tight (<32k or so),
* the Toolbox could crash the system.  This grow-zone proc tries to thwart that
* possibility by releasing the 32K block of emergency memory if it hasnÕt been
* released already and if the amount of memory requested is less than 32K.
* Hopefully, thatÕs enough to satisfy the memory request.
*
* There are three conditions in which the emergency memory isnÕt freed.  If the
* emergency memory is already free, obviously there isnÕt much that can be done.
* If the emergency memory is equal to GZSaveHnd, then it was the reallocation of
* emergency memory that caused this grow-zone proc to be called.  So it doesnÕt
* make much sense to free it in that case.  If the size of the memory request is
* more than the size of emergency memory, then I donÕt bother to free emergency
* memory because I assume that the toolbox handles such huge requests for memory
* properly.  Warning: that isnÕt always a good assumption, but thatÕs not my
* fault.
*
*     WARNING: Register A5 might not be valid when grow-zone procedures
*     are called. Read Technical Note #136 and 208.
*
* The "cbNeeded" parameter is the number of bytes that the Memory Manager needs
* to fulfill the memory request it had received.  The number of bytes actually
* freed by AppGrowZone is returned.
\******************************************************************************/

static pascal long AppGrowZone(
    Size cbNeeded) /* Number of bytes needed by Memory Manager */
{
    long theA5;       /* Value of A5 when AppGrowZone is called */
    long amountFreed; /* Number of bytes freed up */

    /* Remember the current value of A5 */
    theA5 = SetCurrentA5();

    /* Free emergency memory if possible */
    if (!NoEmergMem() && (gEmergMem != GZSaveHnd()) &&
            (cbNeeded <= kEmergMemSize))
    {
        EmptyHandle( gEmergMem );
        amountFreed = kEmergMemSize;
    }
    else
        amountFreed = 0;

    /* Restore A5 */
    (void)SetA5( theA5 );

    /* Return number of bytes freed */
    return amountFreed;
}


/******************************************************************************\
* Public: InstallAppGZ
*
* Installing our custom grow-zone procedure simply involves calling SetGrowZone
* with the address of our custom grow-zone procedure.
\******************************************************************************/

void InstallAppGZ()
{
    SetGrowZone( NewGrowZoneProc(AppGrowZone) );
}


/******************************************************************************\
* Public: DeinstallAppGZ
*
* Passing NIL to SetGrowZone is all thatÕs needed to tell the Memory Manager not
* to call a grow-zone procedure whenenver memory requests canÕt be satisfied.
\******************************************************************************/

void DeinstallAppGZ()
{
    SetGrowZone( nil );
}


/******************************************************************************\
* Public: InitEmergMem
*
* If the block of emergency memory couldnÕt be allocated, then weÕre probably in
* some pretty big trouble.  But InitEmergMem tries to deal as best it can in
* that case by allocating an empty handle; that is, it allocates a master
* pointer thatÕs set to NIL.  That leaves it up to the rest of the application
* to decide what to do.
\******************************************************************************/

void InitEmergMem()
{
    /* Allocate the block of emergency memory */
    gEmergMem = NewHandle( kEmergMemSize );
    if (gEmergMem == nil)
        /* CouldnÕt allocate emergency memory; just allocate an empty handle */
        gEmergMem = NewEmptyHandle();

    /* Now that emergency memory is initialized, can install grow zone proc */
    InstallAppGZ();
}


/******************************************************************************\
* Public: RecoverEmergMem
*
* ReallocHandle takes an existing empty handle (handle whose master pointer is
* nil) and allocates a block of memory for it.  Perfect for this job!
\******************************************************************************/

void RecoverEmergMem()
{
    ReallocateHandle( gEmergMem, kEmergMemSize );
}


/******************************************************************************\
* Public: FailLowMemory
*
* PurgeSpace is used to determine how much free memory thereÕd be in the heap if
* all purgeable blocks were purged.  If this amount is less than the amount
* needed, or if there isnÕt any emergency memory, true is returned.
\******************************************************************************/

Boolean FailLowMemory(
    long memRequest) /* Amount of memory to check */
{
    long total;  /* Total amount of free memory if heap was purged */
    long contig; /* Max amount of free contiguous memory if heap was purged */

    PurgeSpace( /*<*/&total, /*<*/&contig );
    return (total < (memRequest + kMemoryMargin)) || NoEmergMem();
}


/******************************************************************************\
* Public: NoEmergMem
*
* We check on the handle and the master pointer of gEmergMem to see if the
* emergency memory block has been emptied by AppGrowZone, or was never allocated
* in the first place.  StripAddress is called because weÕre comparing the master
* pointer of the emergency memory handle against zero, and the upper byte of
* master pointers can be non-zero if the machine is booted in 24-bit addressing
* mode.
\******************************************************************************/

Boolean NoEmergMem()
{
    /* Empty handle means no emergency memory */
    return (gEmergMem == nil) || (StripAddress( *gEmergMem ) == nil);
}


/******************************************************************************\
* Public: NewHandleMargin
*
* I donÕt call SysError with an ID 25 if there isnÕt enough memory to satisfy
* the request, so there isnÕt much reason to use the grow-zone proc.  So, I
* deinstall the grow-zone proc temporarily just before I allocate the memory.
\******************************************************************************/

Handle NewHandleMargin(
    Size    requestedSize, /* Number of bytes requested to be allocated */
    Boolean appHeapAlloc,  /* Allocate in app heap or system heap? */
    Boolean clearMem)      /* Clear allocated memory or leave it alone? */
{
    Handle aHandle; /* Handle to newly-allocated memory */

    if (FailLowMemory( requestedSize ))
        aHandle = nil;
    else
    {
        /* We handle memFullErr properly, so donÕt need grow-zone proc */
        DeinstallAppGZ();

        /* Allocate the memory with the requested options */
        if (!appHeapAlloc && clearMem)
            aHandle = NewHandleSysClear( requestedSize );
        else if (!appHeapAlloc)
            aHandle = NewHandleSys( requestedSize );
        else if (clearMem)
            aHandle = NewHandleClear( requestedSize );
        else
            aHandle = NewHandle( requestedSize );

        /* Install the grow-zone proc again */
        InstallAppGZ();
    }

    return aHandle;
}


/******************************************************************************\
* Public: NewPtrMargin
*
* I donÕt call SysError with an ID 25 if there isnÕt enough memory to satisfy
* the request, so there isnÕt much reason to use the grow-zone proc.  So, I
* disconnect the grow-zone proc temporarily just before I allocate the memory.
\******************************************************************************/

Ptr NewPtrMargin(
    Size    requestedSize, /* Number of bytes requested to be allocated */
    Boolean appHeapAlloc,  /* Allocate in app heap or system heap? */
    Boolean clearMem)      /* Clear allocated memory or leave it alone? */
{
    Ptr aPtr; /* Pointer to newly-allocated memory */

    if (FailLowMemory( requestedSize ))
        aPtr = nil;
    else
    {
        /* We handle memFullErr properly, so donÕt need grow-zone proc */
        DeinstallAppGZ();

        /* Allocate the memory with the requested options */
        if (!appHeapAlloc && clearMem)
            aPtr = NewPtrSysClear( requestedSize );
        else if (! appHeapAlloc)
            aPtr = NewPtrSys( requestedSize );
        else if (clearMem)
            aPtr = NewPtrClear( requestedSize );
        else
            aPtr = NewPtr( requestedSize );

        /* Connect up the grow-zone proc again */
        InstallAppGZ();
    }

    return aPtr;
}
```

[Next](EmergMem.h.md)[Previous](ColorReset.h.md)

