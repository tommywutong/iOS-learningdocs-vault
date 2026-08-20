---
title: SCSI Simple Sample
apple_id: DTS10000027
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SCSI_Simple_Sample/Listings/Src_DoGetDriveInfo_c.html
archived_at: '2026-07-18T03:22:34.918072Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SCSI Simple Sample](SCSI%20Simple%20Sample.md)


[Next](Src-DoListSCSIDevices.c.md)[Previous](Src-AsyncSCSIPresent.c.md)

# Src/DoGetDriveInfo.c

```c
/*                              DoGetDriveInfo.c                                */
/*
 * DoGetDriveInfo.c
 * Copyright © 1992-94 Apple Computer Inc. All Rights Reserved.
 */
#include "SCSISimpleSample.h"

/*
 * Execute a Bus Inquiry SCSI request on the selected device. If it succeeds,
 * display the results.
 */
void
DoGetDriveInfo(
        DeviceIdent             scsiDevice,             /* -> Bus/target/LUN    */
        Boolean                 noIntroMsg,
        Boolean                 useAsynchManager
    )
{

        ScsiCmdBlock                scsiCmdBlock;
        SCSI_Inquiry_Data           inquiry;
#define SCB (scsiCmdBlock)

        if (noIntroMsg == FALSE)
            ShowSCSIBusID(scsiDevice, "\pGet Drive Info");
        CLEAR(SCB);
        SCB.scsiDevice = scsiDevice;
        SCB.command.scsi6.opcode = kScsiCmdInquiry;
        SCB.command.scsi6.len = sizeof inquiry;
        SCB.bufferPtr = (Ptr) &inquiry;
        SCB.transferSize = sizeof inquiry;
        SCB.transferQuantum = 1;                        /* Force handshake      */
        /* All other command bytes are zero */
        DoSCSICommandWithSense(&scsiCmdBlock, TRUE, useAsynchManager);
        if (SCB.status == noErr)
            DoShowInquiry(scsiDevice, &inquiry);
#undef SCB
}
```

[Next](Src-DoListSCSIDevices.c.md)[Previous](Src-AsyncSCSIPresent.c.md)

