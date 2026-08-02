---
title: vrmovies
apple_id: DTS10001030
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/vrmovies/Listings/Common_Files_MacPrefix_h.html
archived_at: '2026-07-26T19:53:00.454425Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [vrmovies](vrmovies.md)


[Next](Common%20Files-QTUtilities.c.md)[Previous](Common%20Files-MacFramework.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# Common Files/MacPrefix.h

```c
//////////
//
//  File:       MacPrefix.h
//
//  Contains:   Prefix file for our Macintosh projects.
//
//  Written by: Tim Monroe
//
//  Copyright:  © 1999 by Apple Computer, Inc., all rights reserved.
//
//  Change History (most recent first):
//     <2>      10/19/02    era     building Mach-O
//     <1>      11/11/99    rtm     first file
//
//////////

#ifndef __Prefix_File__
#define __Prefix_File__

//////////
//
// header files
//
//////////

#define TARGET_API_MAC_CARBON           1

#ifdef __MWERKS__
#ifdef __MACH__
    #include <MSL MacHeadersMach-O.h>
#else
    #include <ConditionalMacros.h>
#endif
#endif

//////////
//
// compiler macros
//
//////////

#ifndef PASCAL_RTN
#define PASCAL_RTN                      pascal
#endif

#if TARGET_CPU_PPC
#define SOUNDSPROCKET_AVAIL             1
#else
#define SOUNDSPROCKET_AVAIL             0
#endif

#endif // __Prefix_File__
```

[Next](Common%20Files-QTUtilities.c.md)[Previous](Common%20Files-MacFramework.h.md)

