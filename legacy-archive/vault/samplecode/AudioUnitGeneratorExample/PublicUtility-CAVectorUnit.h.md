---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/PublicUtility_CAVectorUnit_h.html
archived_at: '2026-07-18T02:59:52.930360Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](PublicUtility-CAVectorUnitTypes.h.md)[Previous](PublicUtility-CAVectorUnit.cpp.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# PublicUtility/CAVectorUnit.h

```c
/*
 <codex> 
 <abstract>Part of CoreAudio Utility Classes</abstract>
 <\codex>
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
    static bool         HasSSE3() { return GetVectorUnitType() == kVecSSE3; }
    static bool         HasNeon() { return GetVectorUnitType() == kVecNeon; }
};
#endif

#endif // __CAVectorUnit_h__
```

[Next](PublicUtility-CAVectorUnitTypes.h.md)[Previous](PublicUtility-CAVectorUnit.cpp.md)

