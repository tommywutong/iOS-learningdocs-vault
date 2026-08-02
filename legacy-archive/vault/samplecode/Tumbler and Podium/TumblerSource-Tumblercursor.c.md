---
title: Tumbler and Podium
apple_id: DTS10000127
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Tumbler_and_Podium/Listings/TumblerSource_Tumbler_cursor_c.html
archived_at: '2026-07-18T03:27:21.305800Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tumbler and Podium](Tumbler%20and%20Podium.md)


[Next](TumblerSource-Tumblercursor.h.md)[Previous](TumblerSource-Tumblercamera.h.md)

# TumblerSource/Tumbler_cursor.c

```c
//
//
//      cursor.c
//
//      Cursor handling routines.
//      
//
//      Author:     Nick Thompson & Pablo Fernicola, with thanks to the QuickDraw 3D team
//
//      Copyright © 1992-95 Apple Computer, Inc., All Rights Reserved
//

#include "Tumbler_globals.h"
#include "Tumbler_prototypes.h"
#include "Tumbler_resources.h"

#include "QD3DView.h"
#include "QD3DDrawContext.h"
#include "QD3DPick.h"

#include "Tumbler_cursor.h"



void AdjustCursor(Point theLoc, RgnHandle theRgn)
{
    // do nothing for now
}


void GetGlobalMouse(Point *theLoc)

{   EventRecord     theEvent;

    OSEventAvail(0, &theEvent);
    *theLoc = theEvent.where;
}
```

[Next](TumblerSource-Tumblercursor.h.md)[Previous](TumblerSource-Tumblercamera.h.md)

