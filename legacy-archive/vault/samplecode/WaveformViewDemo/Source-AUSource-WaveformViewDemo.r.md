---
title: WaveformViewDemo
apple_id: DTS40008653
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2009-04-15'
source_url: https://developer.apple.com/library/archive/samplecode/WaveformViewDemo/Listings/Source_AUSource_WaveformViewDemo_r.html
archived_at: '2026-07-18T03:28:08.967709Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WaveformViewDemo](WaveformViewDemo.md)


[Next](Source-AUSource-WaveformViewDemoVersion.h.md)[Previous](Source-AUSource-WaveformViewDemo.h.md)

# Source/AUSource/WaveformViewDemo.r

```c
#include <AudioUnit/AudioUnit.r>

#include "WaveformViewDemoVersion.h"

// Note that resource IDs must be spaced 2 apart for the 'STR ' name and description
#define kAudioUnitResID_WaveformViewDemo                1000

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ WaveformViewDemo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#define RES_ID          kAudioUnitResID_WaveformViewDemo
#define COMP_TYPE       kAudioUnitType_Effect
#define COMP_SUBTYPE    WaveformViewDemo_COMP_SUBTYPE
#define COMP_MANUF      WaveformViewDemo_COMP_MANF  

#define VERSION         kWaveformViewDemoVersion
#define NAME            "Apple Demo: WaveformViewDemo"
#define DESCRIPTION     "WaveformViewDemo AU"
#define ENTRY_POINT     "WaveformViewDemoEntry"

#include "AUResources.r"
```

[Next](Source-AUSource-WaveformViewDemoVersion.h.md)[Previous](Source-AUSource-WaveformViewDemo.h.md)

