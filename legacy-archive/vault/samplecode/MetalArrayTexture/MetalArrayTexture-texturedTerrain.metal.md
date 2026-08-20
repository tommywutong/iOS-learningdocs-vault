---
title: MetalArrayTexture
apple_id: TP40016608
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/samplecode/MetalArrayTexture/Listings/MetalArrayTexture_texturedTerrain_metal.html
archived_at: '2026-07-18T03:14:47.203985Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalArrayTexture](MetalArrayTexture.md)


[Next](MetalArrayTexture-OSX-AAPLAppDelegate.m.md)[Previous](MetalArrayTexture-AAPLRenderer.h.md)

# MetalArrayTexture/texturedTerrain.metal

```c
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Textured Terrain shader.
 */

#include <metal_graphics>
#include <metal_matrix>
#include <metal_geometric>
#include <metal_math>
#include <metal_texture>
#include <metal_common>

using namespace metal;

struct VertexInOut
{
    float4 m_Position [[position]];
    float3 m_TexCoord [[user(texturecoord)]];
};

vertex VertexInOut texturedTerrainVertex(constant packed_float3  *pPosition        [[ buffer(0) ]],
                                      constant packed_float3  *pTexCoords       [[ buffer(1) ]],
                                      constant float4x4       *pMVP             [[ buffer(2) ]],
                                      constant float4x4       *pTextureMatrix   [[ buffer(3) ]],
                                      uint                     vid              [[ vertex_id ]])
{
    VertexInOut outVertices;

    outVertices.m_Position = *pMVP * float4(pPosition[vid], 1.0f);
    outVertices.m_TexCoord = float3(*pTextureMatrix * float4(pTexCoords[vid], 1.0f));

    return outVertices;
}

fragment half4 texturedTerrainFragment(VertexInOut             inFrag    [[ stage_in ]],
                                    texture2d_array<half>   tex2D     [[ texture(0) ]])
{
    float2 texCoord = float2(inFrag.m_TexCoord.x , inFrag.m_TexCoord.y);
    float slice = floor(inFrag.m_TexCoord.z);

    constexpr sampler sampler(coord::normalized, address::repeat, filter::linear);
    half4 a = tex2D.sample(sampler, texCoord, slice);
    half4 b = tex2D.sample(sampler, texCoord, slice+1);

    half4 color = mix(a, b, half4(fract(inFrag.m_TexCoord.z)));

    return color;
}
```

[Next](MetalArrayTexture-OSX-AAPLAppDelegate.m.md)[Previous](MetalArrayTexture-AAPLRenderer.h.md)

