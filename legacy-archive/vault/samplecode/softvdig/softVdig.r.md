---
title: softvdig
apple_id: DTS10000334
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-08-29'
source_url: https://developer.apple.com/library/archive/samplecode/softvdig/Listings/softVdig_r.html
archived_at: '2026-07-26T19:52:28.139851Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [softvdig](softvdig.md)


[Next](Document%20Revision%20History.md)[Previous](softVdig.h.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# softVdig.r

```c
#define UseExtendedThingResource 1

#include "MacTypes.r"
#include "Components.r"
#include "ImageCodec.r"

#if !TARGET_OS_MAC
    #if TARGET_OS_WIN32
        #define Target_PlatformType      platformWin32
    #endif

    #if TARGET_OS_UNIX
        #if TARGET_CPU_MIPS
            #define Target_PlatformType      platformIRIXmips
        #endif
        #if TARGET_CPU_SPARC
            #define Target_PlatformType      platformSunOSsparc
        #endif
    #endif

    #ifndef Target_PlatformType
        #error get a real platform type
    #endif
#endif

resource 'thng' (200,  "Software vdig") {
    'vdig', 'soft', 'jph ',
#if TARGET_REZ_MAC_68K
    0,      0,          // Flags, Mask
    'CODE', 200,        // 68k Code
#else
    0,      0,          // Flags, Mask
    0,      0,          // 68k Code
#endif
    'strn', 200,        // Name
    'stri', 200,        // Info
    'ICON', 200,        // Icon
    0,
#if !TARGET_REZ_MAC_68K
    componentHasMultiplePlatforms |
#endif
        componentDoAutoVersion,
    0,
    {
#if TARGET_OS_MAC
#else
        0,
        'dlle', 200,    // Code
        Target_PlatformType,
#endif
    },
};

resource 'strn' (200) {
    "softVdig"
};

resource 'stri' (200) {
    "Software simulation of a video digitizer"
};

#if TARGET_OS_MAC
#else
    resource 'dlle' (200) {
        "softVdig"
    };
#endif
```

[Next](Document%20Revision%20History.md)[Previous](softVdig.h.md)

