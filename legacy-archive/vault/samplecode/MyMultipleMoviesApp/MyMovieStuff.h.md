---
title: MyMultipleMoviesApp
apple_id: DTS10000329
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MyMultipleMoviesApp/Listings/MyMovieStuff_h.html
archived_at: '2026-07-18T03:16:40.305436Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyMultipleMoviesApp](MyMultipleMoviesApp.md)


[Next](Document%20Revision%20History.md)[Previous](MyMovieStuff.c.md)

# MyMovieStuff.h

```
/*
    File:       MyApplication.h

    Contains:   My Application Shell.

    Written by: John Wang

    Copyright:  © 1994 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

        <1>     03/14/94    JW      Re-Created for Universal Headers.

    To Do:

*/

#ifdef THINK_C
#define     applec
#endif

struct WindowInfo {
    //  Document info.
    FSSpec          theFSSpec;      //  FSSpec for document.
    short           refNum;         //  refNum for document.

    //  Current movie playing info.
    Movie           theMovie;       //  Current movie.  nil if none.
    MovieController theMC;          //  Current movie controller.  nil if none.
    Str255          moviename;      //  Name of movie if exists.
    short           resId;          //  resource id of movie in document. -1 if no resId.
    long            movieOffset;    //  offset to movie resource atom in data fork.  -1 if no offset.
};
typedef     struct WindowInfo WindowInfo, *WindowInfoPtr, **WindowInfoHandle;

/* ------------------------------------------------------------------------- */

void        adjustMoviesMenu(WindowPtr theWindow);
void        SelectThisMovie(short item);
void        getNewMovie(Movie *theMovie, Str255 *movieName);
void        Mac_AddMovieResAtom(short *docRefNum, FSSpec *docFSSpec);
void        Mac_AddMovieAll(short *docRefNum, FSSpec *docFSSpec);
void        Cross_AddMovieAll(short *docRefNum, FSSpec *docFSSpec);
void        Both_AddMovieAll(short *docRefNum, FSSpec *docFSSpec);
```

[Next](Document%20Revision%20History.md)[Previous](MyMovieStuff.c.md)

