---
title: echoTouch - Using the Voice Processing I/O audio unit
apple_id: TP40017575
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-11-29'
source_url: https://developer.apple.com/library/archive/samplecode/echoTouch/Listings/PublicUtility_CADebugMacros_cpp.html
archived_at: '2026-07-18T03:29:07.726757Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [echoTouch - Using the Voice Processing I/O audio unit](echoTouch%20-%20Using%20the%20Voice%20Processing%20I-O%20audio%20unit.md)


[Next](PublicUtility-CAStreamBasicDescription.h.md)[Previous](main.m.md)

# PublicUtility/CADebugMacros.cpp

```c
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 TPart of CoreAudio Utility Classes.
*/

#include "CADebugMacros.h"
#include <stdio.h>
#include <stdarg.h>
#if TARGET_API_MAC_OSX
    #include <syslog.h>
#endif

#if DEBUG
#include <stdio.h>

void    DebugPrint(const char *fmt, ...)
{
    va_list args;
    va_start(args, fmt);
    vprintf(fmt, args);
    va_end(args);
}
#endif // DEBUG

void    LogError(const char *fmt, ...)
{
    va_list args;
    va_start(args, fmt);
#if DEBUG
    vprintf(fmt, args);
#endif
#if TARGET_API_MAC_OSX
    vsyslog(LOG_ERR, fmt, args);
#endif
    va_end(args);
}

void    LogWarning(const char *fmt, ...)
{
    va_list args;
    va_start(args, fmt);
#if DEBUG
    vprintf(fmt, args);
#endif
#if TARGET_API_MAC_OSX
    vsyslog(LOG_WARNING, fmt, args);
#endif
    va_end(args);
}
```

[Next](PublicUtility-CAStreamBasicDescription.h.md)[Previous](main.m.md)

