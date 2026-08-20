---
title: qtstreaming
apple_id: DTS10001051
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtstreaming/Listings/IMAAudioRTP_Sources_TCycle_c.html
archived_at: '2026-07-26T19:53:06.378765Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtstreaming](qtstreaming.md)


[Next](IMAAudioRTP-Sources-TQueue.c.md)[Previous](IMAAudioRTP-Sources-RTPRssmIMAAudio.r.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# IMAAudioRTP/Sources/TCycle.c

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

[Next](IMAAudioRTP-Sources-TQueue.c.md)[Previous](IMAAudioRTP-Sources-RTPRssmIMAAudio.r.md)

