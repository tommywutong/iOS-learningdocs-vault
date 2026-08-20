---
title: SCSI Async Sample
apple_id: DTS10000022
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SCSI_Async_Sample/Listings/Src_MicrosecondTrapPresent_c.html
archived_at: '2026-07-18T03:22:31.464459Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SCSI Async Sample](SCSI%20Async%20Sample.md)


[Next](Src-NewSCSIManagerPresent.c.md)[Previous](Src-MicrosecondTrap.h.md)

# Src/MicrosecondTrapPresent.c

```c
/*                              MicrosecondTrapPresent.c                        */
/*
 * MicrosecondTrapPresent.c
 * Copyright © 1992-94 Apple Computer Inc. All Rights Reserved.
 */
#include <OSUtils.h>
#include "MicrosecondTrap.h"

static Boolean              TrapAvailable(
        short                   theTrap
    );

Boolean
MicrosecondTrapPresent(void)
{
        return (TrapAvailable(_Microseconds));
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
        (((theTrap) & 0x800) != 0) ? ToolTrap : OSTrap  \
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

[Next](Src-NewSCSIManagerPresent.c.md)[Previous](Src-MicrosecondTrap.h.md)

