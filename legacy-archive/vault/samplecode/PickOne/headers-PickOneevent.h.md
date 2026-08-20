---
title: PickOne
apple_id: DTS10000117
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PickOne/Listings/headers_PickOne_event_h.html
archived_at: '2026-07-18T03:18:58.342892Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PickOne](PickOne.md)


[Next](headers-PickOnemain.h.md)[Previous](headers-PickOnedocumentStructure.h.md)

# headers/PickOne_event.h

```c
/*  event.h                                                                     

    This contains all the code for routing and handling events.

    Michael Bishop - August 21 1996                                                 
    Nick Thompson
    (c)1994-96 Apple computer Inc., All Rights Reserved                             

*/

#ifndef _BP_EVENT_H_
#define _BP_EVENT_H_

#include    <Events.h>

void    Event_HandleKeyPress(EventRecord *event) ;
void    Event_HandleOSEvent(EventRecord *event) ;
void    Event_DoOSEvent(EventRecord theEvent);
void    Event_DoSuspendResume(EventRecord theEvent);
void    Event_DoNull(void);

#endif
```

[Next](headers-PickOnemain.h.md)[Previous](headers-PickOnedocumentStructure.h.md)

