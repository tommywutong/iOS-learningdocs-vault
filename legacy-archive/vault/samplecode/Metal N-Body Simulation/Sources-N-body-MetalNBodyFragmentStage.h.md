---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_MetalNBodyFragmentStage_h.html
archived_at: '2026-07-18T03:14:57.449718Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-NBodyVisualizer.mm.md)[Previous](Sources-N-body-MetalNBodyPresenter.mm.md)

# Sources/N-body/MetalNBodyFragmentStage.h

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for creating N-body simulation fragment stage.
 */

#import <Metal/Metal.h>

@interface MetalNBodyFragmentStage : NSObject

// Query to determine if all the resource were instantiated.
@property (readonly) BOOL isStaged;

// N-body simulation global parameters
@property (nullable, nonatomic) NSDictionary* globals;

// Fragment function name
@property (nullable) NSString* name;

// Metal library to use for instantiating a fragment stage
@property (nullable) id<MTLLibrary> library;

// Fragment stage function
@property (nullable, readonly) id<MTLFunction> function;

// Generate all the necessary fragment stage resources using a default system device
@property (nullable, nonatomic, setter=acquire:) id<MTLDevice> device;

// Encode texture and sampler for the fragment stage
@property (nullable, nonatomic, setter=encode:) id<MTLRenderCommandEncoder> cmdEncoder;

@end
```

[Next](Sources-N-body-NBodyVisualizer.mm.md)[Previous](Sources-N-body-MetalNBodyPresenter.mm.md)

