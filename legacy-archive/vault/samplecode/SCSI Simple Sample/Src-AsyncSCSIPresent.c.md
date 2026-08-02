---
title: SCSI Simple Sample
apple_id: DTS10000027
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SCSI_Simple_Sample/Listings/Src_AsyncSCSIPresent_c.html
archived_at: '2026-07-18T03:22:34.735017Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SCSI Simple Sample](SCSI%20Simple%20Sample.md)


[Next](Src-DoGetDriveInfo.c.md)[Previous](Src-AsyncSCSI.c.md)

# Src/AsyncSCSIPresent.c

```c
/*                              AsyncSCSIPresent.c                              */
/*
 * AsyncSCSIPresent.c
 * Copyright © 1992-94 Apple Computer Inc. All Rights Reserved.
 */
#include <OSUtils.h>
#include <Traps.h>
#ifndef _SCSIAtomic
/*
 * This is needed if you don't have Universal Headers.
 */
#define _SCSIAtomic 0xA089
#endif

Boolean                     AsyncSCSIPresent(void);
static Boolean              TrapAvailable(
        short                   theTrap
    );

Boolean
AsyncSCSIPresent(void)
{
        return (TrapAvailable(_SCSIAtomic));
}

/*
 * TrapAvailable (see Inside Mac VI 3-8)
 */
#define NumToolboxTraps() (                             \
        (NGetTrapAddress(_InitGraf, ToolTrap)           \
                == NGetTrapAddress(0xAA6E, ToolTrap))   \
            ? 0x200 : 0x400                             \
    )
#define GetTrapType(theTrap) (                          \
        (((theTrap) & 0x0800) != 0) ? ToolTrap : OSTrap \
    )

static Boolean
TrapAvailable(
        short                   theTrap
    )
{
        TrapType                trapType;

        trapType = GetTrapType(theTrap);
        if (trapType == ToolTrap) {
            theTrap &= 0x07FF;
            if (theTrap >= NumToolboxTraps())
                theTrap = _Unimplemented;
        }
        return (
            NGetTrapAddress(theTrap, trapType)
            != NGetTrapAddress(_Unimplemented, ToolTrap)
        );
}
```

[Next](Src-DoGetDriveInfo.c.md)[Previous](Src-AsyncSCSI.c.md)

