---
title: Wake100
apple_id: DTS10000021
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Wake100/Listings/WakeINIT_c.html
archived_at: '2026-07-18T03:28:07.076020Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Wake100](Wake100.md)


[Next](Document%20Revision%20History.md)[Previous](Wake100.c.md)

# WakeINIT.c

```c
//
//
// © Copyright 1991 Apple Computer, Inc.  All Rights Reserved
//
// By Ricardo Batista
//
// This is an INIT which reads the wake up time in the PowerBook 100 and
// old Portable, if the wake up date has elapsed then we add a day to it
// so that the machine wakes up at the same time every day.
// By request of Neal Macklin.  Maybe we can make something useful from
// this later on.
//
//  This file is an INIT that loads a code resource and installs it in
// the sleep queue.

#define     SystemSevenOrLater  1

#include <Types.h>
#include <Power.h>
#include <Resources.h>
#include <Memory.h>
#include <GestaltEqu.h>

typedef unsigned long       ulong;


main()
{
    SleepQRec *slQ;
    Handle H;
    ProcPtr p;
    short err;
    long g = 0L;

    err = Gestalt(gestaltPowerMgrAttr,&g);
    if (err)
        return;
    if ((g && (1 << gestaltPMgrExists)) == 0)       // is there power Mgr ?
        return;
    H = GetResource('Wake',0);
    if (!H)
        return;
    LoadResource(H);
    HLock(H);
    DetachResource(H);
    p = (ProcPtr) StripAddress(*H);
    (*p)();                             // execute our proc, since we just restarted
    slQ = (SleepQRec*) NewPtrSys(sizeof(SleepQRec));
    if (!slQ)
        return;
    slQ = (SleepQRec*) StripAddress(slQ);
    slQ->sleepQLink = 0L;
    slQ->sleepQType = sleepQType;
    slQ->sleepQProc = p;
    slQ->sleepQFlags = 0;
    SleepQInstall(slQ);                 // install our sleep proc
}
```

[Next](Document%20Revision%20History.md)[Previous](Wake100.c.md)

