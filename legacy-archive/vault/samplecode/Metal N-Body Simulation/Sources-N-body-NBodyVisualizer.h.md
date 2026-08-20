---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_NBodyVisualizer_h.html
archived_at: '2026-07-18T03:14:58.950927Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-NBodyURDGenerator.h.md)[Previous](Sources-N-body-MetalNBodyRenderStage.h.md)

# Sources/N-body/NBodyVisualizer.h

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 N-body controller object for visualizing the simulation.
 */

#import <simd/simd.h>
#import <QuartzCore/CAMetalLayer.h>
#import <Metal/Metal.h>

@interface NBodyVisualizer : NSObject

// Query to determine if all resources were instantiated
@property (readonly) BOOL haveVisualizer;

// Generate all the resources necessary for N-body simulation
@property (nullable, nonatomic, setter=acquire:) id<MTLDevice> device;

// Render a frame for N-body simaulation
@property (nullable, nonatomic, setter=render:) id<CAMetalDrawable> drawable;

// Orthographic projection configuration type
@property uint32_t config;

// Coordinate points on the Eunclidean axis of simulation
@property (nonatomic) simd::float3 axis;

// Aspect ratio
@property (nonatomic) float aspect;

// Total number of frames to be rendered for a N-body simulation type
@property (nonatomic) uint32_t frames;

// The number of point particels
@property (nonatomic) uint32_t particles;

// Texture resolution.  The default is 64x64.
@property (nonatomic) uint32_t texRes;

// Becomes true once all the frames for a simulation type are rendered
@property (readonly) BOOL isComplete;

// Current active simulation type
@property (readonly) uint32_t active;

// Current frame being rendered
@property (readonly) uint32_t frame;

@end
```

[Next](Sources-N-body-NBodyURDGenerator.h.md)[Previous](Sources-N-body-MetalNBodyRenderStage.h.md)

