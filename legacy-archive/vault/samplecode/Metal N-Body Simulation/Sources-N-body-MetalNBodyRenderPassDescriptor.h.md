---
title: Metal N-Body Simulation
apple_id: TP40016621
resource_type: Sample Code
platform: iOS
topic: General
technology: Metal
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/Metal_NBody_Simulation/Listings/Sources_N_body_MetalNBodyRenderPassDescriptor_h.html
archived_at: '2026-07-18T03:14:57.707699Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Metal N-Body Simulation](Metal%20N-Body%20Simulation.md)


[Next](Sources-N-body-MetalNBody.metal.md)[Previous](Sources-N-body-MetalNBodyTransform.mm.md)

# Sources/N-body/MetalNBodyRenderPassDescriptor.h

```objc
/*
 Copyright (C) 2015-2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for creating a render pass descriptor.
 */

#import <QuartzCore/CAMetalLayer.h>
#import <Metal/Metal.h>

@interface MetalNBodyRenderPassDescriptor : NSObject

// Set a drawable to set render pass descriptors texture
@property (nullable, nonatomic) id<CAMetalDrawable> drawable;

// Get the render pass descriptor object
@property (nullable, readonly) MTLRenderPassDescriptor* descriptor;

// Query to determine if a texture was acquired from a drawable
@property (readonly) BOOL haveTexture;

// Read the types for render pass descriptors load/store
@property (readonly) MTLLoadAction  load;
@property (readonly) MTLStoreAction store;

// Get or set the clear color for the render pass descriptor
@property (nonatomic) MTLClearColor color;

@end
```

[Next](Sources-N-body-MetalNBody.metal.md)[Previous](Sources-N-body-MetalNBodyTransform.mm.md)

