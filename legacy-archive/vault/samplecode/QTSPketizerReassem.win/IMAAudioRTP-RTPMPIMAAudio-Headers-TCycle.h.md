---
title: QTSPketizerReassem.win
apple_id: DTS10001048
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSPketizerReassem.win/Listings/IMAAudioRTP_RTPMPIMAAudio_Headers_TCycle_h.html
archived_at: '2026-07-18T03:21:12.920042Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSPketizerReassem.win](QTSPketizerReassem.win.md)


[Next](IMAAudioRTP-RTPMPIMAAudio-Headers-TQueue.h.md)[Previous](IMAAudioRTP-RTPMPIMAAudio-Headers-RTPMPIMAAudioResources.h.md)

# IMAAudioRTP/RTPMPIMAAudio/Headers/TCycle.h

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

[Next](IMAAudioRTP-RTPMPIMAAudio-Headers-TQueue.h.md)[Previous](IMAAudioRTP-RTPMPIMAAudio-Headers-RTPMPIMAAudioResources.h.md)

