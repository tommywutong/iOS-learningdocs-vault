---
title: Live Scroll
apple_id: DTS10000591
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/Live_Scroll/Listings/Menus_c.html
archived_at: '2026-07-18T03:13:41.264051Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Live Scroll](Live%20Scroll.md)


[Next](Prototypes.h.md)[Previous](Initialize.c.md)

# Menus.c

```c
/*
    File:       Menus.c

    Contains:   Handles the application's menus

    Written by: Chris White 

    Copyright:  Copyright © 1996-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/6/1999    Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/


#pragma segment Core


#ifndef __MENUS__
    #include <Menus.h>
#endif

#ifndef __WINDOWS__
    #include <Windows.h>
#endif

#ifndef __DIALOGS__
    #include <Dialogs.h>
#endif

#ifndef __TEXTUTILS__
    #include <TextUtils.h>
#endif

#ifndef __DESK__
    #include <Desk.h>
#endif





// Application includes

#ifndef __BAREBONES__
    #include "BareBones.h"
#endif

#ifndef __PROTOTYPES__
    #include "Prototypes.h"
#endif




static void DoAppleCmds ( SInt16 theItem );
static void DoFileCmds ( SInt16 theItem );





void MenuDispatch ( SInt32 menuResult )
{
    SInt16  theMenu = (menuResult >> 16);                   // menu selected
    SInt16  theItem = (menuResult & 0x0000FFFF);            // item selected

    switch (theMenu)
    {
        case kAppleMenu: 
            DoAppleCmds ( theItem );
        break;

        case kFileMenu: 
            DoFileCmds ( theItem );
        break;

    }

    HiliteMenu ( 0 );           // un-hilite selected menu

    return;

} // MenuDispatch



static void DoAppleCmds ( SInt16 theItem )
{
    Str255  name;           // string for DA name


    switch ( theItem )
    {
        case cAbout:
            DoAboutBox ( );
        break;

        default:
            GetMenuItemText ( GetMenuHandle ( kAppleMenu ), theItem, (StringPtr) &name );
            OpenDeskAcc ( (StringPtr) &name );
        break;
    }
}



static void DoFileCmds ( SInt16 theItem )
{   
    switch ( theItem )
    {
        case cQuit:
            gQuit = true;
        break;
    }

    return;

} // DoFileCmds
```

[Next](Prototypes.h.md)[Previous](Initialize.c.md)

