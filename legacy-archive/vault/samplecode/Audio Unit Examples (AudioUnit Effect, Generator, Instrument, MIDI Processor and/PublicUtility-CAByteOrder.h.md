---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CAByteOrder_h.html
archived_at: '2026-07-26T19:54:11.717115Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CAVectorUnit.cpp.md)[Previous](PublicUtility-CABufferList.cpp.md)

# PublicUtility/CAByteOrder.h

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
*/

#if !defined(__CAByteOrder_h__)
#define __CAByteOrder_h__

//=============================================================================
//  Includes
//=============================================================================

//  System Includes
#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <CoreFoundation/CoreFoundation.h>
#else
    #include "CoreFoundation.h"
#endif

#if defined(__cplusplus)
extern "C" {
#endif

CF_INLINE Float32 CASwapFloat32 (Float32 arg) {
    union {
        Float32 f;
        UInt32 i;
    } flip;

    flip.f = arg;
    flip.i = CFSwapInt32 (flip.i);

    return flip.f;
}

CF_INLINE Float64 CASwapFloat64 (Float64 arg) {
    union {
        Float64 f;
        UInt64 i;
    } flip;

    flip.f = arg;
    flip.i = CFSwapInt64 (flip.i);

    return flip.f;
}

#pragma mark -Flippers

CF_INLINE Float32 CASwapFloat32BigToHost(Float32 arg) {
#if defined(__BIG_ENDIAN__)
    return arg;
#else
    return CASwapFloat32(arg);
#endif
}

CF_INLINE Float64 CASwapFloat64BigToHost(Float64 arg) {
#if defined(__BIG_ENDIAN__)
    return arg;
#else
    return CASwapFloat64(arg);
#endif
}

CF_INLINE Float32 CASwapFloat32HostToBig(Float32 arg) {
#if defined(__BIG_ENDIAN__)
    return arg;
#else
    return CASwapFloat32(arg);
#endif
}

CF_INLINE Float64 CASwapFloat64HostToBig(Float64 arg) {
#if defined(__BIG_ENDIAN__)
    return arg;
#else
    return CASwapFloat64(arg);
#endif
}

CF_INLINE Float32 CASwapFloat32LittleToHost(Float32 arg) {
#if defined(__LITTLE_ENDIAN__)
    return arg;
#else
    return CASwapFloat32(arg);
#endif
}

CF_INLINE Float64 CASwapFloat64LittleToHost(Float64 arg) {
#if defined(__LITTLE_ENDIAN__)
    return arg;
#else
    return CASwapFloat64(arg);
#endif
}

CF_INLINE Float32 CASwapFloat32HostToLittle(Float32 arg) {
#if defined(__LITTLE_ENDIAN__)
    return arg;
#else
    return CASwapFloat32(arg);
#endif
}

CF_INLINE Float64 CASwapFloat64HostToLittle(Float64 arg) {
#if defined(__LITTLE_ENDIAN__)
    return arg;
#else
    return CASwapFloat64(arg);
#endif
}

#if defined(__cplusplus)
}
#endif

#endif
```

[Next](PublicUtility-CAVectorUnit.cpp.md)[Previous](PublicUtility-CABufferList.cpp.md)

