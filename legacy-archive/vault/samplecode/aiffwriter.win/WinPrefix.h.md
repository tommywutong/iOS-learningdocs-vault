---
title: aiffwriter.win
apple_id: DTS10000905
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/aiffwriter.win/Listings/WinPrefix_h.html
archived_at: '2026-07-18T03:28:48.764236Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [aiffwriter.win](aiffwriter.win.md)


[Next](Document%20Revision%20History.md)[Previous](SoundOutputDispatch.h.md)

# WinPrefix.h

```c
// WinPrefix.h
// prefix file for our Windows projects

#ifndef __Prefix_File__
#define __Prefix_File__

#if !defined(_MSC_VER)
#include <Win32Headers.mch>
#else
#include <ConditionalMacros.h>
#endif

// Definitions for the project
#define PASCAL_RTN

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

[Next](Document%20Revision%20History.md)[Previous](SoundOutputDispatch.h.md)

