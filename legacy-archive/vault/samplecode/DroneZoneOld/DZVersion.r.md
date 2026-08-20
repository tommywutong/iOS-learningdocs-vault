---
title: DroneZoneOld
apple_id: DTS10000051
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/DroneZoneOld/Listings/DZVersion_r.html
archived_at: '2026-07-18T03:07:20.236998Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DroneZoneOld](DroneZoneOld.md)


[Next](Document%20Revision%20History.md)[Previous](DZUtils.h.md)

# DZVersion.r

```c
/*
    Version.r

    Copyright Apple Computer, Inc. 1997
    All rights reserved.

*/

#include "Types.r"

#define kMajorVersNumber    0x02
#define kMinorVersNumber    0x00
#define kBugFixNumber       0x00
#define kReleaseType        development
#define kBuildNumber        0x02
#define kMajorStr           "2.0"
#define kBuildStr           "d2"


resource 'vers' (1) {
    kMajorVersNumber,
    kMinorVersNumber + kBugFixNumber,
    kReleaseType,
    kBuildNumber,
    verUS,
    kMajorStr kBuildStr,
    kMajorStr kBuildStr ", © Apple Computer, Inc. 1996-98"
};


resource 'vers' (2) {
    kMajorVersNumber,
    kMinorVersNumber + kBugFixNumber,
    kReleaseType,
    kBuildNumber,
    verUS,
    "Apple Game Sprockets",
    "Apple Game Sprockets"
};

#undef  kMajorVersNumber
#undef  kMinorVersNumber
#undef  kBugFixNumber
#undef  kReleaseType
#undef  kBuildNumber
#undef  kMajorStr
#undef  kBuildStr
```

[Next](Document%20Revision%20History.md)[Previous](DZUtils.h.md)

