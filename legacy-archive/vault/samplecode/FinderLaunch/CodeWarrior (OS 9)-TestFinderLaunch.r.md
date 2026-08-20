---
title: FinderLaunch
apple_id: DTS10000666
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: ApplicationServices
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/FinderLaunch/Listings/CodeWarrior____OS_9__TestFinderLaunch_r.html
archived_at: '2026-07-18T03:08:43.338740Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FinderLaunch](FinderLaunch.md)


[Next](ProjectBuilder%20%28OS%20X%29-FinderLaunch.c.md)[Previous](CodeWarrior%20%28OS%209%29-TestFinderLaunch.h.md)

# CodeWarrior (OS 9)/TestFinderLaunch.r

```c
/*
    Sample Template
*/

#include "Processes.r"
#include "CodeFragments.r"

include "TestFinderLaunch.rsrc";

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
        "TestFinderLaunch"
    }
};
```

[Next](ProjectBuilder%20%28OS%20X%29-FinderLaunch.c.md)[Previous](CodeWarrior%20%28OS%209%29-TestFinderLaunch.h.md)

