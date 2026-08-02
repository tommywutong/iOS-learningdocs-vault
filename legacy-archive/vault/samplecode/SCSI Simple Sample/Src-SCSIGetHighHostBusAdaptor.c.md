---
title: SCSI Simple Sample
apple_id: DTS10000027
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SCSI_Simple_Sample/Listings/Src_SCSIGetHighHostBusAdaptor_c.html
archived_at: '2026-07-18T03:22:36.136518Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SCSI Simple Sample](SCSI%20Simple%20Sample.md)


[Next](Src-SCSIGetInitiatorID.c.md)[Previous](Src-SCSIGetCommandLength.c.md)

# Src/SCSIGetHighHostBusAdaptor.c

```c
/*                          SCSIGetHighHostBusAdaptor.c                         */
/*
 * GetHighHostBusAdaptor.c
 * Copyright © 1992-94 Apple Computer Inc. All Rights Reserved.
 */
#include "SCSISimpleSample.h"
/*
 * Get the last host bus adaptor. Returns zero (and noErr) for Old SCSI.
 */
OSErr
SCSIGetHighHostBusAdaptor(
        unsigned short                  *lastHostBus
    )
{
        OSErr                           status;
        SCSIBusInquiryPB                busInquiryPB;
#define PB                              (busInquiryPB)

        if (AsyncSCSIPresent() == FALSE) {
            *lastHostBus = 0;
            status = noErr;
        }
        else {
            CLEAR(PB);
            PB.scsiPBLength = sizeof PB;
            PB.scsiFunctionCode = SCSIBusInquiry;
            PB.scsiDevice.bus = 0xFF;
            status = SCSIAction((SCSI_PB *) &PB);
            DisplaySCSIErrorMessage(status, "\pSCSIBusInquiry failed");
            *lastHostBus = PB.scsiHiBusID;
        }
        return (status);
#undef PB
}
```

[Next](Src-SCSIGetInitiatorID.c.md)[Previous](Src-SCSIGetCommandLength.c.md)

