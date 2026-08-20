---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CAVectorUnit_h.html
archived_at: '2026-07-26T19:54:11.450729Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CAStreamBasicDescription.cpp.md)[Previous](PublicUtility-CAGuard.h.md)

# PublicUtility/CAVectorUnit.h

```swift
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
*/

#ifndef __CAVectorUnit_h__
#define __CAVectorUnit_h__

#include <TargetConditionals.h>
#include "CAVectorUnitTypes.h"
#include <stdlib.h>
#include <stdio.h>

#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <CoreFoundation/CFBase.h>
#else
    #include "CFBase.h"
#endif

// Unify checks for vector units.
// Allow setting an environment variable "CA_NoVector" to turn off vectorized code at runtime (very useful for performance testing).

extern int gCAVectorUnitType;

#ifdef __cplusplus
extern "C" {
#endif

extern SInt32 CAVectorUnit_Examine();   // expensive. use GetType() for lazy initialization and caching.

static inline SInt32 CAVectorUnit_GetType()
{
    int x = gCAVectorUnitType;
    return (x != kVecUninitialized) ? x : CAVectorUnit_Examine();
}

static inline Boolean CAVectorUnit_HasVectorUnit()
{
    return CAVectorUnit_GetType() > kVecNone;
}

#ifdef __cplusplus
}
#endif

#ifdef __cplusplus
class CAVectorUnit {
public:
    static SInt32       GetVectorUnitType() { return CAVectorUnit_GetType(); }
    static bool         HasVectorUnit() { return GetVectorUnitType() > kVecNone; }
    static bool         HasAltivec() { return GetVectorUnitType() == kVecAltivec; }
    static bool         HasSSE2() { return GetVectorUnitType() >= kVecSSE2; }
    static bool         HasSSE3() { return GetVectorUnitType() >= kVecSSE3; }
    static bool         HasAVX1() { return GetVectorUnitType() >= kVecAVX1; }
    static bool         HasNeon() { return GetVectorUnitType() == kVecNeon; }
};
#endif

#endif // __CAVectorUnit_h__
```

[Next](PublicUtility-CAStreamBasicDescription.cpp.md)[Previous](PublicUtility-CAGuard.h.md)

