---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/PublicUtility_CADebugger_cpp.html
archived_at: '2026-07-18T02:59:51.688746Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](PublicUtility-CADebugger.h.md)[Previous](PublicUtility-CAByteOrder.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# PublicUtility/CADebugger.cpp

```c
/*
 <codex> 
 <abstract>CADebugger.h</abstract>
 <\codex>
*/
//=============================================================================
//  Includes
//=============================================================================

#include "CADebugger.h"

#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <CoreAudio/CoreAudioTypes.h>
#else
    #include <CoreAudioTypes.h>
#endif

//  on X, use the Unix routine, otherwise use Debugger()
#if TARGET_API_MAC_OSX
    #include <signal.h>
#endif

//=============================================================================
//  CADebugger
//=============================================================================

void    CADebuggerStop()
{
    #if CoreAudio_Debug
        #if TARGET_API_MAC_OSX
            raise(SIGINT);
        #else
            __debugbreak();
        #endif
    #endif
}
```

[Next](PublicUtility-CADebugger.h.md)[Previous](PublicUtility-CAByteOrder.h.md)

