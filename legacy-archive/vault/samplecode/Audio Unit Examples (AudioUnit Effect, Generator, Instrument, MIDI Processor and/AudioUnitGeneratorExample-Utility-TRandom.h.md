---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitGeneratorExample_Utility_TRandom_h.html
archived_at: '2026-07-26T19:54:11.117939Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitGeneratorExample-Utility-Biquad.cpp.md)[Previous](AudioUnitGeneratorExample-AUPinkNoiseVersion.h.md)

# AudioUnitGeneratorExample/Utility/TRandom.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

*/

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  TRandom.h
//
//      a random number generator
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#include <CoreFoundation/CoreFoundation.h>

#ifndef __TRandom
#define __TRandom

#define kRandomSeed 161803398

UInt32  GetRandomLong(UInt32 inRange);
UInt32  GetRandomLong(UInt32 inLowerLimit, UInt32 inUpperLimit);

class TRandom
{
public:
    TRandom();
    TRandom(UInt32 n) {Seed(n);};

    void Seed(UInt32 n);

    UInt32 operator()(UInt32 inLimit)
    {
        mIndex1 = (mIndex1 + 1) % 55;
        mIndex2 = (mIndex2 + 1) % 55;
        mTable[mIndex1] = mTable[mIndex1] - mTable[mIndex2];
        return mTable[mIndex1] % inLimit;
    };

protected:
    UInt32 mTable[55];
    long mIndex1;
    long mIndex2;
};

#endif      // __TRandom
```

[Next](AudioUnitGeneratorExample-Utility-Biquad.cpp.md)[Previous](AudioUnitGeneratorExample-AUPinkNoiseVersion.h.md)

