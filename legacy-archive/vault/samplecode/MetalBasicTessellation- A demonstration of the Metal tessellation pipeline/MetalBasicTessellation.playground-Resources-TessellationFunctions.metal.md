---
title: 'MetalBasicTessellation: A demonstration of the Metal tessellation pipeline'
apple_id: TP40017289
resource_type: Sample Code
platform: macOS
topic: null
technology: Metal
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalBasicTessellation/Listings/MetalBasicTessellation_playground_Resources_TessellationFunctions_metal.html
archived_at: '2026-07-18T03:14:47.793188Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalBasicTessellation: A demonstration of the Metal tessellation pipeline](MetalBasicTessellation-%20A%20demonstration%20of%20the%20Metal%20tessellation%20pipeline.md)


[Next](MetalBasicTessellation.playground-Contents.swift.md)[Previous](LICENSE.txt.md)

# MetalBasicTessellation.playground/Resources/TessellationFunctions.metal

```c
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Playground version of MetalBasicTessellation.
 */

#include <metal_stdlib>
using namespace metal;

// Control Point struct
struct ControlPoint {
    float4 position [[attribute(0)]];
};

// Patch struct
struct PatchIn {
    patch_control_point<ControlPoint> control_points;
};

// Vertex-to-Fragment struct
struct FunctionOutIn {
    float4 position [[position]];
    half4  color [[flat]];
};

// Triangle compute kernel
kernel void tessellation_kernel_triangle(constant float& edge_factor [[ buffer(0) ]],
                                         constant float& inside_factor [[ buffer(1) ]],
                                         device MTLTriangleTessellationFactorsHalf* factors [[ buffer(2) ]],
                                         uint pid [[ thread_position_in_grid ]])
{
    // Simple passthrough operation
    factors[pid].edgeTessellationFactor[0] = edge_factor;
    factors[pid].edgeTessellationFactor[1] = edge_factor;
    factors[pid].edgeTessellationFactor[2] = edge_factor;
    factors[pid].insideTessellationFactor = inside_factor;
}

// Triangle post-tessellation vertex function
[[patch(triangle, 3)]]
vertex FunctionOutIn tessellation_vertex_triangle(PatchIn patchIn [[stage_in]],
                                                  float3 patch_coord [[ position_in_patch ]])
{
    // Barycentric coordinates
    float u = patch_coord.x;
    float v = patch_coord.y;
    float w = patch_coord.z;

    // Convert to cartesian coordinates
    float x = u * patchIn.control_points[0].position.x + v * patchIn.control_points[1].position.x + w * patchIn.control_points[2].position.x;
    float y = u * patchIn.control_points[0].position.y + v * patchIn.control_points[1].position.y + w * patchIn.control_points[2].position.y;

    // Output
    FunctionOutIn vertexOut;
    vertexOut.position = float4(x, y, 0.0, 1.0);
    vertexOut.color = half4(u, v, w, 1.0);
    return vertexOut;
}

// Common fragment function
fragment half4 tessellation_fragment(FunctionOutIn fragmentIn [[stage_in]])
{
    return fragmentIn.color;
}
```

[Next](MetalBasicTessellation.playground-Contents.swift.md)[Previous](LICENSE.txt.md)

