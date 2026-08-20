---
title: qtcustombutton.win
apple_id: DTS10000856
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtcustombutton.win/Listings/QTCustomButton_h.html
archived_at: '2026-07-26T19:52:46.232746Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtcustombutton.win](qtcustombutton.win.md)


[Next](Document%20Revision%20History.md)[Previous](QTCustomButton.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTCustomButton.h

```c
//////////
//
//  File:       QTCustomButton.h
//
//  Contains:   Header file for displaying and managing the custom button in the controller bar.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      11/25/99    rtm     first file
//
//////////

//////////
//
// header files
//
//////////

#ifndef __MOVIES__
#include <Movies.h>
#endif

//////////
//
// constants
//
//////////

#define kCustomButtonMenuID         1000

#define kItem1Index                 1
#define kItem2Index                 2
#define kItem3Index                 3
#define kSaveItemIndex              kItem3Index

#define kMenuTitle                  ""
#define kItem1Text                  "Beep"
#define kItem2Text                  "About QTShell..."
#define kItem3Text                  "Save"
#define kDividingLine               "-"

#if TARGET_OS_WIN32
#define EnableMenuItem                      EnableItem
#define DisableMenuItem                     DisableItem
#endif

//////////
//
// function prototypes
//
//////////

void                    QTCustom_ShowCustomButton (MovieController theMC);
void                    QTCustom_HandleCustomButtonClick (MovieController theMC, EventRecord *theEvent, long theRefCon);
```

[Next](Document%20Revision%20History.md)[Previous](QTCustomButton.c.md)

