---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/PublicUtility_CAMath_h.html
archived_at: '2026-07-18T02:59:52.236937Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](PublicUtility-CAMutex.cpp.md)[Previous](PublicUtility-CALogMacros.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# PublicUtility/CAMath.h

```c
/*
 <codex> 
 <abstract>Part of CoreAudio Utility Classes</abstract>
 <\codex>
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

[Next](PublicUtility-CAMutex.cpp.md)[Previous](PublicUtility-CALogMacros.h.md)

