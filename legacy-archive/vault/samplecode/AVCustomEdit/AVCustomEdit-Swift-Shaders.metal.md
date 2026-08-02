---
title: AVCustomEdit
apple_id: DTS40013411
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVCustomEdit/Listings/AVCustomEdit_Swift_Shaders_metal.html
archived_at: '2026-07-18T03:00:12.119863Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVCustomEdit](AVCustomEdit.md)


[Next](AVCustomEdit-Swift-APLCustomVideoCompositionInstruction.swift.md)[Previous](ReadMe.md.md)

# AVCustomEdit-Swift/Shaders.metal

```c
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The vertex and fragment shaders.
 */

#include <metal_stdlib>
#include <simd/simd.h>

using namespace metal;

/*
 Vertex input/output structure for passing results
 from a vertex shader to a fragment shader.
*/
struct VertexInOut
{
    float4 position [[position]];
    float4 color;
    float2 texCoord [[user(texturecoord)]];
};

// Vertex shader for a textured quad.
vertex VertexInOut passthroughVertexShader(uint vid [[ vertex_id ]],
                                           constant float4* position [[ buffer(0) ]],
                                           constant packed_float4* color [[ buffer(1) ]],
                                           constant packed_float2* pTexCoords [[ buffer(2) ]])
{
    VertexInOut outVertex;

    // Copy the vertex, texture and color coordinates.
    outVertex.position =  position[vid];
    outVertex.color    =  color[vid];
    outVertex.texCoord =  pTexCoords[vid];

    return outVertex;
};

vertex VertexInOut vertexShader_DiagonalWipe(uint vid [[ vertex_id ]],
                                            constant float4* position [[ buffer(0) ]],
                                            constant packed_float4* color [[ buffer(1) ]],
                                            constant packed_float2* pTexCoords [[ buffer(2) ]])
{
    VertexInOut outVertex;

    outVertex.position =  position[vid];
    outVertex.color    =  color[vid];

    /*
     Invert the y texture coordinate -- this is a simple modification to prevent the frame 
     from being flipped while using the same algorithm from the ObjC/OpenGL target 
     'quadVertexCoordinates' function (see APLDiagonalWipeRenderer.m) to compute the vertex 
     data for the foreground frame.
    */
    outVertex.texCoord = pTexCoords[vid];
    outVertex.texCoord.y = 1.0 - outVertex.texCoord.y;

    return outVertex;
}

// Fragment shader for a textured quad.
fragment half4 texturedQuadFragmentShader(VertexInOut inFrag [[ stage_in ]],
                                          texture2d<half> tex2D [[ texture(0) ]])
{
    constexpr sampler quad_sampler;

    // Sample the texture to get the surface color at this point.
    half4 color = tex2D.sample(quad_sampler, inFrag.texCoord);

    return color;
}
```

[Next](AVCustomEdit-Swift-APLCustomVideoCompositionInstruction.swift.md)[Previous](ReadMe.md.md)

