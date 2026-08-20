---
title: QT Internals
apple_id: DTS10000848
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QT_Internals/Listings/Mac_Framework_MacApplication_h.html
archived_at: '2026-07-18T03:21:22.439431Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QT Internals](QT%20Internals.md)


[Next](Mac%20Framework-MacFramework.c.md)[Previous](Mac%20Framework-MacApplication.c.md)

# Mac Framework/MacApplication.h

```
/*
    File:       MacApplication.h

    Contains:   Functions that could be overridden in a specific application.

    Written by: DTS

    Copyright:  © 1994-1995 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

       <1>      12/21/94    khs     first file

*/


#pragma once


// APPLICATION SPECIFIC ENUMS
// MENUS
enum eAppMenus {
    mTesting = 131
};

enum eTestingMenu {
    iMovieInfo =1, iTrackInfo, iVideoInfo, iSoundInfo, iTextInfo
};
```

[Next](Mac%20Framework-MacFramework.c.md)[Previous](Mac%20Framework-MacApplication.c.md)

