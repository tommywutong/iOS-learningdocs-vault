---
title: MetalInstancedHelix
apple_id: TP40015091
resource_type: Sample Code
platform: iOS
topic: null
technology: Metal
published: '2015-01-24'
source_url: https://developer.apple.com/library/archive/samplecode/MetalInstancedHelix/Listings/MetalInstancedHelix_AAPLTransforms_h.html
archived_at: '2026-07-18T03:14:50.862073Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalInstancedHelix](MetalInstancedHelix.md)


[Next](MetalInstancedHelix-AAPLTransforms.mm.md)[Previous](MetalInstancedHelix-AAPLSharedTypes.h.md)

# MetalInstancedHelix/AAPLTransforms.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility methods for linear transformations of projective
  geometry of the left-handed coordinate system.
 */

#ifndef _METAL_MATH_TRANSFORMS_H_
#define _METAL_MATH_TRANSFORMS_H_

#import <simd/simd.h>

#ifdef __cplusplus

namespace AAPL
{
    float radians(const float& degrees);

    simd::float4x4 scale(const float& x,
                         const float& y,
                         const float& z);

    simd::float4x4 scale(const simd::float3& s);

    simd::float4x4 translate(const float& x,
                             const float& y,
                             const float& z);

    simd::float4x4 translate(const simd::float3& t);

    simd::float4x4 rotate(const float& angle,
                          const float& x,
                          const float& y,
                          const float& z);

    simd::float4x4 rotate(const float& angle,
                          const simd::float3& u);

    simd::float4x4 frustum(const float& fovH,
                           const float& fovV,
                           const float& near,
                           const float& far);

    simd::float4x4 frustum(const float& left,
                           const float& right,
                           const float& bottom,
                           const float& top,
                           const float& near,
                           const float& far);

    simd::float4x4 frustum_oc(const float& left,
                              const float& right,
                              const float& bottom,
                              const float& top,
                              const float& near,
                              const float& far);

    simd::float4x4 lookAt(const float * const pEye,
                          const float * const pCenter,
                          const float * const pUp);

    simd::float4x4 lookAt(const simd::float3& eye,
                          const simd::float3& center,
                          const simd::float3& up);

    simd::float4x4 perspective(const float& width,
                               const float& height,
                               const float& near,
                               const float& far);

    simd::float4x4 perspective_fov(const float& fovy,
                                   const float& aspect,
                                   const float& near,
                                   const float& far);

    simd::float4x4 perspective_fov(const float& fovy,
                                   const float& width,
                                   const float& height,
                                   const float& near,
                                   const float& far);

    simd::float4x4 ortho2d_oc(const float& left,
                              const float& right,
                              const float& bottom,
                              const float& top,
                              const float& near,
                              const float& far);

    simd::float4x4 ortho2d_oc(const simd::float3& origin,
                              const simd::float3& size);

    simd::float4x4 ortho2d(const float& left,
                           const float& right,
                           const float& bottom,
                           const float& top,
                           const float& near,
                           const float& far);

    simd::float4x4 ortho2d(const simd::float3& origin,
                           const simd::float3& size);
} // AAPL

#endif

#endif
```

[Next](MetalInstancedHelix-AAPLTransforms.mm.md)[Previous](MetalInstancedHelix-AAPLSharedTypes.h.md)

