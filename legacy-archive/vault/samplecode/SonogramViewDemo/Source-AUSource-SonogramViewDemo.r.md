---
title: SonogramViewDemo
apple_id: DTS40008647
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2012-01-24'
source_url: https://developer.apple.com/library/archive/samplecode/SonogramViewDemo/Listings/Source_AUSource_SonogramViewDemo_r.html
archived_at: '2026-07-18T03:25:01.637152Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SonogramViewDemo](SonogramViewDemo.md)


[Next](Source-AUSource-SonogramViewDemoVersion.h.md)[Previous](Source-AUSource-SonogramViewDemo.h.md)

# Source/AUSource/SonogramViewDemo.r

```c
#include <AudioUnit/AudioUnit.r>

#include "SonogramViewDemoVersion.h"

// Note that resource IDs must be spaced 2 apart for the 'STR ' name and description
#define kAudioUnitResID_SonogramViewDemo                1000

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SonogramViewDemo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#define RES_ID          kAudioUnitResID_SonogramViewDemo
#define COMP_TYPE       kAudioUnitType_Effect
#define COMP_SUBTYPE    SonogramViewDemo_COMP_SUBTYPE
#define COMP_MANUF      SonogramViewDemo_COMP_MANF  

#define VERSION         kSonogramViewDemoVersion
#define NAME            "Apple Demo: SonogramViewDemo"
#define DESCRIPTION     "SonogramViewDemo AU"
#define ENTRY_POINT     "SonogramViewDemoEntry"

#include "AUResources.r"
```

[Next](Source-AUSource-SonogramViewDemoVersion.h.md)[Previous](Source-AUSource-SonogramViewDemo.h.md)

