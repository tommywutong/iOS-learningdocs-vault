---
title: qtcontroller.win
apple_id: DTS10000776
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtcontroller.win/Listings/QTCustomButton_c.html
archived_at: '2026-07-26T19:52:30.770586Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtcontroller.win](qtcontroller.win.md)


[Next](QTCustomButton.h.md)[Previous](Common%20Files-WinPrefix.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTCustomButton.c

```c
//////////
//
//  File:       QTCustomButton.c
//
//  Contains:   Sample code for displaying and managing the custom button in the controller bar.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      11/25/99    rtm     first file
//
//  This code snippet shows one way to display a pop-up menu when the user clicks on the custom
//  button in the movie controller bar (just like the QuickTime web browser plug-in does for its
//  custom button). The basic idea is very simple: just call PopUpMenuSelect when the user clicks
//  the custom button. Before we do that, however, we need to obtain a MenuHandle to the desired
//  pop-up menu. Here we use NewMenu and MacAppendMenu to create the menu on the fly; we do this
//  mainly so that we don't need to drag a resource file around. A real application would just
//  call MacGetMenu to read the menu from its resource file.
//
//  Note that all menu-handling here uses the Macintosh Menu Manager APIs. This code executes
//  just fine on Windows, though.
//
//////////

//////////
//
// header files
//
//////////

#include "QTCustomButton.h"
#include "ComFramework.h"

//////////
//
// QTCustom_HandleCustomButtonClick
// Handle a click on the custom button in the controller bar.
//
//////////

void QTCustom_HandleCustomButtonClick (MovieController theMC, EventRecord *theEvent, long theRefCon)
{
#pragma unused(theMC)
    MenuHandle          myMenu = NULL;
    WindowObject        myWindowObject = NULL;
    StringPtr           myMenuTitle = QTUtils_ConvertCToPascalString(kMenuTitle);
    StringPtr           myItem1Text = QTUtils_ConvertCToPascalString(kItem1Text);
    StringPtr           myItem2Text = QTUtils_ConvertCToPascalString(kItem2Text);
    StringPtr           myItem3Text = QTUtils_ConvertCToPascalString(kItem3Text);

    myWindowObject = (WindowObject)theRefCon;
    if (myWindowObject == NULL)
        goto bail;

    // make sure we got a valid event
    if (theEvent == NULL)
        goto bail;

    // create a new menu;
    // we do this programmatically (rather than using resources) to facilitate cross-platform deployment;
    // to read the menu from your resource file, use MacGetMenu instead of NewMenu
    myMenu = NewMenu(kCustomButtonMenuID, myMenuTitle);
    if (myMenu != NULL) {
        long            myItem = 0;
        Point           myPoint;

        // add some items to the menu
        MacAppendMenu(myMenu, myItem1Text);
        MacAppendMenu(myMenu, myItem2Text);
        MacAppendMenu(myMenu, myItem3Text);

        // insert the menu into the menu list
        MacInsertMenu(myMenu, kInsertHierarchicalMenu);

        // by default, MacAppendMenu enables the item; do any desired menu item disabling here
        if (!(**myWindowObject).fIsDirty)
            DisableMenuItem(myMenu, kSaveItemIndex);

        // find the location of the mouse click;
        // the top-left corner of the pop-up menu is anchored at this point
        myPoint = theEvent->where;
        LocalToGlobal(&myPoint);

        // display the pop-up menu and handle the item selected
        myItem = PopUpMenuSelect(myMenu, myPoint.v, myPoint.h, myItem);
        switch (MENU_ITEM(myItem)) {
            case kItem1Index:
                QTFrame_Beep();
                break;
            case kItem2Index:
                QTFrame_ShowAboutBox();
                break;
            case kItem3Index:
                QTFrame_UpdateMovieFile((**myWindowObject).fWindow);
                break;
        }

        // remove the menu from the menu list
#if ACCESSOR_CALLS_ARE_FUNCTIONS
        MacDeleteMenu(GetMenuID(myMenu));
#else
        MacDeleteMenu((**myMenu).menuID);
#endif

        // dispose of the menu
        DisposeMenu(myMenu);
    }

bail:
    free(myMenuTitle);
    free(myItem1Text);
    free(myItem2Text);
    free(myItem3Text);
}
```

[Next](QTCustomButton.h.md)[Previous](Common%20Files-WinPrefix.h.md)

