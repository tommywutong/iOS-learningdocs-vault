---
title: vrflattenmovie
apple_id: DTS10001023
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrflattenmovie/Listings/VRFlatten_c.html
archived_at: '2026-07-26T19:52:57.121544Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrflattenmovie](vrflattenmovie.md)


[Next](VRFlatten.h.md)[Previous](vrflattenmovie.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# VRFlatten.c

```c
//////////
//
//  File:       VRFlatten.c
//
//  Contains:   Code showing how to call the QTVR file flattener.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 2000 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      05/11/00    rtm     first file
//
//////////

#include "VRFlatten.h"

//////////
//
// QTVRUtils_FlattenMovieForStreaming
// Export the specified a QuickTime VR movie, using the QTVR flattener movie export component.
//
//////////

OSErr QTVRUtils_FlattenMovieForStreaming (Movie theMovie, FSSpecPtr theFSSpecPtr)
{
    ComponentDescription        myCompDesc;
    MovieExportComponent        myExporter = NULL;
    long                        myFlags = createMovieFileDeleteCurFile | showUserSettingsDialog | movieFileSpecValid;
    ComponentResult             myErr = badComponentType;

    // find and open a movie export component that can flatten a QuickTime VR movie file
    myCompDesc.componentType = MovieExportType;
    myCompDesc.componentSubType = MovieFileType;
    myCompDesc.componentManufacturer = FOUR_CHAR_CODE('vrwe');
    myCompDesc.componentFlags = 0;
    myCompDesc.componentFlagsMask = 0;
    myExporter = OpenComponent(FindNextComponent(NULL, &myCompDesc));
    if (myExporter == NULL)
        goto bail;

    // use the default progress procedure
    SetMovieProgressProc(theMovie, (MovieProgressUPP)-1L, 0);

    // export the movie into a file
    myErr = ConvertMovieToFile( theMovie,               // the movie to convert
                                NULL,                   // all tracks in the movie
                                theFSSpecPtr,           // the output file
                                MovieFileType,          // the output file type
                                sigMoviePlayer,         // the output file creator
                                smSystemScript,         // the script
                                NULL,                   // no resource ID to be returned
                                myFlags,                // conversion flags
                                myExporter);            // QTVR flattener movie export component

bail:
    // close the movie export component
    if (myExporter != NULL)
        CloseComponent(myExporter);

    return((OSErr)myErr);
}
```

[Next](VRFlatten.h.md)[Previous](vrflattenmovie.md)

