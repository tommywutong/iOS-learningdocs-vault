---
title: qtinfo
apple_id: DTS10000782
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtinfo/Listings/QTInfo_h.html
archived_at: '2026-07-26T19:52:32.864899Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtinfo](qtinfo.md)


[Next](Document%20Revision%20History.md)[Previous](QTInfo.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTInfo.h

```c
//////////
//
//  File:       QTInfo.h
//
//  Contains:   Sample code for working with QuickTime movie information.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 2000 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      04/23/00    rtm     first file
//
//////////

#pragma once

//////////
//
// header files
//
//////////

#include "ComApplication.h"

//////////
//
// compiler flags
//
//////////

//////////
//
// constants
//
//////////

// resource ID for Edit Annotations dialog box
#define kEditTextResourceID         548
#define kEditTextItemOK             1
#define kEditTextItemCancel         2
#define kEditTextItemEditBox        3
#define kEditTextItemEditLabel      4

#define kTextKindsResourceID        2000
#define kTextKindsFullName          1
#define kTextKindsCopyright         2
#define kTextKindsInformation       3

//////////
//
// function prototypes
//
//////////

Boolean                     QTInfo_MovieHasPreview (Movie theMovie);
Boolean                     QTInfo_MovieHasPoster (Movie theMovie);

OSErr                       QTInfo_SetPreviewToSelection (Movie theMovie, MovieController theMC);
OSErr                       QTInfo_SetSelectionToPreview (Movie theMovie, MovieController theMC);
OSErr                       QTInfo_ClearPreview (Movie theMovie, MovieController theMC);

OSErr                       QTInfo_GoToPosterFrame (Movie theMovie, MovieController theMC);
OSErr                       QTInfo_SetPosterToFrame (Movie theMovie, MovieController theMC);

OSErr                       QTInfo_MakeFilePreview (Movie theMovie, short theRefNum, ICMProgressProcRecordPtr theProgressProc);

Boolean                     QTInfo_IsRefNumOfResourceFork (short theRefNum);

Boolean                     QTInfo_EditAnnotation (Movie theMovie, OSType theType);

void                        QTInfo_TextHandleToPString (Handle theHandle, Str255 theString);
void                        QTInfo_PStringToTextHandle (Str255 theString, Handle theHandle);
```

[Next](Document%20Revision%20History.md)[Previous](QTInfo.c.md)

