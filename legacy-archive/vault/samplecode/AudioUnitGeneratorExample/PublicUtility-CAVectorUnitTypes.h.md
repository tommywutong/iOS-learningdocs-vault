---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/PublicUtility_CAVectorUnitTypes_h.html
archived_at: '2026-07-18T02:59:52.847200Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](PublicUtility-CAXException.cpp.md)[Previous](PublicUtility-CAVectorUnit.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# PublicUtility/CAVectorUnitTypes.h

```
/*
 <codex> 
 <abstract>Part of CoreAudio Utility Classes</abstract>
 <\codex>
*/
#ifndef __CAVectorUnitTypes_h__
#define __CAVectorUnitTypes_h__

enum {
    kVecUninitialized = -1,
    kVecNone = 0,
    kVecAltivec = 1,
    kVecSSE2 = 100,
    kVecSSE3 = 101,
    kVecNeon = 200
};

#endif
```

[Next](PublicUtility-CAXException.cpp.md)[Previous](PublicUtility-CAVectorUnit.h.md)

