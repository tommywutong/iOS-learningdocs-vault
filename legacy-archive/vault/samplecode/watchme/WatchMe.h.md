---
title: watchme
apple_id: DTS10001080
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/watchme/Listings/WatchMe_h.html
archived_at: '2026-07-26T19:53:34.676099Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [watchme](watchme.md)


[Next](Document%20Revision%20History.md)[Previous](WatchMe.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# WatchMe.h

```c
//////////
//
//  File:       WatchMe.h
//
//  Contains:   Application-specific code for WatchMe shell.
//              This file is used for BOTH MacOS and Windows.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      07/23/98    rtm     first file
//
//////////

#include "ComApplication.h"
#include <Processes.h>
#include <stdlib.h>

// compiler flags

#define TESTING_ON_NONCD        0

// constants

#ifndef MAX_PATH
#define MAX_PATH                512                 // maximum size of a path name
#endif

#define kWM_URLSeparator        (char)'/'           // URL path separator

#if TARGET_OS_MAC
#define kWM_PathSeparator       (char)':'           // on Macintosh, the path separator is ':'
#elif TARGET_OS_WIN32
#define kWM_PathSeparator       (char)'\\'          // on Windows, the path separator is '\\'
#endif

// function prototypes

void                            WatchMe_ConvertRelativeToAbsoluteURL (Handle theURLHandle, long theRefCon);
char *                          WatchMe_GetLaunchVolumeName (void);
static char *                   WatchMe_FSSpecToFullPath (const FSSpec *theFSSpec);
static char *                   WatchMe_FullPathToURL(char *thePath);
static char *                   WatchMe_EncodeURL (char *theURL);
static Boolean                  WatchMe_IsAbsoluteURL (char *theURL);
static OSErr                    WatchMe_FSpGetFullPath (const FSSpec *spec, short *fullPathLength, Handle *fullPath);
```

[Next](Document%20Revision%20History.md)[Previous](WatchMe.c.md)

