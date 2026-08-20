---
title: qtgraphimp.win
apple_id: DTS10000864
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtgraphimp.win/Listings/QTGraphImp_h.html
archived_at: '2026-07-26T19:52:46.538283Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtgraphimp.win](qtgraphimp.win.md)


[Next](Document%20Revision%20History.md)[Previous](QTGraphImp.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTGraphImp.h

```c
//////////
//
//  File:       QTGraphImp.h
//
//  Contains:   Sample code for using QuickTime's graphic import routines.
//              This file is used for BOTH MacOS and Windows.
//
//  Written by: Tim Monroe
//              Based loosely on the SimpleGIExample.c code written by Apple DTS.
//
//  Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      04/14/98    rtm     first file
//
//////////

//////////
//
// header files
//
//////////

#include <ImageCompression.h>
#include <Movies.h>
#include <OSUtils.h>
#include <QuickTimeComponents.h>
#include <Script.h>
#include <StandardFile.h>

//////////
//
// compiler flags
//
//////////

// do we use a data-flushing procedure?
#define USE_FLUSH_PROC              1

//////////
//
// constants
//
//////////

#if USE_FLUSH_PROC
#define kBufferSize                 codecMinimumDataSize
#else
#define kBufferSize                 (500 * 1024)
#endif

#define kImageFileCreator           FOUR_CHAR_CODE('ogle')

//////////
//
// function prototypes
//
//////////

void                            QTGraphImp_OpenImageFileAndDisplay (FSSpecPtr theFSSpecPtr);
void                            QTGraphImp_SaveCompressedImageIntoDiskFile (FSSpecPtr theFSSpecPtr);
void                            QTGraphImp_SaveCompressedImage (GWorldPtr theWorld, FSSpec *theFile);
PASCAL_RTN OSErr                QTGraphImp_DataUnloadProc (Ptr theData, long theBytesNeeded, long theRefCon);
OSErr                           QTGraphImp_ExportGWorldToFile (GWorldPtr theWorld, FSSpec *theFile, OSType theType);
OSErr                           QTGraphImp_GetAvailableExportTypes (GraphicsImportComponent theImporter);
OSErr                           QTGraphImp_ExportImageFile (GraphicsImportComponent theImporter);
```

[Next](Document%20Revision%20History.md)[Previous](QTGraphImp.c.md)

