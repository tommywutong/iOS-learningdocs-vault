---
title: MovieShell
apple_id: DTS10000326
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MovieShell/Listings/TestFunctions_c.html
archived_at: '2026-07-18T03:16:08.882598Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MovieShell](MovieShell.md)


[Next](TestFunctions.h.md)[Previous](Mac%20Framework-MWPrefix.h.md)

# TestFunctions.c

```c
/*
    File:       TestFunctions.c

    Contains:   Insert the test functions inside this file.

    Written by: DTS

    Copyright:  © 1995 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

        <1>     2/26/95 khs     first file

*/


// INCLUDES
#include "TestFunctions.h"

#include "DTSQTUtilities.h"
#include "MacFramework.h"


// TEST FUNCTIONS
// ______________________________________________________________________
void ResizeTheMovieWindow(long theMovieSize)
{
    MovieController     mc = NULL;
    Rect                        originalRect;
    WindowRef           aWindow = NULL;
    WindowObject        aWindowObject = NULL;

    // We need all this code below
    aWindow = FrontWindow();                            // do we have a window?
    if(aWindow == NULL)
    {
        SysBeep(10);
        return;
    }

    mc = GetMCFromFrontWindow();                    // does the front window have a movie controller?
    if(mc == NULL)
    {
        SysBeep(10);
        return;
    }

    aWindowObject = (WindowObject)GetWRefCon(aWindow); DebugAssert(aWindowObject != NULL);
    originalRect = (**aWindowObject).originalSize;

    if ( QTUResizeMCWindow(mc, (WindowPtr) aWindow, theMovieSize,  originalRect) != noErr)
        SysBeep(10);
}
```

[Next](TestFunctions.h.md)[Previous](Mac%20Framework-MWPrefix.h.md)

