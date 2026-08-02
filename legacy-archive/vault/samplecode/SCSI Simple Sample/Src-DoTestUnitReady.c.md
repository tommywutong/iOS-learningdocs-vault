---
title: SCSI Simple Sample
apple_id: DTS10000027
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SCSI_Simple_Sample/Listings/Src_DoTestUnitReady_c.html
archived_at: '2026-07-18T03:22:35.146064Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SCSI Simple Sample](SCSI%20Simple%20Sample.md)


[Next](Src-LogManager.c.md)[Previous](Src-DoSCSICommandWithSense.c.md)

# Src/DoTestUnitReady.c

```c
/*                              DoTestUnitReady.c                               */
/*
 * DoTestUnitReady.c
 * Copyright © 1992-94 Apple Computer Inc. All Rights Reserved.
 */
#include "SCSISimpleSample.h"

/*
 * Execute a Test Unit Ready command on the specified device and display
 * the result.
 */
void
DoTestUnitReady(
        DeviceIdent             scsiDevice              /* -> Bus/target/LUN    */
    )
{

        ScsiCmdBlock                scsiCmdBlock;
#define SCB (scsiCmdBlock)

        ShowSCSIBusID(scsiDevice, "\pTest Unit Ready");
        CLEAR(SCB);
        SCB.scsiDevice = scsiDevice;
        SCB.command.scsi6.opcode = kScsiCmdTestUnitReady;
        /* All other command bytes are zero */
        DoSCSICommandWithSense(&scsiCmdBlock, TRUE, TRUE);
        if (SCB.status == noErr)
            LOG("\pTest Unit Ready successful");
#undef SCB
}
```

[Next](Src-LogManager.c.md)[Previous](Src-DoSCSICommandWithSense.c.md)

