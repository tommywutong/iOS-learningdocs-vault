---
title: MetalShaderShowcase
apple_id: TP40014696
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalShaderShowcase/Listings/MetalShaderShowcase_AAPLParticleSystem_h.html
archived_at: '2026-07-18T03:14:52.326649Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalShaderShowcase](MetalShaderShowcase.md)


[Next](MetalShaderShowcase-AAPLViewController.mm.md)[Previous](MetalShaderShowcase-AAPLTransforms.mm.md)

# MetalShaderShowcase/AAPLParticleSystem.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Metal Particle System for Metal Shader Showpiece. Initializes the particle system data that is sent to the GPU.
 */

#import <Foundation/Foundation.h>
#import <Metal/Metal.h>
#import "AAPLSharedTypes.h"

@interface AAPLParticleSystem : NSObject

@property (nonatomic) id <MTLBuffer> initial_direction_buffer;
@property (nonatomic) id <MTLBuffer> birth_offsets_buffer;
@property (nonatomic, readonly) unsigned int num_particles;
@property (nonatomic, readonly) float lifespan;

- (instancetype)initWithDevice:(id <MTLDevice>)device;
@end
```

[Next](MetalShaderShowcase-AAPLViewController.mm.md)[Previous](MetalShaderShowcase-AAPLTransforms.mm.md)

