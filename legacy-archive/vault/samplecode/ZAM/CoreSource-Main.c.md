---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/CoreSource_Main_c.html
archived_at: '2026-07-18T03:28:32.285049Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](CoreSource-MenuDispatch.c.md)[Previous](CoreSource-InitMac.c.md)

# CoreSource/Main.c

```c
/*
    9-30-92  ¥ Brigham Stevens
    --------------------------

    main program for Slim.
    Change Drawing.c to effect window contents.

*/


#include "EventLoop.h"
#include "MenuDispatch.h"
#include "CoreGlobals.h"
#include "ZAM.h"
#include "GameSounds.h"


Boolean gColorQD;

void main(void)
{

    /* Expand the heap and make the Mac go */
    MaxApplZone();
    InitToolBox(kNumMoreMasters);
    UnloadSeg(InitToolBox);


    /* Create the menus */
    BuildMenuBars();
    InstallAppleEvents();
    InitGame();


    /* Run until Quit is selected */
    while(!gDone) {
        MainEvent();
        IdleGameWindow();
    }   

    FreeSounds();
    SendGoodBye();
    KillAllXThingTasks();
}
```

[Next](CoreSource-MenuDispatch.c.md)[Previous](CoreSource-InitMac.c.md)

