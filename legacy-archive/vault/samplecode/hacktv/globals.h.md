---
title: hacktv
apple_id: DTS10000802
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/hacktv/Listings/globals_h.html
archived_at: '2026-07-18T03:29:28.702779Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [hacktv](hacktv.md)


[Next](hacktv.r.md)[Previous](globals.c.md)

# globals.h

```c
/*
    File:       Globals.h

    Contains:   HackTV application globals

    Copyright:  © 1992-1998 by Apple Computer, Inc.
*/

#ifndef _APP_GLOBALS_
#define _APP_GLOBALS_

#include <QTML.h>
#include <Menus.h>
#include <Printing.h>
#include <QuickTimeComponents.h>

//----------------------------------------------------------------------
// Defines

// Dialog IDs
enum
{
    kAboutDLOGID = 128,
    kMonitorDLOGID,
    kMovieHasBeenRecordedAlertID
};

//-----------------------------------------------------------------------
// Globals
extern Boolean                  gQuitFlag;
extern SeqGrabComponent         gSeqGrabber;
extern SGChannel                gVideoChannel;
extern SGChannel                gSoundChannel;
extern WindowPtr                gMonitor;
extern Rect                     gActiveVideoRect;
extern PicHandle                gMonitorPICT;
extern Boolean                  gFullSize;
extern Boolean                  gHalfSize;
extern Boolean                  gQuarterSize;
extern THPrint                  gPrintRec;
extern ICMAlignmentProcRecord   gSeqGrabberAlignProc;
extern Boolean                  gRecordVideo;
extern Boolean                  gRecordSound;
extern Boolean                  gSplitTracks;

#endif
```

[Next](hacktv.r.md)[Previous](globals.c.md)

