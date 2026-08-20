---
title: ISp SampleOld
apple_id: DTS10000056
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/ISp_SampleOld/Listings/Source_AppleEventHandler_h.html
archived_at: '2026-07-18T03:12:08.701885Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ISp SampleOld](ISp%20SampleOld.md)


[Next](Source-AppShellResources.h.md)[Previous](Source-AppleEventHandler.c.md)

# Source/AppleEventHandler.h

```c
/*
    File:       AppleEventHandler.h

    Contains:   xxx put contents here xxx

    Version:    xxx put version here xxx

    Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.

    File Ownership:

        DRI:                xxx put dri here xxx

        Other Contact:      xxx put other contact here xxx

        Technology:         xxx put technology here xxx

    Writers:

        (BWS)   Brent Schorsch

    Change History (most recent first):

       <SP1>      7/1/99    BWS     first checked in
*/

#ifndef __APPLEEVENTHANDLER__
#define __APPLEEVENTHANDLER__

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Includes

#ifndef __APPLEEVENTS__
#include <AppleEvents.h>
#endif

//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Definitions
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Types
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Variables
//¥ ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ    Public Functions

#ifdef __cplusplus
extern "C" {
#endif

extern void     AppleEventsInit(void);
extern void     AppleEventsShutDown(void);
extern Boolean  AppleEventsGotRequiredParams(const AppleEvent *inEvent);
extern void     AppleEventsRegisterQuitFlag(Boolean *inFlag);

#ifdef __cplusplus
}
#endif

#endif
```

[Next](Source-AppShellResources.h.md)[Previous](Source-AppleEventHandler.c.md)

