---
title: MakeIcon
apple_id: DTS10000089
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MakeIcon/Listings/InitMac_c.html
archived_at: '2026-07-18T03:14:21.339902Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MakeIcon](MakeIcon.md)


[Next](InitMac.h.md)[Previous](IconUtil.h.md)

# InitMac.c

```c
/*
    File:       InitMac.c

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
                7/9/1999    Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#include "InitMac.h"
#include <GestaltEQU.h>
#include <OSUtils.h>
#include <Menus.h>
#include <Fonts.h>
#include <Quickdraw.h>
#include <Windows.h>
#include <Dialogs.h>
#include <TextEdit.h>
#include <Events.h>

SysEnvRec   TheWorld;
Boolean     WNE_available;
Boolean     HasGWorlds;
Boolean     HasCQD;

#define _Unimplemented 0xA89F
#define _WaitNextEvent 0xA860

Boolean TrapAvailable (short tNum,short tType)
{
    return ( NGetTrapAddress(tNum,tType) != NGetTrapAddress(_Unimplemented,kOSTrapType) );
}

Boolean WNEIsImplemented()
{
    if (TheWorld.machineType < 0)
    {
        return false;
    }
    else
    {
        return TrapAvailable ( _WaitNextEvent, ToolTrap);
    }
}


void CheckQuickDraw ()
{
    long      qdVersion;  /* Version of QuickDraw on this machine */
    /* Find out if GWorlds and CQD are implemented on this machine */
    (void) Gestalt (gestaltQuickdrawVersion, &qdVersion);

    HasGWorlds = (qdVersion > gestaltOriginalQD && qdVersion < gestalt8BitQD)
                  || qdVersion >= gestalt32BitQD;

    HasCQD = qdVersion >= gestalt8BitQD;

}


void InitToolBox(int numberOfMasters)
{

    InitGraf(&qd.thePort);
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
    SysEnvirons(1,&TheWorld);
    WNE_available = WNEIsImplemented();

    CheckQuickDraw ();

}
```

[Next](InitMac.h.md)[Previous](IconUtil.h.md)

