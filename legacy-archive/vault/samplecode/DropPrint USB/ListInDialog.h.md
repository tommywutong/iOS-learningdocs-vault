---
title: DropPrint USB
apple_id: DTS10000288
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/DropPrint_USB/Listings/ListInDialog_h.html
archived_at: '2026-07-18T03:07:21.648846Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DropPrint USB](DropPrint%20USB.md)


[Next](ListInDialog.r.md)[Previous](ListInDialog.c.md)

# ListInDialog.h

```c
/*
    File:       ListInDialog.h

    Contains:   

    Written by: Olav Andrade

    Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.

    Change History:


    To Do:
*/

#ifndef __DIALOGS__
#include <dialogs.h>
#endif
#ifndef __LISTS__
#include <lists.h>
#endif

void            SetupMenus( void );
pascal Boolean  theListFilter( DialogPtr theDialog, EventRecord *theEvent, short *itemHit);

void            SetUpList(ListHandle theList, char *path );
void            GetNameFromCell (StringPtr theString, Cell cell, ListHandle hList);
ListHandle      MakeDialogList( DialogPtr dlg, int item );
int             ChoosePrinter( char *name, long *blocksize, int *repeat_count );
void            HiliteOk( DialogPtr dlg );
void            FrameOk( DialogPtr dlg );
int             GetDialogPopupValue( DialogPtr dlg, int item );
void            SetDialogPopupValue( DialogPtr dlg, int item, int value );
```

[Next](ListInDialog.r.md)[Previous](ListInDialog.c.md)

