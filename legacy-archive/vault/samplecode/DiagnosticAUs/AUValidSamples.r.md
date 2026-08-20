---
title: DiagnosticAUs
apple_id: DTS40008639
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2009-04-15'
source_url: https://developer.apple.com/library/archive/samplecode/DiagnosticAUs/Listings/AUValidSamples_r.html
archived_at: '2026-07-18T03:06:49.975388Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DiagnosticAUs](DiagnosticAUs.md)


[Next](AUValidSamplesShared.h.md)[Previous](AUValidSamples.cpp.md)

# AUValidSamples.r

```c
/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   AUValidSamples.r
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

#include <AudioUnit/AudioUnit.r>

#include "AUValidSamplesVersion.h"

// Note that resource IDs must be spaced 2 apart for the 'STR ' name and description
#define kAudioUnitResID_AUValidSamples              10000

// So you need to define these appropriately for your audio unit.
// For the name the convention is to provide your company name and end it with a ':',
// then provide the name of the AudioUnit.
// The Description can be whatever you want.
// For an effect unit the Type and SubType should be left the way they are defined here...

#define RES_ID          kAudioUnitResID_AUValidSamples
#define COMP_TYPE       kAudioUnitType_Effect
#define COMP_SUBTYPE    'vsmp'
#define COMP_MANUF      'appl'  
#define VERSION         kAUValidSamplesVersion
#define NAME            "Apple_DEBUG: AUValidSamples"
#define DESCRIPTION     "Validates the samples as it passes through the AU"
#define ENTRY_POINT     "AUValidSamplesEntry"

#include "AUResources.r"


#define RES_ID          1002
#define COMP_TYPE       kAudioUnitCarbonViewComponentType
#define COMP_SUBTYPE    'vsmp'
#define COMP_MANUF      'appl'
#define VERSION         0x00010000
#define NAME            "Apple_DEBUG: AUValidSamples"
#define DESCRIPTION     "View for the AUValidSamples"
#define ENTRY_POINT     "AUValidSamplesViewEntry"

#include "AUResources.r"
```

[Next](AUValidSamplesShared.h.md)[Previous](AUValidSamples.cpp.md)

