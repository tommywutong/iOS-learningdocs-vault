---
title: Play Movie with Controller
apple_id: DTS10001041
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Play_Movie_with_Controller/Listings/Completed_Lab_Edit_c.html
archived_at: '2026-07-18T03:19:12.841400Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Play Movie with Controller](Play%20Movie%20with%20Controller.md)


[Next](Completed%20Lab-Events.c.md)[Previous](Common%20Files-WinPrefix.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html](https://developer.apple.com/mac/library/samplecode/QTKitPlayer/index.html)

# Completed Lab/Edit.c

```c
// Play Movie with Controller Sample
// Based on QTShell
// WWDC 2000

#include "ComApplication.h"
#include "ComFramework.h"
#include "MacFramework.h"

//////////
//
// HandleEditMenuItem
// Perform the specified edit operation on the specified window.
//
//////////

void HandleEditMenuItem (WindowReference theWindow, UInt16 theMenuItem)
{
    WindowObject        myWindowObject = NULL;
    MovieController     myMC = NULL;
    Movie               myEditMovie = NULL;             // the movie created by some editing operations

    // give the application-specific code a chance to intercept the menu item selection
    if (QTApp_HandleMenu(theMenuItem))
        return;

    myWindowObject = QTFrame_GetWindowObjectFromWindow(theWindow);
    myMC = QTFrame_GetMCFromWindow(theWindow);

    // make sure we have a valid movie controller and a valid window object
    if ((myMC == NULL) || (myWindowObject == NULL))
        return;

    switch (theMenuItem) {

        case IDM_EDITUNDO:
            MCUndo(myMC);
            (**myWindowObject).fIsDirty = true;
            break;

        case IDM_EDITCUT:
            myEditMovie = MCCut(myMC);
            (**myWindowObject).fIsDirty = true;
            break;

        case IDM_EDITCOPY:
            myEditMovie = MCCopy(myMC);
            break;

        case IDM_EDITPASTE:
            MCPaste(myMC, NULL);
            (**myWindowObject).fIsDirty = true;
            break;

        case IDM_EDITCLEAR:
            MCClear(myMC);
            (**myWindowObject).fIsDirty = true;
            break;

        case IDM_EDITSELECTALL:
            SelectAllMovie(myMC);
            break;

        case IDM_EDITSELECTNONE:
            SelectNoneMovie(myMC);
            break;

        default:
            break;
    } // switch (theMenuItem)

    // place any cut or copied movie segment onto the scrap
    if (myEditMovie != NULL) {
        PutMovieOnScrap(myEditMovie, 0L);
        DisposeMovie(myEditMovie);
    }
}

//////////
//
// SelectAllMovie
// Select the entire movie associated with the specified movie controller.
// 
//////////

OSErr SelectAllMovie (MovieController theMC)
{
    TimeRecord          myTimeRecord;
    Movie               myMovie = NULL;
    ComponentResult     myErr = noErr;

    if (theMC == NULL)
        return(paramErr);

    myMovie = MCGetMovie(theMC);
    if (myMovie == NULL)
        return(paramErr);

    myTimeRecord.value.hi = 0;
    myTimeRecord.value.lo = 0;
    myTimeRecord.base = 0;
    myTimeRecord.scale = GetMovieTimeScale(myMovie);    
    myErr = MCDoAction(theMC, mcActionSetSelectionBegin, &myTimeRecord);
    if (myErr != noErr)
        return((OSErr)myErr);

    myTimeRecord.value.hi = 0;
    myTimeRecord.value.lo = GetMovieDuration(myMovie);  
    myTimeRecord.base = 0;
    myTimeRecord.scale = GetMovieTimeScale(myMovie);    
    myErr = MCDoAction(theMC, mcActionSetSelectionDuration, &myTimeRecord);

    return((OSErr)myErr);
}


//////////
//
// SelectNoneMovie
// Select none of the movie associated with the specified movie controller.
// 
//////////

OSErr SelectNoneMovie (MovieController theMC)
{
    TimeRecord          myTimeRecord;
    Movie               myMovie = NULL;
    ComponentResult     myErr = noErr;

    if (theMC == NULL)
        return(paramErr);

    myMovie = MCGetMovie(theMC);
    if (myMovie == NULL)
        return(paramErr);

    myTimeRecord.value.hi = 0;
    myTimeRecord.value.lo = 0;  
    myTimeRecord.base = 0;
    myTimeRecord.scale = GetMovieTimeScale(myMovie);    
    myErr = MCDoAction(theMC, mcActionSetSelectionDuration, &myTimeRecord);

    return((OSErr)myErr);
}
```

[Next](Completed%20Lab-Events.c.md)[Previous](Common%20Files-WinPrefix.h.md)

