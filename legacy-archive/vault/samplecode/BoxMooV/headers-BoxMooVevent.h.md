---
title: BoxMooV
apple_id: DTS10000099
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BoxMooV/Listings/headers_BoxMooV_event_h.html
archived_at: '2026-07-18T03:02:13.910142Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BoxMooV](BoxMooV.md)


[Next](headers-BoxMooVQuickTime.h.md)[Previous](headers-BoxMooVdocument.h.md)

# headers/BoxMooV_event.h

```c
/*  event.h                                                                     

    This contains all the code for routing and handling events.

    Michael Bishop - August 21 1996                                                 
    Nick Thompson
    (c)1994-96 Apple computer Inc., All Rights Reserved                             

*/

#ifndef _EVENT_H_
#define _EVENT_H_

#include    <Events.h>

void    Event_HandleKeyPress(EventRecord *event) ;
void    Event_HandleOSEvent(EventRecord *event) ;
void    Event_DoOSEvent(EventRecord theEvent);
void    Event_DoSuspendResume(EventRecord theEvent);
void    Event_DoNull(void);

#endif
```

[Next](headers-BoxMooVQuickTime.h.md)[Previous](headers-BoxMooVdocument.h.md)

