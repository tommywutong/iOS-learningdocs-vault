---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitGeneratorExample_AUPinkNoiseVersion_h.html
archived_at: '2026-07-26T19:54:11.112142Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitGeneratorExample-Utility-TRandom.h.md)[Previous](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)

# AudioUnitGeneratorExample/AUPinkNoiseVersion.h

```
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Pink Noise AU
*/

#ifndef __AUPinkNoiseVersion_h__
#define __AUPinkNoiseVersion_h__

#ifdef DEBUG
    #define kAUPinkNoiseVersion 0xFFFFFFFF
#else
    #define kAUPinkNoiseVersion 0x00010000
#endif

//~~~~~~~~~~~~~~  Change!!! ~~~~~~~~~~~~~~~~~~~~~//
#define AUPinkNoise_COMP_SUBTYPE    'pink'
#define AUPinkNoise_COMP_MANF       'Demo'
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//

#endif
```

[Next](AudioUnitGeneratorExample-Utility-TRandom.h.md)[Previous](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)

