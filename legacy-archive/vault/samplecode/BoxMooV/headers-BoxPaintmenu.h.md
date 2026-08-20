---
title: BoxMooV
apple_id: DTS10000099
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BoxMooV/Listings/headers_BoxPaint_menu_h.html
archived_at: '2026-07-18T03:02:14.216966Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BoxMooV](BoxMooV.md)


[Next](headers-BoxPaintSupport.h.md)[Previous](headers-BoxPaintmain.h.md)

# headers/BoxPaint_menu.h

```c
/*  menu.h                                                                          

    This contains all the menu code.

    Michael Bishop - August 21 1996                                                 
    Nick Thompson
    (c)1994-96 Apple computer Inc., All Rights Reserved                             

*/

#ifndef _MENU_H_
#define _MENU_H_

#include <Menus.h>

enum {
    kMBARResID = 128
} ; 

enum {
    mApple = 128,
    mFile,
    mEdit,
    mResolution
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
    i64 = 1,
    i128,
    i256
};


/* -------------------------------------------------------------------------------------------
** 
*/

void Menu_Adjust( void ) ;
void Menu_HandleCommand(long menuResult) ;

#endif
```

[Next](headers-BoxPaintSupport.h.md)[Previous](headers-BoxPaintmain.h.md)

