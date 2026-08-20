---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CADebugMacros_cpp.html
archived_at: '2026-07-26T19:54:11.650569Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CAException.h.md)[Previous](PublicUtility-CABufferList.h.md)

# PublicUtility/CADebugMacros.cpp

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
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

[Next](PublicUtility-CAException.h.md)[Previous](PublicUtility-CABufferList.h.md)

