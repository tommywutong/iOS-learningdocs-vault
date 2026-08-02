---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_MetalNBodyVertexStage_h.html
archived_at: '2026-07-18T03:14:58.335171Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-NBodyProperties.h.md)[Previous](Sources-N-body-MetalNBodyTransform.h.md)

# Sources/N-body/MetalNBodyVertexStage.h

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for creating and managing of N-body simulation vertex stage and resources.
 */

#import <simd/simd.h>

#import <Metal/Metal.h>

@interface MetalNBodyVertexStage : NSObject

// Query to determine if all the resource were instantiated.
@property (readonly) BOOL isStaged;

// Update the linear transformation mvp matrix
@property (nonatomic) BOOL update;

// Number of point particles in the N-body simulation
@property (nonatomic) uint32_t particles;

// Orthographic projection configuration type
@property (nonatomic) uint32_t config;

// Aspect ratio
@property (nonatomic) float aspect;

// Point particle size
@property (nonatomic) float pointSz;

// Vertex function name
@property (nullable) NSString* name;

// Metal library to use for instantiating a vertex stage
@property (nullable) id<MTLLibrary> library;

// Buffer for point particle positions
@property (nullable) id<MTLBuffer>  positions;

// Vertex stage function
@property (nullable, readonly) id<MTLFunction>  function;

// Point particle colors
@property (nullable, readonly) simd::float4* colors;

// Generate all the necessary vertex stage resources using a default system device
@property (nullable, nonatomic, setter=acquire:) id<MTLDevice> device;

// Encode the buffers for the vertex stage
@property (nullable, nonatomic, setter=encode:) id<MTLRenderCommandEncoder> cmdEncoder;

@end
```

[Next](Sources-N-body-NBodyProperties.h.md)[Previous](Sources-N-body-MetalNBodyTransform.h.md)

