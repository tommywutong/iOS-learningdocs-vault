---
title: PBDTGetAppl
apple_id: DTS10000042
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PBDTGetAppl/Listings/Source_SlimMain_c.html
archived_at: '2026-07-18T03:18:20.225374Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PBDTGetAppl](PBDTGetAppl.md)


[Next](Document%20Revision%20History.md)[Previous](Source-SlimFunctions.c.md)

# Source/SlimMain.c

```c
/*
    9-30-92  ¥ Brigham Stevens
    --------------------------

    main program for Slim.
    Slaps up a window and some menus.
    Change Drawing.c to effect window contents.

*/


#include "EventLoop.h"
#include "MenuDispatch.h"

WindowPtr   MainView;

main(void)
{
    InitToolBox(4);
    UnloadSeg(InitToolBox);

    BuildMenuBars();

    MainView = GetNewWindow(128,nil,(void*)-1L);
    SetPort(MainView);

    /* Run until Quit is selected */
    while(!Done) {
        MainEvent();
        if(!FrontWindow()) 
            MainView = nil;
    }   

}
```

[Next](Document%20Revision%20History.md)[Previous](Source-SlimFunctions.c.md)

