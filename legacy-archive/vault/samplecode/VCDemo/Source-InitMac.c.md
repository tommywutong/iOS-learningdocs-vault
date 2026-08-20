---
title: VCDemo
apple_id: DTS10000128
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/VCDemo/Listings/Source_InitMac_c.html
archived_at: '2026-07-18T03:27:40.297566Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VCDemo](VCDemo.md)


[Next](Source-MenuDispatch.c.md)[Previous](Source-EventLoop.c.md)

# Source/InitMac.c

```c
/*
    InitMac.c

    Initialize application environment.

    © 1995 Apple Computer, Inc.
*/

#include <OSUtils.h>
#include <QuickDraw.h>
#include <Fonts.h>
#include <Windows.h>
#include <Menus.h>
#include <TextEdit.h>
#include <Events.h>
#include <Dialogs.h>
#include <Memory.h>

#include "EventLoop.h"

#define _Unimplemented 0xA89F
#define _WaitNextEvent 0xA860

Boolean TrapAvailable ( short tNum, short tType);
void InitToolBox(short numberOfMasters);
Boolean WNEIsImplemented( void );


Boolean TrapAvailable ( short tNum, short tType)
{
    return ( NGetTrapAddress(tNum,tType) != GetToolTrapAddress(_Unimplemented) );
}

Boolean WNEIsImplemented( void )
{
    SysEnvRec   theWorld;

    SysEnvirons(1, &theWorld);
    if (theWorld.machineType < 0)
        return false;
    else
        return TrapAvailable ( _WaitNextEvent, ToolTrap);
}

void InitToolBox(short numberOfMasters)
{
    InitGraf(&qd.thePort);
    InitFonts();
    InitWindows();
    InitMenus();
    InitCursor();
    TEInit();
    FlushEvents(everyEvent, 0);
    InitDialogs(0L);

    while(numberOfMasters--)
        MoreMasters();

    MaxApplZone();

    WNE_available = WNEIsImplemented();
}

/* EOF */
```

[Next](Source-MenuDispatch.c.md)[Previous](Source-EventLoop.c.md)

