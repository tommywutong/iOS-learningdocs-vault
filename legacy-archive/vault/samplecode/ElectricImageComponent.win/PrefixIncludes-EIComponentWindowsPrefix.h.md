---
title: ElectricImageComponent.win
apple_id: DTS10000889
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2004-01-23'
source_url: https://developer.apple.com/library/archive/samplecode/ElectricImageComponent.win/Listings/PrefixIncludes_EIComponentWindowsPrefix_h.html
archived_at: '2026-07-18T03:07:36.365385Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ElectricImageComponent.win](ElectricImageComponent.win.md)


[Next](PrefixIncludes-ImportExampleLinked.h.md)[Previous](PrefixIncludes-EIComponentWindows.r.md)

# PrefixIncludes/EIComponentWindowsPrefix.h

```
// EIComponentWindowsPrefix.h
// prefix file for our Windows projects

// Definitions for the project
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
```

[Next](PrefixIncludes-ImportExampleLinked.h.md)[Previous](PrefixIncludes-EIComponentWindows.r.md)

