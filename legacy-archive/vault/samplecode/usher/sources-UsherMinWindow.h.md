---
title: usher
apple_id: DTS10001057
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/usher/Listings/sources_UsherMinWindow_h.html
archived_at: '2026-07-26T19:53:09.083077Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [usher](usher.md)


[Next](sources-UsherMinWindow.r.md)[Previous](sources-UsherMinWindow.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# sources/UsherMinWindow.h

```
/*
    File:       UsherMinWindow.h

    Copyright:  © 2000-2001 by Apple Computer, Inc., all rights reserved.

*/

#ifndef __USHERMINWINDOW__
#define __USHERMINWINDOW__

#ifndef forRez

// ---------------------------------------------------------------------------
//      D E F I N I T I O N S
// ---------------------------------------------------------------------------

#define kSignature_UsherMinWind     FOUR_CHAR_CODE('wmin')

// ---------------------------------------------------------------------------
//      P R O T O T Y P E S
// ---------------------------------------------------------------------------

OSErr UsherMinWind_New(Boolean inUseAlt, WindowPtr *outWindow);
void UsherMinWind_Close(WindowPtr inWindow);

void UsherMinWind_Idle(WindowPtr inWindow);

void UsherMinWind_GrowWindow(WindowPtr inWindow, EventRecord *inEvent);
void UsherMinWind_DoContentClick(WindowPtr inWindow, EventRecord *inEvent);
void UsherMinWind_ActivateWindow(WindowPtr inWindow, Boolean inBecomingActive);
void UsherMinWind_Draw(WindowPtr inWindow);

long UsherMinWind_GetMenuCommand(WindowPtr inWindow, long inMenuResult, void **outCommandParams);
OSErr UsherMinWind_DoCommand(WindowPtr inWindow, long inCommand, void *inCommandParams);

OSErr UsherMinWind_HandleMessage(WindowPtr inWindow, long inMessage, void *inMessageParams);

#endif  /* forRez */

// ---------------------------------------------------------------------------
//      R E Z   D E F I N I T I O N S       (also used by .r file)
// ---------------------------------------------------------------------------

#define kRezIDBase_UsherMinWindow       5000

#define rStringList_UsherMinWind        kRezIDBase_UsherMinWindow
    #define rUsherMinWindString_DefaultName         1
    #define rUsherMinWindString_StatusLabel         2
    #define rUsherMinWindString_DataRateLabel       3
    #define rUsherMinWindString_SPStateLabel        4
    #define rUsherMinWindString_SPStateUnknownTemplate  5
    #define rUsherMinWindString_TimeLabel           6
    #define rUsherMinWindString_StoredMovieLabel    7
    #define rUsherMinWindString_TimeRemainingLabel  8
    #define rUsherMinWindString_FrameRateLabel      9

#define rDLOG_UsherMinWindow            kRezIDBase_UsherMinWindow
#define rDITL_UsherMinWindow            kRezIDBase_UsherMinWindow
#define rDLOG_UsherMinWindowLarge           kRezIDBase_UsherMinWindow+1
#define rDITL_UsherMinWindowLarge           kRezIDBase_UsherMinWindow+1
    #define rMinWindDITLItem_VideoArea          1
    #define rMinWindDITLItem_StartButton        2
    #define rMinWindDITLItem_PresStateLabel     3
    #define rMinWindDITLItem_PresStateText      4
    #define rMinWindDITLItem_DataRateLabel      5
    #define rMinWindDITLItem_DataRateText       6
    #define rMinWindDITLItem_StatusLabel        7
    #define rMinWindDITLItem_StatusText         8
    #define rMinWindDITLItem_TimeLabel          9
    #define rMinWindDITLItem_TimeText           10
    #define rMinWindDITLItem_StoredMovieLabel           11
    #define rMinWindDITLItem_StoredMovieText            12
    #define rMinWindDITLItem_TimeRemainingLabel         13
    #define rMinWindDITLItem_TimeRemainingText          14
    #define rMinWindDITLItem_SkipToNextButton           15
    #define rMinWindDITLItem_FrameRateLabel     16
    #define rMinWindDITLItem_FrameRateText      17

#endif /* __USHERMINWINDOW__ */
```

[Next](sources-UsherMinWindow.r.md)[Previous](sources-UsherMinWindow.c.md)

