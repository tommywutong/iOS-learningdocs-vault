---
title: qtvectors
apple_id: DTS10001060
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtvectors/Listings/QTVectors_h.html
archived_at: '2026-07-26T19:53:10.363466Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtvectors](qtvectors.md)


[Next](Document%20Revision%20History.md)[Previous](QTVectors.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTVectors.h

```c
//////////
//
//  File:       QTVectors.h
//
//  Contains:   QuickTime vector support for QuickTime movies.
//
//  Written by: Tim Monroe
//              parts modeled on VectorSample code by Tom Dowdy(?).
//
//  Copyright:  © 1997 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      11/03/97    rtm     first file
//
//////////

#include "ComApplication.h"

#if TARGET_OS_MAC
#include "MacFramework.h"
#endif

#if TARGET_OS_WIN32
#include "WinFramework.h"
#endif

#define kVectorSavePrompt               "Save New Curve Movie As:"
#define kVectorSaveMovieFileName        "shapes.mov"

#define kSizeOfSizeAndTagFields         sizeof(long)*2
#define kSizeOfZeroAtomHeader           0

// parameters for QTVectors_CreateVectorMovie
#define kUseRawDataStream               0
#define kUseCurveUtilities              1

// function prototypes
void                        QTVectors_CreateVectorMovie (UInt32 theBuildAtomMethod);
```

[Next](Document%20Revision%20History.md)[Previous](QTVectors.c.md)

