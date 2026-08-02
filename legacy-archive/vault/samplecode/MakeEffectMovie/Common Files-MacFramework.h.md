---
title: MakeEffectMovie
apple_id: DTS10001038
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MakeEffectMovie/Listings/Common_Files_MacFramework_h.html
archived_at: '2026-07-18T03:14:13.370483Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MakeEffectMovie](MakeEffectMovie.md)


[Next](Common%20Files-MacPrefix.h.md)[Previous](Common%20Files-MacFramework.c.md)

# Common Files/MacFramework.h

```c
//////////
//
//
//  File:       MacFramework.h
//
//  Contains:   Basic functions for windows, menus, and similar things.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//     
//     <1>      11/05/99    rtm     first file
//     
//////////

#pragma once


//////////
//     
// header files
//     
//////////

#ifndef __APPLEEVENTS__
#include <AppleEvents.h>
#endif

#ifndef __CONTROLDEFINITIONS__
#include <ControlDefinitions.h>
#endif

#ifndef __CONTROLS__
#include <Controls.h>
#endif

#ifndef __DEVICES__
#include <Devices.h>
#endif

#ifndef __DIALOGS__
#include <Dialogs.h>
#endif

#ifndef __FIXMATH__
#include <FixMath.h>
#endif

#ifndef __FONTS__
#include <Fonts.h>
#endif

#ifndef __MACMEMORY__
#include <MacMemory.h>
#endif

#ifndef __MENUS__
#include <Menus.h>
#endif

#ifndef __PROCESSES__
#include <Processes.h>
#endif

#ifndef __QUICKTIMECOMPONENTS__
#include <QuickTimeComponents.h>
#endif

#ifndef __TOOLUTILS__
#include <ToolUtils.h>
#endif

#ifndef _STDIO_H
#include <stdio.h>
#endif

#ifndef _STRING_H
#include <string.h>
#endif

#include "ComFramework.h"


//////////
//
// constants
//
//////////

#define kEmergencyMemorySize        40*1024L        // size of the block of memory used for our grow zone procedure
#define kExtraStackSpaceSize        32*1024L        // amount of additional stack space
#define kWNEDefaultSleep            0               // WaitNextEvent sleep time
#define kBroughtToFront             3               // number of times to call EventAvail at application startup

// resource IDs for dialogs
#define kAboutBoxID                 128             // dialog ID for About box
#define kAlertErrorID               129             // dialog ID for warning box

// resource ID for string resource containing application's name
#define kAppNameResID               1000
#define kAppNameResIndex            1

#define kDefaultWindowTitle         "\puntitled"            
#define kDefaultWindowRect          {10,10,480,640}         


//////////
//
// function prototypes
//     
//////////

pascal long                 QTFrame_GrowZoneProcedure (Size theBytesNeeded);
void                        QTFrame_HandleEvent (EventRecord *theEvent);
void                        QTFrame_HandleMenuCommand (long theMenuResult);
void                        QTFrame_HandleKeyPress (EventRecord *theEvent);
PASCAL_RTN void             QTFrame_StandardUserItemProcedure (DialogPtr theDialog, short theItem);
PASCAL_RTN Boolean          QTFrame_StandardModalDialogEventFilter (DialogPtr theDialog, EventRecord *theEvent, short *theItemHit);
void                        QTFrame_ShowWarning (Str255 theMessage, OSErr theErr);
```

[Next](Common%20Files-MacPrefix.h.md)[Previous](Common%20Files-MacFramework.c.md)

