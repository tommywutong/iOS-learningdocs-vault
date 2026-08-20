---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_MetalNBodyPresenter_h.html
archived_at: '2026-07-18T03:14:57.556649Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-MetalNBodyRenderStage.h.md)[Previous](Sources-N-body-NBodyPreferences.mm.md)

# Sources/N-body/MetalNBodyPresenter.h

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for rendering (encoding into Metal pipeline components of) N-Body simulation and presenting the frame
 */

#import <simd/simd.h>

#import <QuartzCore/CAMetalLayer.h>
#import <Metal/Metal.h>

@interface MetalNBodyPresenter : NSObject

// Aspect ratio
@property (nonatomic) float aspect;

// Orthographic projection configuration type
@property (nonatomic) uint32_t config;

// Update the linear transformation mvp matrix
@property (nonatomic) BOOL update;

// N-body simulation global parameters
@property (nullable, nonatomic) NSDictionary* globals;

// N-body parameters for simulation types
@property (nullable, nonatomic) NSDictionary* parameters;

// Host pointers
@property (nullable, nonatomic, readonly) simd::float4* position;
@property (nullable, nonatomic, readonly) simd::float4* velocity;
@property (nullable, nonatomic, readonly) simd::float4* colors;

// Query to determine if all the resources are instantiated for render encoder object
@property (readonly) BOOL haveEncoder;

// Query to determine if all stages are encoded
@property (readonly) BOOL isEncoded;

// Generate all the resources (including fragment, vertex and compute stages)
// for rendering N-Body simulation
@property (nullable, nonatomic, setter=acquire:) id<MTLDevice> device;

// Encode vertex, fragment, and compute stages, then present the drawable
@property (nullable, nonatomic, setter=encode:) id<CAMetalDrawable> drawable;

// Wait until the render encoding is complete
- (void) finish;

@end
```

[Next](Sources-N-body-MetalNBodyRenderStage.h.md)[Previous](Sources-N-body-NBodyPreferences.mm.md)

