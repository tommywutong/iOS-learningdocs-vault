---
title: DragWindow INIT
apple_id: DTS10000185
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/DragWindow_INIT/Listings/DragW_c.html
archived_at: '2026-07-18T03:07:11.682998Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DragWindow INIT](DragWindow%20INIT.md)


[Next](Document%20Revision%20History.md)[Previous](DragW%20INIT.c.md)

# DragW.c

```c
// NewDragWindow, Copyright © 1990 Ricardo Batista
// This code gets installed during system startup by an INIT, the purpose is to
// replace the old DragWindow routine with our code so that a window is moved
// along with it's contents as supposed to moving around an outline only.
//
// This code is for MPW C 3.1, when compiled into a resource the SysHeap and
// Locked bits need to be set in the resource attributes.
//
// After compiling copy this resource into a file that includes DragW INIT
//

#include "Types.h"
#include "Windows.h"

// we accept the same parameters as DragWindow, called by all Mac applications

pascal void NewDragWindow(WindowPtr w, Point pt, Rect *bounds)
{
    Point OldPoint, NewPoint, OffsetPoint;
    short h, v;
    GrafPtr savePort;

    GetPort(&savePort);                             // save the current port
    SetPort(w);                                     // set coordinate system to window
    OldPoint = NewPoint = pt;                       // make local copies of current mouse
    OffsetPoint.h = w->portRect.left;               // stuff top-left of window in point
    OffsetPoint.v = w->portRect.top;
    LocalToGlobal(&OffsetPoint);                    // convert too global coordinates
    OffsetPoint.h = pt.h - OffsetPoint.h;           // this offset is from window to mouse
    OffsetPoint.v = pt.v - OffsetPoint.v;
    while (StillDown()) {                           // is mouse still down ?
        GetMouse(&NewPoint);
        LocalToGlobal(&NewPoint);                   // whe now ?
        if (PtInRect(NewPoint, bounds)) {           // respect application boundaries
            if ((NewPoint.h != OldPoint.h) || (NewPoint.v != OldPoint.v)) {
                h = NewPoint.h - OffsetPoint.h;     // calculate new position of window
                v = NewPoint.v - OffsetPoint.v;     // using the offset of mouse-window
                MoveWindow(w, h, v, false);         // just do it
                OldPoint = NewPoint;                // save new 'old' location
            }
        }
    }
    SetPort(savePort);                              // restore coordinate system
}
```

[Next](Document%20Revision%20History.md)[Previous](DragW%20INIT.c.md)

