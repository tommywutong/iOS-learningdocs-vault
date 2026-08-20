---
title: qtstreaming.win
apple_id: DTS10001052
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtstreaming.win/Listings/IMAAudioRTP_RTPMPIMAAudio_Headers_IMAAudioQueue_h.html
archived_at: '2026-07-26T19:53:06.816162Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtstreaming.win](qtstreaming.win.md)


[Next](IMAAudioRTP-RTPMPIMAAudio-Headers-IMAAudioRTP.h.md)[Previous](IMAAudioRTP-RTPMPIMAAudio-Headers-IMAAudioPayload.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# IMAAudioRTP/RTPMPIMAAudio/Headers/IMAAudioQueue.h

```c
/*
    File:       IMAAudioQueue.h

    Contains:   Delcaration of IMAAudioQueue, a queue datatype for IMA
                audio sample data.

    Copyright:  © 1997-1999 by Apple Computer, Inc., all rights reserved.

    The IMAAudioQueue serves several functions:

        -   it internally copies and disposes of RTPMPSampleDataParams
            data structures

        -   it converts from the descriptions of arbitrarily large sample
            blocks, given in RTPMPSampleDataParams data structures, to
            descriptions of single frames

        -   it can convert incoming data to a lower sample rate by dropping
            frames as necessary

*/

#ifndef __IMAAUDIOQUEUE__
#define __IMAAUDIOQUEUE__

#pragma once

#include "TQueue.h"
#include <QTStreamingComponents.h>

typedef struct IMAAudioQueueElement
{
    TimeValue64                 itsTimestamp;
    UInt32                      itsChannel;
    RTPMPSampleDataParams *     itsSampleDataParams;
    UInt32                      itsOffset;
} IMAAudioQueueElement;

typedef struct IMAAudioQueue
{
    TQueue          __itsQueue;
    TimeValue64     __itsStartTime;
    UInt32          __itsFrameCount;
    UInt32          __itsCurrentOffset;
    UInt32          __itsConsumedFrameCount;
    UInt32          __itsDequeuedFrameCount;
    UnsignedFixed   __itsIncomingSampleRate;
    UnsignedFixed   __itsOutgoingSampleRate;
    UInt16          __itsChannelCount;
} IMAAudioQueue;

extern
void
IMAAudioQueueInitialize(
    IMAAudioQueue *     inQueue );

extern
UnsignedFixed
IMAAudioQueueSetFlowControl(
    IMAAudioQueue *     inQueue,
    UnsignedFixed       inIncomingSampleRate,
    UnsignedFixed       inOutgoingSampleRate,
    UInt16              inChannelCount );

extern
UInt32
IMAAudioQueueCount(
    const IMAAudioQueue *   inQueue );

extern
RTPMPSampleDataParams *
IMAAudioQueueEnqueue(
    IMAAudioQueue *                 inQueue,
    const RTPMPSampleDataParams *   inSampleDataParams );

extern
Boolean
IMAAudioQueueDequeue(
    IMAAudioQueue *         inQueue,
    IMAAudioQueueElement *  outElement );

extern
void
IMAAudioQueueFlush(
    IMAAudioQueue *     inQueue );

#endif /* __IMAAUDIOQUEUE__ */
```

[Next](IMAAudioRTP-RTPMPIMAAudio-Headers-IMAAudioRTP.h.md)[Previous](IMAAudioRTP-RTPMPIMAAudio-Headers-IMAAudioPayload.h.md)

