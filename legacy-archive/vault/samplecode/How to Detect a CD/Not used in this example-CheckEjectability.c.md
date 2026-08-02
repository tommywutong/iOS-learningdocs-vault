---
title: How to Detect a CD
apple_id: DTS10000012
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/How_to_Detect_a_CD/Listings/Not_used_in_this_example_CheckEjectability_c.html
archived_at: '2026-07-18T03:11:57.025153Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [How to Detect a CD](How%20to%20Detect%20a%20CD.md)


[Next](Not%20used%20in%20this%20example-Determine%20Devices%20using%20SCSI-cscsi.cp.md)[Previous](main.c.md)

# Not used in this example/CheckEjectability.c

```c
#include <Files.h>
#include <Devices.h>
#include "CheckEjectability.h"


ExtraDriveFlags* GetExtraDriveFlags(short drive)
{
    ExtraDriveFlags*    beforeQEntry = nil;
    DrvQElPtr           qEntry;

    if (drive != 0)                         // itÕs zero if already ejected so 
                                            // weÕre obviously not ejectable
    {
        for ( qEntry = ((DrvQElPtr) (GetDrvQHdr()->qHead)); 
                qEntry; 
                qEntry = (DrvQElPtr) qEntry->qLink )
            if (drive == qEntry->dQDrive)   // found our drive queue entry
            {
                beforeQEntry = ((ExtraDriveFlags*) qEntry) - 1;
                break;
            }
    }

    return beforeQEntry;
}

Boolean DriveIsEjectable(const short drive)
{
    ExtraDriveFlags* flags = GetExtraDriveFlags(drive);             // find drive queue entry
    return flags ? (flags->diskStatus & 0xF) != 0x8 : false;    // ***this is slimy
}
```

[Next](Not%20used%20in%20this%20example-Determine%20Devices%20using%20SCSI-cscsi.cp.md)[Previous](main.c.md)

