---
title: How to Detect a CD
apple_id: DTS10000012
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/How_to_Detect_a_CD/Listings/Not_used_in_this_example_IsDriverOpen_c.html
archived_at: '2026-07-18T03:11:57.360285Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [How to Detect a CD](How%20to%20Detect%20a%20CD.md)


[Next](Not%20used%20in%20this%20example-IsDriverOpen.h.md)[Previous](Not%20used%20in%20this%20example-identifyCD.h.md)

# Not used in this example/IsDriverOpen.c

```c
#include <Memory.h>
#include <Devices.h>
#include <LowMem.h>
#include "IsDriverOpen.h"

// Return driver ref if driver is open

short IsDriverOpen(StringPtr driverName)
{
    short       dref;
    DCtlHandle  dceHndl;

    dref = 0;

    dceHndl = FindTheDriver(driverName);
    if (dceHndl != NULL) {

        if ((*dceHndl)->dCtlFlags & dOpenedMask)        //  if open (bit 5)
            dref = (*dceHndl)->dCtlRefNum;
    }

    return dref;
}


//  FindTheDriver
//  Return driver dctlhandle if it exists.

DCtlHandle FindTheDriver(StringPtr driverName)
{
    DCtlHandle  EntryHand;
    short       count;
    DCtlHandle  *utable;

    EntryHand = NULL;

//  number of entries in unit table.  LMGetUnitTableEntryCount isn't defined
//  for PowerPC, but this does the equivalent.  
    count = GetPtrSize(LMGetUTableBase()) / sizeof(DCtlHandle); 
    utable = (DCtlEntry ***) LMGetUTableBase();

    while (--count >= 0) {
        DCtlHandle  entry;

        entry = *utable++;
        if (entry != NULL) {
            StringPtr   namePtr;

        //  see if ram based (test bit 6)

            if ((*entry)->dCtlFlags & dRAMBasedMask) {

            //  in ram, so we have a handle
                namePtr = (StringPtr) (*(Handle)((*entry)->dCtlDriver)) + 18;

            } else {

            //  in rom, so we have a pointer
                namePtr = (StringPtr) ((*entry)->dCtlDriver) + 18;
            }

            if (RelString(driverName, namePtr, FALSE, TRUE) == 0) {

                EntryHand = entry;
                break;
            }
        }
    }

    return (EntryHand);
}
```

[Next](Not%20used%20in%20this%20example-IsDriverOpen.h.md)[Previous](Not%20used%20in%20this%20example-identifyCD.h.md)

