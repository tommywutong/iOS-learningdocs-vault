---
title: BoxMooV
apple_id: DTS10000099
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BoxMooV/Listings/sources_BoxPaint_menu_c.html
archived_at: '2026-07-18T03:02:15.360755Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BoxMooV](BoxMooV.md)


[Next](sources-BoxPaintSupport.c.md)[Previous](sources-BoxPaintmain.c.md)

# sources/BoxPaint_menu.c

```c
/*  menu.c                                                                          

    This contains all the menu code.

    Michael Bishop - August 21 1996                                                 
    Nick Thompson
    (c)1994-96 Apple computer Inc., All Rights Reserved                             

*/

/* --------------------------------------------------------------------
** Includes
*/

#include <StandardFile.h>
#include <Devices.h>

#include    "BoxPaint_menu.h"
#include    "BoxPaint_utility.h"
#include    "BoxMooV_window.h"
#include    "BoxMooV_document.h"
#include    "BoxPaint_main.h"

/* --------------------------------------------------------------------
** Global Variables
*/


/* --------------------------------------------------------------------
** Local Functions
*/


/*  --------------------------------------------------------------------
**  Menu_Adjust
**  Update the menus to reflect the current status of the App
*/
void Menu_Adjust( void ) 
{
    WindowPtr   theWindow = FrontWindow();

    if (theWindow != NULL) {

    }
}


/*  --------------------------------------------------------------------
**  Menu_HandleCommand
**  Finds out what was selected and does something about it.
*/
void Menu_HandleCommand(long menuResult)
{
    short               menuID;
    short               menuItem;
    Str255              daName;


    short               numTypes = 1 ;
    SFTypeList          myTypes = { '3DMF', 0 } ;


    WindowPtr           theWindow = FrontWindow() ;

    menuID = Utility_HiWrd(menuResult);
    menuItem = Utility_LoWrd(menuResult);

    switch ( menuID ) {
        /*  */
        /* --------------------------------------------------------------------------    */
        /*  */
        case mApple:
            switch ( menuItem ) {

                case iAbout:
                    Main_DoAbout() ;    
                    break ;

                default:
                    GetMenuItemText(GetMenuHandle(mApple), menuItem, daName);
                    (void) OpenDeskAcc(daName);
                    break;
            }
            break;
        /* --------------------------------------------------------------------------    */
        case mFile:
            switch ( menuItem ) {

                case iNew:
                    Document_New() ;
                    break ;

                case iOpen:
                    Document_Open() ;
                    break ;

                case iSave:             
                    break ;

                case iSaveAs:
                    break;              

                case iClose:
                    Document_Delete( Document_GetFromWindow(theWindow) ) ;
                    break ;

                case iQuit:
                    gQuitFlag = true ;
                    break;
            }
            break;


        /* --------------------------------------------------------------------------    */
        case mEdit:

            switch(menuItem)
            {
                case iCut:
                    break;
                case iCopy:
                    break;
                case iPaste:
                    break;
                case iClear:
                    break;
                default:
                    break;
            }
            break; 

        /* --------------------------------------------------------------------------    */

    }
    HiliteMenu(0);      /*  Unhighlight whatever MenuSelect or MenuKey hilited */
}
```

[Next](sources-BoxPaintSupport.c.md)[Previous](sources-BoxPaintmain.c.md)

