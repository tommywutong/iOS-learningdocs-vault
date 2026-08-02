---
title: Imageer
apple_id: DTS10000150
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Imageer/Listings/source_eventloop_c.html
archived_at: '2026-07-18T03:12:47.443335Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Imageer](Imageer.md)


[Next](source-fileCache.c.md)[Previous](source-doevent.c.md)

# source/eventloop.c

```c
/****************************************************/
/*                                                  */
/*  File:       eventloop.c                         */
/*                                                  */
/*  Program:    Imageer                             */
/*                                                  */
/*  By:         Jason Hodges-Harris                 */
/*                                                  */
/*  Created:    26/10/95  00:00:00 AM               */
/*                                                  */
/*  Version:    1.0.0d3                             */
/*                                                  */
/*  Copyright:  © 1995-96 Apple Computer, Inc.,     */ 
/*                  all rights reserved.            */      
/*                                                  */
/****************************************************/


/**** Macintosh Toolbox Headers *****/

#ifndef __EVENTS__
#include <Events.h>
#endif


/****   Application headers and prototypes   ****/


#ifndef __IMAGEERAPPHEADER__
#include "Imageer.app.h"
#endif

#ifndef __IMAGEERPROTOSHEADER__
#include "Imageer.protos.h"
#endif


//  Global Variables

extern Boolean      gDone;              // program loop test condition


// EventLoop handles the application's main WNE loop
// and is called from within the main() function.

#pragma segment Main
void EventLoop (void)
{
    EventRecord event;

    while (!gDone)
    {
        if (WaitNextEvent (everyEvent,&event,kSleep,nil))
        {
            DoEvent (&event);
        }
    }
}
```

[Next](source-fileCache.c.md)[Previous](source-doevent.c.md)

