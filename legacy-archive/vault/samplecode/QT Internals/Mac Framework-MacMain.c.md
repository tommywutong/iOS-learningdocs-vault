---
title: QT Internals
apple_id: DTS10000848
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QT_Internals/Listings/Mac_Framework_MacMain_c.html
archived_at: '2026-07-18T03:21:22.739488Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QT Internals](QT%20Internals.md)


[Next](Mac%20Framework-MWPrefix.h.md)[Previous](Mac%20Framework-MacFramework.h.md)

# Mac Framework/MacMain.c

```c
/*
    File:       MovieShell.c

    Contains:   Simple Mac shell for testing QuickTime.

    Written by: DTS

    Copyright:  © 1994-1995 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

       <1>      12/20/94    khs     first file

*/


// INCLUDES
#include <stdio.h>
#include <sioux.h>

#include "DTSQTUtilities.h"
#include "MacFramework.h"


// ______________________________________________________________________
// MAIN
void main(void)
{
    OSErr anErr;

// This is for controlling the sioux window under Metrowerks (5.0 forward)
#ifdef USESIOUX 
    SIOUXSettings.initializeTB = false;
    SIOUXSettings.setupmenus = false;
    SIOUXSettings.standalone = false;
    SIOUXSettings.asktosaveonclose = true;
#endif // USESIOUX

    InitStack(30000);
    InitMacEnvironment(10L);                    // 10 * MoreMasters
    InitMenubar();

    if( !QTUIsQuickTimeInstalled() )
        ExitToShell();

#if powerc  
    if( !QTUIsQuickTimeCFMInstalled() )
        ExitToShell();                              // I could disable features as well.
#endif 

    anErr = EnterMovies(); DebugAssert(anErr == noErr);
    if(anErr != noErr)
        ExitToShell();

    MainEventLoop();
}
```

[Next](Mac%20Framework-MWPrefix.h.md)[Previous](Mac%20Framework-MacFramework.h.md)

