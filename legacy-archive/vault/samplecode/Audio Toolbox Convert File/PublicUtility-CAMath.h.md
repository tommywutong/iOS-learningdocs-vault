---
title: Audio Toolbox Convert File
apple_id: DTS40008649
resource_type: Sample Code
platform: watchOS|macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2016-09-29'
source_url: https://developer.apple.com/library/archive/samplecode/ConvertFile/Listings/PublicUtility_CAMath_h.html
archived_at: '2026-07-18T03:04:16.752825Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Toolbox Convert File](Audio%20Toolbox%20Convert%20File.md)


[Next](README.md.md)[Previous](PublicUtility-CAXException.h.md)

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

[Next](README.md.md)[Previous](PublicUtility-CAXException.h.md)

