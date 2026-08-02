---
title: qtmoviefromurl.win
apple_id: DTS10000870
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtmoviefromurl.win/Listings/QTMovieFromURL_h.html
archived_at: '2026-07-26T19:52:46.708361Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtmoviefromurl.win](qtmoviefromurl.win.md)


[Next](Document%20Revision%20History.md)[Previous](QTMovieFromURL.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTMovieFromURL.h

```c
//////////
//
//  File:       QTMovieFromURL.h
//
//  Contains:   Sample code for opening a QuickTime movie specified by a URL.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      10/29/98    rtm     first file
//
//////////

#include <Movies.h>

#include <string.h>
#include <stdlib.h>

#define TESTING_OPEN_URL        1               // compiler flag for our test shell

//////////
//
// constants
//
//////////

#define kURLSeparator           (char)'/'       // URL path separator

//////////
//
// function prototypes
//
//////////

Movie                           QTURL_NewMovieFromURL (char *theURL);
char *                          QTURL_GetURLBasename (char *theURL);
```

[Next](Document%20Revision%20History.md)[Previous](QTMovieFromURL.c.md)

