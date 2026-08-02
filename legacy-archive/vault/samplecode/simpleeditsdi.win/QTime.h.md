---
title: simpleeditsdi.win
apple_id: DTS10000795
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/simpleeditsdi.win/Listings/QTime_h.html
archived_at: '2026-07-26T19:52:38.040968Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [simpleeditsdi.win](simpleeditsdi.win.md)


[Next](resource.h.md)[Previous](QTime.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTime.h

```c
 /*
    File:       QTime.c

    Written by: Keith Gurganus

    Copyright:  © 1997 by Apple Computer, Inc., all rights reserved.
*/

#ifndef __QTIME__
#define __QTIME__

typedef struct{
    char            filename[255];
    Movie           theMovie;
    MovieController theMC;
    Boolean         movieOpened;
    HWND            theHwnd;
}MovieStuff;

BOOL OpenMovie(HWND hwnd, MovieStuff *movieStuff);
void CloseMovie(MovieStuff *movieStuff);
OSErr SaveMovie(MovieStuff *movieStuff);
OSErr SaveAsMovie(MovieStuff *movieStuff);
BOOL GetFile(char *fileName);

ComponentResult EditCut(MovieController mc);
ComponentResult EditCopy(MovieController mc);
ComponentResult EditPaste(MovieController mc);
ComponentResult EditClear(MovieController mc);
ComponentResult EditUndo(MovieController mc);
ComponentResult EditSelectAll(Movie movie, MovieController mc) ;

void SetWindowTitle(HWND hWnd, unsigned char *theFullPath);
void GetFileNameFromFullPath(unsigned char *theFullPath, unsigned char *fileName);
#endif
```

[Next](resource.h.md)[Previous](QTime.c.md)

