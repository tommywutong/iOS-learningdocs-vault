---
title: MyMultipleMoviesApp
apple_id: DTS10000329
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MyMultipleMoviesApp/Listings/BetterFlattenMovie_h.html
archived_at: '2026-07-18T03:16:39.701340Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyMultipleMoviesApp](MyMultipleMoviesApp.md)


[Next](MyApplication%20Shell%20%282.0%29.c.md)[Previous](BetterFlattenMovie.c.md)

# BetterFlattenMovie.h

```
/*
    File:       BetterFlattenMovie.h

    Contains:   Patched version of FlattenMovie/FlattenMovieData.

    Written by: John Wang

    Copyright:  © 1994 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

        <1>     03/14/94    JW      Re-Created for Universal Headers.

    To Do:

*/

#ifdef THINK_C
#define     applec
#endif

/* ------------------------------------------------------------------------- */

pascal void BetterFlattenMovie(Movie theMovie, long movieFlattenFlags, 
            FSSpec *theFile, OSType creator, ScriptCode scriptTag,
            long createMovieFileFlags, short *resId, const StringPtr resName);

pascal Movie BetterFlattenMovieData(Movie theMovie, long movieFlattenFlags, 
            FSSpec *theFile, OSType creator, ScriptCode scriptTag,
            long createMovieFileFlags);

OSErr CountMoviesInDataFork(FSSpec *theFile, short *count);
OSErr SearchMoviesInDataFork(FSSpec *theFile, short index, long *fileOffset);
```

[Next](MyApplication%20Shell%20%282.0%29.c.md)[Previous](BetterFlattenMovie.c.md)

