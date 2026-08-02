---
title: hacktv.win
apple_id: DTS10000804
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/hacktv.win/Listings/globals_h.html
archived_at: '2026-07-18T03:29:28.205406Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [hacktv.win](hacktv.win.md)


[Next](resource.h.md)[Previous](globals.c.md)

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

[Next](resource.h.md)[Previous](globals.c.md)

