---
title: SCSI DriveID Sample
apple_id: DTS10000023
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SCSI_DriveID_Sample/Listings/AsyncSCSIPresent_c.html
archived_at: '2026-07-18T03:22:33.715978Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SCSI DriveID Sample](SCSI%20DriveID%20Sample.md)


[Next](SCSIDriveIDSample.c.md)[Previous](SCSI%20DriveID%20Sample.md)

# AsyncSCSIPresent.c

```c
/*
    File:       AsyncSCSIPresent.c

    Contains:   

    Written by:     

    Copyright:  Copyright © 1992-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/14/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


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

[Next](SCSIDriveIDSample.c.md)[Previous](SCSI%20DriveID%20Sample.md)

