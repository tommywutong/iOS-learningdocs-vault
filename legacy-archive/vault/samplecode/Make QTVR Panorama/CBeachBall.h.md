---
title: Make QTVR Panorama
apple_id: DTS10000339
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Make_QTVR_Panorama/Listings/CBeachBall_h.html
archived_at: '2026-07-18T03:14:24.837594Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Make QTVR Panorama](Make%20QTVR%20Panorama.md)


[Next](CKeyFilters.cp.md)[Previous](CBeachBall.cp.md)

# CBeachBall.h

```c
/*
    Implements an interrupt time spinning cursor

    Created 29 Jan 1996 by EGH

    Copyright © 1996, Apple Computer, Inc. All rights reserved.
*/

#pragma once

#include <Retrace.h>

#pragma options align=mac68k

struct Acur
{
    short n;        // Number of cursors ("frames of film")
    short index;    //  Next frame to show <for internal use>
    short frame1;   // 'CURS' resource id for frame #1
    short fill1;    // <for internal use>
    short frame2;   // 'CURS' resource id for frame #2
    short fill2;    // <for internal use>
    short frameN;   // 'CURS' resource id for frame #N
    short fillN;    // <for internal use>
};
typedef struct Acur acur,*acurPtr,**acurHandle;

typedef struct
{
    VBLTask task;
    long a5;
} VBLTaskNA5;

#pragma options align=reset

class CBeachBall
{
public:

    static void InitBeachBall();

    static void SpinBeachBall();

    static void StartSpinningTask(
        short inCount);
    static void StopSpinningTask();
#ifdef powerc
    static void SpinTask(
        VBLTaskNA5 *inTask);
#else
    static void SpinTask(
        VBLTaskNA5 *inTask : __D0);
#endif

private:

    static short sNumBBCur;
    static Cursor *sBBCursors;
    static short sCurBB;
    static UInt32 sSpinTime;
    static short sSpinCount;
    static VBLTaskNA5 *sSpinTask;
};
```

[Next](CKeyFilters.cp.md)[Previous](CBeachBall.cp.md)

