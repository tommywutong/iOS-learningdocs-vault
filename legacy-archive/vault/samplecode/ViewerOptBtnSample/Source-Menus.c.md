---
title: ViewerOptBtnSample
apple_id: DTS10000139
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ViewerOptBtnSample/Listings/Source_Menus_c.html
archived_at: '2026-07-18T03:28:01.010867Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ViewerOptBtnSample](ViewerOptBtnSample.md)


[Next](Source-Misc.c.md)[Previous](Source-Main.c.md)

# Source/Menus.c

```c
/****************************/
/*        MENUS             */
/****************************/


/***************/
/* EXTERNALS   */
/***************/
#include <Dialogs.h>
#include <Menus.h>
#include <ToolUtils.h>
#include <Devices.h>

#include "myglobals.h"
#include "mymenus.h"
#include "misc.h"
#include "process.h"


/******************/
/*  PROTOTYPES    */
/******************/

static void HandleSpecialMenuChoice(short theItem);


/****************************/
/*    CONSTANTS             */
/****************************/

                                    // MENU BAR ITEMS //
#define NOT_A_NORMAL_MENU   -1
#define APPLE_MENU_ID       400
#define FILE_MENU_ID        401
#define EDIT_MENU_ID        402


                                    // EDIT MENU ITEMS //

enum
{
    UNDO_ITEM   =   1,
    CUT_ITEM    =   3,
    COPY_ITEM   =   4,  
    PASTE_ITEM  =   5,
    CLEAR_ITEM  =   6
};

                                    // FILE MENU ITEMS //
enum
{
    SAVE_ITEM   = 1,
    QUIT_ITEM   = 2
};


                                    // APPLE MENU ITEMS //
enum                                    
{                                   
    ABOUT_ITEM = 1,
    HELP_ITEM = 2
};



/**********************/
/*     VARIABLES      */
/**********************/

MenuHandle  gAppleMenu;


/******************/
/* INIT MENU BAR  */
/******************/

void InitMenuBar(void)
{
Handle  myMenuBar;

                    /* ALLOCATE MAIN MENU BAR */

    if ((myMenuBar  =   GetNewMBar(400)) == nil)
            DoFatalAlert("\pWhered the menu bar go?!");;
    SetMenuBar(myMenuBar);

                    /* SET APPLE MENU */

    if ((gAppleMenu =   GetMenuHandle(400)) == nil)
            DoFatalAlert("\pGetMHandle failed!");
    AppendResMenu (gAppleMenu, 'DRVR');                     // APPEND DESK ACCESSORIES

    DrawMenuBar();
}


/***************************/
/* HANDLE MENU BAR CHOICE  */
/***************************/

void HandleMenuChoice(long menuChoice)
{
short   theMenu;
short   theItem;

    if  (menuChoice != 0)
    {
        theMenu =   HiWord(menuChoice);
        theItem =   LoWord(menuChoice);
        switch  (theMenu)
        {
            case    APPLE_MENU_ID:
                    HandleAppleChoice(theItem);
                    break;

            case    FILE_MENU_ID:
                    HandleFileChoice(theItem);
                    break;

            case    EDIT_MENU_ID:
                    HandleEditChoice(theItem);
                    break;


        }
        HiliteMenu(0);
    }
}


/*****************************/
/* HANDLE APPLE MENU CHOICE  */
/*****************************/

void HandleAppleChoice(short theItem)
{
Str255  accName;
short       accNumber;

    switch  (theItem)
    {
        case    ABOUT_ITEM:

                Alert(402,nil);
                break;
        case    HELP_ITEM:
                Alert(128,nil);
                break;

        default:
                GetMenuItemText(gAppleMenu,theItem,accName);
                accNumber   =   OpenDeskAcc(accName);
                break;
    }
}

/****************************/
/* HANDLE FILE MENU CHOICE  */
/****************************/

void HandleFileChoice(short theItem)
{
    switch(theItem)
    {
        case    SAVE_ITEM:
                SaveViewerPICT();
                break;

        case    QUIT_ITEM:
                CleanQuit();
    }
}


/****************************/
/* HANDLE EDIT MENU CHOICE  */
/****************************/

void HandleEditChoice(short theItem)
{
    SystemEdit(theItem-1);

    switch(theItem)
    {
    }
}
```

[Next](Source-Misc.c.md)[Previous](Source-Main.c.md)

