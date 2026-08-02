---
title: qtstreaming.win
apple_id: DTS10001052
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtstreaming.win/Listings/IMAAudioRTP_RTPMPIMAAudio_Headers_TCycle_h.html
archived_at: '2026-07-26T19:53:06.874217Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtstreaming.win](qtstreaming.win.md)


[Next](IMAAudioRTP-RTPMPIMAAudio-Headers-TQueue.h.md)[Previous](IMAAudioRTP-RTPMPIMAAudio-Headers-RTPMPIMAAudioResources.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# IMAAudioRTP/RTPMPIMAAudio/Headers/TCycle.h

```swift
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

