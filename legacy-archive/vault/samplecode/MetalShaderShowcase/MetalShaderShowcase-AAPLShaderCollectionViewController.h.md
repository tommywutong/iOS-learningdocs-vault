---
title: MetalShaderShowcase
apple_id: TP40014696
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalShaderShowcase/Listings/MetalShaderShowcase_AAPLShaderCollectionViewController_h.html
archived_at: '2026-07-18T03:14:52.714279Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalShaderShowcase](MetalShaderShowcase.md)


[Next](MetalShaderShowcase-AAPLWoodShader.metal.md)[Previous](MetalShaderShowcase-AAPLMesh.h.md)

# MetalShaderShowcase/AAPLShaderCollectionViewController.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The CollectionViewController for the CollectionView of the shaders.
 */

#import <UIKit/UIKit.h>
#import <Metal/Metal.h>

typedef enum
{
    Phong, Wood, Fog, CelShading, SphereMap, NormalMap, ParticleSystem
} ShaderType;

@interface AAPLShaderCollectionViewController : UICollectionViewController

// renderer will create a default device at init time.
@property (nonatomic, readonly) id <MTLDevice> device;

@end
```

[Next](MetalShaderShowcase-AAPLWoodShader.metal.md)[Previous](MetalShaderShowcase-AAPLMesh.h.md)

