---
title: MyCaptureApp
apple_id: DTS10000327
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MyCaptureApp/Listings/MySGStuff_h.html
archived_at: '2026-07-18T03:16:33.674569Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyCaptureApp](MyCaptureApp.md)


[Next](MyUtils.c.md)[Previous](MySGStuff.c.md)

# MySGStuff.h

```
/*
    File:       MyApplication.h

    Contains:   My Application Shell.

    Written by: John Wang

    Copyright:  © 1994 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

        <1>     03/14/94    JW      Re-Created for Universal Headers.

    To Do:

*/

#ifdef THINK_C
#define     applec
#endif

#define     kMAXCHANNELS        5
#define     STR_PREFSNAME       128

/* ------------------------------------------------------------------------- */

long        MyInitialize(void);
void        MyFinishup(void);
void        MyIdle(void);
long        MyDoCommand(short theMenu, short theItem);
long        MyYieldTime(long message);
void        MyAdjustMenus(void);

void        MyNew(void);
void        MyClose(void);

void        MySettings(short item);
void        MyResize(short item);
void        MySpecial(short item);
void        MyRecord(void);
void        MyDrag(WindowPtr theWindow, Point where);
void        MyUpdate(WindowPtr theWindow);
long        MyUpdateChannels(WindowPtr theWindow);

Boolean     GetCustomSize(short *width, short *height);

void        GetText(DialogPtr theDialog, short item, Str255 myStr);
void        SetText(DialogPtr theDialog, short item, Str255 myStr);
```

[Next](MyUtils.c.md)[Previous](MySGStuff.c.md)

