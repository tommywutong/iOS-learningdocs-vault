---
title: aurioTouch
apple_id: DTS40007770
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/samplecode/aurioTouch/Listings/PublicUtility_CADebugMacros_cpp.html
archived_at: '2026-07-18T03:28:53.165905Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [aurioTouch](aurioTouch.md)


[Next](PublicUtility-CAXException.cpp.md)[Previous](PublicUtility-CAXException.h.md)

# PublicUtility/CADebugMacros.cpp

```c
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 CADebugMacros.h
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

[Next](PublicUtility-CAXException.cpp.md)[Previous](PublicUtility-CAXException.h.md)

