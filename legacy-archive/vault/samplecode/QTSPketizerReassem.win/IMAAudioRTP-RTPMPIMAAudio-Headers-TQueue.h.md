---
title: QTSPketizerReassem.win
apple_id: DTS10001048
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem.win/Listings/IMAAudioRTP_RTPMPIMAAudio_Headers_TQueue_h.html
archived_at: '2026-07-18T03:21:12.963176Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem.win](QTSPketizerReassem.win.md)


[Next](IMAAudioRTP-RTPMPIMAAudio-Sources-ComponentThing.r.md)[Previous](IMAAudioRTP-RTPMPIMAAudio-Headers-TCycle.h.md)

# IMAAudioRTP/RTPMPIMAAudio/Headers/TQueue.h

```c
/*
    File:       TQueue.h

    Contains:   Declaration of TQueue, a generic queue datatype

    Copyright:  © 1997-1999 by Apple Computer, Inc., all rights reserved.

*/



#ifndef __TQUEUE__
#define __TQUEUE__

#pragma once



#include "TCycle.h"
#include <MacTypes.h>



typedef struct TQueue
{
    TCycle **   __itsList;
    UInt32      __itsCount;
} TQueue;



extern
void
QueueInitialize(
    TQueue *    inQueue );

extern
UInt32
QueueCount(
    const TQueue *  inQueue );

extern
void *
QueueHead(
    const TQueue *  inQueue );

extern
void *
QueueEnqueue(
    TQueue *    inQueue,
    void *      inElement );

extern
void *
QueueDequeue(
    TQueue *    inQueue );



#endif /* __TQUEUE__ */
```

[Next](IMAAudioRTP-RTPMPIMAAudio-Sources-ComponentThing.r.md)[Previous](IMAAudioRTP-RTPMPIMAAudio-Headers-TCycle.h.md)

