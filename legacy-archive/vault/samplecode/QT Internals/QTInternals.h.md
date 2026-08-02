---
title: QT Internals
apple_id: DTS10000848
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QT_Internals/Listings/QTInternals_h.html
archived_at: '2026-07-18T03:21:22.963807Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QT Internals](QT%20Internals.md)


[Next](Document%20Revision%20History.md)[Previous](QTInternals.c.md)

# QTInternals.h

```c
/*
    File:       QTInternals.h

    Contains:   Functions dealing with dumping internal movie information.

    Written by: DTS

    Copyright:  © 1995 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

       <1>      1/4/95  khs     first file

*/

#pragma once


// INCLUDES
#include <Movies.h>
#include <stdio.h>

#ifdef __MWERKS__
#include <sioux.h>
#endif

// TYPEDEFS & DATA STRUCTURES

// FUNCTION PROTOTYPES
void ShowMovieTrackInfo(Movie theMovie);                                                        // display track information about movies
void ShowMovieVideoInfo(Movie theMovie);                                                        // display video related information
void ShowMovieSoundInfo(Movie theMovie);                                                        // display sound related information
void ShowGlobalMovieInfo(Movie theMovie);                                                       // display global information related to the movie and system
void ShowTextTrackInformation(Movie theMovie);                                          // dump text track information
pascal long QTUCountKeySamples(Movie theMovie, OSType theMediaType);        // get key samples
```

[Next](Document%20Revision%20History.md)[Previous](QTInternals.c.md)

