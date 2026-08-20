---
title: Tumbler and Podium
apple_id: DTS10000127
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Tumbler_and_Podium/Listings/TumblerSource_Tumbler_main_c.html
archived_at: '2026-07-18T03:27:22.551313Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tumbler and Podium](Tumbler%20and%20Podium.md)


[Next](TumblerSource-Tumblermain.h.md)[Previous](TumblerSource-Tumblerinitialize.h.md)

# TumblerSource/Tumbler_main.c

```c
//      Tumbler_main.c
//
//      main function for the Tumbler application
//
//      Author:     Nick Thompson & Pablo Fernicola, with thanks to the QuickDraw 3D team
//      Date:       Tuesday, January 14, 1992
//
//      Copyright © 1992-95 Apple Computer, Inc., All Rights Reserved
//
//



#include <ToolUtils.h>

#define _AllocateGlobals_

#include "Tumbler_globals.h"
#include "Tumbler_prototypes.h"

#include "Tumbler_AEVT.h"

#undef _AllocateGlobals_

#include "Tumbler_main.h"
#include "Tumbler_initialize.h"
#include "Tumbler_AEVT.h"
#include "Tumbler_event.h"
#include "Tumbler_podium.h"


#include "MyErrorHandler.h"

main(void)

{
    const short kNumMoreMasters = 10 ;

    InitializeToolbox();

    SetCursor(*GetCursor(watchCursor)) ;

#ifdef PODIUM_APP
    Podium_Init() ; 
#endif

    SplashSetUp() ;                         // put up a pretty picture to while away the time

    InitializeAppStuff( kNumMoreMasters ) ; // call maxApplZone and moremasters

    InitializeGlobals();                    // init our app globals
    InitAEStuff();                          // install our appleevent handlers
    SetupMenus();                           // setup them menus

    // install the error & warning handler - these get called whenever
    // errors or warnings occur, which means we don't have to check so 
    // much, since the debugging version of the library will let 
    // you know about problems
    Q3Error_Register( MyErrorHandler, 0L );     
    Q3Warning_Register( MyWarningHandler, 0L );     


    SetCursor(&qd.arrow) ;                  // set up the cursor to something useful

    SplashTearDown() ;                      // get rid of the splash screen

    EventLoop();                            // process events until the user quits

    DeallocateGlobals();
}
```

[Next](TumblerSource-Tumblermain.h.md)[Previous](TumblerSource-Tumblerinitialize.h.md)

