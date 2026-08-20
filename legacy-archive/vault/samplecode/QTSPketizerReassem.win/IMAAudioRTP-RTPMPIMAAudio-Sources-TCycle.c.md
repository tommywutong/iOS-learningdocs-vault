---
title: QTSPketizerReassem.win
apple_id: DTS10001048
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem.win/Listings/IMAAudioRTP_RTPMPIMAAudio_Sources_TCycle_c.html
archived_at: '2026-07-18T03:21:13.843261Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem.win](QTSPketizerReassem.win.md)


[Next](IMAAudioRTP-RTPMPIMAAudio-Sources-TQueue.c.md)[Previous](IMAAudioRTP-RTPMPIMAAudio-Sources-RTPMPIMAAudio.r.md)

# IMAAudioRTP/RTPMPIMAAudio/Sources/TCycle.c

```c
/*
    File:       TCycle.c

    Contains:   Definition of operations for TCycle, a cyclic list element datatype

    Copyright:  © 1997-1999 by Apple Computer, Inc., all rights reserved.

*/



#include "TCycle.h"
#include <MacMemory.h>



extern
TCycle **
CycleNew(
    unsigned long   inSize )
{
    TCycle **   cycleNew;


    if( inSize < sizeof( **cycleNew ) )
        inSize = sizeof( **cycleNew );

    cycleNew = ( TCycle ** ) NewHandle( inSize );

    if( cycleNew )
        ( **cycleNew ).__itsNext = cycleNew;

    return( cycleNew );
}



extern
void
CycleDispose(
    TCycle **   inElement )
{
    if( inElement )
    {
        if( ( **inElement ).__itsNext == inElement )
            DisposeHandle( ( Handle ) inElement );
    }
}



extern
TCycle **
CyclePut(
    TCycle **   inList,
    TCycle **   inElement )
{
    TCycle **   cyclePut = inList;


    if( inList  &&  inElement )
    {
        if( ( **inElement ).__itsNext == inElement )
        {
            ( **inElement ).__itsNext = ( **inList ).__itsNext;
            ( **inList ).__itsNext = inElement;
            cyclePut = inElement;
        }
    }

    return( cyclePut );
}



extern
TCycle **
CycleGet(
    TCycle **   inList )
{
    TCycle **   cycleGet = 0;


    if( inList )
    {
        cycleGet = ( **inList ).__itsNext;
        ( **inList ).__itsNext = ( **cycleGet ).__itsNext;
        ( **cycleGet ).__itsNext = cycleGet;
    }

    return( cycleGet );
}



extern
TCycle **
CycleNext(
    TCycle **   inElement )
{
    TCycle **   cycleNext = 0;


    if( inElement )
        cycleNext = ( **inElement ).__itsNext;

    return( cycleNext );
}
```

[Next](IMAAudioRTP-RTPMPIMAAudio-Sources-TQueue.c.md)[Previous](IMAAudioRTP-RTPMPIMAAudio-Sources-RTPMPIMAAudio.r.md)

