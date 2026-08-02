---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_MetalNBodyRenderPipeline_h.html
archived_at: '2026-07-18T03:14:57.836296Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-MetalNBodyComputeStage.mm.md)[Previous](Sources-Foundation-CFQueueGenerator.h.md)

# Sources/N-body/MetalNBodyRenderPipeline.h

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for creating a render state pipeline.
 */

#import <Metal/Metal.h>

@interface MetalNBodyRenderPipeline : NSObject

// Query to determine if render pipeline state is instantiated
@property (readonly) BOOL haveDescriptor;

// Vertex function
@property (nullable) id<MTLFunction> vertex;

// Fragment function
@property (nullable) id<MTLFunction> fragment;

// Generate render pipeline state using a default system
// device, fragment and vertex stages
@property (nullable, nonatomic, setter=acquire:) id<MTLDevice> device;

// Render pipeline descriptor state
@property (nullable, readonly) id<MTLRenderPipelineState> render;

// Set blending
@property BOOL blend;

@end
```

[Next](Sources-N-body-MetalNBodyComputeStage.mm.md)[Previous](Sources-Foundation-CFQueueGenerator.h.md)

