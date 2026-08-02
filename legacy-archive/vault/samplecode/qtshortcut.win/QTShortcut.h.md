---
title: qtshortcut.win
apple_id: DTS10000876
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtshortcut.win/Listings/QTShortcut_h.html
archived_at: '2026-07-26T19:52:46.958953Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtshortcut.win](qtshortcut.win.md)


[Next](Document%20Revision%20History.md)[Previous](QTShortcut.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTShortcut.h

```c
//////////
//
//  File:       QTShortcut.h
//
//  Contains:   Sample code for creating a shortcut to a QuickTime movie.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      11/20/98    rtm     first file
//
//////////

#include <Movies.h>
#include <Script.h>
#include "QTUtilities.h"

//////////
//
// compiler flags
//
//////////

#define TESTING_SHORTCUTS       1           // compiler flag for our test shell

//////////
//
// constants
//
//////////

// type and creator for the shortcut file
#define kShortcutFileType       MovieFileType
#define kShortcutFileCreator    FOUR_CHAR_CODE('TVOD')

//////////
//
// function prototypes
//
//////////

OSErr                           QTShortCut_CreateShortcutMovieFile (Handle theDataRef, OSType theDataRefType, FSSpecPtr theFSSpecPtr);
OSErr                           QTShortCut_WriteHandleToFile (Handle theHandle, FSSpecPtr theFSSpecPtr);
```

[Next](Document%20Revision%20History.md)[Previous](QTShortcut.c.md)

