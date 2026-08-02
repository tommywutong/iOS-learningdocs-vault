---
title: MetalShaderShowcase
apple_id: TP40014696
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalShaderShowcase/Listings/MetalShaderShowcase_AAPLMesh_mm.html
archived_at: '2026-07-18T03:14:52.073122Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalShaderShowcase](MetalShaderShowcase.md)


[Next](MetalShaderShowcase-AAPLFogShader.metal.md)[Previous](MetalShaderShowcase-AAPLCubeMesh.mm.md)

# MetalShaderShowcase/AAPLMesh.mm

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A class to represent a mesh and its buffers used for drawing.
 */

#import "AAPLMesh.h"
#import "AAPLSharedTypes.h"

@implementation AAPLMesh

+ (instancetype)sharedInstance
{
    NSLog(@"Error: Should never enter AAPLMesh sharedInstance!");
    assert(0);
    return [[self alloc] init];
}

@end
```

[Next](MetalShaderShowcase-AAPLFogShader.metal.md)[Previous](MetalShaderShowcase-AAPLCubeMesh.mm.md)

