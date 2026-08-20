---
title: qtbroadcast
apple_id: DTS10001046
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-06'
source_url: https://developer.apple.com/library/archive/samplecode/qtbroadcast/Listings/Application_Files_ComApplication_h.html
archived_at: '2026-07-26T19:53:05.194983Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtbroadcast](qtbroadcast.md)


[Next](Application%20Files-ComResource.h.md)[Previous](Application%20Files-ComApplication.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# Application Files/ComApplication.h

```c
//////////
//
//  File:       ComApplication.h
//
//  Contains:   Functions that could be overridden in a specific application.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      11/05/99    rtm     first file; based on earlier sample code
//
//////////

#pragma once

//////////
//
// header files
//
//////////

#ifndef __QUICKTIMEVR__
#include <QuickTimeVR.h>
#endif

#ifndef __TEXTUTILS__
#include <TextUtils.h>
#endif

#ifndef __SCRIPT__
#include <Script.h>
#endif

#ifndef __MEDIAHANDLERS__
#include <MediaHandlers.h>
#endif

#ifndef __MOVIES__
#include <Movies.h>
#endif

#ifndef __RESOURCES__
#include <Resources.h>
#endif

#ifndef __SOUND__
#include <Sound.h>
#endif

#ifndef __SOUNDCOMPONENTS__
#include <SoundComponents.h>
#endif

#ifndef __SOUNDSPROCKET__
#include <SoundSprocket.h>
#endif

#ifndef __TEXTUTILS__
#include <TextUtils.h>
#endif

#include <string.h>
#include <stdlib.h>

#if TARGET_OS_MAC
#ifndef __APPLEEVENTS__
#include <AppleEvents.h>
#endif
#include "MacFramework.h"
#endif

#if TARGET_OS_WIN32
#include "WinFramework.h"
#endif

#ifndef __QTUtilities__
#include "QTUtilities.h"
#endif

#include "ComResource.h"

//////////
//
// constants
//
//////////

//////////
//
// structures
//
//////////

// application-specific data
typedef struct ApplicationDataRecord {
    MediaHandler                fSpriteHandler;     // the media handler for the sprite track
} ApplicationDataRecord, *ApplicationDataPtr, **ApplicationDataHdl;

//////////
//
// function prototypes
//
//////////

#if TARGET_OS_MAC
void                    QTApp_InstallAppleEventHandlers (void);
PASCAL_RTN OSErr        QTApp_HandleOpenApplicationAppleEvent (const AppleEvent *theMessage, AppleEvent *theReply, long theRefcon);
PASCAL_RTN OSErr        QTApp_HandleOpenDocumentAppleEvent (const AppleEvent *theMessage, AppleEvent *theReply, long theRefcon);
PASCAL_RTN OSErr        QTApp_HandlePrintDocumentAppleEvent (const AppleEvent *theMessage, AppleEvent *theReply, long theRefcon);
PASCAL_RTN OSErr        QTApp_HandleQuitApplicationAppleEvent (const AppleEvent *theMessage, AppleEvent *theReply, long theRefcon);
#endif  // TARGET_OS_MAC

// the other function prototypes are in the file MacFramework.h or WinFramework.h
```

[Next](Application%20Files-ComResource.h.md)[Previous](Application%20Files-ComApplication.c.md)

