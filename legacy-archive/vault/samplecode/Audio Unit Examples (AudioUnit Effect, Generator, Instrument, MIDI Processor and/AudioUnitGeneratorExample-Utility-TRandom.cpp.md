---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/AudioUnitGeneratorExample_Utility_TRandom_cpp.html
archived_at: '2026-07-26T19:54:11.176408Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](AudioUnitGeneratorExample-Utility-Pink.h.md)[Previous](AudioUnitGeneratorExample-Utility-Biquad.cpp.md)

# AudioUnitGeneratorExample/Utility/TRandom.cpp

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

*/

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  TRandom.cpp
//
//      a random number generator
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#include "TRandom.h"

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  TRandom::TRandom
//
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TRandom::TRandom()
{
    Seed(12345);
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  TRandom::Seed
//
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
void TRandom::Seed(UInt32 j)
{
    UInt32 k = 1;
    mTable[54] = j;
    long i;
    for (i = 0; i < 54; i++)
    {
        long ii = 21 * i % 55;
        mTable[ii] = k;
        k = j - k;
        j = mTable[ii];
    }
    for (int loop = 0; loop < 4; loop++)
    {
        for (i = 0; i < 55; i++)
            mTable[i] = mTable[i] - mTable[(1 + i + 30) % 55];
    }
    mIndex1 = 0;
    mIndex2 = 31;
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#pragma mark ____EasyFunctions

static TRandom *sGenerator = NULL;

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  GetRandomLong
//
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
UInt32  GetRandomLong(UInt32 inRange)
{
    if (sGenerator == NULL)
        sGenerator = new TRandom(kRandomSeed);
    return (*sGenerator)(inRange);
}

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//  GetRandomLong
//
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
UInt32  GetRandomLong(UInt32 inLowerLimit, UInt32 inUpperLimit )
{
    UInt32 value = GetRandomLong(inUpperLimit - inLowerLimit );

    return value + inLowerLimit;
}
```

[Next](AudioUnitGeneratorExample-Utility-Pink.h.md)[Previous](AudioUnitGeneratorExample-Utility-Biquad.cpp.md)

