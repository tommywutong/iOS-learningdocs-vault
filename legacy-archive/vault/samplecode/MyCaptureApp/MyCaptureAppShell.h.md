---
title: MyCaptureApp
apple_id: DTS10000327
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MyCaptureApp/Listings/MyCaptureAppShell_h.html
archived_at: '2026-07-18T03:16:33.355500Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyCaptureApp](MyCaptureApp.md)


[Next](MyHeaders.c.md)[Previous](MyCaptureAppShell.c.md)

# MyCaptureAppShell.h

```
/*
    File:       MyApplication Shell (2.0).h

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

#define     topLeft(r)      (((Point *) &(r))[0])
#define     botRight(r)     (((Point *) &(r))[1])

#define     kMENUBAR                    128
#define     kMENU_APPLEID               128

#define     kMENU_FILEID                129
#define     kMENU_FILENEW               1
#define     kMENU_FILECLOSE             2
#define     kMENU_FILEQUIT              4

#define     kMENU_SETTINGSID            130

#define     kMENU_RESIZEID              131

#define     kMENU_SPECIALID             132
#define     kMENU_SPECIALPLAYTHRU       1
#define     kMENU_SPECIALSEPARATEFILES  2

#define     kMENU_RECORDID              133
#define     kMENU_RECORDSTART           1

#define     kALERT_ABOUT                128
#define     kALERT_ERROR                129

/* ------------------------------------------------------------------------- */

void            main(void);

void            Initialize(void);
void            DoCommand(long mResult);
void            AdjustMenus(void);
void            Finishup(void);

pascal OSErr    AEOpenHandler(AppleEvent *messagein, AppleEvent *reply, long refIn);
pascal OSErr    AEOpenDocHandler(AppleEvent *messagein, AppleEvent *reply, long refIn);
pascal OSErr    AEPrintHandler(AppleEvent *messagein, AppleEvent *reply, long refIn);
pascal OSErr    AEQuitHandler(AppleEvent *messagein, AppleEvent *reply, long refIn);
```

[Next](MyHeaders.c.md)[Previous](MyCaptureAppShell.c.md)

