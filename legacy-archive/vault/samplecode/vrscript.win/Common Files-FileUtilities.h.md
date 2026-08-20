---
title: vrscript.win
apple_id: DTS10001033
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrscript.win/Listings/Common_Files_FileUtilities_h.html
archived_at: '2026-07-26T19:53:03.365442Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrscript.win](vrscript.win.md)


[Next](Common%20Files-QTUtilities.c.md)[Previous](Common%20Files-FileUtilities.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# Common Files/FileUtilities.h

```c
//////////
//
//  File:       FileUtilities.h
//
//  Contains:   Some utilities for working with pathnames, files, and file specifications.
//              All utilities start with the prefix "FileUtils_".
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      05/27/99    rtm     first file
//
//////////

#pragma once

//////////
//
// header files
//
//////////

#ifndef __FileUtilities__
#define __FileUtilities__

#if defined(_MSC_VER)
#include <windows.h>
#include <winbase.h>
#endif

#if TARGET_OS_WIN32
    #ifndef __QTML__
    #include <QTML.h>
    #endif
#endif

#include <string.h>
#include <stdlib.h>

#ifndef __URLUtilities__
#include "URLUtilities.h"
#endif

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

#define kFileSuffixSeparator        (char)'.'       // file suffix separator
#define kFileSuffixSepString        "."             // file suffix separator as a string

//////////
//
// macros
//
//////////

//////////
//
// function prototypes
//
//////////

OSErr                           FileUtils_MakeFSSpecForPathName (short theVRefNum, long theDirID, char *thePathName, FSSpec *theFSSpec);
OSErr                           FileUtils_MakeFSSpecForAnyFileInDir (Str255 thePathName, FSSpecPtr theFileFSSpec);

static Boolean                  FileUtils_IsFullPathName (char *thePathName);
char *                          FileUtils_GetBaseName (char *thePathName);
char *                          FileUtils_ChangeFileNameSuffix (char *thePathName, char *theNewSuffix);

#endif  // __FileUtilities__
```

[Next](Common%20Files-QTUtilities.c.md)[Previous](Common%20Files-FileUtilities.c.md)

