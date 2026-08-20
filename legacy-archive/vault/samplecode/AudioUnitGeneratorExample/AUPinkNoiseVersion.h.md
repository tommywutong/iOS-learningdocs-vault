---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/AUPinkNoiseVersion_h.html
archived_at: '2026-07-18T02:59:47.816467Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](AUPublic-AUBase-AUBase.cpp.md)[Previous](AUPinkNoise.r.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# AUPinkNoiseVersion.h

```
#ifndef __AUPinkNoiseVersion_h__
#define __AUPinkNoiseVersion_h__


#ifdef DEBUG
    #define kAUPinkNoiseVersion 0xFFFFFFFF
#else
    #define kAUPinkNoiseVersion 0x00010000  
#endif

//~~~~~~~~~~~~~~  Change!!! ~~~~~~~~~~~~~~~~~~~~~//
#define AUPinkNoise_COMP_SUBTYPE        'pink'
#define AUPinkNoise_COMP_MANF       'appl'
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//

#endif
```

[Next](AUPublic-AUBase-AUBase.cpp.md)[Previous](AUPinkNoise.r.md)

