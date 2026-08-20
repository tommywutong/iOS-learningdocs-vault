---
title: QTSPketizerReassem.win
apple_id: DTS10001048
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem.win/Listings/IMAAudioRTP_RTPMPIMAAudio_Sources_TQueue_c.html
archived_at: '2026-07-18T03:21:13.966823Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem.win](QTSPketizerReassem.win.md)


[Next](IMAAudioRTP-RTPRssmIMAAudio-Headers-IMAAudioPayload.h.md)[Previous](IMAAudioRTP-RTPMPIMAAudio-Sources-TCycle.c.md)

# IMAAudioRTP/RTPMPIMAAudio/Sources/TQueue.c

```c
/*
    File:       TQueue.c

    Contains:   Definition of operations for TQueue, a generic queue datatype

    Copyright:  © 1997-1999 by Apple Computer, Inc., all rights reserved.

*/



#include "TQueue.h"



typedef struct __cElement
{
    TCycle  __itsLink;
    void *  __itsPayload;
} __cElement;



static
__cElement **
__ElementNew(
    void *  inPayload )
{
    __cElement **   __elementNew;


    __elementNew = ( __cElement ** ) CycleNew( sizeof( **__elementNew ) );

    if( __elementNew )
        ( **__elementNew ).__itsPayload = inPayload;

    return( __elementNew );
}



static
TCycle **
__ElementCycle(
    __cElement **   inElement )
{
    return( ( TCycle ** ) inElement );
}



static
void *
__ElementPayload(
    __cElement **   inElement )
{
    return( ( **inElement ).__itsPayload );
}



static
void
__ElementDispose(
    __cElement **   inElement )
{
    CycleDispose( ( TCycle ** ) inElement );
}



extern
void
QueueInitialize(
    TQueue *    inQueue )
{
    if( inQueue )
    {
        inQueue->__itsList = 0;
        inQueue->__itsCount = 0;
    }
}



extern
UInt32
QueueCount(
    const TQueue *      inQueue )
{
    UInt32  queueCount = 0;


    if( inQueue )
        queueCount = inQueue->__itsCount;

    return( queueCount );
}



extern
void *
QueueHead(
    const TQueue *  inQueue )
{
    void *  queueHead = 0;


    if( inQueue  &&  inQueue->__itsList )
        queueHead = __ElementPayload( ( __cElement ** ) CycleNext( inQueue->__itsList ) );

    return( queueHead );
}



extern
void *
QueueEnqueue(
    TQueue *    inQueue,
    void *      inElement )
{
    void *          queueEnqueue = 0;
    __cElement **   theElement;


    if( inQueue  &&  inElement )
    {
        theElement = __ElementNew( inElement );

        if( theElement )
        {
            if( inQueue->__itsList )
                CyclePut( inQueue->__itsList, __ElementCycle( theElement ) );

            inQueue->__itsList = __ElementCycle( theElement );
            inQueue->__itsCount++;

            queueEnqueue = inElement;
        }
    }

    return( queueEnqueue );
}



extern
void *
QueueDequeue(
    TQueue *    inQueue )
{
    void *          queueDequeue = 0;
    __cElement **   theElement;


    if( inQueue  &&  inQueue->__itsList )
    {
        theElement = ( __cElement ** ) CycleGet( inQueue->__itsList );

        queueDequeue = __ElementPayload( theElement );
        __ElementDispose( theElement );

        --inQueue->__itsCount;

        if( !inQueue->__itsCount )
            inQueue->__itsList = 0;
    }

    return( queueDequeue );
}
```

[Next](IMAAudioRTP-RTPRssmIMAAudio-Headers-IMAAudioPayload.h.md)[Previous](IMAAudioRTP-RTPMPIMAAudio-Sources-TCycle.c.md)

