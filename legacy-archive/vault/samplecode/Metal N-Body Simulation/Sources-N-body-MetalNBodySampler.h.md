---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_MetalNBodySampler_h.html
archived_at: '2026-07-18T03:14:58.106710Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-MetalNBodyPresenter.mm.md)[Previous](Sources-N-body-NBodyComputePrefs.h.md)

# Sources/N-body/MetalNBodySampler.h

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for creating a sampler.
 */

#import <Metal/Metal.h>

@interface MetalNBodySampler : NSObject

// Generate a Metal sampler state using a default system device
@property (nullable, nonatomic, setter=acquire:) id<MTLDevice> device;

// Sample state object for N-body simulation
@property (nullable, readonly) id<MTLSamplerState> sampler;

// Query to find if the sampler state object was generated
@property (readonly) BOOL haveSampler;

@end
```

[Next](Sources-N-body-MetalNBodyPresenter.mm.md)[Previous](Sources-N-body-NBodyComputePrefs.h.md)

