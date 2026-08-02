---
title: usher
apple_id: DTS10001057
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/usher/Listings/sources_AppSupport_h.html
archived_at: '2026-07-26T19:53:08.495184Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [usher](usher.md)


[Next](sources-MovieSourcing.c.md)[Previous](sources-AppSupport.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# sources/AppSupport.h

```swift
/*
    File:       AppSupport.h

    Copyright:  © 2000-2001 by Apple Computer, Inc., all rights reserved.

*/

#ifndef __APPSUPPORT__
#define __APPSUPPORT__

#include "QTSSampleCodeUtils.h"

// ---------------------------------------------------------------------------
//      D E F I N I T I O N S
// ---------------------------------------------------------------------------

// ---------------------------------------------------------------------------
//      A P P   U T I L S
// ---------------------------------------------------------------------------

void GenericAlertUser(short inStringList, short inStringIndex, short inErrorCode);
void GenericAlertUserString(Str255 inMessage, short inErrorCode);
void GenericErrorAlert(OSErr inErrorCode);

enum  {
    kProcessMessageFlag_Log         = 0x00000001,
    kProcessMessageFlag_ShowDialog  = 0x00000002

};

void ProcessUserMessage(SInt32 inFlags, const char* format, ...);

// ---------------------------------------------------------------------------
//      G L O B A L S
// ---------------------------------------------------------------------------

struct AppGlobals {
    Boolean     inBackground;
    Boolean     useAppearanceCalls;
    Point       defaultWindowOffset;
    UInt32      sleepTime;
    GrafPtr     safetyPort;
    Logger      log;

    Boolean     exitNow;
};
typedef struct AppGlobals AppGlobals;

extern AppGlobals gGlobals;

#define AppGlobals_SetInBackground(_b)          (gGlobals.inBackground = (_b))
#define AppGlobals_GetInBackground()            (gGlobals.inBackground)

#define AppGlobals_SetUseAppearance(_b)         (gGlobals.useAppearanceCalls = (_b))
#define AppGlobals_GetUseAppearance()           (gGlobals.useAppearanceCalls)

#define AppGlobals_SetDefaultOffset(_v, _h)     {gGlobals.defaultWindowOffset.v = (_v); gGlobals.defaultWindowOffset.h = (_h);}
#define AppGlobals_GetDefaultOffset()           (gGlobals.defaultWindowOffset)
#define AppGlobals_GetDefaultOffsetPtr()        (&(gGlobals.defaultWindowOffset))

#define AppGlobals_SetExitNow(_b)               (gGlobals.exitNow = (_b))
#define AppGlobals_GetExitNow()                 (gGlobals.exitNow)

#define AppGlobals_SetSleepTime(_st)            (gGlobals.sleepTime = (_st))
#define AppGlobals_GetSleepTime()               (gGlobals.sleepTime)

#define AppGlobals_GetAppSignature()            (kAppSignature)

#define AppGlobals_GetLog()                     (gGlobals.log)

#endif /* __APPSUPPORT__ */
```

[Next](sources-MovieSourcing.c.md)[Previous](sources-AppSupport.c.md)

