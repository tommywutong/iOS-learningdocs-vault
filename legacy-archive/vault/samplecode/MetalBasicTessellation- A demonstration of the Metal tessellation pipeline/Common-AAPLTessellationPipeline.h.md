---
title: 'MetalBasicTessellation: A demonstration of the Metal tessellation pipeline'
apple_id: TP40017289
resource_type: Sample Code
platform: macOS
topic: null
technology: Metal
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalBasicTessellation/Listings/Common_AAPLTessellationPipeline_h.html
archived_at: '2026-07-18T03:14:47.429815Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalBasicTessellation: A demonstration of the Metal tessellation pipeline](MetalBasicTessellation-%20A%20demonstration%20of%20the%20Metal%20tessellation%20pipeline.md)


[Next](Common-TessellationFunctions.metal.md)[Previous](Common-AAPLAppDelegate.m.md)

# Common/AAPLTessellationPipeline.h

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Tessellation Pipeline for MetalBasicTessellation.
            The exposed properties are user-defined via the ViewController UI elements.
            The compute pipelines are built with a compute kernel (one for triangle patches; one for quad patches).
            The render pipelines are built with a post-tessellation vertex function (one for triangle patches; one for quad patches) and a fragment function. The render pipeline descriptor also configures tessellation-specific properties.
            The tessellation factors buffer is dynamically populated by the compute kernel.
            The control points buffer is populated with static position data.
 */

#import <Metal/Metal.h>
#import <MetalKit/MetalKit.h>

@interface AAPLTessellationPipeline : NSObject <MTKViewDelegate>

@property (readwrite) MTLPatchType patchType;
@property (readwrite) BOOL wireframe;
@property (readwrite) float edgeFactor;
@property (readwrite) float insideFactor;

- (nullable instancetype)initWithMTKView:(nonnull MTKView *)mtkView;

@end
```

[Next](Common-TessellationFunctions.metal.md)[Previous](Common-AAPLAppDelegate.m.md)

