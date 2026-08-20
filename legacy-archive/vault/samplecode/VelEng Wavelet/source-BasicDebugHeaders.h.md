---
title: VelEng Wavelet
apple_id: DTS10000460
resource_type: Sample Code
platform: macOS
topic: Mathematical Computation
technology: Accelerate
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/VelEng_Wavelet/Listings/source_Basic_DebugHeaders_h.html
archived_at: '2026-07-18T03:27:45.788776Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VelEng Wavelet](VelEng%20Wavelet.md)


[Next](source-CBasicApp.cp.md)[Previous](VelEng%20Wavelet.md)

# source/Basic_DebugHeaders.h

```c
// ===========================================================================
//  Basic_DebugHeaders.h        ©1996-1998 Metrowerks Inc. All rights reserved.
// ===========================================================================

    // Use PowerPlant-specific Precompiled header

#if __POWERPC__
    #include "Basic_DebugHeadersPPC++"

#else
    #include "Basic_DebugHeaders68K++"
#endif
```

[Next](source-CBasicApp.cp.md)[Previous](VelEng%20Wavelet.md)

