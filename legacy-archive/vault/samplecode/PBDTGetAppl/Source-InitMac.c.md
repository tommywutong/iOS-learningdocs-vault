---
title: PBDTGetAppl
apple_id: DTS10000042
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PBDTGetAppl/Listings/Source_InitMac_c.html
archived_at: '2026-07-18T03:18:19.963620Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PBDTGetAppl](PBDTGetAppl.md)


[Next](Source-MenuDispatch.c.md)[Previous](Source-GetCreator.c.md)

# Source/InitMac.c

```c
/*
    9-30-92  ¥ Brigham Stevens
    --------------------------

    This file contains the standard witch chant for getting the Mac going
*/

/* Need this header file because we set the WNE flag */
#include "EventLoop.h"



#define _Unimplemented 0xA89F
#define _WaitNextEvent 0xA860

Boolean TrapAvailable ( short tNum, short tType)
{
    return ( NGetTrapAddress(tNum,tType) != GetTrapAddress(_Unimplemented) );
}

Boolean WNEIsImplemented()
{
    SysEnvRec   theWorld;

    SysEnvirons(1,&theWorld);
    if (theWorld.machineType < 0)
        return false;
    else
        return TrapAvailable ( _WaitNextEvent, ToolTrap);
}



InitToolBox(short numberOfMasters)
/*
    pass the number of times you want MoreMasters to be called
    if your app has lots of Handles to allocate
    then call MoreMasters lots of times.
*/
{

    InitGraf(&thePort);
    InitFonts();
    InitWindows();
    InitMenus();
    InitCursor();
    TEInit();
    FlushEvents(everyEvent, 0);
    InitDialogs(nil);

    while(numberOfMasters--)
        MoreMasters();

    MaxApplZone();

    WNE_available = WNEIsImplemented();
}
```

[Next](Source-MenuDispatch.c.md)[Previous](Source-GetCreator.c.md)

