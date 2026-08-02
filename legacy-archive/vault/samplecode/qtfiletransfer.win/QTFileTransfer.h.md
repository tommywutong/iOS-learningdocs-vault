---
title: qtfiletransfer.win
apple_id: DTS10000858
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtfiletransfer.win/Listings/QTFileTransfer_h.html
archived_at: '2026-07-26T19:52:46.301334Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtfiletransfer.win](qtfiletransfer.win.md)


[Next](Document%20Revision%20History.md)[Previous](QTFileTransfer.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTFileTransfer.h

```c
//////////
//
//  File:       QTFileTransfer.h
//
//  Contains:   Sample code for transferring a file asynchronously from a web server.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      11/11/98    rtm     first file
//
//////////

#include <FixMath.h>
#include <Movies.h>
#include <QuickTimeComponents.h>
#include <Script.h>

#include <string.h>

#define TESTING_FTP_TRANSFER    1           // compiler flag for our test shell

//////////
//
// constants
//
//////////

#define kDataBufferSize         1024*10     // the size, in bytes, of our data buffer

// type and creator for the transferred file
#define kTransFileType          FOUR_CHAR_CODE('TEXT')
#define kTransFileCreator       FOUR_CHAR_CODE('CWIE')

//////////
//
// function prototypes
//
//////////

OSErr                           QTFileTrans_CopyRemoteFileToLocalFile (char *theURL, FSSpecPtr theFSSpecPtr);
PASCAL_RTN void                 QTFileTrans_ReadDataCompletionProc (Ptr theRequest, long theRefCon, OSErr theErr);
PASCAL_RTN void                 QTFileTrans_WriteDataCompletionProc (Ptr theRequest, long theRefCon, OSErr theErr);
void                            QTFileTrans_CloseDownHandlers (void);
```

[Next](Document%20Revision%20History.md)[Previous](QTFileTransfer.c.md)

