---
title: MyCaptureApp
apple_id: DTS10000327
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MyCaptureApp/Listings/MyUtils_h.html
archived_at: '2026-07-18T03:16:33.773318Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyCaptureApp](MyCaptureApp.md)


[Next](Document%20Revision%20History.md)[Previous](MyUtils.c.md)

# MyUtils.h

```
/*
    File:       MyUtils.c

    Contains:   Utility functions.

    Written by: John Wang

    Copyright:  © 1994 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

        <1>     04/04/94    JW      Created.

    To Do:

*/

#ifdef THINK_C
#define     applec
#endif

/* ------------------------------------------------------------------------- */

void            ReportWarning(Str255 procStr, long err);
void            ReportFatal(Str255 procStr, long err);
void            GetGlobalWindow(WindowPtr theWindow, Rect *windowRect);

short           readPreferencesFile(void);
short           writePreferencesFile(void);
void            closePreferencesFile(short myRefNum);
```

[Next](Document%20Revision%20History.md)[Previous](MyUtils.c.md)

