---
title: Tabs LDEF
apple_id: DTS10000621
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/Tabs_LDEF/Listings/Lists_c.html
archived_at: '2026-07-18T03:26:18.826875Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabs LDEF](Tabs%20LDEF.md)


[Next](Menus.c.md)[Previous](Initialize.c.md)

# Lists.c

```c
/*
    File:       Lists.c

    Contains:   List Manager stuff and associated routines

    Written by:     

    Copyright:  Copyright © 1995-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/10/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/


#pragma segment Core


// System Includes



// Application Includes

#ifndef __BAREBONES__
    #include "BareBones.h"
#endif

#ifndef __PROTOTYPES__
    #include "Prototypes.h"
#endif






Boolean HandleListClick ( WindowRef theWindow, EventRecord* event )
{
    Point       localPt;
    ListRef     theList;


    localPt = event->where;
    GlobalToLocal ( &localPt );
    theList = (ListRef) GetWRefCon ( theWindow );

    if ( (*theList)->lActive == true )
    {
        Rect    listRect;

        GetListRect ( theList, &listRect );
        // Include the scroll bars
        listRect.right += 15;

        if ( PtInRect ( localPt, &listRect ) )
            LClick ( localPt, event->modifiers, theList );

    }

    return true;
}



void AddToList ( ListRef theList, Str255 theString )
{
    Rect    dataRect;
    Cell    theCell;
    short   nuRow;

    #if DEBUGGING
    if ( theList == nil ) DebugStr ( "\p theList == nil");
    #endif

    dataRect = (*theList)->dataBounds;
    nuRow = LAddRow ( 1, dataRect.bottom, theList );
    SetPt ( &theCell, 0, nuRow );
    LSetCell ( &theString[1], theString[0], theCell, theList );

    return;
}



void GetListRect ( ListRef theList, Rect* theRect )
{
    *theRect = (*theList)->rView;
}
```

[Next](Menus.c.md)[Previous](Initialize.c.md)

