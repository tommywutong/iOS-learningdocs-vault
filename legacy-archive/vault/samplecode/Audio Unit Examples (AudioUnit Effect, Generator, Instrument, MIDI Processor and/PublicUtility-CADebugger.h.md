---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CADebugger_h.html
archived_at: '2026-07-26T19:54:11.281129Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CADebugMacros.h.md)[Previous](PublicUtility-CAVectorUnitTypes.h.md)

# PublicUtility/CADebugger.h

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
*/

#if !defined(__CADebugger_h__)
#define __CADebugger_h__

//=============================================================================
//  Includes
//=============================================================================

#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <CoreAudio/CoreAudioTypes.h>
#else
    #include <CoreAudioTypes.h>
#endif

//=============================================================================
//  CADebugger
//=============================================================================

#if TARGET_API_MAC_OSX
    extern bool CAIsDebuggerAttached(void);
#endif
extern void CADebuggerStop(void);

#endif
```

[Next](PublicUtility-CADebugMacros.h.md)[Previous](PublicUtility-CAVectorUnitTypes.h.md)

