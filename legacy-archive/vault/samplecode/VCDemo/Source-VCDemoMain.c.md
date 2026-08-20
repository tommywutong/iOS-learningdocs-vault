---
title: VCDemo
apple_id: DTS10000128
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/VCDemo/Listings/Source_VCDemoMain_c.html
archived_at: '2026-07-18T03:27:40.510381Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VCDemo](VCDemo.md)


[Next](Source-ViewFunctions.c.md)[Previous](Source-TestFunctions.c.md)

# Source/VCDemoMain.c

```c
/*
    VCDemoMain.c

    main function for VCDemo.

    ====================
    A friendly reminder:

    The intent here is just to test and demo a QD3D Viewer client.

    This application performs virtually NO error checking.

    This application is not supported by anyone,
    not even the author, who shall thankfully remain anonymous.

    DO NOT USE THIS CODE FOR ANYTHING OTHER THAN "GETTING THE GENERAL IDEA"!
    ========================================================================

    © 1995 Apple Computer, Inc.
*/
#include <QuickDraw.h>
#include <Windows.h>

#include "EventLoop.h"
#include "MenuDispatch.h"

WindowPtr       MainView;

extern void InitToolBox(short numberOfMasters);
extern void MainEvent(void);
extern void BuildMenuBars(void); 
extern void ChooseFile(short item);

void main(void)
{
    InitToolBox(4);

    BuildMenuBars();
    ChooseFile(cmdNew);
    SetPort(MainView);

    while(!Done) {
        MainEvent();
        if(!FrontWindow()) 
            MainView = nil;
    }   
}

/* EOF */
```

[Next](Source-ViewFunctions.c.md)[Previous](Source-TestFunctions.c.md)

