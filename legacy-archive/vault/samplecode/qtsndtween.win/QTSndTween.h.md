---
title: qtsndtween.win
apple_id: DTS10000917
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtsndtween.win/Listings/QTSndTween_h.html
archived_at: '2026-07-26T19:52:51.753240Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtsndtween.win](qtsndtween.win.md)


[Next](Document%20Revision%20History.md)[Previous](QTSndTween.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTSndTween.h

```c
//////////
//
//  File:       QTSndTween.h
//
//  Contains:   Sound tweening support for QuickTime movies.
//
//  Written by: Tim Monroe
//              based largely on the tween sample code in the QuickTime 2.5 Developers Guide.
//
//  Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      04/10/98    rtm     first file; revised to personal coding style
//
//////////

#include <Movies.h>
#include <Endian.h>

#define kTweenTimeScale                 600
#define k3DDuration                     5000

// IDs for the various tween entries we want to use
#define kSoundTweenID                   1

// function prototypes
OSErr                       QTSndTween_AddTweenTrackToMovie (Movie theMovie);
OSErr                       QTSndTween_AddTweenEntryToSample (QTAtomContainer theSample, QTAtomID theID, QTAtomType theType, void *theData, long theDataSize);
OSErr                       QTSndTween_AddTweenEntryToInputMap (QTAtomContainer theInputMap, long theRefIndex, long theID, OSType theType, char *theName);
```

[Next](Document%20Revision%20History.md)[Previous](QTSndTween.c.md)

