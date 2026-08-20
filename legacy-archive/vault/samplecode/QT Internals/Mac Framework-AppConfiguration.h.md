---
title: QT Internals
apple_id: DTS10000848
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QT_Internals/Listings/Mac_Framework_AppConfiguration_h.html
archived_at: '2026-07-18T03:21:22.300379Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QT Internals](QT%20Internals.md)


[Next](Mac%20Framework-MacApplication.c.md)[Previous](DTSQTUtilities.h.md)

# Mac Framework/AppConfiguration.h

```c
/*
    File:       AppConfiguration.h

    Contains:   Values for configuration purposes inside the actual application.
    Written by: DTS

    Copyright:  © 1994-1995 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

       <1>      12/30/94    khs     first file

*/


#pragma once


#include <Movies.h>


// TOOLBOX CONSTANTS
enum eBasicConstants {
    kWNEDefaultSleep = 0,                                                               // WNE Sleep time value
    kDefaultSysBeep = 10
};

enum eWindowConstants {
    kDefaultX = 100,
    kDefaultY = 100
};


// MOVIE AND MOVIE CONTROLLER CONSTANTS
enum eMCValues {
    kMCFlags =  0L | mcTopLeftMovie | mcWithBadge           // default MC setup
};

enum eMovieValues {
    kMaxMilliSecToUse = 0L                                          // MoviesTask value, 0 indicates as much as possible (serve all movies,
                                                                                    // define other millisecond values if needed.
};
```

[Next](Mac%20Framework-MacApplication.c.md)[Previous](DTSQTUtilities.h.md)

