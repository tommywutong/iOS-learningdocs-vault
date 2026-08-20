---
title: MetalShaderShowcase
apple_id: TP40014696
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalShaderShowcase/Listings/MetalShaderShowcase_AAPLCubeMesh_h.html
archived_at: '2026-07-18T03:14:51.807114Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalShaderShowcase](MetalShaderShowcase.md)


[Next](MetalShaderShowcase-AAPLRenderer.mm.md)[Previous](MetalShaderShowcase-AAPLNormalMapShader.metal.md)

# MetalShaderShowcase/AAPLCubeMesh.h

```objc
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A class to represent a cube mesh used for drawing.
 */

#import "AAPLMesh.h"

extern const int num_cube_indices;
extern const int num_cube_vertices;
extern const int num_cube_normals;
extern const int num_cube_uvs;

extern float cube_vertices[];
extern float cube_normals[];
extern float cube_uvs[];
extern short cube_indices[];
extern float cube_tangents[];
extern float cube_bitangents[];

extern unsigned int sizeof_cube_vertices;
extern unsigned int sizeof_cube_normals;
extern unsigned int sizeof_cube_uvs;
extern unsigned int sizeof_cube_indices;


@interface AAPLCubeMesh : AAPLMesh

@end
```

[Next](MetalShaderShowcase-AAPLRenderer.mm.md)[Previous](MetalShaderShowcase-AAPLNormalMapShader.metal.md)

