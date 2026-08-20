---
title: SCSI Async Sample
apple_id: DTS10000022
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SCSI_Async_Sample/Listings/Src_GetSCSICDBLength_c.html
archived_at: '2026-07-18T03:22:30.752451Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SCSI Async Sample](SCSI%20Async%20Sample.md)


[Next](Src-LogManager.c.md)[Previous](Src-GetDevicesToTest.c.md)

# Src/GetSCSICDBLength.c

```c
/*                              GetSCSICDBLength.c                              */
/*
 * GetSCSICDBLength.c
 * Copyright © 1992-93 Apple Computer Inc. All Rights Reserved.
 */
#include    "SCSIAsyncSample.h"

/*
 * Look at the "group code" in the command operation. Return zero (error) for
 * the reserved (3, 4) and vendor-specific command (6, 7) command groups.
 * Otherwise, return the command length from the group code value as specified
 * in the SCSI-II spec.
 */
short
GetSCSICDBLength(
        const SCSI_CommandPtr   scsiCommandPtr
    )
{
        short                   result;

        switch (scsiCommandPtr->scsi[0] & 0xE0) {
        case (0 << 5):  result = 6;     break;
        case (1 << 5):
        case (2 << 5):  result = 10;    break;
        case (5 << 5):  result = 12;    break;
        default:        result = 0;     break;
        }
        return (result);
}
```

[Next](Src-LogManager.c.md)[Previous](Src-GetDevicesToTest.c.md)

