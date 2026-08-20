---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitEffectExample_Source_AUSource_FilterVersion_h.html
archived_at: '2026-07-26T19:54:12.844344Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitEffectExample-Source-AUSource-Filter.h.md)[Previous](AUPublic-AUInstrumentBase-LockFreeFIFO.h.md)

# AudioUnitEffectExample/Source/AUSource/FilterVersion.h

```
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

*/

#ifndef __FilterVersion_h__
#define __FilterVersion_h__

#ifdef DEBUG
    #define kFilterVersion 0xFFFFFFFF
#else
    #define kFilterVersion 0x00010000
#endif

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//
#define Filter_COMP_SUBTYPE     'FILT'
#define Filter_COMP_MANF        'appl'
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//

#endif
```

[Next](AudioUnitEffectExample-Source-AUSource-Filter.h.md)[Previous](AUPublic-AUInstrumentBase-LockFreeFIFO.h.md)

