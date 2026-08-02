---
title: AudioUnitGeneratorExample
apple_id: DTS40008637
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-10-08'
source_url: https://developer.apple.com/library/archive/samplecode/AUPinkNoise/Listings/AUPinkNoise_r.html
archived_at: '2026-07-18T02:59:47.978661Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioUnitGeneratorExample](AudioUnitGeneratorExample.md)


[Next](AUPinkNoiseVersion.h.md)[Previous](AUPinkNoise.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969](https://developer.apple.com/library/mac/samplecode/sc2195/Introduction/Intro.html#//apple_ref/doc/uid/DTS40013969)

# AUPinkNoise.r

```c
/*
 <codex>
 <abstract>AUPinkNoise.r</abstract>
 <\codex>
*/
#include <AudioUnit/AudioUnit.r>

#include "AUPinkNoiseVersion.h"

// Note that resource IDs must be spaced 2 apart for the 'STR ' name and description
#define kAudioUnitResID_AUPinkNoise             1000

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ AUPinkNoise~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#define RES_ID          kAudioUnitResID_AUPinkNoise
#define COMP_TYPE       kAudioUnitType_Generator
#define COMP_SUBTYPE    'pink'
#define COMP_MANUF      kAudioUnitManufacturer_Apple    

#define VERSION         0x00010000
#define NAME            "Apple: AUPinkNoise"
#define DESCRIPTION     "Audio Unit Pink Noise Generator"
#define ENTRY_POINT     "AUPinkNoiseEntry"

#include "AUResources.r"
```

[Next](AUPinkNoiseVersion.h.md)[Previous](AUPinkNoise.h.md)

