---
title: ControlBackground
apple_id: DTS10000565
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/ControlBackground/Listings/MoveableModalDialog_c.html
archived_at: '2026-07-18T03:04:16.103772Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ControlBackground](ControlBackground.md)


[Next](MoveableModalDialog.h.md)[Previous](ControlBackground.c.md)

# MoveableModalDialog.c

```c
/*
    File:       MoveableModalDialog.c

    Contains:   

    Written by: Pete Gontier    

    Copyright:  Copyright © 1997-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/19/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/

#include <Sound.h>

#include "MoveableModalDialog.h"

pascal void MoveableModalDialog (ModalFilterUPP mfp, short *itemHit)
{
    EventRecord event;
    DialogRef pop, dummy;
    WindowRef whichWindow;
    short partCode;
    Boolean handledIt = false;

    pop = FrontWindow( );
    *itemHit = -1;

    do
    {
        WaitNextEvent (everyEvent & ~highLevelEventMask, &event, GetCaretTime( ), nil);

        switch (event.what)
        {
            case mouseDown:

                partCode = FindWindow (event.where, &whichWindow);

                if (whichWindow != pop)
                {
                    if (partCode == inSysWindow)
                        SystemClick (&event,whichWindow);
                    else
                        SysBeep(10);
                    break;
                }

                if (inDrag == partCode)
                {
                    Rect dragBounds;


                    dragBounds = qd.screenBits.bounds;
                    InsetRect (&dragBounds, 4, 4);
                    DragWindow (pop, event.where, &dragBounds);
                    break;
                }

                // fall thru

            default:

                if (mfp)
                    handledIt = CallModalFilterProc (mfp,pop,&event,itemHit);

                if (!handledIt && IsDialogEvent(&event))
                    DialogSelect(&event,&dummy,itemHit);

                break;
        }
    }
    while (*itemHit == -1);
}
```

[Next](MoveableModalDialog.h.md)[Previous](ControlBackground.c.md)

