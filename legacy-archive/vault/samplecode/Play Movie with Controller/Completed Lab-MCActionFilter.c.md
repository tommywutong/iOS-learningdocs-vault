---
title: Play Movie with Controller
apple_id: DTS10001041
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Play_Movie_with_Controller/Listings/Completed_Lab_MCActionFilter_c.html
archived_at: '2026-07-18T03:19:12.992420Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Play Movie with Controller](Play%20Movie%20with%20Controller.md)


[Next](Completed%20Lab-OpenMovieInWindow.c.md)[Previous](Completed%20Lab-Events.c.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html](https://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html)

# Completed Lab/MCActionFilter.c

```c
// Play Movie with Controller Sample
// Based on QTShell
// WWDC 2000

#include "ComApplication.h"
#include "ComFramework.h"
#include "MacFramework.h"

//////////
//
// myMCActionFilterProc 
// Intercept some actions for the movie controller.
//
// NOTE: The theRefCon parameter is a handle to a window object record.
//
//////////

PASCAL_RTN Boolean myMCActionFilterProc (MovieController theMC, short theAction, void *theParams, long theRefCon)
{
#pragma unused(theMC, theParams)

    Boolean             isHandled = false;          // false => allow controller to process the action
    WindowObject        myWindowObject = NULL;

    myWindowObject = (WindowObject)theRefCon;
    if (myWindowObject == NULL)
        return(isHandled);

    switch (theAction) {

        // handle window resizing
        case mcActionControllerSizeChanged:
            if (MCIsControllerAttached(theMC) == 1)
                QTFrame_SizeWindowToMovie(myWindowObject);
            break;

        // handle idle events
        case mcActionIdle:
            QTApp_Idle((**myWindowObject).fWindow);
            break;

        default:
            break;

    } // switch (theAction)

    return(isHandled);  
}
```

[Next](Completed%20Lab-OpenMovieInWindow.c.md)[Previous](Completed%20Lab-Events.c.md)

