---
title: QTSPketizerReassem
apple_id: DTS10001047
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem/Listings/IMAAudioRTP_Headers_TCycle_h.html
archived_at: '2026-07-18T03:21:16.949810Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem](QTSPketizerReassem.md)


[Next](IMAAudioRTP-Headers-TQueue.h.md)[Previous](IMAAudioRTP-Headers-RTPRssmIMAAudioResources.h.md)

# IMAAudioRTP/Headers/TCycle.h

```
/*
    File:       TCycle.h

    Contains:   Declaration of TCycle, a cyclic list element datatype

    Copyright:  © 1997-1999 by Apple Computer, Inc., all rights reserved.

*/



#ifndef __TCYCLE__
#define __TCYCLE__

#pragma once



typedef struct TCycle
{
    struct TCycle **    __itsNext;
} TCycle;



extern
TCycle **
CycleNew(
    unsigned long   inSize );

extern
void
CycleDispose(
    TCycle **   inElement );

extern
TCycle **
CyclePut(
    TCycle **   inList,
    TCycle **   inElement );

extern
TCycle **
CycleGet(
    TCycle **   inList );

extern
TCycle **
CycleNext(
    TCycle **   inElement );



#endif /* __TCYCLE__ */
```

[Next](IMAAudioRTP-Headers-TQueue.h.md)[Previous](IMAAudioRTP-Headers-RTPRssmIMAAudioResources.h.md)

