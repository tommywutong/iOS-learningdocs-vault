---
title: ElectricImageComponent
apple_id: DTS10000888
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2010-05-17'
source_url: https://developer.apple.com/library/archive/samplecode/ElectricImageComponent/Listings/PrefixIncludes_EIComponentWindowsPrefix_h.html
archived_at: '2026-07-18T03:07:40.655582Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ElectricImageComponent](ElectricImageComponent.md)


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

