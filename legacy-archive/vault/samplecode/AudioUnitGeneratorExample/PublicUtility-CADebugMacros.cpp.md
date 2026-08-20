---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/PublicUtility_CADebugMacros_cpp.html
archived_at: '2026-07-18T02:59:51.384578Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](PublicUtility-CADebugMacros.h.md)[Previous](PublicUtility-CADebugger.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# PublicUtility/CADebugMacros.cpp

```c
/*
 <codex> 
 <abstract>CADebugMacros.h</abstract>
 <\codex>
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

#if TARGET_API_MAC_OSX
void    LogError(const char *fmt, ...)
{
    va_list args;
    va_start(args, fmt);
#if DEBUG
    vprintf(fmt, args);
#endif
    vsyslog(LOG_ERR, fmt, args);
    va_end(args);
}

void    LogWarning(const char *fmt, ...)
{
    va_list args;
    va_start(args, fmt);
#if DEBUG
    vprintf(fmt, args);
#endif
    vsyslog(LOG_WARNING, fmt, args);
    va_end(args);
}
#endif
```

[Next](PublicUtility-CADebugMacros.h.md)[Previous](PublicUtility-CADebugger.h.md)

