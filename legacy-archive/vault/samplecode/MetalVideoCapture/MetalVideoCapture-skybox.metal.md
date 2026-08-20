---
title: MetalVideoCapture
apple_id: TP40015131
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2015-10-29'
source_url: https://developer.apple.com/library/archive/samplecode/MetalVideoCapture/Listings/MetalVideoCapture_skybox_metal.html
archived_at: '2026-07-18T03:14:55.908164Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalVideoCapture](MetalVideoCapture.md)


[Next](MetalVideoCapture-AAPLAppDelegate.mm.md)[Previous](MetalVideoCapture-AAPLAppDelegate.h.md)

# MetalVideoCapture/skybox.metal

```c
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Metal skybox shader
 */

#include <metal_graphics>
#include <metal_matrix>
#include <metal_geometric>
#include <metal_math>
#include <metal_texture>
#include <metal_stdlib>

#include "AAPLSharedTypes.h"

using namespace metal;

struct CubeVertexOutput
{
    float4 position [[position]];
    float3 texCoords;
};

vertex CubeVertexOutput skyboxVertex(constant float4 *pos_data [[ buffer(SKYBOX_VERTEX_BUFFER) ]],
                                     constant float4 *texcoord [[ buffer(SKYBOX_TEXCOORD_BUFFER) ]],
                                     constant AAPL::uniforms_t& uniforms [[ buffer(SKYBOX_CONSTANT_BUFFER) ]],
                                     uint vid [[vertex_id]])
{
    CubeVertexOutput out;
    out.position = uniforms.skybox_modelview_projection_matrix * pos_data[vid];
    out.texCoords = texcoord[vid].xyz;
    return out;
}

fragment half4 skyboxFragment(CubeVertexOutput in [[stage_in]],
                               texturecube<half> skybox_texture [[texture(SKYBOX_IMAGE_TEXTURE)]])
{
    constexpr sampler s_cube(filter::linear, mip_filter::linear);
    return skybox_texture.sample(s_cube, in.texCoords);
}
```

[Next](MetalVideoCapture-AAPLAppDelegate.mm.md)[Previous](MetalVideoCapture-AAPLAppDelegate.h.md)

