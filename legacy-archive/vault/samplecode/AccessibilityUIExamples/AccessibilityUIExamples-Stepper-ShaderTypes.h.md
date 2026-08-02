---
title: AccessibilityUIExamples
apple_id: DTS40012307
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2017-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/AccessibilityUIExamples/Listings/AccessibilityUIExamples_Stepper_ShaderTypes_h.html
archived_at: '2026-07-18T03:00:37.686734Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AccessibilityUIExamples](AccessibilityUIExamples.md)


[Next](AccessibilityUIExamples-Stepper-CustomStepperView.swift.md)[Previous](AccessibilityUIExamples-Stepper-Bridging-Header.h.md)

# AccessibilityUIExamples/Stepper/ShaderTypes.h

```c
/*
See LICENSE folder for this sample’s licensing information.

Abstract:
Header containing types and enum constants shared between Metal shaders and C/ObjC/Swift sources.
*/

#ifndef ShaderTypes_h
#define ShaderTypes_h

#include <simd/simd.h> // for vector_float4

// Buffer index values shared between shader and C code to ensure Metal shader buffer inputs match
//   Metal API buffer set calls.
typedef enum BufferIndices
{
    BufferIndexVertices     = 0,
    BufferIndexViewportSize = 1,
    BufferIndexColor        = 2,
} VertexInputIndex;

// Structure defining the layout of each vertex.  Shared between C code filling in the vertex data
//   and Metal vertex shader consuming the vertices.
typedef struct {
    vector_float4 position;
    vector_float4 texcoord;
} Vertex;

// Texture index values shared between shader and C code to ensure Metal shader texture indices
//   match indices of Metal API texture set calls.
typedef enum TextureIndices {
    TextureIndexColor = 0,
} TextureIndices;

#endif /* ShaderTypes_h */
```

[Next](AccessibilityUIExamples-Stepper-CustomStepperView.swift.md)[Previous](AccessibilityUIExamples-Stepper-Bridging-Header.h.md)

