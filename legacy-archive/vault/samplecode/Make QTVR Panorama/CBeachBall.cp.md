---
title: Make QTVR Panorama
apple_id: DTS10000339
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Make_QTVR_Panorama/Listings/CBeachBall_cp.html
archived_at: '2026-07-18T03:14:24.759149Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Make QTVR Panorama](Make%20QTVR%20Panorama.md)


[Next](CBeachBall.h.md)[Previous](CApp.h.md)

# CBeachBall.cp

```c
/*
    Implements an interrupt time spinning cursor

    Created 29 Jan 1996 by EGH

    Copyright © 1996, Apple Computer, Inc. All rights reserved.
*/

#include <UException.h>

#include "CBeachBall.h"

SInt16 CBeachBall::sNumBBCur = 0;
Cursor *CBeachBall::sBBCursors = nil;
SInt16 CBeachBall::sCurBB = 0;
UInt32 CBeachBall::sSpinTime = 0;

void CBeachBall::InitBeachBall()
{
    CursHandle cursH;
    acurHandle aH;
    SInt16 t;

        // get the beach ball acur
    aH = (acurHandle)GetResource('acur', 128);
    ThrowIfNil_(aH);
    ::HNoPurge((Handle)aH);

        // get the beach ball cursors
    sNumBBCur = (*aH)-> n;
    sBBCursors = (Cursor *)::NewPtrClear(sNumBBCur * sizeof (Cursor));
    for (t = 0; t < (*aH)-> n; t++)
    {
        if ((cursH = ::GetCursor(*(SInt16 *)(&(*aH)-> frame1 + (t * 2)))) != nil)
        {
            ::BlockMove((Ptr)*cursH, (Ptr)&sBBCursors[t], sizeof (Cursor));
            ::ReleaseResource((Handle)cursH);
        }
    }
    ::ReleaseResource((Handle)aH);
    sCurBB = 0;                                         // set to first cursor
}

void CBeachBall::SpinBeachBall()
{
    if (sBBCursors != nil && ::TickCount() > sSpinTime)
    {       
            // display the current spinnable cursor
        ::SetCursor(&sBBCursors[sCurBB]);
        sCurBB++;
        if (sCurBB == sNumBBCur)
            sCurBB = 0;
        sSpinTime = ::TickCount() + 2;
    }
}

short CBeachBall::sSpinCount;
VBLTaskNA5 *CBeachBall::sSpinTask = nil;

void CBeachBall::StartSpinningTask(
    short inCount)
{
    sSpinCount = inCount;
    sSpinTask = (VBLTaskNA5 *)::NewPtr(sizeof (VBLTaskNA5));
    sSpinTask->task.qType = vType;
    sSpinTask->task.vblAddr = NewVBLProc(SpinTask);
    sSpinTask->task.vblCount = inCount;
    sSpinTask->task.vblPhase = 0;
    sSpinTask->a5 = (long)LMGetCurrentA5();

    (void)::VInstall((QElemPtr)sSpinTask);
}

void CBeachBall::StopSpinningTask()
{
    if (sSpinTask != nil)
    {
        (void)::VRemove((QElemPtr)sSpinTask);
        ::DisposePtr((Ptr)sSpinTask);
        sSpinTask = nil;
    }
}

#ifdef powerc
void CBeachBall::SpinTask(
    VBLTaskNA5 *inTask)
#else
void CBeachBall::SpinTask(
    VBLTaskNA5 *inTask : __D0)
#endif
{   
    if (LMGetCrsrBusy() == 0)
    {
#ifndef powerc
        long oldA5 = SetA5(inTask->a5);
#endif
        ::SetCursor(&sBBCursors[sCurBB]);
        sCurBB++;
        if (sCurBB < 0)
            ::SetCursor(&qd.arrow);
        if (sCurBB >= sNumBBCur)
            sCurBB = 0;
        sSpinTime = ::TickCount() + 2;
        inTask->task.vblCount = sSpinCount;
#ifndef powerc
        (void)SetA5(oldA5);
#endif
    }
}
```

[Next](CBeachBall.h.md)[Previous](CApp.h.md)

