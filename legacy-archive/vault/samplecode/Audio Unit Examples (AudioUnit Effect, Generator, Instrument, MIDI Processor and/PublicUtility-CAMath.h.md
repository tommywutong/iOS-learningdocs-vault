---
title: Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor
  and Offline)
apple_id: DTS40013969
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-19'
source_url: https://developer.apple.com/library/archive/samplecode/sc2195/Listings/PublicUtility_CAMath_h.html
archived_at: '2026-07-26T19:54:11.413513Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Unit Examples (AudioUnit Effect, Generator, Instrument, MIDI Processor and Offline)](Audio%20Unit%20Examples%20%28AudioUnit%20Effect%2C%20Generator%2C%20Instrument%2C%20MIDI%20Processor%20and.md)


[Next](PublicUtility-CAAudioChannelLayout.h.md)[Previous](PublicUtility-CAStreamBasicDescription.h.md)

# PublicUtility/CAMath.h

```c
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
Part of Core Audio Public Utility Classes
*/

#ifndef __CAMath_h__
#define __CAMath_h__

#if !defined(__COREAUDIO_USE_FLAT_INCLUDES__)
    #include <CoreAudio/CoreAudioTypes.h>
#else
    #include <CoreAudioTypes.h>
#endif

inline bool fiszero(Float64 f) { return (f == 0.); }
inline bool fiszero(Float32 f) { return (f == 0.f); }

inline bool fnonzero(Float64 f) { return !fiszero(f); }
inline bool fnonzero(Float32 f) { return !fiszero(f); }

inline bool fequal(const Float64 &a, const Float64 &b) { return a == b; }
inline bool fequal(const Float32 &a, const Float32 &b) { return a == b; }

inline bool fnotequal(const Float64 &a, const Float64 &b) { return !fequal(a, b); }
inline bool fnotequal(const Float32 &a, const Float32 &b) { return !fequal(a, b); }

#endif // __CAMath_h__
```

[Next](PublicUtility-CAAudioChannelLayout.h.md)[Previous](PublicUtility-CAStreamBasicDescription.h.md)

