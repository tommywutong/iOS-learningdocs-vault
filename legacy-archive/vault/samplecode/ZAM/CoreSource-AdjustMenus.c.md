---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/CoreSource_AdjustMenus_c.html
archived_at: '2026-07-18T03:28:31.988522Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](CoreSource-AEventCoreDisp.c.md)[Previous](CoreHeaders-WindowDispatch.h.md)

# CoreSource/AdjustMenus.c

```c
/*
    AdjustMenus.c

    This procedure contains code to adjust the menus before MenuSelect or MenuKey is called.
*/


#include "MenuDispatch.h"
#include "CoreGlobals.h"


void AdjustMenus(void)
{

    WindowPtr   fWindow;

    fWindow = FrontWindow();

    /* If there is no open window then.... */
    if(!fWindow) {
        DisableItem ( GetMHandle(FILE_MENU), FILE_CLOSE );
    } else {
        EnableItem ( GetMHandle(FILE_MENU), FILE_CLOSE );
        /* LET THE DOCUMENT HAVE A CHANCE TO CHANGE MENUS */
        AdjustMenuGameWindow(fWindow);
    }


    /* THESE ARE NOT IMPLEMENTED YET */
    DisableItem ( GetMHandle(FILE_MENU), FILE_SAVE );
    DisableItem ( GetMHandle(FILE_MENU), FILE_OPEN );
    DisableItem ( GetMHandle(FILE_MENU), FILE_PRINT );
}
```

[Next](CoreSource-AEventCoreDisp.c.md)[Previous](CoreHeaders-WindowDispatch.h.md)

