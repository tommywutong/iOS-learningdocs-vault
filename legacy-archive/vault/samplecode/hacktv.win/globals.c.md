---
title: hacktv.win
apple_id: DTS10000804
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/hacktv.win/Listings/globals_c.html
archived_at: '2026-07-18T03:29:28.168514Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [hacktv.win](hacktv.win.md)


[Next](globals.h.md)[Previous](common.h.md)

# globals.c

```c
/*
    File:       Globals.c

    Contains:   HackTV application globals

    Copyright:  © 1992-1998 by Apple Computer, Inc.
*/

#include <QTML.h>
#include <Menus.h>
#include <Printing.h>
#include <QuickTimeComponents.h>

//-----------------------------------------------------------------------
// Globals

Boolean                 gQuitFlag = 0;
SeqGrabComponent        gSeqGrabber=0;
SGChannel               gVideoChannel=0;
SGChannel               gSoundChannel=0;
WindowPtr               gMonitor=0;
Rect                    gActiveVideoRect;
PicHandle               gMonitorPICT=0;
Boolean                 gFullSize;
Boolean                 gHalfSize;
Boolean                 gQuarterSize;
THPrint                 gPrintRec;
ICMAlignmentProcRecord  gSeqGrabberAlignProc;
Boolean                 gRecordVideo = 1;
Boolean                 gRecordSound = 1;
Boolean                 gSplitTracks = 0;
```

[Next](globals.h.md)[Previous](common.h.md)

