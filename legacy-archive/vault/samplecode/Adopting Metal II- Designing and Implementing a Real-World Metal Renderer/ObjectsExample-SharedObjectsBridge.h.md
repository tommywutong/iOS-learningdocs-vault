---
title: 'Adopting Metal II: Designing and Implementing a Real-World Metal Renderer'
apple_id: TP40017288
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: Metal
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/AdoptingMetalII/Listings/ObjectsExample_SharedObjectsBridge_h.html
archived_at: '2026-07-18T03:00:48.469990Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Adopting Metal II: Designing and Implementing a Real-World Metal Renderer](Adopting%20Metal%20II-%20Designing%20and%20Implementing%20a%20Real-World%20Metal%20Renderer.md)


[Next](ObjectsExample-AppDelegate.swift.md)[Previous](ObjectsExample-Visualize.metal.md)

# ObjectsExample/SharedObjectsBridge.h

```c
#include <simd/simd.h>

struct ObjectData
{
    matrix_float4x4 LocalToWorld;
    vector_float4 color;
    vector_float4 pad0;
    vector_float4 pad01;
    vector_float4 pad02;
    matrix_float4x4 pad1;
    matrix_float4x4 pad2;

};

struct ShadowPass
{
    matrix_float4x4 ViewProjection;
    matrix_float4x4 pad1;
    matrix_float4x4 pad2;
    matrix_float4x4 pad3;
};

struct MainPass
{
    matrix_float4x4 ViewProjection;
    matrix_float4x4 ViewShadow0Projection;
    vector_float4   LightPosition;
    vector_float4   pad00;
    vector_float4   pad01;
    vector_float4   pad02;
    matrix_float4x4 pad1;
};
```

[Next](ObjectsExample-AppDelegate.swift.md)[Previous](ObjectsExample-Visualize.metal.md)

