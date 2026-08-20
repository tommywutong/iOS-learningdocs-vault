---
title: How to Detect a CD
apple_id: DTS10000012
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/How_to_Detect_a_CD/Listings/WhereCDs_c.html
archived_at: '2026-07-18T03:11:57.534389Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [How to Detect a CD](How%20to%20Detect%20a%20CD.md)


[Next](WhereCDs.h.md)[Previous](Not%20used%20in%20this%20example-IsDriverOpen.h.md)

# WhereCDs.c

```c
/*
**  Apple Macintosh Developer Technical Support
**
**  Sample code demonstrating detecting CD-ROM drives
**
**  by Brian Bechtel, Apple Developer Technical Support
**
**  File:       WhereCDs.c
**
**  Copyright © 1995 Apple Computer, Inc.
**  All rights reserved.
**
**  You may incorporate this sample code into your applications without
**  restriction, though the sample code has been provided "AS IS" and the
**  responsibility for its operation is 100% yours.  However, what you are
**  not permitted to do is to redistribute the source as "DTS Sample Code"
**  after having made changes. If you're going to re-distribute the source,
**  we require that you make it clear in the source that the code was
**  descended from Apple Sample Code, but that you've made changes.
*/
#include <Devices.h>
#include <TextUtils.h>
#include "WhereCDs.h"

// From tech note DV 22, CD-ROM Driver Calls.  Detects drives which
// are using the driver name ".AppleCD" in the range of driver
// reference numbers assigned to the original SCSI bus.  Will not
// handle drives which aren't using a driver named ".AppleCD", nor
// drives on additional SCSI buses.
UInt8 WhereCDs() 
{ 
    UInt8       where = 0; /* assume no drives handled at beginning */
    short       scsiAddress; 
    short       drvrRefNum; 
    DCtlHandle  aDCtlEntry; 
    StringPtr   aDriverName; 
    StringPtr   appleDriverName = "\p.AppleCD";

    for (scsiAddress = 0; scsiAddress < 7; scsiAddress++) 
    { 
        drvrRefNum = -33 - scsiAddress;
        aDCtlEntry = GetDCtlEntry(drvrRefNum); 
        if (aDCtlEntry != nil) 
        { 
            if ((**aDCtlEntry).dCtlFlags & dRAMBasedMask) 
                aDriverName = (StringPtr) ((*(DCtlPtr)aDCtlEntry).dCtlDriver+18); 
            else 
                aDriverName = (StringPtr)((**aDCtlEntry).dCtlDriver+18); 
            if ( EqualString(aDriverName, appleDriverName, false, false) == true ) 
                where |= (1 << scsiAddress); 
        }
    }
    return where; 
}
```

[Next](WhereCDs.h.md)[Previous](Not%20used%20in%20this%20example-IsDriverOpen.h.md)

