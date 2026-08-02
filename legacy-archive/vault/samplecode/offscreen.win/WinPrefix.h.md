---
title: offscreen.win
apple_id: DTS10000772
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/offscreen.win/Listings/WinPrefix_h.html
archived_at: '2026-07-18T03:29:54.226351Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [offscreen.win](offscreen.win.md)


[Next](Document%20Revision%20History.md)[Previous](resource.h.md)

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
#define DEBUG                           0
#define ONLY_ENCODED_SCRIPTS            0
#define PROFILING_ON                    0
#undef QD3D_NO_DIRECTDRAW

#define QD3D_AVAIL                      !TARGET_CPU_68K
#define SOUNDSPROCKET_AVAIL             TARGET_CPU_PPC
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

[Next](Document%20Revision%20History.md)[Previous](resource.h.md)

