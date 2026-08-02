---
title: SCSI Async Sample
apple_id: DTS10000022
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SCSI_Async_Sample/Listings/Src_SCSIBusInquiry_c.html
archived_at: '2026-07-18T03:22:32.978193Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SCSI Async Sample](SCSI%20Async%20Sample.md)


[Next](Src-SCSIDefinitions.h.md)[Previous](Src-SCSIAsyncSampleMain.c.md)

# Src/SCSIBusInquiry.c

```c
/*                              SCSIBusInquiry.c                                */
/*
 * SCSIBusInquiry.c
 * Copyright © 1992-93 Apple Computer Inc. All Rights Reserved.
 *
 * Get information on a specified host bus adaptor (HBA) incluing the number
 * of HBA's installed.
 *
 * This function will crash if the New SCSI Manager is not installed.
 *
 */
#include "SCSIAsyncSample.h"

OSErr
GetHostBusCount(
        short                       *busCount
    )
{

        OSErr                       status;
        SCSIBusInquiryPB            busInquiryPB;
#define PB                          (busInquiryPB)

        CLEAR(PB);
        PB.scsiPBLength = sizeof PB;
        PB.scsiFunctionCode = SCSIBusInquiry;
        PB.scsiDevice.bus = 0;
        status = SCSIAction((SCSI_PB *) &PB);
        if (status == noErr)
            *busCount = PB.scsiHiBusID;
        return (status);
}       
```

[Next](Src-SCSIDefinitions.h.md)[Previous](Src-SCSIAsyncSampleMain.c.md)

