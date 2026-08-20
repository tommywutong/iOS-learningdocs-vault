---
title: qtcapture
apple_id: DTS10000805
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtcapture/Listings/Common_Files_WinPrefix_h.html
archived_at: '2026-07-26T19:52:38.777496Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtcapture](qtcapture.md)


[Next](QTCapture.c.md)[Previous](Common%20Files-WinFramework.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

Relevant replacement documents include:

- [http://developer.apple.com/documentation/QuickTime/Conceptual/QTKitCaptureProgrammingGuide/Introduction/Introduction.html](https://developer.apple.com/documentation/QuickTime/Conceptual/QTKitCaptureProgrammingGuide/Introduction/Introduction.html)
- [http://developer.apple.com/samplecode/MYRecorder/index.html#//apple_ref/doc/uid/DTS10004263](https://developer.apple.com/samplecode/MYRecorder/index.html#//apple_ref/doc/uid/DTS10004263)
- [http://developer.apple.com/samplecode/QTCompressionOptionsWindow/index.html#//apple_ref/doc/uid/DTS10004627](https://developer.apple.com/samplecode/QTCompressionOptionsWindow/index.html#//apple_ref/doc/uid/DTS10004627)
- [http://developer.apple.com/samplecode/StillMotion/index.html#//apple_ref/doc/uid/DTS10004355](https://developer.apple.com/samplecode/StillMotion/index.html#//apple_ref/doc/uid/DTS10004355)

# Common Files/WinPrefix.h

```c
//////////
//
//  File:       WinPrefix.h
//
//  Contains:   Prefix file for our Windows projects.
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

#pragma once

#ifndef __Prefix_File__
#define __Prefix_File__

//////////
//
// header files
//
//////////

#if !defined(_MSC_VER)
#include <Win32Headers.mch>
#else
#include <ConditionalMacros.h>
#endif

//////////
//
// compiler macros
//
//////////

#ifndef PASCAL_RTN
#define PASCAL_RTN
#endif

#define SetPortDialogPort(dialog)           MacSetPort(dialog)
#define GetDialogPort(dialog)               ((CGrafPtr)dialog)

//////////
//
// compiler pragmas
//
//////////

// if we're being compiled by Microsoft Visual C++, turn off some warnings
#if defined(_MSC_VER) && !defined(__MWERKS__)
    #pragma warning(disable:4068)       // ignore unknown pragmas
    #pragma warning(disable:4244)       // ignore conversion from "long" to "short", possible loss of data
    #pragma warning(disable:4761)       // ignore integral size mismatch in argument: conversion supplied
    #pragma warning(disable:4129)       // ignore 'p': unrecognized character escape sequence
    #pragma warning(disable:4229)       // ignore anachronism used: modifiers on data are ignored
#endif

#endif  // __Prefix_File__
```

[Next](QTCapture.c.md)[Previous](Common%20Files-WinFramework.h.md)

