---
title: TimeZone.Daylight
apple_id: DTS10000275
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/TimeZone.Daylight/Listings/InitMac_h.html
archived_at: '2026-07-18T03:26:57.223819Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TimeZone.Daylight](TimeZone.Daylight.md)


[Next](Document%20Revision%20History.md)[Previous](InitMac.c.md)

# InitMac.h

```c
/*
    File:       InitMac.h

    Contains:   

    Written by:     

    Copyright:  Copyright © 1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/23/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#include <Traps.h>

short           NumToolboxTraps (void);
TrapType        GetTrapType         (short theTrap);
Boolean     TrapAvailable       (short theTrap);
Boolean     WNEAvailable        (void);
void            CheckQuickDraw      (void);
void            InitToolBox         (short numberOfMasters);

extern Boolean      WNE_available;
extern Boolean      HasGWorlds;
extern Boolean      HasCQD;
```

[Next](Document%20Revision%20History.md)[Previous](InitMac.c.md)

