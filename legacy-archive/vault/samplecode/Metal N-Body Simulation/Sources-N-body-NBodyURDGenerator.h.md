---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_NBodyURDGenerator_h.html
archived_at: '2026-07-18T03:14:58.817286Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-MetalNBodyRenderPassDescriptor.mm.md)[Previous](Sources-N-body-NBodyVisualizer.h.md)

# Sources/N-body/NBodyURDGenerator.h

```objc
/*
 <codex>
 <abstract>
 Base class for generating random packed or split data sets for the gpu bound simulator using unifrom real distribution.
 </abstract>
 </codex>
 */

#import <simd/simd.h>

#import <Foundation/Foundation.h>

@interface NBodyURDGenerator : NSObject

// Generate a inital simulation data
@property (nonatomic, setter=acquire:) uint32_t config;

// N-body simulation global parameters
@property (nullable, nonatomic) NSDictionary* globals;

// N-body parameters for simulation types
@property (nullable, nonatomic) NSDictionary* parameters;

// Coordinate points on the Eunclidean axis of simulation
@property (nonatomic) simd::float3 axis;

// Position and velocity pointers
@property (nullable) simd::float4* position;
@property (nullable) simd::float4* velocity;

// Colors pointer
@property (nullable, nonatomic) simd::float4* colors;

@end
```

[Next](Sources-N-body-MetalNBodyRenderPassDescriptor.mm.md)[Previous](Sources-N-body-NBodyVisualizer.h.md)

