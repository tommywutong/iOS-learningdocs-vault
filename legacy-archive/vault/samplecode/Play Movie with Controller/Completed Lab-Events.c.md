---
title: Play Movie with Controller
apple_id: DTS10001041
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Play_Movie_with_Controller/Listings/Completed_Lab_Events_c.html
archived_at: '2026-07-18T03:19:12.917637Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Play Movie with Controller](Play%20Movie%20with%20Controller.md)


[Next](Completed%20Lab-MCActionFilter.c.md)[Previous](Completed%20Lab-Edit.c.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html](https://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html)

# Completed Lab/Events.c

```c
// Play Movie with Controller Sample
// Based on QTShell
// WWDC 2000

#include "ComApplication.h"
#include "ComFramework.h"
#include "MacFramework.h"

//////////
//
// ActivateController
// Activate or deactivate the movie controller in the specified window.
//
//////////

void ActivateController (WindowReference theWindow, Boolean IsActive)
{
    WindowObject        myWindowObject = NULL;
    MovieController     myMC = NULL;
    GrafPtr             mySavedPort = NULL;

    if (theWindow == NULL)
        return;

    GetPort(&mySavedPort);
    MacSetPort(QTFrame_GetPortFromWindowReference(theWindow));

    // get the window object associated with the specified window
    myWindowObject = QTFrame_GetWindowObjectFromWindow(theWindow);
    if (myWindowObject != NULL) {
        myMC = (**myWindowObject).fController;
        if (myMC != NULL)
            MCActivate(myMC, QTFrame_GetWindowFromWindowReference(theWindow), IsActive);
    }

    MacSetPort(mySavedPort);
}

//////////
//
// Draw
// Update the specified window.
//
//////////

void Draw (WindowReference theWindow, Rect *theRefreshArea)
{
#pragma unused(theRefreshArea)

    GrafPtr             mySavedPort;

    GetPort(&mySavedPort);
    MacSetPort(QTFrame_GetPortFromWindowReference(theWindow));

    BeginUpdate(QTFrame_GetWindowFromWindowReference(theWindow));
    //EraseRect(theRefreshArea);        // this is important only for non-rectangular movies

    // ***insert application-specific drawing here***

    // draw the movie controller and its movie
    MCDoAction(QTFrame_GetMCFromWindow(theWindow), mcActionDraw, theWindow);

    EndUpdate(QTFrame_GetWindowFromWindowReference(theWindow));
    MacSetPort(mySavedPort);
}

//////////
//
// CheckMovieControllers
// Let all movie controllers have a chance to process the event.
//
// Returns true if the event was handled by some movie controller, false otherwise
//
//////////

Boolean CheckMovieControllers (EventRecord *theEvent)
{   
    WindowPtr               myWindow = NULL;
    MovieController         myMC = NULL;

    myWindow = QTFrame_GetFrontMovieWindow();
    while (myWindow != NULL) {
        myMC = QTFrame_GetMCFromWindow(myWindow);
        if (myMC != NULL)
            if (MCIsPlayerEvent(myMC, theEvent))
                return(true);

        myWindow = QTFrame_GetNextMovieWindow(myWindow);
    }

    return(false);
}
```

[Next](Completed%20Lab-MCActionFilter.c.md)[Previous](Completed%20Lab-Edit.c.md)

