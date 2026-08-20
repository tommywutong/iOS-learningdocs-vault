---
title: FinderLaunch
apple_id: DTS10000666
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: ApplicationServices
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/FinderLaunch/Listings/CodeWarrior____OS_9__MPWTool_FinderLaunchTool_r.html
archived_at: '2026-07-18T03:08:42.788109Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FinderLaunch](FinderLaunch.md)


[Next](CodeWarrior%20%28OS%209%29-TestFinderLaunch.c.md)[Previous](CodeWarrior%20%28OS%209%29-MPWTool-FinderLaunchTool.c.md)

# CodeWarrior (OS 9)/MPWTool/FinderLaunchTool.r

```c
/*
    FinderLaunchTool.r
*/

#include "Processes.r"
#include "CodeFragments.r"

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
        "FinderLaunchTool"
    }
};
```

[Next](CodeWarrior%20%28OS%209%29-TestFinderLaunch.c.md)[Previous](CodeWarrior%20%28OS%209%29-MPWTool-FinderLaunchTool.c.md)

