---
title: PickOne
apple_id: DTS10000117
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PickOne/Listings/headers_PickOne_menu_h.html
archived_at: '2026-07-18T03:18:58.406163Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PickOne](PickOne.md)


[Next](headers-PickOneSupport.h.md)[Previous](headers-PickOnemain.h.md)

# headers/PickOne_menu.h

```c
/*  PickOne_menu.h                                                                          

    This contains all the menu code.

    Michael Bishop - August 21 1996                                                 
    Nick Thompson
    (c)1994-96 Apple computer Inc., All Rights Reserved                             

*/

#ifndef _BP_MENU_H_
#define _BP_MENU_H_

#include    <Menus.h>

enum {
    kMBARResID = 128
} ; 

enum {
    mApple = 128,
    mFile,
    mEdit,
    mRenderer
} ;

enum {
    iAbout = 1
} ;

enum {
    iNew = 1,
    iOpen,
    iClose,
    iUnused1,
    iSave,
    iSaveAs,
    iUnused2,
    iQuit
} ;

enum {
    iUndo,
    iEditUnused1,
    iCut = 3,
    iCopy,
    iPaste,
    iEditUnused2,
    iClear
} ;

enum {
    iSoftware = 1,
    iHardware,
    iEditUnused3,
    iBest
} ;

enum {
    iCenter = 1,
    iEditUnused4,
    iRight,
    iLeft
} ;


/* -------------------------------------------------------------------------------------------
** 
*/

void Menu_Adjust( void ) ;
void Menu_HandleCommand(long menuResult) ;

#endif
```

[Next](headers-PickOneSupport.h.md)[Previous](headers-PickOnemain.h.md)

