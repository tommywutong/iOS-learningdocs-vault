---
title: SCSI Simple Sample
apple_id: DTS10000027
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SCSI_Simple_Sample/Listings/Src_SCSIGetMaxTargetID_c.html
archived_at: '2026-07-18T03:22:36.244665Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SCSI Simple Sample](SCSI%20Simple%20Sample.md)


[Next](Src-SCSISimpleSample.h.md)[Previous](Src-SCSIGetInitiatorID.c.md)

# Src/SCSIGetMaxTargetID.c

```c
/*                              SCSIGetMaxTargetID.c                            */
/*
 * SCSIGetMaxTargetID.c
 * Copyright © 1992-94 Apple Computer Inc. All Rights Reserved.
 */
#include "SCSISimpleSample.h"
/*
 * Get the last host bus adaptor. Returns zero (and noErr) for Old SCSI.
 */
OSErr
SCSIGetMaxTargetID(
        DeviceIdent                     scsiDevice,
        unsigned short                  *maxTarget
    )
{
        OSErr                           status;
        SCSIBusInquiryPB                busInquiryPB;       
#define PB                              (busInquiryPB)

        if (gEnableNewSCSIManager == FALSE || (scsiDevice.bus == 0)) {
            /*
             * It is possible for the "sophisticated user" to change
             * the initiator id from seven to some other value. This
             * allows a Macintosh to be used in a multiple-initiator
             * environment. We return seven in all cases, as the loop
             * in DoListSCSIDevices will skip over the initiator id.
             */
            *maxTarget = 7;
            status = noErr;
        }
        else {
            CLEAR(PB);
            PB.scsiPBLength = sizeof PB;
            PB.scsiFunctionCode = SCSIBusInquiry;
            PB.scsiDevice = scsiDevice;
            status = SCSIAction((SCSI_PB *) &PB);
            if (status == noErr)
                *maxTarget = PB.scsiMaxTarget;
        }
        return (status);
#undef PB
}
```

[Next](Src-SCSISimpleSample.h.md)[Previous](Src-SCSIGetInitiatorID.c.md)

