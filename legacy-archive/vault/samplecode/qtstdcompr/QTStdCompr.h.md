---
title: qtstdcompr
apple_id: DTS10000879
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtstdcompr/Listings/QTStdCompr_h.html
archived_at: '2026-07-26T19:52:48.088734Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtstdcompr](qtstdcompr.md)


[Next](Document%20Revision%20History.md)[Previous](QTStdCompr.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTStdCompr.h

```c
//////////
//
//  File:       QTStdCompr.h
//
//  Contains:   Sample code for using QuickTime's standard image compression dialog routines.
//
//  Written by: Tim Monroe
//              Based on existing code by Apple Developer Technical Support, which was itself
//              based on the code in Chapter 3 of Inside Macintosh: QuickTime Components.
//
//  Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      04/22/98    rtm     first file
//
//////////

//////////
//
// header files
//
//////////

#include <ImageCompression.h>
#include <Movies.h>
#include <QuickTimeComponents.h>
#include <StandardFile.h>

#include "QTUtilities.h"

//////////
//
// constants
//
//////////

#define kImageFileCreator               FOUR_CHAR_CODE('ogle')
#define kSaveMoviePrompt                "Save compressed image as:"
#define kSaveMovieFileName              "Untitled.mov"
#define kButtonTitle                    "Defaults"

//////////
//
// function prototypes
//
//////////

void                            QTStdCompr_PromptUserForImageFileAndCompress (void);
void                            QTStdCompr_PromptUserForDiskFileAndSaveCompressed (Handle theHandle, ImageDescriptionHandle theDesc);
void                            QTStdCompr_InstallExtendedProcs (ComponentInstance theComponent, long theRefCon);
void                            QTStdCompr_RemoveExtendedProcs (void);
PASCAL_RTN Boolean              QTStdCompr_FilterProc (DialogPtr theDialog, EventRecord *theEvent, short *theItemHit, long theRefCon);
PASCAL_RTN short                QTStdCompr_ButtonProc (DialogPtr theDialog, short theItemHit, void *theParams, long theRefCon);
```

[Next](Document%20Revision%20History.md)[Previous](QTStdCompr.c.md)

