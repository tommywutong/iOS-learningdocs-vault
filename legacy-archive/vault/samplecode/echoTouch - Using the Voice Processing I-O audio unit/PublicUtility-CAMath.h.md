---
title: echoTouch - Using the Voice Processing I/O audio unit
apple_id: TP40017575
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-11-29'
source_url: https://developer.apple.com/library/archive/samplecode/echoTouch/Listings/PublicUtility_CAMath_h.html
archived_at: '2026-07-18T03:29:07.902380Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [echoTouch - Using the Voice Processing I/O audio unit](echoTouch%20-%20Using%20the%20Voice%20Processing%20I-O%20audio%20unit.md)


[Next](README.md.md)[Previous](PublicUtility-CAXException.h.md)

# PublicUtility/CAMath.h

```c
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 TPart of CoreAudio Utility Classes.
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

[Next](README.md.md)[Previous](PublicUtility-CAXException.h.md)

