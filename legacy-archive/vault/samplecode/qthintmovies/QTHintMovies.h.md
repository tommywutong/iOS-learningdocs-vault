---
title: qthintmovies
apple_id: DTS10000865
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qthintmovies/Listings/QTHintMovies_h.html
archived_at: '2026-07-26T19:52:46.580375Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qthintmovies](qthintmovies.md)


[Next](Document%20Revision%20History.md)[Previous](QTHintMovies.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTHintMovies.h

```c
//////////
//
//  File:       QTHintMovies.h
//
//  Contains:   Sample code for adding hint tracks to a QuickTime movie.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      10/16/98    rtm     first file
//
//////////

#include <Files.h>
#include <Movies.h>
#include <QuickTimeComponents.h>
#include <Script.h>
#include <TextUtils.h>

#include <string.h>
#include <stdlib.h>

#define TESTING_HINTING         1           // compiler flag for our test shell

//////////
//
// constants
//
//////////

// type and creator for our sample settings preferences file
#define kSettingsFileType       FOUR_CHAR_CODE('Pref')
#define kSettingsFileCreator    FOUR_CHAR_CODE('RTM ')

// the name of our preferences file
#define kSettingsFileName       "HintPrefs.rtm"

//////////
//
// data types
//
//////////

//////////
//
// function prototypes
//
//////////

OSErr                           QTHints_HintMovieUsingToolbox (Movie theMovie, FSSpecPtr theFSSpecPtr);
OSErr                           QTHints_HintMovieUsingExportComponent (Movie theMovie, FSSpecPtr theFSSpecPtr, Boolean thePromptUser);

Track                           QTHints_GetIndHintTrack (Movie theMovie, long theIndex);
Track                           QTHints_GetIndHintedTrack (Track theHintTrack, long theIndex);
Boolean                         QTHints_MovieHasHintTrack (Movie theMovie);

OSErr                           QTHints_GetPrefsFileSpec (FSSpecPtr thePrefsSpecPtr, void *theRefCon);

OSErr                           QTUtils_SaveExporterSettingsInFile (MovieExportComponent theExporter, FSSpecPtr theFSSpecPtr);
OSErr                           QTUtils_GetExporterSettingsFromFile (MovieExportComponent theExporter, FSSpecPtr theFSSpecPtr);
OSErr                           QTUtils_WriteHandleToFile (Handle theHandle, FSSpecPtr theFSSpecPtr);
Handle                          QTUtils_ReadHandleFromFile (FSSpecPtr theFSSpecPtr);
```

[Next](Document%20Revision%20History.md)[Previous](QTHintMovies.c.md)

