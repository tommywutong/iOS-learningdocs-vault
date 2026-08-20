---
title: ColorPopUpMenus
apple_id: DTS10000564
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/ColorPopUpMenus/Listings/ColorPopUpMenus_r.html
archived_at: '2026-07-18T03:03:59.448484Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ColorPopUpMenus](ColorPopUpMenus.md)


[Next](Document%20Revision%20History.md)[Previous](ColorPopUpMenus.h.md)

# ColorPopUpMenus.r

```c
/*
    ColorPopUpMenus rez declarations
*/

#include "Processes.r"
#include "CodeFragments.r"

include "ColorPopUpMenus.rsrc";

resource 'SIZE' (-1, purgeable)  {
    reserved,
    acceptSuspendResumeEvents,
    reserved,
    canBackground,
    doesActivateOnFGSwitch,
    backgroundAndForeground,
    dontGetFrontClicks,
    ignoreAppDiedEvents,
    is32BitCompatible,
    isHighLevelEventAware,
    localAndRemoteHLEvents,
    isStationeryAware,
    dontUseTextEditServices,
    reserved,
    reserved,
    reserved,
    1024 * 300,
    1024 * 300
};

resource 'cfrg' (0) {
    {   kPowerPC,
        kFullLib,
        kNoVersionNum,
        kNoVersionNum,
        kDefaultStackSize,
        kNoAppSubFolder,
        kIsApp,
        kOnDiskFlat,
        kZeroOffset,
        kWholeFork,
        "ColorPopUpMenus"
    }
};
```

[Next](Document%20Revision%20History.md)[Previous](ColorPopUpMenus.h.md)

