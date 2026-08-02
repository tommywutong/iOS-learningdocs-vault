---
title: qtaddeffectseg.win
apple_id: DTS10000832
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/qtaddeffectseg.win/Listings/AddEffectSegment_h.html
archived_at: '2026-07-26T19:52:39.492489Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtaddeffectseg.win](qtaddeffectseg.win.md)


[Next](Document%20Revision%20History.md)[Previous](AddEffectSegment.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# AddEffectSegment.h

```c
//////////
//
//  File:       AddEffectSegment.h
//
//  Contains:   Sample code for adding a visual effect to a segment of a movie.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      05/05/99    rtm     first file; ole!
//
//////////

//////////
//
// header files
//
//////////

#include <Movies.h>
#include <Sound.h>
#include <Endian.h>
#include <ImageCodec.h>
#include <MediaHandlers.h>

//////////
//
// compiler flags
//
//////////

#define USES_MAKE_IMAGE_DESC_FOR_EFFECT 0       // use MakeImageDescriptionForEffect (QT 4.0 and later)
#define COPY_MOVIE_MEDIA                1       // 0 == effect source track references original media; 1 == copy media

//////////
//
// constants
//
//////////

// effects sources names
#define kSourceOneName                  FOUR_CHAR_CODE('srcA')
#define kSourceTwoName                  FOUR_CHAR_CODE('srcB')
#define kSourceThreeName                FOUR_CHAR_CODE('srcC')
#define kSourceNoneName                 FOUR_CHAR_CODE('srcZ')

//////////
//
// function prototypes
//
//////////

OSErr                       QTEffSeg_AddEffectToMovieSegment (Movie theMovie, OSType theEffectType, long theNumSources, TimeValue theStartTime, TimeValue theDuration);
QTAtomContainer             QTEffSeg_CreateEffectDescription (OSType theEffectName, OSType theSourceName1, OSType theSourceName2);
OSErr                       QTEffSeg_AddTrackReferenceToInputMap (QTAtomContainer theInputMap, Track theTrack, Track theSrcTrack, OSType theSrcName);
ImageDescriptionHandle      QTEffSeg_MakeSampleDescription (OSType theEffectType, short theWidth, short theHeight);
short                       QTEffSeg_GetFrontmostTrackLayer (Movie theMovie, OSType theTrackType);
```

[Next](Document%20Revision%20History.md)[Previous](AddEffectSegment.c.md)

