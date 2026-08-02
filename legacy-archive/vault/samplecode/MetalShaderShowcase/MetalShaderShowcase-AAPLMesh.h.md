---
title: MetalShaderShowcase
apple_id: TP40014696
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalShaderShowcase/Listings/MetalShaderShowcase_AAPLMesh_h.html
archived_at: '2026-07-18T03:14:52.021150Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalShaderShowcase](MetalShaderShowcase.md)


[Next](MetalShaderShowcase-AAPLShaderCollectionViewController.h.md)[Previous](MetalShaderShowcase-AAPLFogShader.metal.md)

# MetalShaderShowcase/AAPLMesh.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A class to represent a mesh and its buffers used for drawing.
 */

#import <Foundation/Foundation.h>
#import <Metal/Metal.h>
#import "AAPLSharedTypes.h"


@interface AAPLMesh : NSObject

@property (nonatomic) id <MTLBuffer> vertex_buffer;
@property (nonatomic) id <MTLBuffer> normal_buffer;
@property (nonatomic) id <MTLBuffer> uv_buffer;
@property (nonatomic) id <MTLBuffer> tangents_buffer;
@property (nonatomic) id <MTLBuffer> bitangents_buffer;
@property (nonatomic) id <MTLBuffer> index_buffer;
@property (nonatomic) short* indices;
@property (nonatomic) float* vertices;
@property (nonatomic) float* normals;
@property (nonatomic) float* uvs;
@property (nonatomic) float* tangents;
@property (nonatomic) float* bitangents;
@property (nonatomic) unsigned int index_count;
@property (nonatomic) unsigned int vertex_count;
@property (nonatomic) MTLPrimitiveType primitive_type;
@property (nonatomic) float translate_x;
@property (nonatomic) float translate_y;
@property (nonatomic) float translate_z;

+ (instancetype)sharedInstance;

@end
```

[Next](MetalShaderShowcase-AAPLShaderCollectionViewController.h.md)[Previous](MetalShaderShowcase-AAPLFogShader.metal.md)

