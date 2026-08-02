---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitMidiProcessorExample_AUMidiPassThruVersion_h.html
archived_at: '2026-07-26T19:54:11.977234Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitMidiProcessorExample-AUMidiPassThruTest-AUMidiPassThruTest.cpp.md)[Previous](AudioUnitMidiProcessorExample-AUMidiPassThru.h.md)

# AudioUnitMidiProcessorExample/AUMidiPassThruVersion.h

```
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
MIDI Processor AU
*/

#ifndef __AUMidiPassThruVersion_h__
#define __AUMidiPassThruVersion_h__

#ifdef DEBUG
    #define kAUMidiPassThruVersion    0xFFFFFFFF
#else
    #define kAUMidiPassThruVersion    0x00010000
#endif

#define AUMidiPassThru_COMP_TYPE      'aumi'
#define AUMidiPassThru_COMP_SUBTYPE   'aump'
#define AUMidiPassThru_COMP_MANF      'appl'

#endif
```

[Next](AudioUnitMidiProcessorExample-AUMidiPassThruTest-AUMidiPassThruTest.cpp.md)[Previous](AudioUnitMidiProcessorExample-AUMidiPassThru.h.md)

