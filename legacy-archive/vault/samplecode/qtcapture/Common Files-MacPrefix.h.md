---
title: qtcapture
apple_id: DTS10000805
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtcapture/Listings/Common_Files_MacPrefix_h.html
archived_at: '2026-07-26T19:52:38.547668Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtcapture](qtcapture.md)


[Next](Common%20Files-QTUtilities.c.md)[Previous](Common%20Files-MacFramework.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

Relevant replacement documents include:

- [http://developer.apple.com/documentation/QuickTime/Conceptual/QTKitCaptureProgrammingGuide/Introduction/Introduction.html](https://developer.apple.com/documentation/QuickTime/Conceptual/QTKitCaptureProgrammingGuide/Introduction/Introduction.html)
- [http://developer.apple.com/samplecode/MYRecorder/index.html#//apple_ref/doc/uid/DTS10004263](https://developer.apple.com/samplecode/MYRecorder/index.html#//apple_ref/doc/uid/DTS10004263)
- [http://developer.apple.com/samplecode/QTCompressionOptionsWindow/index.html#//apple_ref/doc/uid/DTS10004627](https://developer.apple.com/samplecode/QTCompressionOptionsWindow/index.html#//apple_ref/doc/uid/DTS10004627)
- [http://developer.apple.com/samplecode/StillMotion/index.html#//apple_ref/doc/uid/DTS10004355](https://developer.apple.com/samplecode/StillMotion/index.html#//apple_ref/doc/uid/DTS10004355)

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

#define TARGET_API_MAC_CARBON           1

#include <ConditionalMacros.h>

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

