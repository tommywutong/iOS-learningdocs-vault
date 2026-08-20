---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/CoreSource_InitMac_c.html
archived_at: '2026-07-18T03:28:32.251866Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](CoreSource-Main.c.md)[Previous](CoreSource-GetBackTime.c.md)

# CoreSource/InitMac.c

```c
/*
    9-30-92  ¥ Brigham Stevens
    --------------------------

    This file contains the standard witch chant for getting the Mac going
*/

#include "CoreGlobals.h"


void SystemCheck(void)
/*
    This routine checks the minimum requirements to execute.
    If it does not return, then the machine does not cut
    the mustard.
*/
{
    long    gestResult;

    (void) Gestalt(gestaltSystemVersion,&gestResult);

    if (gestResult < 0x0700)    {
        ErrMsg("\pRequires System 7 or later!");
        ExitToShell();
    }

    /* initialize the color quickdraw flag */   
    (void) Gestalt(gestaltQuickdrawVersion,&gestResult);
    if(gestResult >= gestalt8BitQD) gColorQD = true;
}

void InitToolBox(short numberOfMasters)
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

    SystemCheck();

}
```

[Next](CoreSource-Main.c.md)[Previous](CoreSource-GetBackTime.c.md)

