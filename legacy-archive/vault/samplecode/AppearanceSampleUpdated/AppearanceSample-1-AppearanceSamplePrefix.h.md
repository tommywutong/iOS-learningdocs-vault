---
title: AppearanceSampleUpdated
apple_id: DTS10003689
resource_type: Sample Code
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2005-06-27'
source_url: https://developer.apple.com/library/archive/samplecode/AppearanceSampleUpdated/Listings/AppearanceSample_1_AppearanceSamplePrefix_h.html
archived_at: '2026-07-26T19:53:52.692072Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AppearanceSampleUpdated](AppearanceSampleUpdated.md)


[Next](AppearanceSample-1-BaseDialog.cp.md)[Previous](AppearanceSample-1-AppearanceSamplePictures.r.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# AppearanceSample-1/AppearanceSamplePrefix.h

```c
#define TARGET_CARBON   1

#include "PrefixCommon.h"

#ifndef CARBON_ON_MACH_O
#define CARBON_ON_MACH_O    0
#endif

#ifndef BUILDING_FOR_CARBON_8
#define BUILDING_FOR_CARBON_8   0
#endif

#ifndef HELP_TAGS_ENABLED
#define HELP_TAGS_ENABLED   1
#endif

#include <Carbon/Carbon.h>
```

[Next](AppearanceSample-1-BaseDialog.cp.md)[Previous](AppearanceSample-1-AppearanceSamplePictures.r.md)

