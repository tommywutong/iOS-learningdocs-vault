---
title: SCSI Simple Sample
apple_id: DTS10000027
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SCSI_Simple_Sample/Listings/Src_DoReadBlockZero_c.html
archived_at: '2026-07-18T03:22:35.037531Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SCSI Simple Sample](SCSI%20Simple%20Sample.md)


[Next](Src-DoSCSICommandWithSense.c.md)[Previous](Src-DoListSCSIDevices.c.md)

# Src/DoReadBlockZero.c

```c
/*                                  DoReadBlockZero.c                           */
/*
 * DoReadBlockZero.c
 * Copyright © 1992-94 Apple Computer Inc. All Rights Reserved.
 * Read the first block off of the SCSI Device.
 */
#include "SCSISimpleSample.h"

/*
 * Read block zero from the indicated device..
 */
void
DoReadBlockZero(
        DeviceIdent             scsiDevice              /* -> Bus/target/LUN    */
    )
{
        ScsiCmdBlock                    scsiCmdBlock;
        unsigned long                   transferLength;
#define SCB (scsiCmdBlock)

        ShowSCSIBusID(scsiDevice, "\pRead Block Zero");
#define kLogicalBlockLength 512
#define kNumberOfBlocks     1
        /*
         * Note: this is slightly incorrect - it presumes that the device logical
         * block length is 512 bytes. The correct algorithme would have first
         * issued a Drive Capacity command to get the actual logical block length.
         * This would be stored in a per-drive information record.
         */
        transferLength = kNumberOfBlocks * kLogicalBlockLength;
        CLEAR(SCB);
        SCB.scsiDevice = scsiDevice;
        /*
         * The 6-byte read command can read up to 128 blocks of data (1-127
         * reads that number of blocks, while zero reads 128 blocks). For more
         * flexibility, you should use the 10-byte Read command.
         */
        SCB.command.scsi6.opcode = kScsiCmdRead6;
        SCB.command.scsi6.len = transferLength / kLogicalBlockLength;
        SCB.bufferPtr = NewPtrClear(transferLength);
        if (SCB.bufferPtr == NULL)
            LOG("\pNo Memory for ReadBlockZero data buffer");
        else {
            SCB.transferSize = transferLength;
            SCB.transferQuantum = kLogicalBlockLength;
            DoSCSICommandWithSense(&scsiCmdBlock, TRUE, TRUE);
            if (SCB.status == noErr)
                DisplayLogString(gLogListHandle, "\pRead was successful");
            /*
             * Here's where we can look at the data.
             */
            DisposePtr(SCB.bufferPtr);
        }
#undef SCB
}
```

[Next](Src-DoSCSICommandWithSense.c.md)[Previous](Src-DoListSCSIDevices.c.md)

