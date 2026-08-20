---
title: SlideShowImporter.win
apple_id: DTS10000902
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SlideShowImporter.win/Listings/PrefixIncludes_WinPrefix_h.html
archived_at: '2026-07-18T03:24:48.705850Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SlideShowImporter.win](SlideShowImporter.win.md)


[Next](Resources-SlideShowImport.r.md)[Previous](PrefixIncludes-SlideShowImporterWin32Config.h.md)

# PrefixIncludes/WinPrefix.h

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

#ifndef QD3D_AVAIL
#define QD3D_AVAIL                      !TARGET_CPU_68K
#endif
#ifndef SOUNDSPROCKET_AVAIL
#define SOUNDSPROCKET_AVAIL             TARGET_CPU_PPC
#endif
#ifndef PASCAL_RTN
#define PASCAL_RTN
#endif

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

[Next](Resources-SlideShowImport.r.md)[Previous](PrefixIncludes-SlideShowImporterWin32Config.h.md)

