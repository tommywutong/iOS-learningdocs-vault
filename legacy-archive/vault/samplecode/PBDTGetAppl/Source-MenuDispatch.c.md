---
title: PBDTGetAppl
apple_id: DTS10000042
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PBDTGetAppl/Listings/Source_MenuDispatch_c.html
archived_at: '2026-07-18T03:18:20.032145Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PBDTGetAppl](PBDTGetAppl.md)


[Next](Source-PrintLoop.c.md)[Previous](Source-InitMac.c.md)

# Source/MenuDispatch.c

```c
/*
    9-30-92  ¥ Brigham Stevens
    --------------------------
    Menu.c      This handles Menu command dispatching 

    This is a bare minimum menu initializer and dispatcher.
    Menus are initialized from an MBAR resource id 128.  To add new menus
    you must change this resource.

*/

#include "EventLoop.h"
#include "MenuDispatch.h"

void BuildMenuBars(void)
{
    Handle mbar;

    mbar=GetNewMBar(128);
    if(mbar) {
        SetMenuBar(mbar);
        AddResMenu(GetMHandle(APPLE_MENU),'DRVR');
        DrawMenuBar();
    } else {
        ErrMsg("\pMenubar resouce not loaded.  Program will abort.");
        ExitToShell();
    }
}

void RunDeskAccesory(short item)
{
    GrafPtr     savePort;
    short       daRefNum;
    Str255      daName;

    GetPort(&savePort);
    GetItem(GetMHandle(APPLE_MENU), item, &daName);
    daRefNum = OpenDeskAcc(&daName);
    SetPort(savePort);
}

void ChooseApple(short itemNumber)
{
    short item;

    if(itemNumber == APPLE_ABOUT) {
        item = Alert(ABOUT_BOX_ID,nil);
    } else {
        RunDeskAccesory(itemNumber);
    }
}

void ChooseFile(short item)
{
    switch(item) {
        case FILE_PRINT :   PrintWindow();
                            break;
        case FILE_QUIT  :   Done = true;
                            break;
        default:            break;
    }
}


void ChooseEdit(short item)
/*
    Does not support edit menu.  Assumes that if the edit menu is enabled
    that it is for desk accessories.  (pre MF or system 7, or MF with optionkey)
*/
{
    SystemEdit(item-1);
}

void MenuDispatch(short menuNumber,short itemNumber)
{
    if(menuNumber != 0)
        switch(menuNumber) {
            case APPLE_MENU :   ChooseApple(itemNumber);
                                break;
            case FILE_MENU :    ChooseFile(itemNumber);
                                break;
            case EDIT_MENU :    ChooseEdit(itemNumber);
                                break;
            case SLIM_MENU :    ChooseSlim(itemNumber);
                                break;
            default :           break;
        }
}
```

[Next](Source-PrintLoop.c.md)[Previous](Source-InitMac.c.md)

