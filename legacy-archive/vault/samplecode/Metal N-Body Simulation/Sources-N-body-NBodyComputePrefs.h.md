---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_NBodyComputePrefs_h.html
archived_at: '2026-07-18T03:14:58.525608Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-MetalNBodySampler.h.md)[Previous](Sources-N-body-MetalGaussianMap.h.md)

# Sources/N-body/NBodyComputePrefs.h

```
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 N-Body compute preferences common structure for the kernel and the utility class.
 */

#ifndef _NBODY_COMPUTE_PREFS_H_
#define _NBODY_COMPUTE_PREFS_H_

#ifdef __cplusplus

namespace NBody
{
    namespace Compute
    {
        struct Prefs
        {
            float  timestep;
            float  damping;
            float  softeningSqr;

            unsigned int particles;
        }; // Prefs

        typedef Prefs Prefs;
    } // Compute
} // NBody

#endif

#endif
```

[Next](Sources-N-body-MetalNBodySampler.h.md)[Previous](Sources-N-body-MetalGaussianMap.h.md)

