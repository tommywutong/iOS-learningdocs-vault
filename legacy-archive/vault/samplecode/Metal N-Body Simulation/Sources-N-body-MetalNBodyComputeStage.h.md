---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_MetalNBodyComputeStage_h.html
archived_at: '2026-07-18T03:14:57.231446Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](LICENSE.txt.md)[Previous](Sources-N-body-MetalGaussianMap.mm.md)

# Sources/N-body/MetalNBodyComputeStage.h

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for managing the N-body compute resources.
 */

#import <simd/simd.h>
#import <Metal/Metal.h>

@interface MetalNBodyComputeStage : NSObject

// Query to determine if all the resource were instantiated.
@property (readonly) BOOL isStaged;

// Compute kernel's function name
@property (nullable) NSString* name;

// Metal library to use for instantiating a compute stage
@property (nullable) id<MTLLibrary> library;

// N-body simulation global parameters
@property (nullable, nonatomic) NSDictionary* globals;

// N-body parameters for simulation types
@property (nullable, nonatomic) NSDictionary* parameters;

// Position buffer
@property (nullable, readonly) id<MTLBuffer> buffer;

// Host pointers
@property (nullable, readonly) simd::float4* position;
@property (nullable, readonly) simd::float4* velocity;

// Thread execution width multiplier
@property (nonatomic) uint32_t multiplier;

// Generate all the necessary compute stage resources using a default system device
@property (nullable, nonatomic, setter=acquire:) id<MTLDevice> device;

// Setup compute pipeline state and encode
@property (nullable, nonatomic, setter=encode:) id<MTLCommandBuffer> cmdBuffer;

// Swap the read and write buffers
- (void) swapBuffers;

@end
```

[Next](LICENSE.txt.md)[Previous](Sources-N-body-MetalGaussianMap.mm.md)

