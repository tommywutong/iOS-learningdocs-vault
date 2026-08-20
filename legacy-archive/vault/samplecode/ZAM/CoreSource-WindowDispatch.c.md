---
title: ZAM
apple_id: DTS10000063
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ZAM/Listings/CoreSource_WindowDispatch_c.html
archived_at: '2026-07-18T03:28:32.360351Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ZAM](ZAM.md)


[Next](Dude%20-includes.c.md)[Previous](CoreSource-MenuDispatch.c.md)

# CoreSource/WindowDispatch.c

```c
#include "CoreGlobals.h"


Handle  GetWData(WindowPtr  wp)
{
    return (Handle)GetWRefCon(wp);
}


void SetWData(WindowPtr wp, Handle data)
{
    SetWRefCon(wp,(long)data);
}

WindowPtr NewDispatchWindow(short ID)
/*
    This routine will create a window and allocate the event handler pointers
*/
{
    wDispHandle     disp;
    WindowPeek      wp;


    /* Get the window template */
    if(gColorQD)
        wp = (WindowPeek)GetNewCWindow(ID,nil,(WindowPtr)-1L);

    ShowWindow(wp);

    return (WindowPtr)wp;
}

void DisposeDispatchWindow(WindowPeek wp)
{
    DisposeWindow(wp);
}
```

[Next](Dude%20-includes.c.md)[Previous](CoreSource-MenuDispatch.c.md)

