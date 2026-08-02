---
title: qtactiontargets.win
apple_id: DTS10001069
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/qtactiontargets.win/Listings/Common_Files_WinPrefix_h.html
archived_at: '2026-07-18T03:30:08.233742Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [qtactiontargets.win](qtactiontargets.win.md)


[Next](QTActionTargets.c.md)[Previous](Common%20Files-WinFramework.h.md)

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

#define GetDialogPort(d)                (GrafPtr)d
#define GetDialogFromWindow(w)          (DialogPtr)w

#endif  // __Prefix_File__
```

[Next](QTActionTargets.c.md)[Previous](Common%20Files-WinFramework.h.md)

