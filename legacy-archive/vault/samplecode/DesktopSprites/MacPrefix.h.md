---
title: DesktopSprites
apple_id: DTS10001066
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/DesktopSprites/Listings/MacPrefix_h.html
archived_at: '2026-07-18T03:06:45.887776Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DesktopSprites](DesktopSprites.md)


[Next](QTSprites.c.md)[Previous](ImageCompressionUtilities.h.md)

# MacPrefix.h

```
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
//     
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

#define TARGET_API_MAC_CARBON 1

// no need to set these if above is set
//#define ACCESSOR_CALLS_ARE_FUNCTIONS 1
//#define OPAQUE_TOOLBOX_STRUCTS 1

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

[Next](QTSprites.c.md)[Previous](ImageCompressionUtilities.h.md)

