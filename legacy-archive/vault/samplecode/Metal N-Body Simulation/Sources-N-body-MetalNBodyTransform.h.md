---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_MetalNBodyTransform_h.html
archived_at: '2026-07-18T03:14:58.203620Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-MetalNBodyVertexStage.h.md)[Previous](Sources-N-body-NBodyProperties.mm.md)

# Sources/N-body/MetalNBodyTransform.h

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for managing N-body linear transformation matrix and buffer.
 */

#import <simd/simd.h>
#import <Metal/Metal.h>

@interface MetalNBodyTransform : NSObject

// Query to determine if a Metal buffer was generated successfully
@property (readonly) BOOL haveBuffer;

// Generate a Metal buffer and linear tranformations using a default system device
@property (nullable, nonatomic, setter=acquire:) id<MTLDevice> device;

// Metal buffer for linear transformation matrix
@property (nullable, readonly) id<MTLBuffer> buffer;

// Linear transformation matrix
@property (readonly) simd::float4x4 transform;

// Metal buffer size
@property (readonly) size_t size;

// Update the mvp linear transformation matrix
@property (nonatomic) BOOL update;

// Set the aspect ratio for the orthographic 2d projection
@property (nonatomic) float aspect;

// Orthographic projection configuration type
@property (nonatomic) uint32_t config;

// Orthographic 2d bounds
@property simd::float3 bounds;

// (x,y,z) centers
@property float center;
@property float zCenter;

@end
```

[Next](Sources-N-body-MetalNBodyVertexStage.h.md)[Previous](Sources-N-body-NBodyProperties.mm.md)

