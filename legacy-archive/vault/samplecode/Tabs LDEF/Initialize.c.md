---
title: Tabs LDEF
apple_id: DTS10000621
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/Tabs_LDEF/Listings/Initialize_c.html
archived_at: '2026-07-18T03:26:18.750222Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabs LDEF](Tabs%20LDEF.md)


[Next](Lists.c.md)[Previous](Events.c.md)

# Initialize.c

```c
/*
    File:       Initialize.c

    Contains:   Initialization code for this application

    Written by: Chris White 

    Copyright:  Copyright © 1995-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/10/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/


#pragma segment Initialize



// System includes

#ifndef __QUICKDRAW__
    #include <Quickdraw.h>
#endif

#ifndef __FONTS__
    #include <Fonts.h>
#endif

#ifndef __TEXTEDIT__
    #include <TextEdit.h>
#endif

#ifndef __DIALOGS__
    #include <Dialogs.h>
#endif

#ifndef __GESTALT__
    #include <Gestalt.h>
#endif

#ifndef __SEGLOAD__
    #include <SegLoad.h>
#endif




// Application includes

#ifndef __BAREBONES__
    #include "BareBones.h"
#endif

#ifndef __PROTOTYPES__
    #include "Prototypes.h"
#endif



// static prototypes
static Boolean CheckConfiguration ( void );




void InitToolbox ( void )
{   

    InitGraf ( &qd.thePort );
    InitFonts ( );
    InitWindows ( );
    InitMenus ( );
    TEInit ( );
    InitDialogs ( nil );
    InitCursor ( );

    FlushEvents ( everyEvent, 0 );

    return;
}



void InitApplication ( void )
{
    SetMenuBar ( GetNewMBar ( kMenuBarID ) );
    AppendResMenu ( GetMenuHandle ( kAppleMenu ), 'DRVR' );
    DrawMenuBar ( );

    if ( !CheckConfiguration ( ) )
    {
        AlertUser ( kNeedSystem7, 0, nil );
        ExitToShell ( );
    }

    gQuit = false;                      // Initialize flag that controls main event loop
    gSleepTime = kSleepTime;

    InstallAppleEventHandlers ( );
    CreateWindow ( );

    return;
}



static Boolean CheckConfiguration ( void )
{
    long        theResult;
    OSErr       theErr;
    Boolean     bHasAppleEvents;


    // Verify that we can run on the current configuration

    // We require AppleEvent Manager and FSSpec-based file traps and Standard File
    theErr = Gestalt ( gestaltAppleEventsAttr, &theResult );
    bHasAppleEvents = (theErr == noErr && (theResult & (1L << gestaltAppleEventsPresent)));

    return bHasAppleEvents;
}
```

[Next](Lists.c.md)[Previous](Events.c.md)

