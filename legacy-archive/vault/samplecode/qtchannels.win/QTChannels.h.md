---
title: qtchannels.win
apple_id: DTS10000854
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtchannels.win/Listings/QTChannels_h.html
archived_at: '2026-07-26T19:52:46.180949Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtchannels.win](qtchannels.win.md)


[Next](Document%20Revision%20History.md)[Previous](QTChannels.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# QTChannels.h

```c
//////////
//
//  File:       QTChannels.h
//
//  Contains:   Sample code for managing items in QuickTime Player's favorites drawer.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//
//     <1>      09/24/99    rtm     first file
//
//////////

#pragma once

//////////
//
// header files
//
//////////

#ifndef __MOVIES__
#include <Movies.h>
#endif

#ifndef __ENDIAN__
#include <Endian.h>
#endif

#ifndef _STRING_H
#include <string.h>
#endif

//////////
//
// constants
//
//////////

#define kIndexOne               1
#define kIndexTwo               2
#define kIndexThree             3

#define kZeroDataLength         0

//////////
//
// function prototypes
//
//////////

OSErr                           QTChan_AddChannelToFavorites (Str255 theChannelName, char *theChannelURL, char *theChannelPictureURL);
OSErr                           QTChan_RemoveChannelFromFavorites (char *theChannelURL);
```

[Next](Document%20Revision%20History.md)[Previous](QTChannels.c.md)

