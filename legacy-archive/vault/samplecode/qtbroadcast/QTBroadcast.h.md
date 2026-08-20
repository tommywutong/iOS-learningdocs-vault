---
title: qtbroadcast
apple_id: DTS10001046
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-06'
source_url: https://developer.apple.com/library/archive/samplecode/qtbroadcast/Listings/QTBroadcast_h.html
archived_at: '2026-07-26T19:53:05.729491Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtbroadcast](qtbroadcast.md)


[Next](Document%20Revision%20History.md)[Previous](QTBroadcast.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTBroadcast.h

```c
//////////
//
//  File:       QTBroadcast.h
//
//  Contains:   Code for broadcasting QuickTime movies.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 2001 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      04/11/01    rtm     first file
//
//////////

//////////
//
// header files
//
//////////

#include "ComApplication.h"

#if TARGET_OS_MAC
#include "MacFramework.h"
#endif

#if TARGET_OS_WIN32
#include "WinFramework.h"
#endif

#ifndef __QUICKTIMESTREAMING__
#include <QuickTimeStreaming.h>
#endif

//////////
//
// compiler defines
//
//////////

#if TARGET_OS_WIN32
#define GetPortBounds(port,rectptr)         (*(rectptr)=port->portRect)
#endif

//////////
//
// constants
//
//////////

#define kMonitorDLOGID                      1000
#define kMonitorUserItemID                  1
#define kMonitorButtonID                    2

#define kDefaultPresTimeScale               600

//////////
//
// function prototypes
//
//////////

OSErr                           QTBC_Init (void);
void                            QTBC_Stop (void);

OSErr                           QTBC_SetupPresentation (void);

OSErr                           QTBC_StartBroadcasting (void);
OSErr                           QTBC_PauseBroadcasting (void);
OSErr                           QTBC_StopBroadcasting (void);

static PASCAL_RTN ComponentResult
                                QTBC_NotificationProc (ComponentResult theErr, OSType theNotificationType, void *theNotificationParams, void *theRefCon);

DialogPtr                       QTBC_CreateMonitorWindow (void);
PASCAL_RTN void                 QTBC_UserItemProcedure (DialogPtr theDialog, short theItem);
void                            QTBC_HandleMonitorWindowEvents (DialogPtr theDialog, short theItemHit);
```

[Next](Document%20Revision%20History.md)[Previous](QTBroadcast.c.md)

