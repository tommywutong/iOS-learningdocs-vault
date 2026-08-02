---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CAVectorUnitTypes_h.html
archived_at: '2026-07-26T19:54:11.276315Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CADebugger.h.md)[Previous](PublicUtility-CAAUMIDIMapManager.cpp.md)

# PublicUtility/CAVectorUnitTypes.h

```
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
*/

#ifndef __CAVectorUnitTypes_h__
#define __CAVectorUnitTypes_h__

enum {
    kVecUninitialized = -1,
    kVecNone = 0,
    kVecAltivec = 1,
    kVecSSE2 = 100,
    kVecSSE3 = 101,
    kVecAVX1 = 110,
    kVecNeon = 200
};

#endif
```

[Next](PublicUtility-CADebugger.h.md)[Previous](PublicUtility-CAAUMIDIMapManager.cpp.md)

