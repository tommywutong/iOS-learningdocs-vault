---
title: ISp SampleOld
apple_id: DTS10000056
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/ISp_SampleOld/Listings/Source_EventHandler_h.html
archived_at: '2026-07-18T03:12:09.197701Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ISp SampleOld](ISp%20SampleOld.md)


[Next](Source-ISpSample.c.md)[Previous](Source-EventHandler.cp.md)

# Source/EventHandler.h

```c
/*
    File:       EventHandler.h

    Contains:   xxx put contents here xxx

    Version:    xxx put version here xxx

    Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.

    File Ownership:

        DRI:                xxx put dri here xxx

        Other Contact:      xxx put other contact here xxx

        Technology:         xxx put technology here xxx

    Writers:

        (BWS)   Brent Schorsch

    Change History (most recent first):

       <SP1>      7/1/99    BWS     first checked in
*/

#ifndef __EVENT_HANDLER__
#define __EVENT_HANDLER__

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Includes

#ifndef __EVENTS__
#include <Events.h>
#endif

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Definitions
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Types

typedef Boolean (*EventHandlerProc)(const EventRecord *inEvent);

typedef struct EventHandlerSet
{
    EventHandlerProc keyHandler;
    EventHandlerProc autoKeyHandler;
    EventHandlerProc clickHandler;
    EventHandlerProc updateHandler;
    EventHandlerProc diskHandler;
    EventHandlerProc idleHandler;
} EventHandlerSet;

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Variables

extern Boolean gDone;
extern EventHandlerSet gEventHandlers;

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Functions

#ifdef __cplusplus
extern "C" {
#endif

extern short EventInit(void);
extern void EventLoop(void);
extern void RegisterEventHandlers(EventHandlerProc inKeyDown, EventHandlerProc inAutoKey, EventHandlerProc inMouseDown,
                            EventHandlerProc inUpdate, EventHandlerProc inIdle);
extern void ModifyEventHandlers(EventHandlerProc inKeyDown, EventHandlerProc inAutoKey, EventHandlerProc inMouseDown,
                            EventHandlerProc inUpdate, EventHandlerProc inIdle);

#ifdef __cplusplus
}
#endif

#endif
```

[Next](Source-ISpSample.c.md)[Previous](Source-EventHandler.cp.md)

