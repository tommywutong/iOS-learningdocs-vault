---
title: NetSprocketTestOld
apple_id: DTS10000058
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/NetSprocketTestOld/Listings/init_c.html
archived_at: '2026-07-18T03:16:59.358825Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NetSprocketTestOld](NetSprocketTestOld.md)


[Next](NetStuff.cp.md)[Previous](Global.h.md)

# init.c

```c
/***********************************************************************
#
#       init.c
#
#       basic initialization code.
#
#       Author: Michael Marinkovich
#               Apple Developer Technical Support
#
#
#       Modification History: 
#
#           6/4/95      MWM     Initial coding                   
#           10/12/95    MWM     cleaned up
#
#       Copyright © 1992-95 Apple Computer, Inc., All Rights Reserved
#
#
***********************************************************************/


#include <AppleEvents.h>
#include <Displays.h>
#include <Events.h>
#include <Fonts.h>
#include <Gestalt.h>
#include <Menus.h>
#include <OSUtils.h>

#include "App.h"
#include "Proto.h"
#include "NetStuff.h"

extern Boolean          gHasDMTwo;
extern Boolean          gHasDrag;
extern Boolean          gInBackground;
extern short            gWindCount;


//----------------------------------------------------------------------
//
//  Initialize - the main entry point for the initialization
//
//
//----------------------------------------------------------------------

OSErr Initialize(void)
{
    OSErr       err = noErr;
    OSStatus    status; 

    ToolBoxInit();
    CheckEnvironment();
    err = InitApp();
    status = InitNetworking('BLAm');

    return err;
}


//----------------------------------------------------------------------
//
//  ToolBoxInit - initialization all the needed managers
//
//
//----------------------------------------------------------------------

void ToolBoxInit(void)
{

    InitGraf(&qd.thePort);
    InitFonts();
    InitWindows();
    InitMenus();
    TEInit();
    InitDialogs(nil);
    InitCursor();

    FlushEvents(everyEvent, 0);

}


//----------------------------------------------------------------------
//
//  CheckEnvironment - make sure we can run with current sys and managers.
//                     Also initialize globals - have drag & drop
//                    
//----------------------------------------------------------------------

void CheckEnvironment(void)
{

    // your stuff here
}


//----------------------------------------------------------------------
//
//  InitApp - initialization all the application specific stuff
//
//
//----------------------------------------------------------------------

OSErr InitApp(void)
{
    OSErr               err;

    // init AppleEvents
    err = AEInit();
    MenuSetup();

    // init any globals
    gWindCount = 1;

    return err;

}


//----------------------------------------------------------------------
//
//  MenuSetup - 
//
//
//----------------------------------------------------------------------

void MenuSetup(void)
{
    Handle          menu;


    menu = GetNewMBar(rMBarID);     //  get our menus from resource
    SetMenuBar(menu);
    DisposeHandle(menu);
    AppendResMenu(GetMenuHandle(mApple ), 'DRVR');      //  add apple menu items

    DrawMenuBar();


}
```

[Next](NetStuff.cp.md)[Previous](Global.h.md)

