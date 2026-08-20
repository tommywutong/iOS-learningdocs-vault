---
title: qtreadwritejpeg
apple_id: DTS10000873
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtreadwritejpeg/Listings/QTReadWriteJPEG_h.html
archived_at: '2026-07-26T19:52:46.827097Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtreadwritejpeg](qtreadwritejpeg.md)


[Next](Document%20Revision%20History.md)[Previous](QTReadWriteJPEG.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTReadWriteJPEG.h

```swift
//////////
//
//  File:       QTReadWriteJPEG.h
//
//  Contains:   Sample code for compressing and decompressing JPEG images.
//
//  Written by: Michael Marinkovich and Guillermo Ortiz
//  Revised by: Tim Monroe
//              Based heavily on the existing "JPEG Sample" code.
//
//  Copyright:  © 1996-1998 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      04/27/98    rtm     first file
//
//////////

//////////
//
// header files
//
//////////

#include <FixMath.h>
#include <ImageCompression.h>
#include <Movies.h>
#include <QuickTimeComponents.h>
#include <StandardFile.h>

//////////
//
// constants
//
//////////

#define kImageFileCreator       FOUR_CHAR_CODE('ogle')
#define kBufferSize             codecMinimumDataSize        // data unload buffer size

#define kSaveImagePrompt        "Save compressed image as:"
#define kSaveImageFileName      "Untitled.jpg"
#define kWindowTitle            "Photo - JPEG"

// JFIF (JPEG) markers
enum {
    kSOFMarker                  = 0xC0,                     // start Of Frame N
    kSOFMarker2                 = 0xC2,
    kDHTMarker                  = 0xC4,                     // DHT Marker
    kDACMarker                  = 0xCC,                     // DAC

    kRSTOMarker                 = 0xD0,                     // RSTO marker
    kSOIMarker                  = 0xD8,                     // image start marker
    kEOIMarker                  = 0xD9,                     // image end marker
    kSOSMarker                  = 0xDA,                     // SOS marker
    kDQTMarker                  = 0xDB,                     // DQT marker

    kAPPOMarker                 = 0xE0,                     // APPO marker
    kCommentMarker              = 0xFE,                     // comment marker

    kStartMarker                = 0xFF                      // marker loacted after this byte
};

//////////
//
// data types
//
//////////

// a record to hold info about the JPEG data while we're loading it from disk
struct DLDataRec
{
    long                        fRefNum;                    // ref number of current file
    long                        fFileLength;
    Ptr                         fOrigPtr;                   // address of start of buffer
    Ptr                         fEndPtr;                    // address of end of buffer
};
typedef struct DLDataRec DLDataRec;
typedef DLDataRec *DLDataPtr, **DLDataHnd;

//////////
//
// function prototypes
//
//////////

void                            QTJPEG_PromptUserForJPEGFileAndDisplay (void);
OSErr                           QTJPEG_ReadJPEG (FSSpec theFSSpec, CGrafPtr *theGWorld);
OSErr                           QTJPEG_ConvertJPEG (Handle image, CGrafPtr *newWorld);
OSErr                           QTJPEG_ReadJPEGHeader (short theRefNum, ImageDescriptionHandle theDesc, Rect *theRect);
UInt8                           QTJPEG_FindNextMarker (long theRefNum);
OSErr                           QTJPEG_HandleAPPOMarker (UInt8 theMarker, long theRefNum, ImageDescriptionHandle theDesc, Boolean *readingExtension);
OSErr                           QTJPEG_HandleSOFMarker (long theRefNum, ImageDescriptionHandle theDesc, Boolean readingExtension);
void                            QTJPEG_HandleSOSMarker (long theRefNum);
UInt8                           QTJPEG_ReadByte (short theRefNum);
UInt16                          QTJPEG_ReadWord (short theRefNum);
void                            QTJPEG_SkipLength (long theRefNum);
OSErr                           QTJPEG_NewJPEGWorld (GWorldPtr *theWorld, short theDepth, Rect theRect);
OSErr                           QTJPEG_SaveJPEG (GWorldPtr theWorld);
PASCAL_RTN OSErr                QTJPEG_DataUnloadProc (Ptr theData, long theBytesNeeded, long theRefCon);
PASCAL_RTN OSErr                QTJPEG_DataLoadingProc (Ptr *theData, long theBytesNeeded, long theRefCon);
```

[Next](Document%20Revision%20History.md)[Previous](QTReadWriteJPEG.c.md)

