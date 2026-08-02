---
title: MyQuickTimeApp
apple_id: DTS10000330
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MyQuickTimeApp/Listings/MyApplication_h.html
archived_at: '2026-07-18T03:16:43.623186Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyQuickTimeApp](MyQuickTimeApp.md)


[Next](Document%20Revision%20History.md)[Previous](MyApplication.c.md)

# MyApplication.h

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

//  Set the following according to your application's needs
#define     kNEWDOCATSTARTUP    1   //  set to 1 if MyNew called at startup.  0 is not called.
#define     kMYEVENTDEF         2   //  2 is per window.  1 is once per eventloop.  0 is never.
#define     kMYIDLEDEF          2   //  2 is per window.  1 is once per eventloop.  0 is never.

//  Menus - Add any custom menus here starting from NEXTID (Use ResEdit on .rsrc file).
#define     kMENU_NEXTID        160
#define     kMENU_NEXT1stITEM   1

//  Alert Resources - Add Alerts starting from ALERT_NEXT
#define     kALERT_NEXT         160

/* ------------------------------------------------------------------------- */

OSErr       MyInitialize(void);
Boolean     MyEvent(WindowPtr theWindow, EventRecord *myEvent);
void        MyIdle(WindowPtr theWindow);
OSErr       MyDoCommand(short theMenu, short theItem);
void        MyDoKeyDown(EventRecord *myEvent);
void        MyDraw(WindowPtr theWindow);
void        MyFinishup(void);
long        MyYieldTime(long message);
void        MyInContent(WindowPtr foundWindow, Point where);
void        MyZoomWindow(WindowPtr foundWindow, short windowPart);
void        MyAdjustMenus(void);

void        MyNew(void);
void        MyOpen(FSSpec *theFSS);
void        MyClose(void);
void        MySave(void);
void        MySaveAs(void);
void        MyPageSetup(void);
void        MyPrint(void);

void        MyUndo(void);
void        MyCut(void);
void        MyCopy(void);
void        MyPaste(void);
void        MyClear(void);
void        MySelectAll(void);
```

[Next](Document%20Revision%20History.md)[Previous](MyApplication.c.md)

