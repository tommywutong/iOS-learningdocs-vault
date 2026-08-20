---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CADebugger_cpp.html
archived_at: '2026-07-26T19:54:11.256981Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CAAUMIDIMapManager.cpp.md)[Previous](PublicUtility-CAReferenceCounted.h.md)

# PublicUtility/CADebugger.cpp

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
*/

//=============================================================================
//  Includes
//=============================================================================

#include "CADebugger.h"

//=============================================================================
//  CADebugger
//=============================================================================

#if TARGET_API_MAC_OSX

#include <sys/sysctl.h>
#include <stdlib.h>
#include <unistd.h>

bool CAIsDebuggerAttached(void)
{
    int                 mib[4];
    struct kinfo_proc   info;
    size_t              size;

    mib[0] = CTL_KERN;
    mib[1] = KERN_PROC;
    mib[2] = KERN_PROC_PID;
    mib[3] = getpid();
    size = sizeof(info);
    info.kp_proc.p_flag = 0;

    sysctl(mib, 4, &info, &size, NULL, 0);

    return (info.kp_proc.p_flag & P_TRACED) == P_TRACED;
}

#endif

void    CADebuggerStop(void)
{
    #if CoreAudio_Debug
        #if TARGET_API_MAC_OSX
            if(CAIsDebuggerAttached())
            {
                #if defined(__i386__) || defined(__x86_64__)
                    asm("int3");
                #else
                    __builtin_trap();
                #endif
            }
            else
            {
                abort();
            }
        #else
            __debugbreak();
        #endif
    #endif
}
```

[Next](PublicUtility-CAAUMIDIMapManager.cpp.md)[Previous](PublicUtility-CAReferenceCounted.h.md)

