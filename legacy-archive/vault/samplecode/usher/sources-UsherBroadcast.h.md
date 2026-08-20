---
title: usher
apple_id: DTS10001057
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/usher/Listings/sources_UsherBroadcast_h.html
archived_at: '2026-07-26T19:53:08.992621Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [usher](usher.md)


[Next](sources-UsherCarbon.r.md)[Previous](sources-UsherBroadcast.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# sources/UsherBroadcast.h

```swift
/*
    File:       UsherBroadcast.h

    Copyright:  © 2000-2001 by Apple Computer, Inc., all rights reserved.

*/

#ifndef __USHERBROADCAST__
#define __USHERBROADCAST__

#include "SimplePres.h"

// ---------------------------------------------------------------------------
//      D E F I N I T I O N S
// ---------------------------------------------------------------------------

#define kUsherBroadcastSignature            FOUR_CHAR_CODE('ubrd')

#define kUsherBroadcastMaxWindows           10
#define kMaxPresNameLength                  255

#define kUsherBroadcastMaxSourceHandlers        5

struct UsherBroadcastSourceHandlerInfo {
    void        *handler;
    Boolean     handlerWantsNotifications;
    char        pad[3];

};
typedef struct UsherBroadcastSourceHandlerInfo UsherBroadcastSourceHandlerInfo;

struct UsherBroadcast {
    OSType                  signature;  // this is always a constant so we can identify our structure
    struct UsherBroadcast   *next;

    SimplePresRecord        *simplePres;
    Boolean                 disposing;

    QTSStatusParams         statusParams;
    char                    presName[kMaxPresNameLength+1];
    TimeBase                presTimeBase;
    TimeScale               presTimeScale;

    // ----- sourcers
    UInt32                  numSourceHandlers;
    UsherBroadcastSourceHandlerInfo sourceHandlers[kUsherBroadcastMaxSourceHandlers];
    Boolean                 someHandlerWantsNotifications;

    // ------ dealing with ui
    UInt32                  numWindows;
    WindowPtr               windowList[kUsherBroadcastMaxWindows];
};
typedef struct UsherBroadcast UsherBroadcast;

// ---------------------------------------------------------------------------
//      P R O T O T Y P E S
// ---------------------------------------------------------------------------

// ----- new / dispose -----

OSErr UsherBroadcast_NewFromFile(const FSSpec *inFileSpec, GWorldPtr inGWorld, GDHandle inGD,
                        const Rect *inPresBox, UsherBroadcast **outBroadcast);

void UsherBroadcast_Dispose(UsherBroadcast *inBroadcast);

// ----- commands -----

long UsherBroadcast_GetMenuCommand(UsherBroadcast *inBroadcast, long inMenuResult, void **outCommandParams);
OSErr UsherBroadcast_DoCommand(UsherBroadcast *inBroadcast, long inCommand, void *inCommandParams);

void UsherBroadcast_Idle(UsherBroadcast *inBroadcast);
OSErr UsherBroadcast_Start(UsherBroadcast *inBroadcast);
OSErr UsherBroadcast_Stop(UsherBroadcast *inBroadcast);

// ----- get /set  -----

QTSStatusParams *UsherBroadcast_GetStatusParams(UsherBroadcast *inBroadcast);

OSErr UsherBroadcast_GetInfo(UsherBroadcast *inBroadcast, OSType inSelector, void *ioParams);
OSErr UsherBroadcast_SetInfo(UsherBroadcast *inBroadcast, OSType inSelector, void *ioParams);

QTSPresentation UsherBroadcast_GetQTSPresentation(UsherBroadcast *inBroadcast);

// ----- infrastructure stuff -----

OSErr UsherBroadcast_AddWindow(UsherBroadcast *inBroadcast, WindowPtr inWindow);
void UsherBroadcast_RemoveWindow(UsherBroadcast *inBroadcast, WindowPtr inWindow);

OSErr UsherBroadcast_AddSourceHandler(UsherBroadcast *inBroadcast, void *inSourceHandler);

// ----- global calls -----

void UsherBroadcast_CleanUp(void);  // dispose of everything
void UsherBroadcast_IdleAll(void);  // idle everyone

long UsherBroadcast_GetNumBroadcasts(void);

#endif /* __USHERBROADCAST__ */
```

[Next](sources-UsherCarbon.r.md)[Previous](sources-UsherBroadcast.c.md)

