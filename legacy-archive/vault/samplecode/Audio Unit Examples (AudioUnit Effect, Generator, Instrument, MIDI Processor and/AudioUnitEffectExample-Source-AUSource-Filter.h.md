---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitEffectExample_Source_AUSource_Filter_h.html
archived_at: '2026-07-26T19:54:12.849161Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitEffectExample-Source-AUSource-Filter.cpp.md)[Previous](AudioUnitEffectExample-Source-AUSource-FilterVersion.h.md)

# AudioUnitEffectExample/Source/AUSource/Filter.h

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Filter Effect AU
*/

#define kNumberOfResponseFrequencies 512

// Here we define a custom property so the view is able to retrieve the current frequency
// response curve.  The curve changes as the filter's cutoff frequency and resonance are
// changed...

// custom properties id's must be 64000 or greater
// see <AudioUnit/AudioUnitProperties.h> for a list of Apple-defined standard properties
//
enum
{
    kAudioUnitCustomProperty_FilterFrequencyResponse = 65536
};

// We'll define our property data to be a size kNumberOfResponseFrequencies array of structs
// The UI will pass in the desired frequency in the mFrequency field, and the Filter AU
// will provide the linear magnitude response of the filter in the mMagnitude field
// for each element in the array.
typedef struct FrequencyResponse
{
    Float64     mFrequency;
    Float64     mMagnitude;
} FrequencyResponse;
```

[Next](AudioUnitEffectExample-Source-AUSource-Filter.cpp.md)[Previous](AudioUnitEffectExample-Source-AUSource-FilterVersion.h.md)

