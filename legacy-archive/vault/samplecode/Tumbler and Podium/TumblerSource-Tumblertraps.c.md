---
title: Tumbler and Podium
apple_id: DTS10000127
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Tumbler_and_Podium/Listings/TumblerSource_Tumbler_traps_c.html
archived_at: '2026-07-18T03:27:23.448232Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tumbler and Podium](Tumbler%20and%20Podium.md)


[Next](TumblerSource-Tumblertraps.h.md)[Previous](TumblerSource-Tumblerteutilities.h.md)

# TumblerSource/Tumbler_traps.c

```c
// Simple framework for Macintosh sample code
//
// Nick Thompson, DEVSUPPORT
//
// This file contains the trap detection related code code for the framework.
// 
// 9/16/94  nick    first cut

#include <Types.h>
#include <Traps.h>
#include <OSUtils.h>
#include <Gestalt.h>

#include "Tumbler_Traps.h"

#include "Tumbler_traps.h"

short myNumToolboxTraps(void);
TrapType myGetTrapType(short theTrap);

short myNumToolboxTraps(void)
{
    if (NGetTrapAddress(_InitGraf, ToolTrap) == NGetTrapAddress(0xAA6E,ToolTrap))
        return 0x0200;
    else
        return 0x0400;
}

TrapType myGetTrapType(short theTrap)
{
    if ((theTrap & 0x0800) > 0)
        return ToolTrap;
    else
        return OSTrap;
}

Boolean myTrapAvailable(short theTrap)
{
    TrapType tType;
    Boolean isAvail;

    tType = myGetTrapType(theTrap);
    if (tType == ToolTrap)
        {
            theTrap &= 0x07FF;
            if (theTrap >= myNumToolboxTraps())
                theTrap = _Unimplemented;
        }

    isAvail = NGetTrapAddress(theTrap, tType) != NGetTrapAddress(_Unimplemented, ToolTrap);
    return isAvail;
}
```

[Next](TumblerSource-Tumblertraps.h.md)[Previous](TumblerSource-Tumblerteutilities.h.md)

