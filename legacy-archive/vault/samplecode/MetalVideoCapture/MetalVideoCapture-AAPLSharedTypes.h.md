---
title: MetalVideoCapture
apple_id: TP40015131
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2015-10-29'
source_url: https://developer.apple.com/library/archive/samplecode/MetalVideoCapture/Listings/MetalVideoCapture_AAPLSharedTypes_h.html
archived_at: '2026-07-18T03:14:55.177534Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalVideoCapture](MetalVideoCapture.md)


[Next](MetalVideoCapture-AAPLAppDelegate.h.md)[Previous](MetalVideoCapture-AAPLTransforms.mm.md)

# MetalVideoCapture/AAPLSharedTypes.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Shared data types between CPU code and metal shader code
 */

#ifndef _AAPL_SHARED_TYPES_H_
#define _AAPL_SHARED_TYPES_H_

#import <simd/simd.h>

#ifdef __cplusplus

#define QUAD_VERTEX_BUFFER 0
#define QUAD_VERTEX_CONSTANT_BUFFER 1
#define QUAD_FRAGMENT_CONSTANT_BUFFER 0

#define QUAD_ENVMAP_TEXTURE 0
#define QUAD_IMAGE_TEXTURE 1

#define SKYBOX_VERTEX_BUFFER 0
#define SKYBOX_TEXCOORD_BUFFER 1
#define SKYBOX_CONSTANT_BUFFER 2
#define SKYBOX_IMAGE_TEXTURE 0


namespace AAPL
{
    typedef enum : int
    {
        Unknown,
        Portrait,
        PortraitUpsideDown,
        LandscapeLeft,
        LandscapeRight
    } Orientation;

    typedef struct
    {
        simd::float4x4 modelview_matrix;
        simd::float4x4 modelview_projection_matrix;
        simd::float4x4 normal_matrix;
        simd::float4x4 inverted_view_matrix;
        simd::float4x4 skybox_modelview_projection_matrix;
        simd::float4x4 _reserved;
        simd::float4x4 _reserved1;
        Orientation orientation;
    } uniforms_t;
}

#endif // cplusplus

#endif // _AAPL_SHARED_TYPES_H_
```

[Next](MetalVideoCapture-AAPLAppDelegate.h.md)[Previous](MetalVideoCapture-AAPLTransforms.mm.md)

