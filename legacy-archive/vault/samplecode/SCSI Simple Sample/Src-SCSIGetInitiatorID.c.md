---
title: SCSI Simple Sample
apple_id: DTS10000027
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SCSI_Simple_Sample/Listings/Src_SCSIGetInitiatorID_c.html
archived_at: '2026-07-18T03:22:36.192645Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SCSI Simple Sample](SCSI%20Simple%20Sample.md)


[Next](Src-SCSIGetMaxTargetID.c.md)[Previous](Src-SCSIGetHighHostBusAdaptor.c.md)

# Src/SCSIGetInitiatorID.c

```c
/*                              SCSIGetInitiatorID.c                            */
/*
 * SCSIGetInitiatorID.c
 * Copyright © 1992-94 Apple Computer Inc. All Rights Reserved.
 */
#include "SCSISimpleSample.h"

/*
 * Get the SCSI bus ID of the Macintosh (initiator) on this bus (only
 * scsiDevice.bus is referenced).
 */
OSErr
SCSIGetInitiatorID(
        DeviceIdent             scsiDevice,
        unsigned short          *initiatorID
    )
{
        OSErr                       status;
        SCSIBusInquiryPB            busInquiryPB;
#define PB                          (busInquiryPB)

        if (AsyncSCSIPresent() == FALSE) {
            *initiatorID = 7;
            status = noErr;
        }
        else {
            CLEAR(PB);
            PB.scsiPBLength = sizeof PB;
            PB.scsiFunctionCode = SCSIBusInquiry;
            PB.scsiDevice = scsiDevice;
            status = SCSIAction((SCSI_PB *) &PB);
            DisplaySCSIErrorMessage(status, "\pSCSIBusInquiry failed");
            *initiatorID = PB.scsiInitiatorID;
        }
        return (status);
}
```

[Next](Src-SCSIGetMaxTargetID.c.md)[Previous](Src-SCSIGetHighHostBusAdaptor.c.md)

